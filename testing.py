#execute this in cmd to get clear understanding of execution of the code
from freshworksassignment import*
p=freshworks() #object for class is created


#call ds_create() function using object
#syntax for calling create function ds_create('key name',value,time_to_live)
#if no value is given in the args for time_to_live(only third argument) by default it will be 0 
#but key_name,value must be provided for sure in order to insert data in the data store
p.ds_create('ravi',25)
p.ds_create('teja',30,20) #20 means seconds
# key value must be string(as mentioned in the given problem statement)
p.ds_create(8,25)
# error will be thrown as the key we provided is not a string, the length of the string can be 32 at max
p.ds_create('sai',30)
p.ds_create('raja',31,60)
p.ds_create('prav',32)


#call ds_read() function using object
#syntax for calling read function ds_read('key name')
#in order to read the key value pairs, we must provide key name as argument to the call
# if the key does not exists in the data store then Error will be thrown
p.ds_read('avi')
# if exists but time_to_live period of the key expires then Error will be thrown
p.ds_read('teja')
# Time expired error will be thrown
# if the key exists and time_to_live is not expired then key, value will be displayed(printed)
p.ds_read('ravi')
# if time_to_live period of a key expires then error will be thrown
# within 20 seconds
p.ds_read('teja') #read or displayed successfully
# After 20 seconds
p.ds_read('teja')
# Time expired error will be thrown
p.ds_read('sai')
p.ds_read('raja')
p.ds_read('prav')


#call ds_delete() function using object
#syntax for calling delete function ds_delete('key name')
#in order to delete the key value pairs, we must provide key name as argument to the call
# if the key does not exists in the data store then Error will be thrown
p.ds_delete('avi')
# if exists but time_to_live period of the key expires then Error will be thrown
p.ds_delete('teja')
# Time expired error will be thrown
# if the key exists and time_to_live is not expired then key, value will be deleted
p.ds_delete('ravi')
# if time_to_live period of a key expires then error will be thrown
# within 20 seconds
p.ds_delete('teja') #deletion successful
# After 20 seconds
p.ds_delete('teja')
# Time expired error will be thrown
p.ds_delete('sai')


#call ds_modify() function using object
#syntax for calling modify function ds_delete('key name',value)
#in order to modify the key value pairs, we must provide key name and value as arguments to the call
# if the key does not exists in the data store then Error will be thrown
p.ds_modify('avi',50)
# if exists but time_to_live period of the key expires then Error will be thrown
p.ds_modify('raja',50)
# Time expired error will be thrown
# if the key exists and time_to_live is not expired then value will be modified
p.ds_modify('sai',50)
# if time_to_live period of a key expires then error will be thrown
# within 60 seconds
p.ds_modify('raja',50) #modified successfully
# After 60 seconds
p.ds_modify('raja',90)
# Time expired error will be thrown


#MULTI THREAD EXECUTION OF DATA STORE
#Client process is allowed to access data store using multiple threads
m1=Thread(target=(p.ds_create),args=('kl',199,25)) #creating data using threading
m1.start()
#m1.sleep()
n1=Thread(target=(p.ds_create),args=('rgs',264)) #creating data using threading
n1.start()
#n1.sleep()
m2=Thread(target=(p.ds_read),args=('kl',)) #reading data using threading
m2.start()
#m2.sleep()
n2=Thread(target=(p.ds_read),args=('rgs',)) #reading data using threading
n2.start()
#n2.sleep()
m3=Thread(target=(p.ds_delete),args=('ml',)) #deleting data using threading
m3.start()
#m3.sleep()
n3=Thread(target=(p.ds_delete),args=('rgs',)) #deleting data using threading
n3.start()
#n3.sleep()
p.ds_read('rgs')
p.ds_modify('kl',149)
#p.ds_modify('l',149)
p.ds_read('kl')
