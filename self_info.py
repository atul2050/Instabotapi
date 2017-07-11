#This imorts the request
import requests
#We import base url and access token from another file called constant
from constants import base_url ,access_token

#Here we take collection data from user
def self_info():
    url = base_url + "/users/self/?access_token=" + access_token
    my_info = requests.get(url).json()
    print my_info
    print my_info["data"]["full_name"]
    print my_info["data"]["profile_picture"]
    print my_info["data"]["bio"]
    print my_info["data"]["counts"]["followed_by"]
    print my_info["data"]["counts"]["follows"]

