from threading import*
import time as t
dic={} 

class freshworks:
    def ds_create(self,key,val,time_out=0): # this is create operation in the data store
        if key in dic: # check if key already exists in the data store in order to create
            print("Error! This key already exists in the Data Store") #error when key already exists in the data store
        else:
            if(isinstance(key,str)): #check if given input key is only a string (as mentioned in the constraints that it should always be a string)
                if len(dic)<(1020*1024*1024) and val<=(1024*1024*16): #check if the file size less than 1GB and Jasonobject value less than 16KB 
                    if time_out!=0: # if there is exists time to live property for the given input key
                        l=[val,t.time()+time_out]
                    else: # if there is no time to live property for the given input key
                        l=[val,time_out]
                    if len(key)<=32: #constraints for input key capped at max 32chars
                        dic[key]=l #inserting key, val pair into data store
                    else:
                        print("Error! Key has more than 32chars(len of key), as it is not valid") #if key length exceeds 32 throw this error
                else:
                    print("Error! Memory limit exceeded in the given input ") #error when file size exceeds 1GB or JSON object value exceeds 16KB
            else:
                print("Error! Invalid key, key must be a string") #error when given input key is not a string

 
    def ds_read(self,key): # this is read operation in the data store
        if key not in dic: # check if key exists in the data store in order to read
            print("Error! This key does not exist in datastore to read") #error when key does not exists in the data store to perform read operation
        else:
            k=dic[key]
            if k[1]==0: # if there is no time to live property for the given input key
                s=str(key)+":"+str(k[0]) # returning the key name,value in JasonObject format,"keyname:val"
                print(s)
            else: # if there is exists time to live property for the given input key
                if t.time()<k[1]: #comparing expiry time of the key with the current time
                    s=str(key)+":"+str(k[0]) # returning the key name,value in JasonObject format,"keyname:val"
                    print(s)
                else:
                    del dic[key] #deleting the key, val from the store as time-to-live got expired
                    print("Error: Key no longer exists as time-to-live of",key,"has expired") #error when time to live of the given key gets expired

 
    def ds_delete(self,key): #this is delete operation in the data store
        if key not in dic: # check if key exists in the data store in order to delete
            print("Error: This key does not exist in datastore to delete") #error when key does not exists in the data store to perform deletion
        else:
            k=dic[key]
            if k[1]==0: # if there is no time to live property for the given input key
                del dic[key] #deleting the key, val from the store
                print("key is successfully deleted")
            else:
                if t.time()<k[1]: #comparing expiry time of the key with the current time
                    del dic[key] #deleting the key, val from the store
                    print("key is successfully deleted")
                else:
                    del dic[key] #deleting the key, val from the store as time-to-live got expired
                    print("Error: Key no longer exists as time-to-live of",key,"has expired") #error when time to live of the given key gets expired


    def ds_modify(self,key,val): #this is modify operation in the data store
        if key not in dic: # check if key exists in the data store in order to modify
            h=print("Error! This key does not exist in datastore to modify") #error when key does not exists in the data store to perform modify operation
            return(h)
        k=dic[key]
        if k[1]==0: # if there is no time to live property for the given input key
            l=[]
            l.append(val)
            l.append(k[1])
            dic[key]=l #modifying the data with given input
        else: # if there is exists time to live property for the given input key
            if t.time()<k[1]: #comparing expiry time of the key with the current time
                l=[]
                l.append(val)
                l.append(k[1])
                dic[key]=l #modifying the data with given input
            else:
                del dic[key] #deleting the key, val from the store as time-to-live got expired
                print("Error: Key no longer exists as time-to-live of",key,"has expired") #error when time to live of the given key gets expired

