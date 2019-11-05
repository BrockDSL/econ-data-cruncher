# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:28:22 2019
@author: dsouvage
"""

import settings


import os,sys


#ensure you python install settings.py inside couchdb
sys.path.append(r'\OneDrive - Brock University\CitationProject\econ-data-cruncher\CouchDB-1.2\CouchDB-1.2') #append your file path to CouchDB


import couchdb




CDB_USER = "------"
CDB_PASSWORD = "-------"

CDB_HOST = "https://"+CDB_USER+":"+CDB_PASSWORD+"@rtod.library.brocku.ca:32771/econ_data/working"
CDB_NAME = "econ_data_working"

couch = couchdb.Server(CDB_HOST)

try:
    db = couch.create(CDB_NAME)
    print("Connection successful")
except:
    db = couch[CDB_NAME]
