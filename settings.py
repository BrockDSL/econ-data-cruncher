# Base URL for DB product
E_URL = "http://search.ebscohost.com/login.aspx?direct=true&db=bth&AN="

#COUCH CONFIGS

import os,sys

#ensure you python install settings.py inside couchdb
sys.path.append(r'.\CouchDB-1.2\CouchDB-1.2') #append your file path to CouchDB

import couchdb


#see dylan/tim/anyone for access

CDB_USER = "----"
CDB_PASSWORD = "----"

CDB_HOST = "http://"+CDB_USER+":"+CDB_PASSWORD+"@rtod.library.brocku.ca:32771/"
CDB_NAME = "econ_data_test"

couch = couchdb.Server(CDB_HOST)

dbname = CDB_NAME
if dbname in couch:
    db = couch[dbname]
else:
    db = couch.create(dbname)


#Data File locations
DATA_BASE = "data/"

TOC_IN = "TOC_in/"
TOC_OUT = "TOC_out/"
TOC_ERROR = "TOC_error/"

AN_IN = "AN_in/"
AN_OUT = "AN_out/"
AN_ERROR = "AN_error/"

#Log File locations
LOG_BASE = "logs/"
TOC_PROCESS = "toc_process/"
AN_PROCESS = "an_process/"


# run once to create all directories need
if __name__ == "__main__":
    print("Creating directories...")
    import os
    cwd = os.getcwd()
    os.makedirs(os.path.join(cwd,DATA_BASE), exist_ok = True)
    os.makedirs(os.path.join(cwd,DATA_BASE,TOC_IN), exist_ok = True)
    os.makedirs(os.path.join(cwd,DATA_BASE,TOC_OUT), exist_ok = True)
    os.makedirs(os.path.join(cwd,DATA_BASE,TOC_ERROR), exist_ok = True)
    os.makedirs(os.path.join(cwd,DATA_BASE,AN_IN), exist_ok = True)
    os.makedirs(os.path.join(cwd,DATA_BASE,AN_OUT), exist_ok = True)
    os.makedirs(os.path.join(cwd,DATA_BASE,AN_ERROR), exist_ok = True)
    os.makedirs(os.path.join(cwd,LOG_BASE,TOC_PROCESS), exist_ok = True)
    os.makedirs(os.path.join(cwd,LOG_BASE,AN_PROCESS), exist_ok = True)
    print("done")
