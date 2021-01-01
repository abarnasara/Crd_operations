### test - 2 => testing from the predefined values 

from crud import DataStore 


#  case 1 
#-----------


data1 = DataStore('store/data.json')  # with optional filepath

### create operations ###

data1.create('lang','python')  # creates a key-value pair 

data1.create('assignment','done',90)   # creates a key-value pair with timeout

data1.create('lang','python')   # returns 'Error: key already exists.'



### read operations ###

data1.read('lang')     # returns 'python'

data1.read('assignment') # returns 'key expired' ( After 90 seconds from created )

data1.read('place') # returns invalid key



### delete operations ###

data1.delete('lang') # returns '{lang: python} deleted.'

data1.delete('lang') # returns 'invalid key'

data1.delete('assignment') # returns 'key expired' ( After 90 seconds from created )


#     case 2 
# --------------


data2 = DataStore() ### without specific filepath

data2.create('project','crd')
data2.read('project')

data2.delete('project')

data2.delete('project') # returns invalid key