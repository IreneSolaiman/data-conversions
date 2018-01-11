#!/usr/bin/env python2

import requests
import lxml.html

response = requests.get("https://twitter.com/datadhrumil")
doc = lxml.html.fromstring(response.content)

for el in doc.cssselect("div.js-tweet-text-container"):
    print el.text_content().strip()
    print "-------------------------------------"