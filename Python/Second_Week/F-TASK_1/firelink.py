#!/usr/bin/python3

import webbrowser

Facebook  = 'https://www.facebook.com/'
Linkedin  = 'https://www.linkedin.com/'
Youtube   = 'https://www.youtube.com/'
Github    = 'https://github.com/'
Instagram = 'https://www.instagram.com/'

def firefox (url=''):
 c = webbrowser.get('firefox')
 c.open(url)

def Choose_Site (site_no):
 if site_no == 1 :
    firefox(Facebook)
 elif site_no == 2 :
    firefox(Linkedin)
 elif site_no == 3 :
    firefox(Youtube)
 elif site_no == 4 :
    firefox(Github)
 elif site_no == 5 :
    firefox(Instagram)

