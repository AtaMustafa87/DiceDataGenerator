#!/usr/bin/env python
# coding: utf-8

from PIL import Image
from numpy.random import randint
from numpy.random import rand
import os
dirs = ['data/train/images','data/train/labels','data/valid/images','data/valid/labels']

for d in dirs:
    if not os.path.exists(d):
        os.makedirs(d)
def getSecondLocation(imgSize,diceSize,ix,iy):
    x,y = 0,0
    while True:
        x,y = getFirstLocation(imgSize,diceSize)
        if ((x > (ix+diceSize*2)) or (x< (ix-diceSize*2))) and((y > (iy+diceSize*2)) or (y <(iy-diceSize*2) )):
            break
    return x,y

def getFirstLocation(imgSize,diceSize):
    x,y = 0,0
    while True:
        x = int(rand()*imgSize)
        if (x > diceSize) and (x<(imgSize-diceSize)):
            break
    while True:
        y = int(rand()*imgSize)
        if (y > diceSize) and (y<(imgSize-diceSize)) :
            break
    return int(x),int(y)

def generateImage(ifn,txtfn,imageSize,diceSize):
    img = Image.new('RGB', (imageSize,imageSize))
    bgi = Image.open('bg.png')
    bgi = bgi.resize((imageSize,imageSize))
    imgInd1 = randint(1,7)
    imgInd2 = randint(1,7)
    fgi1 = Image.open(str(imgInd1)+'.png')
    fgi1 = fgi1.resize((diceSize,diceSize))
    fgi2 = Image.open(str(imgInd2)+'.png')
    fgi2 = fgi2.resize((diceSize,diceSize))
    #place background
    img.paste(bgi,(0,0))
    x1,y1 = getFirstLocation(imageSize,diceSize)
    img.paste(fgi1,(x1,y1))
    x2,y2 = getSecondLocation(imageSize,diceSize,x1,y1)
    x2,y2 = int(x2),int(y2)
    img.paste(fgi2,(x2,y2))
    img.save(ifn)
    ofs = diceSize // 2
    with open(txtfn,'w') as f:
        f.write(f'{imgInd1-1}\t{(x1+ofs)/imageSize}\t{(y1+ofs)/imageSize}\t{(diceSize)/imageSize}\t{(diceSize)/imageSize}\n')
        f.write(f'{imgInd2-1}\t{(x2+ofs)/imageSize}\t{(y2+ofs)/imageSize}\t{(diceSize)/imageSize}\t{(diceSize)/imageSize}')

for i in range(1,301):
    generateImage('Data/train/images/'+str(i)+'.png','Data/train/labels/'+str(i)+'.txt',200,randint(20,30))

for i in range(1,201):
    generateImage('Data/valid/images/'+str(i)+'.png','Data/valid/labels/'+str(i)+'.txt',200,randint(20,30))


# In[19]:





# In[ ]:




