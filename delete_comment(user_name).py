#This imorts the request
import requests
#We import base url and access token from another file called constant
from constants import base_url ,access_token
from latest_post(user_name) import latest_post(user_name)
from comment_user_post(user_name) import comment_user_post(user_name)

#for deleting the comment
def delete_comment(user_name):
    post_id = latest_post(user_name)
    comment_id = comment_user_post(user_name)
    request_url = base_url + "/media/" + post_id + "/comments/" + comment_id + "?access_token=" + access_token
    request_comment = requests.delete(request_url).json()
    if request_comment['meta']['code'] == 200:
        print("your comment is deleted")
        # print comments
    else:
        print("Some error occurred! Try Again.")
        print request_comment
