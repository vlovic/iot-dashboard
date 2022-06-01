import requests
import time
import random

host = "localhost"
port = "8000"

while True: 
    #make a POST request
    try: 
        dictToSend = {"wifi":-21,"pm02":random.randint(0, 10),"rco2":random.randint(0,100),"atmp":random.randint(0, 10),"rhum":random.randint(0,100)}
        res = requests.post("http://{host}:{port}/airgradient:dc8c38/measures".format(host=host, port=port), json=dictToSend)

    except requests.exceptions.ConnectionError:
        print("Could not establish a connection with http://{host}:{port}/".format(host=host, port=port))
    time.sleep(2)