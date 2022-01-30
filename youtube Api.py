# libraries
import requests
import pandas as pd


# keys
API_KEY = "AIzaSyDHd5rPHXz5N5xZgwzezvA0PnOodEFJix0"
CHANNEL_ID = "UCZM-BXS5DOWUWDDwoS22_qw"


# functions
def get_video_details(video_id):
    # collecting view, like, comment counts
    url_video_stats = "https://www.googleapis.com/youtube/v3/videos?id=" + video_id \
                      + "&part=statistics&key=" + API_KEY
    response_video_stats = requests.get(url_video_stats).json()

    view_count = response_video_stats['items'][0]['statistics']['viewCount']
    like_count = response_video_stats['items'][0]['statistics']['likeCount']

    return view_count, like_count


def get_videos(df):
    pageToken = ""
    while 1:
        url = "https://www.googleapis.com/youtube/v3/search?key=" + API_KEY\
              + "&channelId=" + CHANNEL_ID \
              + "&part=snippet,id&order=date&maxResults=10000&" + pageToken

        response = requests.get(url).json()
        for video in response['items']:
            if video['id']['kind'] == "youtube#video":
                video_id = video['id']['videoId']
                video_title = video['snippet']['title']
                video_title = str(video_title).replace("&amp;", "")
                upload_date = video['snippet']['publishedAt']
                upload_date = str(upload_date).split("T")[0]
                view_count, like_count = get_video_details(video_id)
                df2 = pd.DataFrame([[video_id, video_title, upload_date, view_count, like_count]],
                                   columns=['video_id', 'video_title', 'upload_date',
                                            'view_count', 'like_count'])

                df = pd.concat([df, df2])
        try:
            if response['nextPageToken'] is not None:
                pageToken = "pageToken=" + response['nextPageToken']

        except:
            break
    return df


# main
data = pd.DataFrame(
    columns=["video_id", "video_title", "upload_date", "view_count", "like_count"])
print("Code starts")
data = get_videos(data)
print("Code is Ok")
data.to_csv('youtube_vids.csv')

