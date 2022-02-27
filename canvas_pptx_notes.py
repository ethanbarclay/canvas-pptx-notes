#!python3
from canvasapi import Canvas
from io import BytesIO
import browser_cookie3
import pptx_notes
import requests

API_URL = 'API URL'
API_KEY = 'API KEY'
COURSE_ID = 0

canvas = Canvas('https://' + API_URL, API_KEY)
modules = canvas.get_course(COURSE_ID).get_modules()

print('downloading...')

# get canvas cookies from chrome and add to request
cj = browser_cookie3.chrome(domain_name=API_URL)
cookie_string = ''.join([cookie.name + "=" + cookie.value + ";" for cookie in cj])
headers_dict = {"cookie": cookie_string}

# find pptx in modules
for module in modules:
    items = module.get_module_items()
    for item in items:
        # download pptx
        if 'pptx' in item.title:
            download_url = 'https://' + API_URL + '/files/' + \
                str(item.content_id) + '/download'
            # follow redirect to cdn location
            download_url = requests.get(download_url,
                             cookies=cj, headers=headers_dict).history[1].url
            # download and read notes from presentation
            pptx_notes.process_presentation(BytesIO(requests.get(download_url).content))
print('finished!')