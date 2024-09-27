---
tags:
  - posix
  - operatingsystem
---
1. [reddit](https://www.reddit.com/r/osdev/comments/lq9bbn/forkexec_vs_createprocess/)
2. The `fork` system call creates a new process and continue execution in both the parent and the child from the point where the `fork` function was called.
3. `CreateProcess` creates a new process and load a program from disk. 
4. The only similarity is that the end result is a new process is created.

CreateProcess takes the following steps:
- Create and initialize the process control block (PCB) in the kernel.
- Create and initialize a new address space.
- Load the program prog into the address space.
- Copy arguments args into memory in the address space.
- Initialize the hardware context to start execution at “start”.
- Inform the scheduler that the new process is ready to run.

Unix's fork takes the following steps:
- Create and initialize the process control block (PCB) in the kernel
- Create a new address space
- Initialize the address space with a copy of the entire contents of the address space of the parent
- Inherit the execution context of the parent (e.g., any open files)
- Inform the scheduler that the new process is ready to run


5. [stackoverflow ans](https://stackoverflow.com/questions/13839935/forking-and-createprocess)
6. 