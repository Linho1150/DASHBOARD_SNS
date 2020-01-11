import requests
import time
import os

def kill_process():
    os.system("taskkill /f /im chrome.exe")
def open_proecess():
    filepath = "GUI\index.html"
    os.startfile(filepath)

def save_html(YF,IF):
    f = open("GUI\index.html","w")
    f.write("""
    <!doctype html>
    <html lang="en">
      <head>
      <link href="css/bootstrap.min.css" rel="stylesheet">
        <style>
          .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
          }
    
          @media (min-width: 768px) {
            .bd-placeholder-img-lg {
              font-size: 3.5rem;
            }
          }
        </style>
       <link href="cover.css" rel="stylesheet">
      </head>
    
    <body class="text-center">
        <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
          <h3 class="masthead-brand">Myongji University MJUPR</h3>
    
      <header class="masthead mb-auto">
        <div class="inner">
          <nav class="nav nav-masthead justify-content-center">
          </nav>
        </div>
      </header>
    
      <main role="main" class="inner cover">
        <h1 class="cover-heading" style="font-size: 3em">YOUTUBE SUBSCRIBER : """+str(YF)+"""</h1>
        <h1 class="cover-heading" style="font-size: 3em">INSTAGRAM FOLLOWERS : """+str(IF)+"""</h1>
      </main>
    
      <footer class="mastfoot mt-auto">
        <div class="inner">
          <p style="font-size: 1.5em">Myongji University</p>
        </div>
      </footer>
    </div>
    </body>
    </html>
    
    """)

def get_api():
    f = open(".idea/api_num.txt", "r")
    API = f.readline()
    return API

def IF(BINSTA):
    #instagram_api
    data=requests.get("https://www.instagram.com/myongji_univ/?__a=1").json()
    INSTA=data["graphql"]["user"]["edge_followed_by"]["count"]

    if(int(BINSTA)<int(INSTA)):
        return str(INSTA)+" ↑",INSTA
    elif(int(BINSTA)>int(INSTA)):
        return str(INSTA)+" ↓",INSTA
    else:
        return "",0

def YS(BYOUTUBE,API):
    #youtube_api
    data=requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCYuO1dJiQ_MSCrOEO8UmzDA&key="+API).json()
    YOUTUBE=data["items"][0]["statistics"]["subscriberCount"]
    if(int(BYOUTUBE)<int(YOUTUBE)):
        return str(YOUTUBE)+" ↑",YOUTUBE
    elif(int(BYOUTUBE)>int(YOUTUBE)):
        return  str(YOUTUBE)+" ↓",YOUTUBE
    else:
        return "",0

BINSTA=0
BYOUTUBE=0
API=str(get_api())
while(True):
    time.sleep(1)
    INSTA_str,INSTA=IF(BINSTA)
    YOUTUBE_str,YOUTUBE=YS(BYOUTUBE,API)
    INSTA_str, YOUTUBE_str = str(INSTA_str),str(YOUTUBE_str)
    if INSTA==0 and YOUTUBE==0:
        pass
    elif INSTA==0 and YOUTUBE!=0:
        save_html(BINSTA, YOUTUBE_str)
        kill_process()
        open_proecess()
        BYOUTUBE=int(YOUTUBE)
    elif INSTA!=0 and YOUTUBE==0:
        save_html(INSTA_str,BYOUTUBE)
        kill_process()
        open_proecess()
        BINSTA=int(INSTA)
    elif INSTA!=0 and YOUTUBE!=0:
        save_html(INSTA_str,YOUTUBE_str)
        kill_process()
        open_proecess()
        BYOUTUBE=int(YOUTUBE)
        BINSTA=int(INSTA)