# unix_rest_api

## UNIX BANKING APP API


### FUNDAMENTAL IDEAS :

The API is divided into 4 subpages - /get, /post, /put, /delete. 

All arguments are supplied as request args in the URL (the ?/& format appended to the URL). 

The following arguments are possible (depending on the page being used as well - they can't be used in every page): 

###### id : a unique integer describing the transaction ID 

###### amount : a numeric value that is internally used as float (you can supply it as int in the POST/PUT queries but must use the float form in GET queries) - e.g. 49.95 

###### vendor : a string describing the transaction vendor (recommended: also use street names to single out vendors) - e.g. Burger King, 7th Street 

###### location : a string describing the transaction location (recommended format: city, state abbrev, country abbrev) - e.g. San Francisco, CA, USA 

###### purpose : a string describing the purpose of the transaction (recommended format: single word) - e.g. Coffee 

###### date : a hyphen separated string of ISO format - YYYY-MM-DD - can only be used in GET queries for filtering 

Everything else is described in the following sections.



### GET

Access this page by adding /get to the core URL 

Supports one or many of all the aforementioned arguments together. If no row found, returns single element json result containing key NotFoundError with value true 

Examples

- Inspect all rows in database: ```/get``` 

- Get row corresponding to ID 3 in database ```/get?id=3 ```

- Get row(s) corresponding to 27 July 2020 ```/get?date=2020-07-27 ```

- Get rows(s) corresponding to amount 45.99 and location Los Angeles: ```/get?amount=45.99&location=Los Angeles, CA, USA``` 




### PUT

Access this page by adding /put to the core URL 

An ID that exists must be supplied. Date can not be modified. Same ?/& format for updating fields 

Examples

- Modify amount corresponding to ID 2 ```/put?id=2&amount=35.99 ```

- Modify purpose corresponding to ID 1 ```/put?id=1&purpose=Tea ```




### POST

Access this page by adding /post to the core URL 

ID and Amount must be supplied. Date can not be supplied (it is automatically assigned as the time the request was forwarded). Same ?/& format for other fields 
Examples

- Add new row for ID = 10, Amount = 29.99, purpose = Dinner ```/post?id=10&amount=29.99&purpose=Dinner``` 

- Add example bare minimum row for ID = 7, Amount = 15.99 ```/post?id=7&amount=15.99 ```




### DELETE

Access this page by adding /delete to the core URL 

Only one mandatory argument is considered - the unique ID - and it must exist. 

Examples

- Delete Row Corresponding to ID 3 ```/delete?id=3 ```



