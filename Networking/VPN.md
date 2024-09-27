---
tags:
  - networking
---
1. Network architecture to virtually extend a private network across multiple networks which are either untrusted (not controlled by the entity) or needs to be isolated(making lower n/w invisible).
2. Achieved by creating a link b/w computing devices and computer networks using [[tunneling protocols]] 
3. It is possible to make an unencrypted communication secure by using VPN with a tunneling protocol which uses encrpytion 
4. There are VPN Services which sell their own private newtwork for internet access. 
5. **Provider-Provision VPN** to isolate parts of the provider's own network infrastructure in virtual segments. (VLAN)


## VPN General Working 

1. A tunneling protocol is used to transfer the n/w message from applications(operating at OSI7) on one side of the tunnel and replay it on the other side, acting like a virtual substitute to the lower n/w or link layer. 
2. Application do not need to modify their message since virtual n/w or link is made available to the os 


## VPN topology configurations
## Remote Access 
1. A _host-to-network_ configuration is analogous to joining one or more computers to a network which cannot be directly connected.
2. This type of extension provides that computer access to [local area network](https://en.wikipedia.org/wiki/Local_area_network "Local area network") of a remote site, or any wider enterprise networks, such as an [intranet](https://en.wikipedia.org/wiki/Intranet "Intranet").
3. Each computer is in charge of activating its own tunnel towards the network it wants to join. The joined network is only aware of a single remote host for each tunnel.
## Site-to-site
1. Connects two networks. 




