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
    print(img)
    print('./posted_memes/' +
          os.path.normpath(img).replace(os.path.normpath(MEMES_DIR), ''))
    move(img, './posted_memes/' +
         os.path.normpath(img).replace(os.path.normpath(MEMES_DIR), ''))
    images.remove(img)


def getRandomImage():
    global images
    return random.choice(images)
