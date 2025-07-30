# YouTube Summarizer Ver 1.0

# Description: This is the main file that runs the Flask web application.
from flask import Flask, request, render_template
import SummarizeYoutube as sy
 
# Create the Flask app
app = Flask(__name__) 
 
# Define the routes
@app.route('/hello')
def hello():
    return 'Hello, World'

# Define the index route
@app.route('/', methods=['GET', 'POST'])
def index():
    
    # Initialize the variables
    video_url = ''
    result = ''
    videothumbnail = ''
    transcript = ''
    error_message = ''
    
    # Check if the form is submitted
    if request.method == 'POST':

        try:
            # Get the video URL from the form
            video_url = request.form.get('video_url')

            #get the video thumbnail
            videothumbnail= sy.get_video_thumbnail(video_url)

            # Get the video ID
            video_id = sy.get_video_id(video_url)
            
            # Get the video Transcript
            transcript = sy.get_transcript(video_id)

            # Summarize the video Transcript
            result = sy.get_summarizeTranscript(transcript);
        
        except Exception as e:
            error_message = "There was an error processing your request. Please ensure you have entered a valid YouTube video URL and try again."
            result = ''
            videothumbnail = ''
            transcript = ''

    return render_template('index.html', video_url=video_url,result=result, videothumbnail=videothumbnail, transcript=transcript, error_message=error_message)

if __name__ == '__main__':
    #app.run(debug=True)    
    app.run(debug=True, host="0.0.0.0", port=80)