### test - 1 from getting the input at that instance 

from crud import DataStore 

qsn = input('Did you wanna set specific directory : Y/N ') 
if( qsn == 'Y' or qsn == 'y'):
    path = input('Example: file.json or directory/file.json \nPath : ')
    data = DataStore(path)
else :
    data = DataStore()


while True:

    c = int(input('CRD operations:\n 1-create 2-read 3-del 4-exit\n Enter ur choice (in number):'))
    
    if c == 1:
        key = input('\nKey: ')
        val = input('\nValue: ')
        q = input('Do wanna set timeout for key:\n Type Y/N : ')
        if q == 'y' or q == 'Y':
            ttl = int(input('time (in seconds) : '))
            data.create(key, val, ttl)
        else:
            data.create(key, val)

        
    if c == 2:

        key = input('\nKey: ')
        data.read(key)

    if c == 3:

        key = input('\nKey: ')
        data.delete(key)

    if c == 4:
        break
