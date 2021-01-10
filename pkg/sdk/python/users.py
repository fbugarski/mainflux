import requests

def CreateUser(email,password):
  user = {
    "email":email,
    "password":password
  }
  resp = requests.post("http://localhost/users", json=user)
  return resp.headers.get("location")

# id = CreateUser("flp2@gmail.com","12345678")
# if id is not None:  
#   a = id.split('/')
#   print(a[2])