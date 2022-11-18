"""
Preliminaries:
Run this in the terminal:
   pip install flask

Documentation:
https://flask.palletsprojects.com/en/2.1.x/quickstart/
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/<videoid>')
def writeThings(videoid):
    # type: (str) -> str
    if videoid == "favicon.ico":
        return ""
    if videoid == "watch":
        return "INVALID ID."
    f = open(f"ip_{request.remote_addr}.txt", "a")
    f.write(videoid + "\n")
    f.close()
    return f"Added {videoid} to queue."

  
@app.route('/')
def main():
    return "Usage: /video-id-from-youtube <br/>Example: http://192.168.240.180:5000/4fWyzwo1xg0"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
