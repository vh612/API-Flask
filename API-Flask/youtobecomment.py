#!/usr/bin/env python3
# -*- coding: utf-8 -*-
######################

from googleapiclient.discovery import build

#credentials https://console.developers.google.com/

api_key ="AIzaSyDd26Z5vegl9tVe6uMuoD2JvgtOAz5n5i8"  #google cloud platform
video_id= "jO6aaLMrVTc"

#build a resource for youtube
resource = build('youtube', 'v3', developerKey=api_key)

#create a request to get 20 comments on the video
request = resource. commentThreads().list(
                            part="snippet",
                            videoId=video_id,
                            order="orderUnspecified")  #top comments.
#execute the request
response =request.execute()

#get first 10 items for from 20 comments 
items = response["items"][:10]

print("------------------------------------------------------------------------------------------------------")
for item in items:
    item_info = item["snippet"]
    
    #the top level comment can have sub reply comments
    topLevelComment = item_info["topLevelComment"]
    comment_info = topLevelComment["snippet"]
    
    print("Comment By:", comment_info["authorDisplayName"])
    print("Coment Text:" ,comment_info["textDisplay"])
    print("Likes on Comment :", comment_info["likeCount"])
    print("Comment Date: ", comment_info['publishedAt'])
    print("================================\n")
