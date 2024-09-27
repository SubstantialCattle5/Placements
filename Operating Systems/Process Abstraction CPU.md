---
tags:
  - operatingsystem
  - abstraction
---
1. OS creates and manages processes and Loads program executable (code, data) from disk to memory. 
2. Each process has the illusion of having the complete CPU. 
3. OS timeshares CPU between processes
4. OS enables coordination between processes

![[Pasted image 20240920033313.png]]
## Abstraction 

1. Unique Identifier(PID). 
2. Memory Image 
	1. Code & Data (Static)
	2. Stack and heap (dynamic)
3. CPU Context : 
	1. Program Counter 
	2. Stack Pointer
4. File Descriptor table - Pointers to opened files and devices. 

## Related System Calls 
1. fork() 
	1. creates a new process by duplicating the calling process.  The new process is referred to as the child process. The calling process is referred to as the parent process.
	2. child process and the parent process run in separate memory spaces
	3. PID is different for each children and parent processes.
2. exec("./filename")
	1. Exec  replaces  the currently running shell with a new command. On successful completion, exec never returns. exec cannot be used
	    inside a pipeline. 


