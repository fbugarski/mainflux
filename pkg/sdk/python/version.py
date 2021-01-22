def Version():
    resp = requests.get("http://localhost/things"+"/version")
    return resp
