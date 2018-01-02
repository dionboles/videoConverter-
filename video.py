'''
 this is a script that loops though a dir and then uses the ffmpeg to change avi to movi and compress it a bit
'''

import os 
if os.path.isdir("video") is False:
    os.mkdir("video")
    os.chdir("video")
else:
    os.chdir("video")

if os.path.isdir(".") is True:
   for i in os.listdir('.'):
       extension = os.path.splitext(i)[1][1:]
       if extension == "avi":
           name = str(os.path.splitext(i)[0]).replace("_","");
           os.system("ffmpeg -i "+i+" "+name+".mov -crf 14");
         


