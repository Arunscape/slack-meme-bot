import numpy as np
import time


def debugPrint(str, typeoferr):
    print("\n👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀")
    print(typeoferr)
    print(str)
    print("👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀\n")

# I don't even know what a gamma distribution is but it generates
# numbers in like, exactly the way I want "random" numbers


def waitHowManySeconds():
    # to give an idea of the numbers generated by the distribution
    # return np.random.gamma(8, scale=100, size=100) /60 # time in minutes
    return np.random.gamma(8, scale=100)


def waitForNextPost():
    s = waitHowManySeconds()

    print("\n⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳")
    print("NEXT MEME WILL BE POSTED AT {}".format(
        time.asctime(time.localtime(time.time() + s))))
    print("⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛\n")

    time.sleep(s)


def critError(str="EXECUTE main.py NOT THIS FILE"):
    print("\n⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔")
    print(str)
    print("⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔\n")


if __name__ == "__main__":
    critError()
