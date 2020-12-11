# geocoding.py
A robust Python function for geocoding addresses using the Geocoder API (Credits to @DenisCarriere, https://geocoder.readthedocs.io/).
The function queries a variety of geocoding services until valid coordinates are returned.
Users with limited querying options for Googles Geocoding API are encouraged to set the parameter use_google = False, to avoid evoking a sleep() command.
