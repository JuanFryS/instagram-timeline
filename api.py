# -*- coding: utf8 -*-
#!/usr/bin/env python


import webapp2
import urllib2
import sys

class instagramRequest(webapp2.RequestHandler):
  def get(self):
    #endpoint = self.request.get("endpoint", default_value="")
    access_token = self.request.get("access_token", default_value="")
    max_id = self.request.get("max_id", default_value="")
    count = self.request.get("count", default_value="")
    
    if (max_id == ""):
      respuesta = urllib2.urlopen("https://api.instagram.com/v1/users/self/feed?access_token="+access_token).read()
    else:
      respuesta = urllib2.urlopen("https://api.instagram.com/v1/users/self/feed?access_token="+access_token+"&max_id="+max_id+"&count="+count).read()
    self.response.write(respuesta)
    
app = webapp2.WSGIApplication([
    (r'/request/instagram', instagramRequest)
], debug=True)
