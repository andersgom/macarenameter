import spotipy
from spotipy.oauth2 import SpotifyOAuth
import getpass
import pandas as pd
import numpy as np
from IPython import display


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


    if hit_score >= 3:
        #print(needs)

        return (1, 0,0,0)

    else:
        
        return needs


track =frame_maker('https://open.spotify.com/track/2MZSXhq4XDJWu6coGoXX1V?si=6b38baf17f9f4964')
print(track)

