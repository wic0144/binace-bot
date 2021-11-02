import requests
import time
while True:
    requests.get(url="http://localhost:5000/START")
    time.sleep(50)
    print("--------")