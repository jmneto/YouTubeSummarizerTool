# YouTube Video Summarizer

This project is a Flask web application that summarizes YouTube video transcripts using Azure OpenAI. Users can input a YouTube video URL, and the application will fetch the video's transcript, summarize it, and display the summary along with the original transcript.

## Features

- Fetches YouTube video transcripts.
- Summarizes transcripts using Azure OpenAI.
- Displays the original transcript, and summary.
- Simple and user-friendly web interface.

## Project Structure

- `main.py`: The main Flask application file.
- `SummarizeYoutube.py`: Contains functions to fetch video transcripts, thumbnails, and summarize the transcript.
- `templates/index.html`: HTML template for the web interface.
- `requirements.txt`: Lists the Python dependencies for the project.
- `run.ps1`: PowerShell script to activate the virtual environment and run the Flask app.
- `YouTube sum.bat`: Batch file to start the PowerShell script.
- `.env`: Environment file containing sensitive information like API keys.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/YouTubeVideoSummarizer.git
    cd YouTubeVideoSummarizer
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. To connect to Open AI service, Create a .env file in the root of your project with the following content:
    ```env
    AZURE_OPENAI_KEY=your_azure_openai_key
    AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
    DEPLOYMENT_NAME=your_deployment_name
    API_VERSION=your_api_version
    ```

## Usage

1. Run the Flask application:
    ```sh
    python main.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter a YouTube video URL and click "Submit" to get the summary.

## Running with PowerShell and Batch Script

1. Run the batch script to start the application and open it in the browser:
    ```sh
    YouTube sum.bat
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)  (Requires Version 1.1.1)
- [Azure OpenAI](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/)
