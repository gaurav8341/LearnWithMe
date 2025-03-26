# SSL

> Secure Cockets Layer

- Developed in 1995 for ensuring Privacy, Authentication and data integrity.
- Predecessor to modern TLS
- Handshake is done exchanging the keys after TCP.
- Digitally signs data for data integrity.
- Originally data transmitted through ssl was human reaable plaintext.
- After ssl Handshake the data transmitted is encryptes
- SSL certificated which is exchanged in SSL handshake contains websites' public key.


# IETF Notes

## SSL Protocol v3.0

- Protocol consits of 2 layers
- At lowest level , layered on top of reliable transport protocol (TCP RFC793) is SSL record protocol.
- SSL record protocol is used to encapsulate other high level protocols like SSL Handshake Protocol
- In SSL Handshake protocol, server and client aunthenticate each other, and negotiate encrytption alogorithm and encrypt keys.
- After SSL handshake, application protocol kicks in.
- SSL is application protocol independant eg will work with http, SMTP etc.
- TCP-SSL-HTTP
