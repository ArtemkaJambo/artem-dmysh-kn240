# import requests
# r = requests.get('https://google.com')
# r.status_code
# exit()

import requests

response = requests.get('https://httpbin.org/')
for line in response.iter_lines():
    print(line)