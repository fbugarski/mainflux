import requests
import json

class Users:
  def CreateUser(user):
    ''' CreateUser() creates user entity in the database '''
    resp = requests.post("http://localhost/users", json=user)
    return resp.headers.get("location")

  def User(token):
    resp = requests.get("http://localhost/users", headers={"Authorization": token})
    return resp.content

  def CreateToken(user):
    resp = requests.post("http://localhost/tokens",json=user)
    return resp.json()["token"]

  def UpdateUser(user, token):
    resp = requests.put("http://localhost/users", headers={"Authorization": token}, data=json.dumps(user))
    return resp.status_code

  def UpdatePassword(old_password, new_password, token):
    payload = {
      "password":old_password,
      "old_password":new_password
    }
    resp = requests.patch("http://localhost/password", headers={"Authorization": token}, data=json.dumps(payload))
    return resp
