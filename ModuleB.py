# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:06:40 2018

@author: Lazy Scientist
"""
#import requests
#from PIL import Image

##Download and open the image used
#url = 'https://s14-eu5.startpage.com/cgi-bin/serveimage?url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FC644_QeWwAEP7mF.jpg&sp=cfff8d4172d2dbc0d6637f0a90f83e01'
#req = requests.get(url, allow_redirects=True)

#open('magpie.jpg', 'wb').write(req.content)

##Open image in separate program - was only done to check that image was available
#image = Image.open('magpie.jpg')
#image.show()

import matplotlib.image as img
bird = img.imread('magpie.jpg')

edgesx
edgesy