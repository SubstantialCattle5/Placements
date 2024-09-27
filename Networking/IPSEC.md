---
tags:
  - networking
---
1. Group of protocols used to secure connections in between devices. 
2. "IPSEC" -> IP : Internet Protocol + SEC : Security 
3. IPsec is secure because it adds encryption* and authentication to this process.
4. Port - 500 
5. Examples - sending mail through a postal service, a person typically would not write their message on the outside of the envelope. Instead, they enclose their message inside the envelope so that no one who handles the mail between sender and recipient can read their message. However, networking protocol suites like TCP/IP are only concerned with connection and delivery, and messages sent are not concealed. Anyone in the middle can read them. IPsec, and other protocols that encrypt data, essentially put an envelope around data as it traverses networks, keeping it secure.
6. [[VPN]] use the IPsec protocol suite to establish and run these encrypted connections. 
7. not all VPN use IPsec. 
	1. Another protocol for VPNs is [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)/[TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), which operates at a different layer in the [[OSI model]] than IPsec.

## How does IPSEC work? 

1. A protocol is a specified way of formatting data so that any networked computer can interpret the data. 
2. A suite of protocols 
	1. **Authentication Header (AH): The AH protocol ensures that data packets are from a trusted source and that the data has not been tampered**
	2. **Encapsulating Security Protocol (ESP):** 
		1. ESP encrypts the IP header and the payload for each packet  
		2. Transport mode is used, in which case it only encrypts the payload.
	3. **Security Association (SA):**
		1. SA refers to a number of protocols used for negotiating encryption keys and algorithms
		2. One of the most common SA protocols is **Internet Key Exchange (IKE).**
	4. IPSEC runs directly on top of IP 


## What is the difference between IPsec tunnel mode and IPsec transport mode?
### Tunnel Mode 
1. IPsec tunnel mode is used between *two dedicated routers*, with each router acting as one end of a virtual "tunnel" through a public network. 
2. The original IP header containing the final destination of the packet is encrypted, in addition to the packet payload. 
3. To tell intermediary routers where to forward the packets, IPsec adds a new IP header. 
4. At each end of the tunnel, the routers decrypt the IP headers to deliver the packets to their destinations.

## Transport Mode 
1. the payload of each packet is encrypted, but the original IP header is not. 
2. Intermediary routers are thus able to view the final destination of each packet — unless a separate tunneling protocol (such as [GRE](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)) is used.