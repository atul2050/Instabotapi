#This imorts the request
import requests
#We import base url and access token from another file called constant
from constants import base_url ,access_token
from latest_post(user_name) import latest_post(user_name)

def comment_user_post(user_name):
    post_id = latest_post(user_name)
    request_url = (base_url + "/media/%s/comments?access_token=%s") % (post_id, access_token)
    request = requests.post(request_url).json()
    if request['meta']['code'] == 200:
        print("comment added ")
        print request  ["data"]["text"]
    else:
        print("comment not added try again")
     #return request["data"]["id"]

