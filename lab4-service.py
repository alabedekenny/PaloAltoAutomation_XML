#!/usr/bin/env python
import ssl
import urllib3
import requests
import sys
import xml.etree.ElementTree as ET

if __name__ == '__main__':
  
  #---------------------------------------------------------------------------------------------------------------------------------------------------
  # Put your API_KEY , FIREWALL IP , SERVICE OBJECT , PORT & PROTOCOL
  api_key      = "PUT YOUR API KEY HERE"
  firewall_ip  = "PUT YOUR FIREWALL IP KEY HERE"
  service_obj  = [ ["tcp-8081","tcp","8081"], 
                   ["tcp-8082","tcp","8082"], 
                   ["tcp-8083","tcp","8083"], 
                   ["tcp-8084","tcp","8084"], 
                   ["tcp-8085","tcp","8085"]] 
  #---------------------------------------------------------------------------------------------------------------------------------------------------

try:
  
  for service_name, service_proto, service_port in service_obj:
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    # This is the section where you can set your xpath & element
    xpath             = "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/service/entry[@name='"+service_name+"']"
    element           = "<protocol><"+service_proto+"><port>"+service_port+"</port></"+service_proto+"></protocol>"
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    
    api_url = "https://"+firewall_ip+"/api/?type=config&action=set&xpath="+xpath+"&element="+element+"&key="+api_key
    urllib3.disable_warnings()
    api_request       = requests.get(url=api_url,verify=False)
    api_response      = api_request.text
    xml_tree_root     = ET.fromstring(api_response)
    print(service_name + " API RESPONSE ->" + str(api_response))

except:
  print("ERROR   : Connecting to "+firewall_ip+". Check the Firewall IP address and API Key.")
  sys.exit(0)	
