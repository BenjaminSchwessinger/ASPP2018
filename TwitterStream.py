# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from time import sleep
from collections import deque  # list-like container with fast appends and pops on either end

# Variables that contains the user credentials to access Twitter API
access_token = "YOURKEYHERE"
access_token_secret = "YOURKEYHERE"
consumer_key = "YOURKEYHERE"
consumer_secret = "YOURKEYHERE"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    """
    Class with functions to stream tweets
    """

    def __init__(self, api=None, maxlength=int(1e5)):
        super(StdOutListener, self).__init__()
        self.queue = deque(maxlen=maxlength)

    def on_status(self, status):
        if status.lang.find('en') < 0:
            return

        if status.coordinates is not None and status.entities.get('hashtags') != []:
            self.queue.append(status)

    def on_error(self, status_code):
        print('Error:', status_code)
        return False


def gettweets(maxlength=int(1e5), wait_time=0.001):
    """
    Tweets are streamed and stored in a queue. The queue is popped from the left during function call
    :param  maxlength: maximum length of the queue
            wait_time: time to wait for a new tweet
    """

    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    stream.filter(locations=[-180, -90, 180, 90], async=True)  # This listens to tweets from all over the world

    while True:
        if len(listener.queue) > 0:
            yield listener.queue.popleft()
        else:
            sleep(wait_time)
