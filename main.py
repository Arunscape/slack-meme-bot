if __name__ == "__main__":
    from MemeBot import MemeBot
    from util import waitForNextPost

    memebot = MemeBot()
    memebot.getImages()

    while True:
        try:
            memebot.sendMeme()
            waitForNextPost()
        except:
            pass
