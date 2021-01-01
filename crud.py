import json   # for accessing json files
import time   # to obtain time 
import sys    # to know size of values
import os     # for accessing file paths 

data = {}  # dictionary to save json objects

 
class DataStore:

    # creates filepath (fpath) when class initialize

    def __init__(self, fpath = 'data/dstore.json'):   # gets fpath (filepath) and it's an optional.
        
        self.fpath = fpath

        if os.path.exists(self.fpath):          # if path is already exists , it passes
            pass

        else:

            dir = os.path.split(self.fpath) 

            if (dir[0] == "") or os.path.exists(dir[0]):       # if directory already exists but not file, then it passes directory
                with open(self.fpath,'a') as fp:
                    fp.write('{}')                             # creates only file with '{}' written to avoid error when loads the file
            
            else:
                os.makedirs(dir[0])                     
                with open(self.fpath,'a') as fp:               # creates complete directory and file (with intermediate directories)
                    fp.write('{}')


    # checks whether key already existed or not

    def checKey(self, key):
          
        if (os.path.getsize(self.fpath) > 2): 
        
            with open(self.fpath,'r') as read:
                r_data = json.load(read)
        
            if key in r_data.keys():
                return False                    # returns false if key already present

            else:
                return True                     # returns true if key is not present already

        else:
            return True                         # returns true incase file empty

     
    # create operation syntax: create(key, value) or create(key, value, time in seconds)

    def create(self, key, value, ttl=0):

        if os.path.getsize(self.fpath) < (1024*1024*1024):                  # check file_Size less than 1 GB

            if key.isalpha():                                               # checks key always be strings

                if self.checKey(key):                                       

                    if len(key)<=32 and sys.getsizeof(value)<(1024*16):     # make sures key is unique and their size limit 

                        if ttl==0:                          
                            data[key] = [value, ttl]                        # saves new data

                        else: 
                            data[key] = [value, ttl + time.time()]          
                                
                        with open(self.fpath,'r') as read:
                            temp = json.load(read)                          # loads pre-data
                            
                        ldata = dict(temp)
                        ldata.update(data)                                  # combines them 

                        with open(self.fpath,'w') as write:
                            json.dump(ldata, write, indent=2)               # updates them 

                    else:
                        print('Error: Key or Value size beyond the limit.')    

                else:
                    print('Error: Key already existed.')

            else:
                print('Error: Key should be only strings ( and should not be numbers or any other special characters).')

        else:
            print('Error: Memory limit Exceeded.')


    # read operation syntax: read(key)

    def read(self, key):
        
        if (os.path.getsize(self.fpath) > 2):       # makes sure file is not empty
            
            with open(self.fpath,'r') as read:      # loads json
                r_data = json.load(read)
            
            if key in r_data.keys():                # checks for key presence
                temp = r_data[key]                  
                
                value = temp[0]
                ttl = temp[1]

                if(time.time() < ttl) or ttl == 0:      #checks the key's timeout
                    print(value)

                else:
                    print('Key expired.')               # throws an error message if key expired
            
            else:
                print('Error: Invalid Key.')            # throws an error-message if invalid key reads
        
        else:
            print('Error: Empty File.')                 # throws an error message if reads empty file
                

    # delete operation syntax: delete(key)

    def delete(self, key):

        if (os.path.getsize(self.fpath) > 2):       # makes sure file is not empty

            with open(self.fpath,'r') as read:      # loads json
                r_data = json.load(read)
            
            if key in r_data.keys():                # checks for key presence
                temp = r_data[key]
                
                value = {key:temp[0]}
                ttl = temp[1]

                if( time.time() < ttl) or (ttl == 0):       # checks for the key's timeout

                    del r_data[key]
                    print(value,' deleted.')

                    with open(self.fpath,'w') as write:     # updates modification
                        json.dump(r_data,write)

                else:
                    print('Key expired.')
 
            else:
                print("Error: Invalid key.")
        
        else:
            print('Error: Empty File.')