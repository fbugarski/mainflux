import requests
import response
import json

class Messages:
    def __init__(self, url):
        self.url = url

    def send(self, chanID, msg, thing_key):
        '''Sends message via HTTP protocol'''
        url = self.url + "/channels/" + chanID + '/messages'
        mf_resp = response.Response()
        http_resp = requests.post(url, json=msg, headers={"Authorization": thing_key})
        if http_resp.status_code != 202:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Message discarded due to its malformed content"
            if c == 403:
                mf_resp.error.message = "Message discarded due to missing or invalid credentials"
            if c == 404:
                mf_resp.error.message = "Message discarded due to invalid channel id"
            if c == 415:
                mf_resp.error.message = "Message discarded due to invalid or missing content type"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            mf_resp.value = json.loads(http_resp.json)
        return mf_resp

    def read(self, chanID, token):
        '''Reads messages from database for a given channel'''
        url = self.url + "/channels/" + chanID + '/messages'
        mf_resp = response.Response()
        http_resp = requests.get(url, headers={"Authorization": token})
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed query parameters"
            if c == 403:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            mf_resp.value = json.loads(http_resp.json)
        return mf_resp
