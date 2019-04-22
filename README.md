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

The script will create a new folder `./ccc_downloads`( `see line 18`) with the donwloaded videos in it.


## SPCIFY EVENT

To change/add an event you can extend the `event_regex`(`see line  31`) variable with the name/regex of the events you want to download
