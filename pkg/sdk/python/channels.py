import requests


class Channels:
    def __init__(self, url):
        self.url = url

    def create_channel(self, channel, token):
        resp = requests.post(self.url + "/channels", json=channel, headers={"Authorization": token})
        return resp.headers.get("location")

    def create_channels(self, channels, token):
        resp = requests.post(self.url + "/channels", json=channels, headers={"Authorization": token})
        return resp

    def channels(self, query_params, token):
        url = self.url + "/channels" + '?' + 'offset=' + query_params['offset'] + '&' + \
            'limit=' + query_params['limit'] + '&' + 'connected=' + query_params['connected']
        resp = requests.get(url, headers={"Authorization": token})
        return resp.json()

    def channel_by_thing(self, thing_id, query_params, token):
        url = self.url + "/things" + thing_id + '/channels' + '?' + 'offset=' + query_params['offset'] \
                + '&' + 'limit=' + query_params['limit'] + '&' + 'connected=' + query_params['connected']
        resp = requests.post(url, headers={"Authorization": token})
        return resp

    def channel(self, id, token):
        resp = requests.get(self.url + "/channels/"+id, headers={"Authorization": token})
        return resp

    def update_channel(self, channel, token):
        resp= requests.put(self.url + "/channels/" + channel["id"], json=channel, headers={"Authorization": token})
        return resp

    def delete_channel(self, id, token):
        resp = requests.delete(self.url + "/channels/" + id, headers={"Authorization": token})
        return resp
