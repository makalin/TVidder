# TVidder

## 📘 **Description**
**TVidder: Tweet Video Downloader CLI**  
A command-line tool to download videos from X (Twitter) using the official API v2. This tool allows you to extract and download video files directly from Twitter using a simple, intuitive CLI interface.

The script parses a tweet's URL or ID, retrieves video details from the API, and downloads the video file to your local system. It's especially useful for developers, social media managers, or content creators who need quick and easy access to video content on Twitter.

---

## 📋 **Features**
- **Video Downloading**: Extract and download video files from X (Twitter) using its official API v2.
- **Simple CLI Usage**: Run commands with minimal arguments and download video files quickly.
- **Progress Tracking**: Track the download progress using an interactive progress bar.
- **Error Handling**: Handles API errors and failed downloads gracefully.
- **Lightweight and Fast**: Uses minimal libraries and optimizes API calls for fast responses.

---

## 📦 **Dependencies**
This script requires the following Python libraries to run:
- **argparse**: Command-line argument parsing.
- **re**: Regular expressions for tweet URL parsing.
- **dotenv**: Loads environment variables from a `.env` file.
- **os**: File system path handling and directory creation.
- **Progress**: Displays a dynamic progress bar while downloading files.
- **Console**: Terminal output formatting.
- **json**: Parses JSON responses from the Twitter API.
- **sys**: Handles system-level functionality like script exit.
- **pathlib**: Cross-platform file path manipulation.
- **typing**: Type hinting for better code readability.
- **datetime**: Handles timestamps and date formatting.
- **requests**: Handles HTTP requests for API calls.

To install the required libraries, run:
```bash
pip install argparse re dotenv os Progress Console json sys pathlib typing datetime requests
```

---

## 🚀 **Usage**
### **Prerequisites**
1. **Install Python**: Ensure you have Python 3.7 or higher installed.
2. **Install Required Libraries**: Run the following command to install dependencies:
   ```bash
   pip install argparse re dotenv os Progress Console json sys pathlib typing datetime requests
   ```

3. **Set Up API Credentials**:  
   - Create a `.env` file in the same directory as `tvidder.py`.
   - Add the following content with your **Twitter API Bearer Token**:
     ```env
     TWITTER_BEARER_TOKEN=your_bearer_token_here
     ```

---

### **Running the Script**
To download a video from a tweet, use the following command:
```bash
python tvidder.py --url <tweet_url>
```
**Example:**
```bash
python tvidder.py --url https://twitter.com/username/status/1234567890
```

After running the command, the script will:
1. Extract the tweet ID from the URL.
2. Call the Twitter API to retrieve video information.
3. Download the highest quality video.
4. Save the video to a folder on your system.

---

### **Available CLI Arguments**
| Argument         | Required | Description                                   | Example                                |
|------------------|----------|-----------------------------------------------|----------------------------------------|
| `--url`          | ✅ Yes   | URL of the tweet containing the video         | `--url https://twitter.com/...`        |
| `--output-dir`   | ❌ No    | Directory to save the downloaded video        | `--output-dir ./downloads/`            |
| `--quality`      | ❌ No    | Set the video quality to download (low, high) | `--quality high`                       |
| `--help`         | ❌ No    | Show help message and usage instructions      | `--help`                               |

---

## ⚙️ **Functions**
This script contains the following key functions:

### 🔧 **`__init__()`**
**Purpose:**  
Initializes the program, sets up global variables, and configures environment variables from the `.env` file.

**Main Tasks:**  
- Loads the Twitter Bearer Token from the `.env` file.  
- Ensures essential directories exist.  

---

### 🔧 **`extract_tweet_id(url: str) -> str`**
**Purpose:**  
Extracts the Tweet ID from a given tweet URL.  

**Inputs:**  
- `url (str)`: The URL of the tweet.  

**Returns:**  
- `tweet_id (str)`: The extracted Tweet ID.  

**Example Usage:**  
```python
tweet_id = extract_tweet_id("https://twitter.com/username/status/1234567890")
print(tweet_id)  # Output: 1234567890
```

---

### 🔧 **`get_tweet_data(tweet_id: str) -> dict`**
**Purpose:**  
Fetches tweet data from Twitter's API using the given Tweet ID.  

**Inputs:**  
- `tweet_id (str)`: The ID of the tweet to extract video information from.  

**Returns:**  
- `response (dict)`: The response from Twitter API containing tweet information.  

**Example Usage:**  
```python
data = get_tweet_data("1234567890")
print(data)
```

---

### 🔧 **`download_video(video_url: str, output_path: str) -> None`**
**Purpose:**  
Downloads a video file from the given URL and saves it to the specified output path.  

**Inputs:**  
- `video_url (str)`: URL of the video file.  
- `output_path (str)`: Local path where the file should be saved.  

**Returns:**  
- None  

**Example Usage:**  
```python
download_video("https://video-url-here.com", "./downloads/video.mp4")
```

---

### 🔧 **`main()`**
**Purpose:**  
The main entry point for the script. It parses command-line arguments and executes the logic to download the video.  

**Main Tasks:**  
- Parses arguments like `--url`, `--output-dir`, and `--quality`.  
- Calls `extract_tweet_id`, `get_tweet_data`, and `download_video` to complete the video download process.  

**Example Usage:**  
```python
if __name__ == "__main__":
    main()
```

---

## 📂 **Project Structure**
```
📁 TVidder/
  ├── 📄 tvidder.py      # Main script file
  ├── 📄 .env            # Environment file containing the API token
  ├── 📂 downloads/      # Directory where downloaded videos are saved
  └── 📄 README.md       # This documentation file
```

---

## 🛠️ **Environment Variables**
To use this script, you must create a `.env` file in the root directory of the project and specify your **Twitter API Bearer Token**.  
```
TWITTER_BEARER_TOKEN=your_bearer_token_here
```

---

## 📚 **Example Walkthrough**
Here’s an example of how to use the **TVidder** script to download a video.  

1️⃣ **Prepare the .env File**
```
TWITTER_BEARER_TOKEN=ABC123XYZ456
```

2️⃣ **Run the Download Command**
```bash
python tvidder.py --url https://twitter.com/username/status/1234567890
```

3️⃣ **Watch the Progress**
- The script will extract the tweet ID from the URL.  
- It will then call the Twitter API to get video details.  
- The video will be downloaded, and progress will be displayed in the terminal.  

4️⃣ **View the Video**
- The video will be saved in the `downloads/` directory by default.  

---

## 🚨 **Error Handling**
If an error occurs, the script will provide a clear error message, such as:  
- **Invalid URL**: If the tweet URL is malformed or missing, an error message will be displayed.  
- **API Errors**: If the API token is invalid or the request limit is exceeded, an error will be printed.  
- **File I/O Errors**: If the directory is not writable, the script will print an error message.  

**Example Errors:**
```
Error: Unable to extract video from the provided URL.
```

---

## 📘 **Possible Improvements**
- Add support for multiple video qualities (low, medium, high).  
- Handle cases where the tweet does not contain a video.  
- Add support for batch downloads from a list of tweet URLs.  

---

## 📄 **License**
This script is licensed under the MIT License.  

---

## 🛠️ **Contributing**
Contributions, bug fixes, and feature requests are welcome. Fork the repository and submit a pull request with your changes.

**Want to contribute?**  
1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature/your-feature-name`).  
3. Commit your changes.  
4. Push to your branch.  
5. Open a Pull Request.  

---

If you'd like any updates or additional details in this README, feel free to ask.