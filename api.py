# -*- coding: utf8 -*-
#!/usr/bin/env python


import webapp2
import urllib2
import sys

class instagramRequest(webapp2.RequestHandler):
  def get(self):
    access_token = self.request.get("access_token", default_value="")

    print("Peticion")
    
    respuesta = urllib2.urlopen("https://api.instagram.com/v1/users/self/feed?access_token="+access_token).read()

    self.response.write(respuesta)
    
app = webapp2.WSGIApplication([
    (r'/request/instagram', instagramRequest)
], debug=True)