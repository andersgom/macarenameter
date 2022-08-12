import spotipy
from spotipy.oauth2 import SpotifyOAuth
import getpass
import pandas as pd
import numpy as np



client_id = '94c7d23dac2a4225a3ecb57cce99966c' #getpass.getpass()
client_secret = "5a0d909aa4f74df9b98153f5a6cd4a60" # getpass.getpass()



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri="https://localhost:8089/callback",
                                               scope="user-library-read"))



conf_intervals = pd.read_csv('confidence_intervals.csv', index_col='trait')



## Functions 

def frame_maker(link):

    df = pd.DataFrame(sp.audio_features(link))

    df[['Hit', 'Dance_miss', 'Energy_miss', 'Valence_miss']] = df.apply(hit_detector,axis = 1, result_type='expand')

    return df




def hit_detector(row):

    hit_score = 0
    needs = np.array([0, 0, 0, 0])

    traits = ['danceability', 'energy', 'valence']


    for trait in traits:
        
    

        if row[trait] >= conf_intervals.loc[trait, 'bottom']: # (abs(row[trait]) < abs(conf_intervals['top'][traits.index(trait)])):


            hit_score += 1
            
            #print(trait, row[trait])
        
        else:
            hit_score += 0

            if trait == 'danceability':
                needs += np.array([0,1,0,0])
            elif trait == 'energy':
                needs += np.array([0,0,1,0])
            elif trait == 'valence':
                needs += np.array([0,0,0,1])
                
            #needs.append(trait)
            #print(trait,conf_intervals['bottom'][traits.index(trait)],conf_intervals['top'][traits.index(trait)])

            #print(trait, row[trait])

    if row['mode'] == 1:
        hit_score += 0.5
    else:
        hit_score += 0


    if hit_score >= 2.5:
        #print(needs)

        return (1, 0,0,0)

    else:
        
        return needs


def playlist_dataframe(playlist_link):

    playlist_URI = playlist_link.split("/")[-1].split("?")[0]

    track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]] 

    df = pd.DataFrame(columns=['artist_name','track_name','album_name','release_date','artist_popularity','track_popularity', 'artist_genres','danceability',
    'energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','type','id','uri','track_href','analysis_url',
    'duration_ms','time_signature'])



    for track in sp.playlist_tracks(playlist_URI)["items"]:

        info_vector = []
        #URI
        track_uri = track["track"]["uri"]
        
        #Track name
        track_name = track["track"]["name"]
        
        #Main Artist
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)
        
        #Name, popularity, genre
        artist_name = track["track"]["artists"][0]["name"]
        artist_pop = artist_info["popularity"]
        artist_genres = artist_info["genres"]
        
        #Album
        album = track["track"]["album"]["name"]
        #Release Date
        release_date = track['track']['album']['release_date'] ## keep full date 

        #Popularity of the track
        track_pop = track["track"]["popularity"]

        info_vector = [artist_name,track_name,album,release_date,artist_pop,track_pop,artist_genres]

        info_vector.extend(list((sp.audio_features(track_uri)[0].values())))


        df.loc[len(df)] = info_vector

    df[['Hit', 'Dance_miss', 'Energy_miss', 'Valence_miss']] = df.apply(hit_detector,axis = 1, result_type='expand')

    return df



track =frame_maker('https://open.spotify.com/track/2MZSXhq4XDJWu6coGoXX1V?si=6b38baf17f9f4964')
print(track)

playlist = playlist_dataframe('https://open.spotify.com/playlist/08FwuC2mWOk78HgL30lvk8?si=330dafcc50e24282')
print(playlist)