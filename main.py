import os
import random
from glob import glob
from shutil import move
from slackclient import SlackClient
from json import dumps as jsondump
from config import *


class MemeBot:

    def __init__(self):
        self.images = []
        self.sc = SlackClient(API_TOKEN)

    def getImages(self):
        self.images = []
        for ext in IMG_EXTS:
            images.extend(glob(MEMES_DIR + ext))

    def mv_image(self, img):
        move(img, './posted_memes/'
             + os.path.normpath(img).replace(os.path.normpath(MEMES_DIR), ''))
        images.remove(img)

    def getRandomImage(self):
        return random.choice(images)

    def sendMeme(self, img):
        response = sc.api_call(
            'files.upload',
            channels=CHANNEL,
            file=open(img, 'rb')
        )
        if response['ok']:
            mv_image(img)
        else:
            print("\n👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀")
            print(jsondump(response, indent=4))
            print("👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀\n")

    def sendMessage(self, msg):
        sc.api_call(
            'chat.postMessage',
            channel=CHANNEL,
            text=msg
        )


memebot = MemeBot
memebot.getImages(memebot)
memebot.sendMeme(getRandomImage())
# sendMessage("👀")
