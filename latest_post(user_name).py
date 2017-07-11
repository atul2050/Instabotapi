#This imorts the request
import requests
#We import base url and access token from another file called constant
from constants import base_url ,access_token

   

# print user_info['data'][0]['profile_picture']
# user_search("atul2050")

def latest_post(user_name):
    user_id = user_search(user_name)
    url_user = base_url + "/users/" + str(user_id) + "/media/recent/?access_token=" + access_token

    # https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
    latest_post = requests.get(url_user).json()
    print "latest post entered by user is:" + latest_post["data"][0]["link"]
    return latest_post["data"][0]["id"]
