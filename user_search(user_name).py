

# https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN

def user_search(user_name):                #get user id
    if user_name not in ['shafiqur.raghib', 'kunal_pathak21']:
        print"you enter wrong username"
        return
    else:

         url_user = base_url + "/users/search?q=" + user_name + "&access_token=" + access_token
         print url_user
        # https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
         user_detail = requests.get(url_user).json()
         success = user_detail["meta"]["code"]
         if success == 200:
               print "user detail found"
               print"the insta_username is :" + user_detail['data'][0]['full_name']
         else:
               print "user detail not found plz try again"
         return user_detail["data"][0]["id"]
                  # returning user id
