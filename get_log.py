# retrieve log from http

# run "pip install requests" in terminal

import requests
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
myfile = requests.get(url)
open('C:/Users/Amy/Downloads/tcmg412log.txt', 'wb').write(myfile.content)