# CRD_Operations 

Builded a file-based key-value data store that supports the basic CRD ( Create, Read and Delete ) operations. This data store is meant to be used as local storage for one single process on one laptop. The data store exposed as a library to clients that can instantiate a class and work with the data store.

## Instructions 

### create operation

  create(key, value) 
  or
  create(key, value, ttl)  // ttl => (time-to-live)- must be in seconds
  
### read operation
  
  read(key)
   
### delete operation
  
  delete(key)
  

## About 'Errors'
  <ul>
    <li><b>Empty File</b> -\
          Calls read/delete operation when file doesn't have any values (especially at very first instance without creating any values before).</li>
    <li><b>Key or Value size beyond the limit</b> -\
          Raises When Key or Value size beyond the given constraints.</li>
    <li><b>Invalid Key</b> -\
          Raises if given key doesn't exists.
    </li>
    <li><b>Key already exists</b> -\
          Raises when key already exists in the file.
    </li>
  </ul>
