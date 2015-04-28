# -*- coding: utf8 -*-
#!/usr/bin/env python


import webapp2
import urllib2
import sys

class instagramRequest(webapp2.RequestHandler):
  def get(self):
    access_token = self.request.get("access_token", default_value="")
    count = self.request.get("count", default_value="")
    min_id = self.request.get("min_id", default_value="")
    max_id = self.request.get("max_id", default_value="")

    peticion = "https://api.instagram.com/v1/users/self/feed?access_token="+access_token

    #Peticion basica
    if (count == "" and min_id == "" and max_id == ""):
      print ("Peticion basica")
      respuesta = urllib2.urlopen(peticion).read()
    #Recargar datos
    elif (min_id != ""):
      print ("Peticion refresco")
      respuesta = urllib2.urlopen(peticion+"&min_id="+min_id).read()
    #Cargar mas datos
    else:
      print ("Peticion cargar mas")
      respuesta = urllib2.urlopen(peticion+"&max_id="+max_id+"&count="+count).read()
    self.response.write(respuesta)
    
app = webapp2.WSGIApplication([
    (r'/request/instagram', instagramRequest)
], debug=True)
