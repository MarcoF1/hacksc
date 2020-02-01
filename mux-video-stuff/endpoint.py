import flask
import os
from mux import EmotionalVideos

app = flask.Flask(__name__)

@app.route("/video", methods=['POST'])
def return_video():
    """
    Endpoint for video playback
    """
    if flask.request.method == "POST":
        try:
            text = flask.request.args['text']
            video = EmotionalVideos(text).create_video_link()
            return video

        except Exception as e:
            return 'oops... something happened'

    return 'do a post request'

if __name__ == '__main__':
    app.run()
