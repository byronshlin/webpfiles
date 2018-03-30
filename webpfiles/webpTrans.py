# encoding: utf-8
import re
import sys

import subprocess
import shlex
import os
import getopt



path_list = []
path_list.append("./app/src/main/res/drawable-xhdpi")
path_list.append("./app/src/main/res/drawable-xxhdpi")
path_list.append("./app/src/main/res/drawable-xxxhdpi")


def combine(base, fname):
    return base + "/" + fname


def filesize(filePath):
    return os.stat(filePath).st_size


def png2webp(folder, quality, keepSmaller):
    try:
        arr = os.listdir(folder)
        fullPathList = map(lambda f: (folder + '/' + f), arr)
        for f in fullPathList:
            fname = str(f)
            if fname.endswith(".png"):
                idx = fname.index(".png")
                if idx > 0:
                    name = fname[0:idx]
                    webPName = name + '.webp'
                    comd = 'cwebp -q '+str(quality)+' -o ' + webPName + ' ' + fname
                    subprocess.call(comd, shell=True)
                    pngSize = filesize(fname)
                    webpSize = filesize(webPName)
                    if keepSmaller == True and pngSize < webpSize:
                        subprocess.call('rm -f ' + webPName, shell=True)
                        print("keep png " + str(pngSize) + " " + str(webpSize))
                    else:
                        subprocess.call('rm -f ' + fname, shell=True)
                        print("keep webp and save" + str(pngSize - webpSize))
    except:
        print("folder is not valid: " + folder)


def transfer(quality):
    print("transfer by quality: "+str(quality))
    for p in path_list:
       png2webp(p, quality, True)



def main2(argv):
   #print("argv=>" + str(argv))
   opts = []
   args = []
   try:
      opts, args = getopt.getopt(argv,"cq:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ("")
   
   quality = 80
   for opt, arg in opts:
      if opt == '-q':
          quality = arg

   transfer(quality)


if __name__ == "__main__":
    main2(sys.argv[1:])

