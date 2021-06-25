from redvid import Downloader
from imgr import resizer
from imgr import imager
import requests
import os

def Scrapper(timeslooped):
    try:
        rqsturl = "https://www.reddit.com/top/.json"
        page = requests.get(url=rqsturl, headers={'User-agent': 'yourmother'}).json()
        page_data = page["data"]["children"]
        path = "C:\\Users\\john\\PycharmProjects\\AutomatedGmail\\memes"
        count = 0
        while count < timeslooped:
            url = page_data[count]["data"]["url"]
            title = page_data[count]["data"]["title"]
            if (len(title) > 50):  # 221
                while (len(title) > 50):  # 221
                    title_list = title.split()
                    title_list.pop()
                    title = " ".join(title_list)
            if('\"', "/", ":", "*", "?", '"', "<", ">", "|" in title):
                title = title.replace('\"', '')
                title = title.replace("/", "")
                title = title.replace(":", "")
                title = title.replace("*", "")
                title = title.replace("?", "")
                title = title.replace('"', '')
                title = title.replace("<", "")
                title = title.replace(">", "")
                title = title.replace("|", "")
            if ((page_data[count]["data"]["is_video"] == True) and (page_data[count]["data"]["media"]["reddit_video"]["duration"] <= 60)):
                video_title = title + ".mp4"
                video_path = "\\" + video_title
                new_path = path + video_path
                download = Downloader(max_q=True, path=path, url=url)
                download.download()
                os.rename(download.file_name, new_path)
                print("Video Status: Downloaded")
            else:
                try:
                    new_path = imager(url=url, file_path=path, file_name=title)
                    resizer(new_path)
                    print("Photo Status: Downloaded")
                except:
                    print("Photo Status: Not Downloaded")
            count += 1
        print("Scraping: Finished")
    except:
        print("Subreddit Does Not Exist")

