# CCC_EVENT_VIDEO_DOWNLOADER
Downloads the live stream videos from the media.ccc.events site using the rss feed





# FEATURES
* keep X% free of disk space
* select events to download




# USAGE

## SETUP
* download this repo
* `$ cd ./src`
* `$ pip install requirements.txt`

## RUN

* `$ python ccc_rss_downloader.py`

* The script will create a new folder `./ccc_downloads`( `see line 18`) with the donwloaded videos in it.
In this folder a subfolder will be created with the name of the event.


* The amout of disk free disk space the script will leve free can be changed in `line 85`

* The script creates an `downloaded.txt` in which all file urls are collected. only if a video url is not in this file the video will be downlaoded. So you can easy delete a video after watching and the script will not download it again
## SPCIFY EVENT

To change/add an event you can extend the `event_regex`(`see line  31`) variable with the name/regex of the events you want to download
