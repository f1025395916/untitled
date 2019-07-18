import requests

r = requests.get("https://a.jd.com//ajax/queryServerData.html")

print(r.elapsed.microseconds)

print(r.elapsed.total_seconds())

print(ssss)