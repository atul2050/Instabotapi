import requests
from constants import base_url ,access_token


def self_info():                      #getting the collection of user
    url = base_url + "/users/self/?access_token=" + access_token
    my_info = requests.get(url).json()
    print my_info
    print my_info["data"]["full_name"]
    print my_info["data"]["profile_picture"]
    print my_info["data"]["bio"]
    print my_info["data"]["counts"]["followed_by"]
    print my_info["data"]["counts"]["follows"]

