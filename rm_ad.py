import os
import schedule
import applescript
import spotipy.util as util
import spotipy

class SetCreditentials:

    def __init__(self):
        self.CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
        self.CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
        self.REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
        os.environ['SPOTIPY_CLIENT_ID'] = "Insert-client_id"
        os.environ['SPOTIPY_CLIENT_SECRET'] = "insert_client_secret"
        os.environ['SPOTIPY_REDIRECT_URI'] = "http://example.com"

# Authorization Code Flow
#get user 
user = "spotify username"
scope = "user-read-currently-playing"

def task():
    SetCreditentials()
    token = util.prompt_for_user_token(user, scope)
    track = spotipy.Spotify(token).current_user_playing_track()
    print(track['currently_playing_type'])
    if(track['currently_playing_type']=='ad'):
        #add setVoulme for linux
        applescript.AppleScript("set volume output volume 0").run()
    else:
        applescript.AppleScript("set volume output volume 100").run()


schedule.every(10).seconds.do(task)
 
while True:
    schedule.run_pending()
