import requests
import json

class Things:
    def CreateThing(thing, token):
        resp = requests.post("http://localhost/things", json=thing, headers={"Authorization": token})
        return resp.headers.get("location")

    def CreateThings(things, token):
        resp = requests.post("http://localhost/things", json=things, headers={"Authorization": token})
        return resp

    def Things(params, token):
        url = "http://localhost/things"+'?'+'offset='+params['offset']+'&'+'limit='+params['limit']+'&'+'name='+params['name']
        resp = requests.get(url, headers={"Authorization": token})
        return resp.json()

    def ThingsByChannel(channelID, params, token):
        url = "http://localhost/channels"+channelID+'/things'+'?'+'offset='+params['offset']+'&'+'limit='+params['limit']+'&'+'connected='+params['connected']
        resp = requests.post(url, json=channels, headers={"Authorization": token})
        return resp
        
    def Thing(id, token):
        resp = requests.get("http://localhost/things/"+id, headers={"Authorization": token})
        return resp

    def UpdateThing(thing, token):
        resp= requests.put("http://localhost/things/"+thing["id"], json=thing, headers={"Authorization": token}) 
        return resp

    def DeleteThing(id, token):
        resp = requests.delete("http://localhost/things/"+id, headers={"Authorization": token})
        return resp
