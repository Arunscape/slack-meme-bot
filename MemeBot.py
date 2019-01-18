import os
import random
from glob import glob
from shutil import move
from slackclient import SlackClient
from json import dumps as jsondump
from config import API_TOKEN, CHANNEL, MEMES_DIR, IMG_EXTS
from util import waitForNextPost, debugPrint
sc = SlackClient(API_TOKEN)


class MemeBot:

    def __init__(self):
        self.images = []

    def getImages(self):
        self.images = []
        for ext in IMG_EXTS:
            self.images.extend(glob(MEMES_DIR + ext))

    def mv_image(self, img):
        move(img, './posted_memes/' +
             os.path.normpath(img).replace(os.path.normpath(MEMES_DIR), ''))
        self.images.remove(img)

    def getRandomImage(self):
        return random.choice(self.images)

    def sendMeme(self, img):
        response = sc.api_call(
            'files.upload',
            channels=CHANNEL,
            file=open(img, 'rb')
        )
        if response['ok']:
            self.mv_image(img)
        else:
            debugPrint(jsondump(response, indent=4),
                       "ERROR POSTING MEME 😭")

    def sendMessage(self, msg):
        sc.api_call(
            'chat.postMessage',
            channel=CHANNEL,
            text=msg
        )


memebot = MemeBot()
memebot.getImages()
memebot.sendMeme(memebot.getRandomImage())
# sendMessage("👀")
