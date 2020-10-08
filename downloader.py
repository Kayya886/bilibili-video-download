import requests
import json
import subprocess
import os
import math
from you_get import common

GET_VIDEO_LIST_URL = "https://api.bilibili.com/x/space/arc/search"

def getVideos(mid, page):
    videoList = []
    response = requests.get(GET_VIDEO_LIST_URL,
                            {
                                "mid": mid,
                                "pn": page
                            }).json()
    # print(response)
    datas = response['data']['list']['vlist']
    for data in datas:
        videoList.append(data['bvid'])
    return videoList

def getVideoList(mid, page_num):
    list = []
    for page in range(1, page_num + 1):
        # print(page)
        videos = getVideos(mid, page)
        for video in videos:
            list.append(video)
    return list

def getVideoPageNum(mid):
    response = requests.get(GET_VIDEO_LIST_URL,
                            {
                                "mid": mid
                            }).json()
    return math.ceil(response['data']['page']['count'] // response['data']['page']['pn'])


if __name__ == "__main__":
    # Change your bilibili space code here
    # up id
    mid = 344849038
    print("=== up space number is " + str(mid) + " ===")
    os.system('pause')

    pageNum = getVideoPageNum(mid)
    print("===get ", pageNum, " pages of videos===")

    #BVID list
    videoList = getVideoList(mid, pageNum)
    # print(videoList)
    lenV = len(videoList)

    for i, bvid in enumerate(videoList):
        print("=========     downloading video " + str(i + 1) + ' of ' + str(lenV) + "   =========")
        common.any_download(url=('https://www.bilibili.com/video/'+bvid), info_only=False, output_dir=r'D:\OneDrive\Media\Videos', merge=True)

    print("=== all videos downloaded~~~ ===")
