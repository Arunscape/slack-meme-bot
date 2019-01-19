if __name__ == "__main__":
    from MemeBot import MemeBot
    from util import waitForNextPost, critError

    memebot = MemeBot()
    memebot.getImages()

    while memebot.images:
        try:
            memebot.sendMeme()
            waitForNextPost()
        except:
            pass

    critError("RAN OUT OF MEMES 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭")
