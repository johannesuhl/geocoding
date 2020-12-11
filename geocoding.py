# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 06:28:05 2020

@author: Johannes Uhl, Department of Geography, University of Colorado Boulder, USA.
"""

### Credits to @DenisCarriere for the great Geocoder API (https://geocoder.readthedocs.io/) !!!

### Parameters: #################################
### place_str: adress to be geocoded, works best if administrative regions (e.g., county, state, country) are included.
### country: ISO-3166 alpha-2 country code.
### use_google: Boolean, to be set to false if google should not be used. If Google's query limit is reached, a sleep() command may be executed which interrupts the script.

### Returns:
### a list [lon,lat,source] with 'source' indicating the geocoding service used to obtain (lon,lat) in WGS84.
### If none of the geocoding services yield valid coordinates, (0,0) is returned.

### credentials: 
key_google = '< google geocoding api key >'
username = '< geonames username >'
#################################################

def do_geocode(place_str, country, use_google):
    lat=0.0
    lon=0.0
    source=''
    g = geocoder.osm(place_str)
    if g.ok:
        lat=float(g.lat)
        lon=float(g.lng)     
        source='osm'
    else:
        g = geocoder.geonames(place_str,key=username,country=country)
        if g.ok:
            lat=float(g.lat)
            lon=float(g.lng)  
            source='geonames'
        else: 
            if use_google:
                g = geocoder.google(place_str,country=country,key=key_google)
            if g.ok:
                lat=float(g.lat)
                lon=float(g.lng)  
                source='google'
            else:  
                g = geocoder.geocodefarm(place_str,country=country)
                if g.ok:
                    lat=float(g.lat)
                    lon=float(g.lng) 
                    source='geocodefarm'
                else:  
                    g = geocoder.arcgis(place_str,country=country)
                    if g.ok:
                        lat=float(g.lat)
                        lon=float(g.lng)   
                        source='arcgis'
                    else:                
                        lat=0.0
                        lon=0.0
                        source=''
    return [lon,lat,source]