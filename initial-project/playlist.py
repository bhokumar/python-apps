playlist = {
    'title': 'patagonia bus',
    'author': 'Bhoopendra',
    'songs': [
        {'title': 'Song1', 'artist': ['blue'], 'duration': 30.5},
        {'title': 'Song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
        {'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
    ]
}

for song in playlist["songs"]:
    print(song['duration'])