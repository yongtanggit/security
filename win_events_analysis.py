#! /usr/bin/python3

from xml.etree import ElementTree
from Evtx import *

Path = "/opt/python/blueteam/tests/data/security.evtx"
with Evtx.Evtx(Path) as log:
    for record in log.records():
        str_xml = record.xml() # Create a string containing XML data
        str_xml = str_xml.replace('xmlns="http://schemas.microsoft.com/win/2004/08/events/event"', "")
        # Returns an Element instance
        root = ElementTree.fromstring(str_xml)

        # System sub-element
        system = root.findall('System')
        system_elements = system[0]

        # data sub-element
        data = root.findall('EventData')
        data_elements = data[0]

        # Prepare the data
        # Computer Name
        computer = system_elements.findtext('Computer')
        # eventID
        eventID = system_elements.findtext('EventID')
        # Event Data
        eventData = data_elements.findall('Data')
        # Query with keyword "eventID"
        if eventID == "4624":
            print("===================")
            print('Event ID: ',eventID)
            print('PC Name: ',computer)
            print('Event Data: ')
            for data in eventData:
              print('*',data.text)
