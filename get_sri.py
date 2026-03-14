import hashlib
import urllib.request
import base64

urls = [
    "https://cdn.tailwindcss.com/3.4.1",
    "https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    data = response.read()
    digest = hashlib.sha384(data).digest()
    b64 = base64.b64encode(digest).decode('utf-8')
    print(f"{url} -> sha384-{b64}")
