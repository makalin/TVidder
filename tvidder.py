#!/usr/bin/env python3
"""
TVidder: Tweet Video Downloader CLI
A command-line tool to download videos from X (Twitter) using the official API v2.
"""

import argparse
import sys
import re
import json
import requests
from pathlib import Path
from typing import Optional, Dict, Any
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskID
from datetime import datetime
import os
from dotenv import load_dotenv

class TwitterDownloader:
    def __init__(self):
        self.console = Console()
        load_dotenv()  # Load environment variables from .env file
        
        # Get API credentials from environment variables
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        if not self.bearer_token:
            raise ValueError("TWITTER_BEARER_TOKEN environment variable is required")
        
        self.headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'User-Agent': 'TVidder/1.0'
        }
        
        self.api_base = 'https://api.twitter.com/2'
        
    def extract_tweet_id(self, url: str) -> Optional[str]:
        """Extract tweet ID from a Twitter/X URL."""
        patterns = [
            r'(?:twitter|x)\.com/\w+/status/(\d+)',
            r'(?:twitter|x)\.com/i/web/status/(\d+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None

    def get_tweet_data(self, tweet_id: str) -> Dict[str, Any]:
        """Fetch tweet data using Twitter API v2."""
        url = f"{self.api_base}/tweets/{tweet_id}"
        params = {
            'expansions': 'attachments.media_keys',
            'media.fields': 'variants,url,type,duration_ms',
            'tweet.fields': 'attachments,entities'
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise Exception(f"API request failed: {response.text}")
            
        return response.json()

    def download_video(self, url: str, output_dir: str = "downloads") -> bool:
        """Download video from Twitter/X URL."""
        try:
            tweet_id = self.extract_tweet_id(url)
            if not tweet_id:
                self.console.print("[red]Error: Invalid URL[/red]")
                return False

            # Create output directory if it doesn't exist
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)

            # Get tweet data from API
            self.console.print("[yellow]Fetching tweet data...[/yellow]")
            tweet_data = self.get_tweet_data(tweet_id)

            # Extract video URL
            if 'includes' not in tweet_data or 'media' not in tweet_data['includes']:
                self.console.print("[red]Error: No media found in tweet[/red]")
                return False

            media = tweet_data['includes']['media']
            video_media = next((m for m in media if m['type'] in ['video', 'animated_gif']), None)
            
            if not video_media or 'variants' not in video_media:
                self.console.print("[red]Error: No video found in tweet[/red]")
                return False

            # Get highest quality MP4 variant
            variants = video_media['variants']
            video_variants = [v for v in variants if v.get('content_type') == 'video/mp4']
            if not video_variants:
                self.console.print("[red]Error: No MP4 video variants found[/red]")
                return False

            best_variant = max(video_variants, key=lambda x: x.get('bit_rate', 0))
            video_url = best_variant['url']

            # Generate output filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = output_path / f"twitter_video_{tweet_id}_{timestamp}.mp4"
            
            # Download the video with progress bar
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            ) as progress:
                task = progress.add_task("[cyan]Downloading video...", total=100)
                
                response = requests.get(video_url, stream=True)
                total_size = int(response.headers.get('content-length', 0))
                
                with open(output_file, 'wb') as file:
                    if total_size == 0:
                        file.write(response.content)
                    else:
                        downloaded = 0
                        for data in response.iter_content(chunk_size=8192):
                            downloaded += len(data)
                            file.write(data)
                            progress.update(task, completed=int(100 * downloaded / total_size))

            self.console.print(f"[green]Video downloaded to: {output_file}[/green]")
            return True

        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")
            return False

def main():
    parser = argparse.ArgumentParser(description="Download videos from X/Twitter")
    parser.add_argument("url", help="video URL")
    parser.add_argument("-o", "--output", help="Output directory", default="downloads")
    args = parser.parse_args()

    try:
        downloader = TwitterDownloader()
        success = downloader.download_video(args.url, args.output)
        sys.exit(0 if success else 1)
    except ValueError as e:
        Console().print(f"[red]Configuration Error: {str(e)}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
