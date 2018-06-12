import os
import sys

rootdir = "C:\VideoBook"
rootdir = "Z:\VideoBook"
#rootdir = "C:\AudioBook\kongbuxuanyi"
subfolder = rootdir + os.sep + "短篇惊悚悬疑故事集Ⅰ"
#title = "有声恐怖悬疑小说"
title1 = "短篇惊悚悬疑故事集Ⅰ"
title = "有声小说"
#i = 1
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        filepath = file
        #print (file)
        if filepath.endswith(".mp4") and subdir == subfolder:
            #print (subdir)
            #print (os.path.splitext(filepath)[0])
            rename = os.path.splitext(filepath)[0]
            if rename[19:19].isdigit():
                seq = rename[16:19]
            #else:
            #    seq = rename[5:7]
            #if rename[0:4].isdigit():
            #    rename = rename[4:40]
            #seq = rename[20:22]
            #rename = rename[1:6]
            #rename = title + " " + rename + " 第" + seq + "集"
            #rename = "《" + rename + "》 " + title + " 第" + seq.zfill(3) + "集"
            #rename = "《" + title1 + "》 " + title + " 第" + str(i).zfill(2) + "集" + " " + rename
            #rename = title + " " + rename + " " + seq
            #print (rename)
            newname = rename + ".mp4"
            #newname = rename[:9] + "7" + rename[9:20] + ".mp4"
            print(newname)
            #i = i+1
            #print (file)
            #newname = file + ".jpg"
            #print (newname[4:15])
            #newname = newname[4:15#
            #print (newname)
            #os.rename(subdir + os.sep + file, subdir + os.sep + newname)
