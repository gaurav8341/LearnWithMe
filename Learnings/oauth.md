# OAuth 2.0

- Oauth is Token based authentication model. 
- Different than traditional Client server authentication model.

## Entities in Oauth 2.0

1. **Resource Owner**:
    - Owner of the resource
    - is capable of granting access to the resource.
    - When we try to login through google. then we are resource owner

2. **Resource Server**:
    - The server hosting the protected resources (e.g., Google's API endpoints for Photos, Calendar, Drive).
    - Capable of accepting and responding to protected resource requests using access tokens. It enforces access control based on the token's validity and associated permissions.
    
3. **Client**:
    - Entity making resource request on behalf of resource owner along with its auth keys. 
    - The application (e.g., a website, mobile app, desktop application) making protected resource requests on behalf of the Resource Owner.
    - It is identified by a `client_id` and may have a `client_secret` (for confidential clients).

4. **Authorization Server**:
    - Server issuing access tokens to client after authntication and authorization from Resource owner
    - Authorization Server and Resource Server can be same.

## Protocol Flow

```mermaid
graph LR
    subgraph Client
        Client_Start(Client)
    end

    subgraph Resource Server
        RS_Start(Resource Server)
    end

    subgraph Authorization Server
        AS_Start(Authorization Server)
    end


    subgraph Resource Owner
        RO_Start(Resource Owner)
    end

    Client_Start -- (1) Authorization Request --> RO_Start
    RO_Start -- (2) Authorization Grant --> Client_Start

    Client_Start -- (3) Authorization Grant --> AS_Start
    AS_Start -- (4) Access Token --> Client_Start

    Client_Start -- (5) Access Token --> RS_Start
    RS_Start -- (6) Protected Resource --> Client_Start
```

1. **Authorization Request**
    Client asks for authorization from resource owner. It can be made directly or through **Authorization Server** as intermediary

2. **Authorization Grant**
    If authorization request is approved by Resource Owner, then a **Authorization Grant** credential is given to the client. There are four types of authorization grant

    - Authorization Code
    - Implicit
    - Resource Owner Password Credential
    - Client Credential

3. **Access Token Request**
    The Clint requests for Access Token using  **Authorization Grant** to the **Authorization Server**. 

4. **Access Token Issue**
    **Authorization Server** after checking the validity of the grant authenticated the client. If valid, then **Access Token** and **Referesh Token** is given to the client.

5. **Protected Resource Request**
    The **Client** uses the **Access Token** to get the resources it needs from **Resource Server**. I

6. **Protected Resource Response**
    The **Resource Server** validates the token, and serves the request if the token is valid

## Resources

1. (RFC 6749: The OAuth 2.0 Authorization Framework)[https://datatracker.ietf.org/doc/html/rfc6749]

