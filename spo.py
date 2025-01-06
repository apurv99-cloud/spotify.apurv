from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock data for songs
songs = [
    {"id": 1, "title": "Blinding Lights", "artist": "The Weeknd", "url": "/static/songs/blinding_lights.mp3", "image": "/static/images/blinding_lights.jpg"},
    {"id": 2, "title": "Levitating", "artist": "Dua Lipa", "url": "/static/songs/levitating.mp3", "image": "/static/images/levitating.jpg"},
    {"id": 3, "title": "Peaches", "artist": "Justin Bieber", "url": "/static/songs/peaches.mp3", "image": "/static/images/peaches.jpg"},
]

@app.route("/")
def home():
    return render_template("index.html", songs=songs)

@app.route("/songs")
def get_songs():
    return jsonify(songs)

if __name__ == "__main__":
    app.run(debug=True)
