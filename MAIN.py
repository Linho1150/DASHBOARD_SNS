import requests

#instagram_api
data=requests.get("https://www.instagram.com/myongji_univ/?__a=1").json()
print(data["graphql"]["user"]["edge_followed_by"]["count"])

f=open(".idea/api_num.txt","r")
API=f.readline()

#youtube_api
data=requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCYuO1dJiQ_MSCrOEO8UmzDA&key="+API).json()
print(data["items"][0]["statistics"]["subscriberCount"])

