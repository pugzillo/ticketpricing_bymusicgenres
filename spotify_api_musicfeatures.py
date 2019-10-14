import logging
import random
import sys
import spotipy
import os
import time
import numpy as np
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import os.path
import multiprocessing

# spotify credentials
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# open the file and read the contents-List of artists to find discography
f = open("ticket_concert_artists.csv")
lines = f.readlines() # don't read in header
results = []

for x in lines:
    results.append(x.split(',')[0])

f.close()

random.shuffle(results)
# results.sort()
# print(results)

# failed_searches = [] 

## Get discography for each artists
logging.basicConfig(format='%(asctime)s %(message)s')

def runTask(arg):
        nameI, name = arg
        logging.warning(nameI)
        name = name.rstrip()
        file_name = '%s_SongInfo.csv' % name
        if os.path.exists(file_name):
            print("results exist for " + str(file_name))
            return
        print("Attempting search for " + str(name))
        # result = sp.search(q='artist:%s genre:k-pop' % name) #search query for kpop
        result = sp.search(q='artist:%s' % name)

        # failed searches, stop them if query is not found on spotify
        # if not result['tracks']['items']:
        #         failed_searches.append(name)
        #         continue

        # extract the Artist's uri (spotify artist ID)
        uri = result['tracks']['items'][0]['artists'][0]['uri']

        # pull all of the artist's albums
        sp_albums = sp.artist_albums(uri)

        # #Store artist's albums' names' and uris 
        album_names = []
        album_uris = []
        album_release_date = []

        for i in range(len(sp_albums['items'])):
                album_names.append(sp_albums['items'][i]['name'])
                album_uris.append(sp_albums['items'][i]['uri'])
                album_release_date.append(sp_albums['items'][i]['release_date'])

        spotify_albums = {}

        # function to get song from album
        def albumSongs(uri, album, album_name, album_release_dt):
                spotify_albums[uri] = {} #Creates dictionary for that specific album
        #         print(spotify_albums[uri])

                ## Create keys-values of empty lists inside nested dictionary for album
                spotify_albums[uri]['album'] = [] #create empty list
                spotify_albums[uri]['track_number'] = []
                spotify_albums[uri]['id'] = []
                spotify_albums[uri]['name'] = []
                spotify_albums[uri]['uri'] = []
                spotify_albums[uri]['release_date'] = []

                tracks = album['tracks']

                for n in range(len(tracks['items'])): #for each song track
        #                 print(tracks['items'][n])
                        spotify_albums[uri]['album'].append(album_name)
                        spotify_albums[uri]['track_number'].append(tracks['items'][n]['track_number'])
                        spotify_albums[uri]['id'].append(tracks['items'][n]['id'])
                        spotify_albums[uri]['name'].append(tracks['items'][n]['name'])
                        spotify_albums[uri]['uri'].append(tracks['items'][n]['uri'])
                        spotify_albums[uri]['release_date'].append(album_release_dt)

        # ALBUM ------

        albums = sp.albums(album_uris)['albums']
        for i, val in enumerate(zip(album_uris, albums)):
                uri, album = val
                albumSongs(uri, album, album_names[i], album_release_date[i])

        # function to get audio features per song
        def audio_features(album):
        #Add new key-values to store audio features
                def add_key_vals(prop):
                        spotify_albums[album][prop] = []
                for prop in [
                        'acousticness',
                        'danceability',
                        'energy',
                        'instrumentalness',
                        'liveness',
                        'loudness',
                        'speechiness',
                        'tempo',
                        'valence',
                        'popularity'  
                ]:
                        add_key_vals(prop)

                # TRACK FEATURES -------

                #audio features per track
                def getFeatures(arg, numTries=0):
                        if numTries == 3:
                                return None
                        try:
                                features = sp.audio_features(arg)
                                return features
                        except Exception:
                                logging.error(arg)
                                time.sleep(1)
                                return getFeatures(arg, numTries + 1)
                features = getFeatures(spotify_albums[album]['uri'])
                if features is None:
                        raise Exception()

                #Append to relevant key-value
                def append_song_features(spotify_albums, album, features, prop):
                        for feature in features:
                                if not feature:
                                        spotify_albums[album][prop].append("NA")
                                        continue
                                if prop in feature:
                                        spotify_albums[album][prop].append(feature[prop])
                                else:
                                        spotify_albums[album][prop].append("NA")
                for prop in [
                        'acousticness',
                        'danceability',
                        'energy',
                        'instrumentalness',
                        'liveness',
                        'loudness',
                        'speechiness',
                        'tempo',
                        'valence',
                ]:
                        append_song_features(spotify_albums, album, features, prop)

                pops = sp.tracks(spotify_albums[album]['uri'])['tracks']
                for pop in pops:
                        spotify_albums[album]['popularity'].append(pop['popularity']) # popularity is not stored in prop

        # time the api requests
        start_time = time.time()
        request_count = 0
        for i in spotify_albums:
                try:
                        audio_features(i)
                except Exception:
                        continue
                request_count+=1
                if request_count % 10 == 0:
                        print(str(request_count) + " playlists completed")
                        # "The reason why it isn't disclosed is because this number may change without warning. Using Retry-After should be enough to be able to write an application that handles being rate limited. That said, counting on having somewhere around 10-20 requests per second would put you in the correct ballpark"
                        # https://stackoverflow.com/questions/30548073/spotify-web-api-rate-limits
                        print('Loop #: {}'.format(request_count))
                        print('Elapsed Time: {} seconds'.format(time.time() - start_time))

        dic_df = {}
        def make_dictionary(prop):
                dic_df[prop] = []
        
        for prop in [
                'album',
                'track_number',
                'id',
                'name',
                'uri',
                'release_date',
                'acousticness',
                'danceability',
                'energy',
                'instrumentalness',
                'liveness',
                'loudness',
                'speechiness',
                'tempo',
                'valence',
                'popularity'
        ]:
                make_dictionary(prop)
        
        for album in spotify_albums: 
                for feature in spotify_albums[album]:
                        dic_df[feature].extend(spotify_albums[album][feature])
                
        df = pd.DataFrame.from_dict(dic_df)
        df['artist'] = name

        final_df = df.sort_values('popularity', ascending=False).drop_duplicates('name').sort_index()

        # print out file with song information for the artist
        final_df.to_csv('%s_SongInfo.csv' % name)

with multiprocessing.Pool() as workers:
        workers.map(runTask, enumerate(results))

# failed_search_df = pd.DataFrame(failed_searches) 
# failed_search_df.to_csv('Failed_Searches_ticket_artists.csv') #file with the failed queries