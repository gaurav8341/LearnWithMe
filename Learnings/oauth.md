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

To get the **Authorization Grant** from Resource Owner, the **Authorization Server** is usually used as intermediary.

## Resources

1. (RFC 6749: The OAuth 2.0 Authorization Framework)[https://datatracker.ietf.org/doc/html/rfc6749]

## TODO Research:

- Read RFC 9700
- Read OpenID Connect
- Read RFC 6749
    
## Mention

- Scope
- Authorization Bearer
- Threat modelling

## Rough Notes

## Auth Grant type

1. Auth code
The client directs user(Resource Owner) to auth server to get auth code -- auth grant type, after getting auth code auth server redirects RO back to client. This is only for auth code grant type.

Auth code gives ability to also authenticate the client. passes tokens to the client directly instead of user. 

auth code, scope and client id is visible to user, but there also client auth happens also PKCE(Proof Key for Code Exchange).

PKCE in short:

    clinet generates a code verifier and generats code challenge from code verifier before initiating auth flow.

    it passes code challenge to auth server along with code challenge method.

    auth server saves code challeng and method.

    if user authenticates, clint asks for token. it sends code verifier.

    auth server from previous code challenge and method. Recalculates the code challenge from client sent code verifier. if prev. code challenge and newly generated code challenge are same then PKCE is passed.

For private clients where the tokens are not passed to user, the Clinet id client secret can be used in place of PKCE.

State can be used to avoid CSRF attacks

CSRF (Cross-Site Request Forgery) attacks: Prevents an attacker from tricking a logged-in user into initiating an OAuth flow to the attacker's application but redirecting back to your application. If the state doesn't match the one your server initiated, you know the request wasn't legitimate from your app's perspective.

Binding Request and Response: Ensures that the response (the authorization code) belongs to the request that your client originally sent.



Auth code are intermediate creds using which you can get actual tokens

here scope is checked, client creds are (authnticated and authorized)checked and validated 

2. Implicit

No auth code bs. directly access/refresh token.good for frontend only system ie systems which run on browser (extentions). 
 
The authntication of client is not done

-- this is avoided today

3. RO password Creds

directly uuse the user creds to get tokens. 

-- not recommended

4. Client Credentials

authorization scope is limited to resources under control of client.

When client is resource owner. 

Machine to machine Communication. no other user.

auth between two services through api. say communication between orders service and payment service.

No refrech tokens provided.

-------------------------------------------------------------

HTTP Redirections:
 
## Client Registrations:

before Oauth to be enabled. Clint needs to be registered with Auth server. In this registration, clint type, redirect uri asre two main things required.

Two types of clint based on the clients ability to maintain authenticity of client creds, 

    1. Confidential
    2. Public 


