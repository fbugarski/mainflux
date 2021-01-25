import requests

class Messages:
    def __init__(self, url):
        self.url = url

    def send_message(self, channelID, msg, token):
        url = self.url + "/channels" + channelID + '/messages'
        resp = requests.post(url, json=msg, headers={"Authorization": token})
        return resp

    def read_message(self, channelID, token):
        url = self.url + "/channels" + channelID + '/messages'
        resp = requests.get(url, headers={"Authorization": token})
        return resp
