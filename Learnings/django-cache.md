# Django Cache

Django lets you cache certain expensive results that dont have to be calculated for each request. Using Django cache you can cache the results of `GET` and `HEAD` apis. 

## Cache Strategies

### 1. Per-Site Cache
- Caches the entire Site
- Uses Middleware to save and retreive the Cached Data

### 2. Per-View Cache
- Caches perticular view
- Uses decorator to achieve caching

### 3. Template Fragment Caching
- To cache perticular part of tempplate.

### 4. Low Level Caching APIs
- If you want cache perticular query results. which happen constantly
- To design these kinds of custom solution, low level api can be used

## Internals
- Django gives option to choose the Cache backend as per our needs. 
- We can choose proper backend according to system needs. 
- Some of the options are 
    - Redis
    - Local Memory
    - Database Cache
    - MemCached
    - File System 
- Latency and durability will differ according to backend Cache engines.
- But the base implementtation remains same.
- A Internal LRU cache is used. To retain the freshness of cache a `OrderedDict` is used.
- On creation of new cache record or use of old record, the record is moved to the end of cache dict.
- When Cache limit exceeds, certain number of older records are culled.
