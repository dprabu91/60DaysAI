# Day 9: Working with External Libraries
import requests
import time
import webbrowser

time.sleep(1)

webbrowser.open("https://www.google.com")
response = requests.get("https://www.google.com")

print(response)
print("Status Code:", response.status_code)
