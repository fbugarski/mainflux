import requests

class Message:
    def SendMessage(channelID, msg, token):
        url = "http://localhost/channels"+channelID+'/messages'
        resp = requests.post(url, json=msg, headers={"Authorization": token})
        return resp

    def ReadMessage(channelID, token):
        url = "http://localhost/channels"+channelID+'/messages'
        resp = requests.get(url, headers={"Authorization": token})
        return resp
