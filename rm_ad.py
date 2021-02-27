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
        os.environ['SPOTIPY_CLIENT_ID'] = "2f72875a7a354192a519273c32154611"
        os.environ['SPOTIPY_CLIENT_SECRET'] = "c3c47fbc100c4c89a4096ad1e2a5ba34"
        os.environ['SPOTIPY_REDIRECT_URI'] = "http://example.com"

# Authorization Code Flow
#get user 
user = "31tdo3qit44oze5b4fmxpj4ewxzm"
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


schedule.every(1).minutes.do(task)
 
while True:
    schedule.run_pending()