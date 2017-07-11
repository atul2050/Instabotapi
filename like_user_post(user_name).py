#This imorts the request
import requests
#We import base url and access token from another file called constant
from constants import base_url ,access_token


#it is for making the like on te user id
def like_user_post(user_name):
    post_id = latest_post(user_name)
    payload = {"access_token": access_token}
    request_url = base_url + "/media/" + post_id + "/likes"
    response_to_like = requests.post(request_url, payload).json()
    if response_to_like['meta']['code'] == 200:
        print ("pic has been liked")
        # print response_to_like
    else:
        print("Something went wrong! Please do it again")
