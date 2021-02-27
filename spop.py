import requests

CLIENT_ID = '2f72875a7a354192a519273c32154611'
CLIENT_SECRET = 'c3c47fbc100c4c89a4096ad1e2a5ba34'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token="access_token")
}

BASE_URL = 'https://api.spotify.com/v1/31tdo3qit44oze5b4fmxpj4ewxzm/player/currently-playing'

# Track ID from the URI
track_id = '6y0igZArWVi6Iz0rj35c1Y'

# actual GET request with proper header
r = requests.get(BASE_URL, headers=headers)

r = r.json()

print(r)