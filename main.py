import os
import random
from glob import glob
from shutil import move
from slackclient import SlackClient
from config import *

sc = SlackClient(API_TOKEN)

images = []


def getImages():
    global images
    images = []
    for ext in IMG_EXTS:
        images.extend(glob(MEMES_DIR + ext))


def mv_image(img):
    global images
    move(img, './posted_memes/'
         + os.path.normpath(img).replace(os.path.normpath(MEMES_DIR), ''))
    images.remove(img)


def getRandomImage():
    global images
    return random.choice(images)


def sendMeme(img):
    response = sc.api_call(
        'files.upload',
        channels=CHANNEL,
        file=open(img, 'rb')
    )
    print(response)


def sendMessage(msg):
    sc.api_call(
        'chat.postMessage',
        channel=CHANNEL,
        text=msg
    )


getImages()
sendMeme(getRandomImage())
# sendMessage("👀")
