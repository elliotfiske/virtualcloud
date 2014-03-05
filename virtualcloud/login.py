import sys, os.path, json

from db_ops import db
from gd_ops import gd

def login():
    data = ""

    if os.path.isfile('.virtualcloud') == True:
        try:
            json_data = open(".virtualcloud", "r+")
        except e:
            print 'failed to open settings file'                     
        
        try:    
            data = json.load(".virtualcloud")
        except e:
            print 'failed to load settings file'    
        
        try:        
            json_data.close()
        except e:
            print 'failed to close settings file'    

    else:
        data = {
                    'dropbox' : [], # List of db tokens
                    'gdrive' : [] # List of gd tokens
               }
        

    while True:

        cmd = raw_input("To add a service please enter 'dropbox' or 'gdrive'. To go back enter 'back': ")
        cmd.lower()
        if cmd == 'dropbox':
            ndb = db(-1)
            ndb.db_login()
            data['dropbox'].append(nbd.AT)
            
        if cmd == 'gdrive':
            ngd = gd(-1)
            ngd.gd_login()
            data['gdrive'].append(ngd.AT)
        
        if cmd == 'back':
            break


    data = json.dump(data)

    try:
        json_data = open('.virtualcloud', w)
    except e:
        'filed to open/create settings file'    

    try:
        json_data.write(dump)
    except:
        print'failed to write to settings file'

    try:
        json_data.close()
    except e:
        print'failed to close settings file'



    
    

