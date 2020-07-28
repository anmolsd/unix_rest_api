#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 08:31:17 2020

@author: anmolsingh
"""
indexPageSource = """
<body style="background-color:#FFFFFF">
<br><br>
<h1 style="margin-left:30px;font-family:avenir;color:#AE81FF"> UNIX BANKING APP API </h1>
<br>
<h2 style="margin-left:90px;font-family:avenir;color:#FD971F"> <u> FUNDAMENTAL IDEAS </u>: </h2>
<h3 style="margin-left:90px;font-family:avenir">
    <ul>
    <li> The API is divided into 4 subpages - /get, /post, /put, /delete. <br><br>
    <li> All arguments are supplied as request args in the URL (the ?/& format appended to the URL). <br><br>
    <li> The following arguments are possible (depending on the page being used as well - they can't be used in every page): <br><br>
        <ul>
        <li> <code style="color:#F92672;font-size:25px"> id </code>: a unique integer describing the transaction ID <br><br>
        <li> <code style="color:#F92672;font-size:25px"> amount </code>: a numeric value that is internally used as float (you can supply it as int in the POST/PUT queries but must use the float form in GET queries) - e.g. 49.95 <br><br>
        <li> <code style="color:#F92672;font-size:25px"> vendor </code>: a string describing the transaction vendor (recommended: also use street names to single out vendors) - e.g. Burger King, 7th Street <br><br>
        <li> <code style="color:#F92672;font-size:25px"> location </code>: a string describing the transaction location (recommended format: city, state abbrev, country abbrev) - e.g. San Francisco, CA, USA <br><br>
        <li> <code style="color:#F92672;font-size:25px"> purpose </code>: a string describing the purpose of the transaction (recommended format: single word) - e.g. Coffee <br><br>
        <li> <code style="color:#F92672;font-size:25px"> date </code>: a hyphen separated string of ISO format - YYYY-MM-DD  - can only be used in GET queries for filtering <br><br> 
        </ul>                                                   
    <li> Everything else is described in the following sections.
    </ul>
</h3>
<br><br>
<h2 style="margin-left:125px;font-family:avenir;color:#66D9EF"> GET </h2>
<h3 style="margin-left:125px;font-family:avenir"> 
    <ul>
    <li> Access this page by adding /get to the core URL <br><br>
    <li> Supports one or many of all the aforementioned arguments together. If no row found, returns single element json result containing key NotFoundError with value true 
    <br>
    <li> <h3 style="font-family:avenir"> Examples </h3>
    <ul> 
    <li> Inspect all rows in database: <code style="color:#F92672;font-size:25px"> /get </code> <br><br>
    <li> Get row corresponding to ID 3 in database <code style="color:#F92672;font-size:25px"> /get?id=3 </code> <br><br>
    <li> Get row(s) corresponding to 27 July 2020 <code style="color:#F92672;font-size:25px"> /get?date=2020-07-27 </code> <br><br>
    <li> Get rows(s) corresponding to amount 45.99 and location Los Angeles: <code style="color:#F92672;font-size:25px"> /get?amount=45.99&location=Los Angeles, CA, USA </code> <br><br>
    </ul> 
    </ul>
</h3>
<br><br>
<h2 style="margin-left:125px;font-family:avenir;color:#66D9EF"> PUT </h2>
<h3 style="margin-left:125px;font-family:avenir"> 
    <ul>
    <li> Access this page by adding /put to the core URL <br><br>
    <li> An ID that exists must be supplied. Date can not be modified. Same ?/& format for updating fields <br>
    <li> <h3 style="font-family:avenir"> Examples </h3>
    <ul> 
    <li> Modify amount corresponding to ID 2 <code style="color:#F92672;font-size:25px"> /put?id=2&amount=35.99 </code> <br><br>
    <li> Modify purpose corresponding to ID 1 <code style="color:#F92672;font-size:25px"> /put?id=1&purpose=Tea </code> <br><br>
    </ul>
    </ul>
</h3>
<br><br>
<h2 style="margin-left:125px;font-family:avenir;color:#66D9EF"> POST </h2>
<h3 style="margin-left:125px;font-family:avenir"> 
    <ul>
    <li> Access this page by adding /post to the core URL <br><br>
    <li> ID and Amount must be supplied. Date can not be supplied (it is automatically assigned as the time the request was forwarded). Same ?/& format for other fields <br>
    <li> <h3 style="font-family:avenir"> Examples </h3>
    <ul> 
    <li> Add new row for ID = 10, Amount = 29.99, purpose = Dinner <code style="color:#F92672;font-size:25px"> /post?id=10&amount=29.99&purpose=Dinner </code> <br><br>
    <li> Add example bare minimum row for ID = 7, Amount = 15.99 <code style="color:#F92672;font-size:25px"> /post?id=7&amount=15.99 </code> <br><br>
    </ul>
    </ul>
</h3>
<br><br>
<h2 style="margin-left:125px;font-family:avenir;color:#66D9EF"> DELETE </h2>
<h3 style="margin-left:125px;font-family:avenir"> 
    <ul>
    <li> Access this page by adding /delete to the core URL <br><br>
    <li> Only one mandatory argument is considered - the unique ID - and it must exist. <br>
    <li> <h3 style="font-family:avenir"> Examples </h3>
    <ul> 
    <li> Delete Row Corresponding to ID 3 <code style="color:#F92672;font-size:25px"> /delete?id=3 </code> <br><br>
    </ul>
    </ul>
</h3>
<br><br>
</body>
"""