import requests
import os

YTAPI_KEY = os.environ['YTAPI']

def getSuggestedVideo(videoId):
    r = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=id&relatedToVideoId={videoId}&type=video&maxResults=1&key={YTAPI_KEY}")
    if r.status_code == 200:
        try:
            suggestedVideoId = r.json()['items'].pop()['id']['videoId']
            return getYoutubeURL(suggestedVideoId)
        except Exception as error:
            print("Something went bad:", error)
    else:
        print("Status code:", r.status_code)
    return None

def getYoutubeURL(videoId):
    return "https://www.youtube.com/watch?v=" + videoId
