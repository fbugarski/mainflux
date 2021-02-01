import requests

class Messages:
    def __init__(self, url):
        self.url = url

    def send(self, channel_id, msg, token):
        '''Sends message via HTTP protocol'''
        url = self.url + "/channels/" + channel_id + '/messages'
        resp = requests.post(url, json=msg, headers={"Authorization": token})
        return resp

    def read(self, channel_id, token):
        '''Reads messages from database for a given channel'''
        url = self.url + "/channels/" + channel_id + '/messages'
        resp = requests.get(url, headers={"Authorization": token})
        return resp
