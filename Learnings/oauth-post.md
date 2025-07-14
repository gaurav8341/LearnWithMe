# OAuth 2.0

## Introduction

OAuth 2.0 is a token based third party authorization protocol. Its little bit different than traditional client server based authorization, where server has client authorization data stored and client gives that data to access the server. In OAuth 2.0 model, the third party applications ask for certain resources on behalf of user without exposing user credentials. Looking from user perspective, think of it as instead of remembering multiple passwords, you remember one user credential. This model makes the user sign in and sign up very easy. Lets look how it works. This authorization model is stateless so the client do not need to save the user sessions. (Note: While this protocol is stateless for the client, the Authorization Server maintains some data such as Authorization Codes, Code Verifiers for client authentication, and Refresh Tokens.)

## How it works?

### Entities in OAuth 2.0

1.  **Resource Owner**:
    * Owner of the resource
    * is capable of granting access to the resource.
    * When we try to login through Google, then we are the resource owner.

2.  **Resource Server**:
    * The server hosting the protected resources (e.g., Google's API endpoints for Photos, Calendar, Drive).
    * Capable of accepting and responding to protected resource requests using access tokens. It enforces access control based on the token's validity and associated permissions.

3.  **Client**:
    * Entity making resource request on behalf of resource owner along with its auth keys.
    * The application (e.g., a website, mobile app, desktop application) making protected resource requests on behalf of the Resource Owner.
    * It is identified by a `client_id` and may have a `client_secret` (for confidential clients).

4.  **Authorization Server**:
    * Server issuing access tokens to client after authentication and authorization from Resource owner.
    * Authorization Server and Resource Server can be the same.

-----------------------------------------

### Protocol Flow

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
````

1.  **Authorization Request**
    Client asks for authorization from the resource owner. It can be made directly or through the **Authorization Server** as an intermediary.

2.  **Authorization Grant**
    If the authorization request is approved by the Resource Owner, then an **Authorization Grant** credential is given to the client.

3.  **Access Token Request**
    The Client requests for an Access Token using the **Authorization Grant** to the **Authorization Server**.

4.  **Access Token Issue**
    The **Authorization Server** after checking the validity of the grant and authenticating the client. If valid, then an **Access Token** and **Refresh Token** is given to the client.

5.  **Protected Resource Request**
    The **Client** uses the **Access Token** to get the resources it needs from the **Resource Server**.

6.  **Protected Resource Response**
    The **Resource Server** validates the token, and serves the request if the token is valid.

To get the **Authorization Grant** from the Resource Owner, the **Authorization Server** is usually used as an intermediary.


------------------------------------

### Some Important Considerations

####  **Scope**:
    
What kind of resources the client needs to access on behalf of the *Resource Owner* needs to be properly defined. In a normal user flow, this information is presented to the user in the consent screen, and the tokens issued to the application will be limited to the scopes granted. During Client registration with the Authorization Server, the scope required by the client is asked beforehand.



#### **Redirect URI**:
    
During the initial user consent phase, the *redirect URI* is given. After successfully authorizing the client application, the user should be redirected to the client page. This is also important for security, as this URI is sent alongside the auth grant code. To make sure this auth grant code is given to the intended client application, the *redirect URI* is matched with the predefined client *redirect URI*. If the *redirect URI* does not match with the initially provided client URI, the authorization fails.



#### **Tokens**:

After successful authorization, usually two tokens are given: an *Access Token* and a *Refresh Token*. These JWT tokens have a header which contains metadata about the token. The payload contains certain user info along with the expiry date of the token. The Signature is created out of signing the Header and Payload. Either the HMAC algorithm can be used which uses a single secret key, or RSA can be used which uses a public-private key pair to generate the signature. The Public keys are made available by the Authorization Server.

After getting the tokens, the client uses the access token by attaching it to the request header to get any resource from the Resource Server. The **Resource Server** checks the validity of the request; it denies the request if the access token is not present or is expired. The Refresh token, which has a longer expiry time, can be used to get new versions of tokens.




#### **Authorization Grant**:

After the Resource Owner approves the client request, the **Authorization Server provides the Authorization grant**. Using this Authorization grant, the client can get the tokens from the **Authorization Server**.

There are four types of Authorization grants:

* **Authorization Code**:
The auth code is attached with the *redirect URI*. The client gets the auth code from the *redirect URI* and sends the token request to the *Authorization Server*. This gives the ability to also authenticate the client. This is most commonly used today.
* **Implicit**:
The tokens are directly passed to the user itself. This is not recommended.
* **Resource Owner Password Credential**:
The Resource Owner's Password is shared with the client directly. This is not considered a safe practice and is avoided.
* **Client Credential**:
The Client Credential Grant is used for scenarios where the client application itself is the entity requesting access to protected resources. It acts on its own behalf, rather than impersonating or acting on behalf of an end-user (Resource Owner). This grant type is ideal for machine-to-machine interactions, such as one service calling another's API. Refresh Token is not included in this type.



#### **Proof Key for Code Exchange**:

There is a possibility that someone intercepts the Auth Code and uses that auth code to generate the tokens. To avoid the interception of the Auth Code attack, this protocol is used.

```mermaid
graph TD
subgraph Authz Server
    AuthzEndpoint(Authorization Endpoint)
    TokenEndpoint(Token Endpoint)
end

subgraph Client
        Client_Start(Client)
end

Client_Start -- (A) Authorization Request<br>+ t(code_verifier), t_m --> AuthzEndpoint
AuthzEndpoint -- (B) Authorization Code --> Client_Start
Client_Start -- (C) Access Token Request<br>+ code_verifier --> TokenEndpoint
TokenEndpoint -- (D) Access Token --> Client_Start
```

1.  The client creates and records a secret named the `code_verifier` and derives a transformed version `t(code_verifier)` (referred to as the `code_challenge`), which is sent in the OAuth 2.0 Authorization Request along with the transformation method `t_m`.

2.  The Authorization Endpoint responds as usual but records `t(code_verifier)` and the transformation method.

3.  The client then sends the authorization code in the Access Token Request as usual but includes the "code\_verifier" secret generated at (A).

4.  The authorization server transforms `code_verifier` and compares it to `t(code_verifier)` from (B). Access is denied if they are not equal.

An attacker who intercepts the authorization code at (B) is unable to redeem it for an access token, as they are not in possession of the `code_verifier` secret.


-------------------------

## Resources

1.  [RFC 6749: The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)

2.  [RFC 7636: Proof Key for Code Exchange by OAuth Public Clients](https://datatracker.ietf.org/doc/html/rfc7636)

<!-- end list -->
