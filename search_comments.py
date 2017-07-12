#This imorts the request
import requests
#We import base url and access token from another file called constant
from constants import base_url ,access_token
from latest_post import latest_post

#for searching the comment
def search_comments(user_name):
    post_id = latest_post(user_name)
    request_url = base_url + "/media/" + post_id + "/comments?access_token=" + access_token
    request_comment = requests.get(request_url).json()
    return request_comment["data"][0]["id"]
        # print request_comment["data"][0]["text"]
