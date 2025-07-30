# Description: This script fetches the transcript of a YouTube video and summarizes it using Azure OpenAI's 

# Import the required libraries
from openai import AzureOpenAI
from youtube_transcript_api import YouTubeTranscriptApi
import markdown
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define the Azure OpenAI credentials
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")
API_VERSION = os.getenv("API_VERSION")

# Function to get the video ID from a YouTube URL
def get_video_id(youtube_url):
    """Extracts the video ID from a YouTube URL."""
    if "youtu.be/" in youtube_url:
        return youtube_url.split("youtu.be/")[-1].split("?")[0]
    elif "youtube.com/watch?v=" in youtube_url:
        return youtube_url.split("v=")[-1].split("&")[0]
    else:
        raise ValueError("Invalid YouTube URL")

# Function to get the transcript of a YouTube video
def get_transcript(video_id):
    """Fetches the transcript of a YouTube video."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript])
    except Exception as e:
        raise ValueError("Error fetching transcript:" + str(e))
    
# Function to get the thumbnail of a YouTube video
def get_video_thumbnail(youtube_url):
    """Constructs the YouTube thumbnail URL using the video ID."""
    try:
        video_id = get_video_id(youtube_url)  # Use your existing get_video_id function
        return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    except Exception as e:
        raise ValueError(f"Error constructing thumbnail URL: {str(e)}")

# Function to summarize the text using Azure OpenAI's
def summarize_text(text):
    """Sends the transcript to Azure OpenAI's for summarization."""
    try:
        client = AzureOpenAI(
        azure_endpoint = AZURE_OPENAI_ENDPOINT, 
        api_key=AZURE_OPENAI_KEY,
        api_version=API_VERSION
        )

        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME, 
            messages=[
                {"role": "assistant", "content": "With a professional tone, explain in detail the following transcript. Then include a summary of the main points. Finally include a separate detailed summary and a conclusion statement."},
                {"role": "user", "content": text}
            ],
            temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        raise ValueError("Error generating summary:"  + str(e))
    
# Function to summarize a transcript and return the result as HTML
def get_summarizeTranscript(transcript):
    return markdown.markdown(summarize_text(transcript))