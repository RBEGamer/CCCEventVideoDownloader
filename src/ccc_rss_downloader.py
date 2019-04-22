import feedparser
import os
import unicodedata
import re
import wget
import psutil




def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

root_folder = "ccc_downloads"
createFolder(root_folder)
NewsFeed = feedparser.parse("https://media.ccc.de/updates.rdf")
entrys = NewsFeed.entries




linklist =[]
filename = []
event = []


event_regex = [
    "[a-zA-Z]*[(]eh\d\d[)][a-zA-Z]*",  #EH
    "[a-zA-Z]*[(]subscribe10[)][a-zA-Z]*",  #subscribe10
    "[a-zA-Z]*[(]\d\d[cC][3][)][a-zA-Z]*",  #35c3 , XXc3
    "[a-zA-Z]*[(]\d\d[cC][3]-chaoswest[)][a-zA-Z]*",  #XXC3-chaoswest
    "[a-zA-Z]*[(]fossgis\d\d\d\d[)][a-zA-Z]*"  #fossgis2019
]
#PARSE RSS FEED
for entry in entrys:

    #save filename
    t = unicodedata.normalize('NFKD', entry.title).encode('ascii', 'ignore')
    t = t.replace(" ", "_")


    #get event
    ev = "no_category"
    for reg in event_regex:
        #print entry.title
        f = re.search(reg, entry.title)
        if f:
            found = f.group(0)
            found = found.replace(")", "")
            found = found.replace("(", "")
            ev = found
            pass


    if not t in filename:
        #SAVE FILES TO DOWNLOAD TO ARRAY
        filename.append(t)
        event.append(ev)
        linklist.append(entry.link)
        print(t)
    else:
        continue




#CREATE FOLDERS FOR EVENTS
for ev in event:
    n = str(ev)
    createFolder(root_folder + "/" + n)





for x in range(len(linklist)):
    obj_Disk = psutil.disk_usage('/')
    ree_perc = 100.0-obj_Disk.percent
    print(ree_perc)

    if(ree_perc < 3):#leave 10 percent disk pace
        print("SKIP DL FREE DISK SPACE")
        break
    if(os.path.exists(root_folder+ "/" +event[x] + "/" + filename[x] + ".mp4")):
        print("SKIP FILE EXITSTS")
        continue
    print("DL:" + linklist[x])
    try:
        wget.download(
            linklist[x],
            root_folder + "/" + event[x] + "/" + filename[x] + ".mp4")
    except:
        print("error while downloading")
        pass

    pass
