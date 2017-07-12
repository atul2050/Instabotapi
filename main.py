#This imorts the request
import requests
#We import base url and access token from another file called constant
import constants
#Here we take collection data from user
import self_info

# https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
import user_search

# print user_info['data'][0]['profile_picture']
# user_search("atul2050")
import  latest_post

#it is for making the like on te user id
import  like_user_post

# This is to check the comment on users post
import  comment_user_post

#for deleting the comment
import  delete_comment





print("\nHello User! Welcome to the Instabot Environment.")
choice = 1
while choice != '7':
    print("\nWhat do you want to do using the Instabot?")
    print("1. Information of user")
    print("2. Get the name of user.")
    print("3. Recent post of the user.")
    print("4. Like a post of the user.")
    print("5. Comment on post of the user.")
    print("6. Delete the comment containing a particular word.")
    print("7. Exit.\n\n")

    choice = input("Enter Your Choice(1-7) : ")   #choose the number you want

    user_name = raw_input("Enter the following users 1.shafiqur.raghib 2.kunal_pathak21")

        # Perform Actions Depending on the User's Choice. Runs Until User wishes to Exit.
        # if choice in ['1', '2', '3', '4', '5', '6', '7']:
    if int(choice) == 1:
        self_info()

    elif int(choice) == 2:
        user_search(user_name)

    elif int(choice) == 3:
        latest_post(user_name)


    elif int(choice) == 4:
        like_user_post(user_name)

    elif int(choice) == 5:
        comment_user_post(user_name)

    elif int(choice) == 7:
        delete_comment(user_name)

    else:
        print('Exit')
