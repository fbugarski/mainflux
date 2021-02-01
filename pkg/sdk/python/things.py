import requests


class Things:
    def __init__(self, url):
        self.url = url

    def create(self, thing, token):
        '''Creates thing entity in the database'''
        resp = requests.post(self.url + "/things", json=thing, headers={"Authorization": token})
        print(resp.content)
        return resp.headers.get("location").split('/')[2]

    def create_bulk(self, things, token):
        '''Creates multiple things in a bulk'''
        resp = requests.post(self.url + "/things", json=things, headers={"Authorization": token})
        return resp

    def get(self, id, token):
        '''Gets a thing entity for a logged-in user'''
        resp = requests.get(self.url + "/things/" + id, headers={"Authorization": token})
        return resp

    def get_all(self, params, token):
        '''Gets all things from database'''
        url = self.url + "/things" + '?' + 'offset=' + params['offset'] + '&' \
            + 'limit=' + params['limit'] + '&'+'name=' + params['name']
        resp = requests.get(url, headers={"Authorization": token})
        return resp.json()

    def get_by_channel(self, channel_id, params, token):
        '''Gets all things to which a specific thing is connected to'''
        url = self.url + "/channels/" + channel_id + '/things' + '?' + 'offset=' + params['offset'] \
            + '&' + 'limit=' + params['limit'] + '&' + 'connected=' + params['connected']
        resp = requests.post(url, headers={"Authorization": token})
        return resp

    def update(self, thing, token):
        '''Updates thing entity'''
        resp = requests.put(self.url + "/things/" + thing["id"], json=thing, headers={"Authorization": token})
        return resp

    def delete_thing(self, id, token):
        '''Deletes a thing entity from database'''
        resp = requests.delete(self.url + "/things/" + id, headers={"Authorization": token})
        return resp
