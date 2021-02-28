import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pprint as ptp

credentials = json.load(open('Pyhton\Authorization.json'))
client_id = credentials['client_id']
client_secret = credentials['client_secret']

client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlistURI = "spotify:user:Test_1:playlist:1D5LexDULlKdpxwVHNWdL3"
splitURI= playlistURI.split(':')
username = splitURI[2]
playlist_id = splitURI[4]

results = sp.user_playlist(username, playlist_id, 'tracks')
for i in range(0, len(results['tracks']['items'])):
    print(results['tracks']['items'][i]['track']['name'])
