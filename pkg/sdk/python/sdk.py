import users
import things
import message
import channels

class SDK:
    def __init__(self, url):
        self.users = users.Users()
        self.things = things.Things()
        self.message = message.Message()
        self.channels = channels.Channels()
        self.url = url

