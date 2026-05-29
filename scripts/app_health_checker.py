import requests


URL = "http://localhost:8080"


try:
    response = requests.get(URL, timeout=5)

    if response.status_code == 200:
        print("Application is UP")
        print("Status:", response.status_code)

    else:
        print("Application is DOWN")
        print("Status:", response.status_code)

except Exception as e:
    print("Application is DOWN")
    print(e)