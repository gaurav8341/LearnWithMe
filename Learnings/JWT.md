# JWT: Json Web Token

JWT is open standanrd (RFC 7519) to transmit information securely between two parties.
JWT uses HMAC algorithm but can also use public/private key algos like RSA or ECDSA
mostly used for Authentication ie to transmit data from client to server. 

Is token based authentication technique 
Server gives the token upon login. 

Unlike normal token which are created when user is created and saved in db. 
These JWT are made on fly as per algorithm defined.
More secure than normal token based auth
Normal Token if once stolen from client side. Anyone with the token can access apis 
The above can be avoided in JWT if we explore the token expiration policies 

## Structure of JWT.

> Header.Payload.Signature

eg Token : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

### Header:
The Header contains the type of the token and the signing algorithm , i.e. HS256 or RSA. The Header is Base64Url encoded.

```
{
"alg":"HS256",
"typ":"JWT"
}
```

### Payload:
The Header contains the type of the token and the signing algorithm , i.e. HS256 or RSA. The Header is Base64Url encoded.

```
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```

### Signature:
The Signature (the last part of the token) is created out of signing the Header, the Payload, and a Secret that only you know of, using the specified algorithm.

Signature is created using below code. HMAC generated the signature for us. secret key is secret.

```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)
```

## What to Explore:
See how JWT works how it stores the secret how keys are exchanged in case of key pair algos. and so on.Explore SimpleJWT code

## Source: 

1. (Stackoverflow)[https://stackoverflow.com/questions/66044481/is-it-secure-to-authenticate-web-socket-connections-using-jwt]
2. (jwt.io)[https://jwt.io]
3. 
