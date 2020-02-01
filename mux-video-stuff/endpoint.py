import flask
import os


app = flask.Flask(__name__)

@app.route("/video", methods=['POST'])
def return_video():
    """
    Endpoint for video playback
    """
    if flask.request.method == "POST":
        try:
            text = flask.request.args['text']
            #do something to go from text to video


            video = 'https://stream.mux.com/FXRjTHA015GdymQokn5XjcVzOvCY00ul9V.m3u8'
            return video

        except Exception as e:
            return 'oops... something happened'

    return 'do a post request'

if __name__ == '__main__':
    app.run()
