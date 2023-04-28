import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="544ca8430c1848549771871cf9ad5c8c",
                                                client_secret="6ec4cf71a160418aac67bcc792df1b19",
                                                redirect_uri="http://localhost:8000/callback",
                                                scope="user-library-read"))

playlist_id = "https://open.spotify.com/playlist/5wvQJiyu37XLAgfkygyFVg?si=19a2a199092c465d"
results = sp.playlist_tracks(playlist_id)

artists = {}
for track in results['items']:
    artist_list = track['track']['artists']
    for artist in artist_list:
        name = artist['name']
        if name not in artists:
            artists[name] = 1
        else:
            artists[name] += 1

top_artists = sorted(artists.items(), key=lambda x:x[1], reverse=True)[:10]

print("Top artists from your playlist:")
for artist in top_artists:
    print(artist[0], "-", artist[1], "songs")