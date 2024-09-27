---
tags:
  - operatingsystem
---
## What is Operating System ? 

1. A computer program, implemented in either software or firmware, which acts as an intermediary between users of a computer and the computer hardware
2. provide an environment in which a user can execute applications
3. The program that, after being initially loaded into the computer by a boot program, manages all of the other application programs in a computer.

## What is an API ? 

1. API provided by OS is a set of “system calls” – System call is
a function call into OS code that runs at
	1. higher privilege level of the CPU.
	2. Sensitive operations (e.g., access to hardware) are
allowed only at a higher privilege level.

## Different Roles of Operating System

### Role 1 : Provide Standard Library - Abstract Resources(CPU,RAM,Etc)

#### Advantages - 
1. Allow applications to reuse common facilities 
2. Provide higher lvl [[abstraction]]
#### Challenges - 
1. What is the correct amount of [[abstraction]]
2. How much hardware should be exposed. 

#### Abstractions 
1. [[FileSystem Abstraction Disk]]
2. [[Process Abstraction CPU]]
3. [[AddressSpace Abstraction Memory]]



### Role 2 : Resource Manager 

#### Advantages - 
1. Visualize resources so multiple applications can share. 
2. Protect applications from one another. 
#### Challenges - 
1. Correct mechanism
2. policies. 


