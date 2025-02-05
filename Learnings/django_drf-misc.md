# Django Leanings

1. Middleware:
    Middleware acts as layer between the actual view code run and api request.
    They are defined in settings.py
    Are executed sequentially

2. Permissions
    As name suggests each api endpoint should only be authorized for use based on user roles and other relevant info.
    ObjectLevelPermission: 
        While normal permission only gives the permission to any views or View Class
        This can be set on each individual record.


3. Class based views:
    ObjectLevelPermssion isnt possible for functional apis. need CBV
    You can also implment Pagination, Serilizer and other such things here.
    CBV should be preferred.


4. JWT

5. DRF- Django-rest-framework

6. Decorators

7. Websockets and StreamingHttpResponse
    WebSocket is 2 way street . not very efficient

8. ViewSet:
    what is this and what is mixin