from youtube_api import YouTubeDataAPI
from api_keys import youtube_api

print("This program allows you to get the five most recent videos of a musician from his/her/their YouTube channel as well as the lyrics for those songs.")
musician = input("Enter the name of the musician: ")

yt = YouTubeDataAPI(youtube_api)
video_data = yt.search(q=musician, max_results=5)

print("Musician: " + musician)
print("These are the five most recent videos from " + musician + ".")

video_num = 0
for video_num in range(5):
	print("Video #" + str(video_num+1) + ": " + video_data[video_num]["video_title"])

