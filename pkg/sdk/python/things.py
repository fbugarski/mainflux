import requests


class Things:
    def __init__(self, url):
        self.url = url

    def create_thing(self, thing, token):
        resp = requests.post(self.url + "/things", json=thing, headers={"Authorization": token})
        print(resp.content)
        return resp.headers.get("location")

    def create_things(self, things, token):
        resp = requests.post(self.url + "/things", json=things, headers={"Authorization": token})
        return resp

    def things(self, params, token):
        url = self.url + "/things" + '?' + 'offset=' + params['offset'] + '&' \
            + 'limit=' + params['limit'] + '&'+'name=' + params['name']
        resp = requests.get(url, headers={"Authorization": token})
        return resp.json()

    def things_by_channel(self, channelID, params, token):
        url = self.url + "/channels" + channelID + '/things' + '?' + 'offset=' + params['offset'] \
            + '&' + 'limit=' + params['limit'] + '&' + 'connected=' + params['connected']
        resp = requests.post(url, json=channels, headers={"Authorization": token})
        return resp

    def thing(self, id, token):
        resp = requests.get(self.url + "/things" + id, headers={"Authorization": token})
        return resp

    def update_thing(self, thing, token):
        resp = requests.put(self.url + "/things" + thing["id"], json=thing, headers={"Authorization": token}) 
        return resp

    def delete_thing(self, id, token):
        resp = requests.delete(self.url + "/things" + id, headers={"Authorization": token})
        return resp
