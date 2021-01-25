import requests

class Messages:
    def __init__(self, url):
        self.url = url

    def send_message(self, channel_id, msg, token):
        url = self.url + "/channels/" + channel_id + '/messages'
        resp = requests.post(url, json=msg, headers={"Authorization": token})
        return resp

    def read_message(self, channel_id, token):
        url = self.url + "/channels/" + channel_id + '/messages'
        resp = requests.get(url, headers={"Authorization": token})
        return resp
