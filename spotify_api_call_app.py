import token
from requests import post ,get
import base64
import os
from dotenv import load_dotenv
import json

load_dotenv()
client_id = os.getenv("CLIENT_ID")#id :O
client_secret = os.getenv("CLIENT_SECRET")#shhhhh


def get_token():
    auth_string = client_id + ":" + client_secret #encode this to utf-8 --|
    auth_bytes = auth_string.encode("utf-8")      #<-----------------------  
    auth_base = str(base64.b64encode(auth_bytes), "utf-8")#spotify told to do this idk why

    url = "https://accounts.spotify.com/api/token"#endpoint to request access token

    headers = {# cool headers
        "Authorization":"Basic " + auth_base,
        "Content-Type":"application/x-www-form-urlencoded"#spotify correct
    }
    data = {"grant_type": 'client_credentials'}#???
    result = post(url,headers=headers,data=data)# token here
    if result.status_code == 200:#200 means success btw
        json_result = json.loads(result.content) #token convertd to python object
        return json_result["access_token"]#the token returned to the function call
    else:
        print(f"Error getting token. Status Code: {result.status_code}")
        print(f"Response: {result.text}")
        return None # Return None on failure to prevent further errors
def get_header(token):
    return {"Authorization":"Bearer " + token}#header to be sent given in spoitfy api docs

    
def get_artist_details(token,artist_name):
    base_url = "https://api.spotify.com/v1/search"#the base endpoint for artist info
    query = f"?q={artist_name}&type=artist&limit=1"#query string
    url = base_url+query



    if token is None:
        print("Failed to retrieve token. Exiting.")
        return
    
    
    headers = get_header(token)
        
    
    artist = get(url = url,headers=headers)#wow a http get request :O
    json_result = json.loads(artist.content)["artists"]["items"]#converting json to python object(deserializing)
    if not json_result: # Check if the list is empty
        print(f"No artist found with the name: {artist_name}")
        return None
    
    return json_result[0] 

def get_album_details(token,album_name):
    base_url = "https://api.spotify.com/v1/search"#the base endpoint for artist info
    query = f"?q={album_name}&type=album&limit=1"#query string
    url = base_url+query
    


    if token is None:
        print("Failed to retrieve token. Exiting.")
        return
    
    headers = get_header(token)
        
    
    artist = get(url = url,headers=headers)#wow a http get request :O
    json_result = json.loads(artist.content)["albums"]["items"]#converting json to python object(deserializing)
    if not json_result: # Check if the list is empty
        print(f"No artist found with the name: {album_name}")
        return None
    return json_result[0] 

def get_songs(token,id):
    url = f"https://api.spotify.com/v1/artists/{id}/top-tracks?country=US"
    headers = get_header(token)
    result = get(url = url,headers=headers)
    json_result = json.loads(result.content)["tracks"]
    if not json_result: # Check if the list is empty
        print(f"No songs found for artist ID: {id}")
        return None
    return json_result
def get_albumsongs(token,id):
    url = f"https://api.spotify.com/v1/albums/{id}"
    headers = get_header(token)
    result = get(url = url,headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    if not json_result: # Check if the list is empty
        print(f"No tracks found for album ID: {id}")
        return None
    return json_result
"""<<<-------------------------------------------------------------------------->>>"""


if __name__ == "__main__"  :  
        token = get_token()#get the token first

        name = input("enter artist name: ")
        result = get_artist_details(token,name)
        artist_id = result["id"]# we can use this id to get songs of artist
        songs = get_songs(token,artist_id)

        for i , song in enumerate(songs,start=1):
                    print(f"{i}. {song['name']}")

        album_name = input("enter album name")
        result_2 = get_album_details(token , album_name)
        album_id = result_2["id"]
        albums = get_album(token ,album_id)

        for i , album in enumerate(albums,start=1):
                    print(f"{i}. {album['name']}")

    
    

    

"""idx = 1
for song in songs:

    print(f"{idx}. {song['name']}")
    idx +=1"""


