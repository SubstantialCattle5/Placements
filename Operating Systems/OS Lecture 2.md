---
tags:
  - operatingsystem
---
## Case study: Unix/xv6 shell (simplified)

```shell 
while(1) { 
	write(1,"$ ",2) ;  // system call with fd as 1 
	readcommand(0,command,args) ;  // parse user input, 0 = STDIN_FILENO
	if ((pid = fork()) == 0 ) { // fork calls a child process and executes it if pid is 1 
		exec(command,args,0) ; 
	} else if (pid > 0) { 
		wait(0);
	} else { 
		perror("Failed to Fork") ; 
	}
}
```

### Purpose for `wait(0)` 

1. both the parent and the child run concurrently.
2. prevent the parent from finishing its work before the child (which could lead to issues like zombie processes or improper resource cleanup), the parent can call `wait()`.
3. **Zombie Process** : 
	1. Completed execution but still exists in the process table because the parent hasn't yet collected its termination status.
	2. `wait()` helps the parent collect the exit status and clean up the child process properly.
4. **Return Value of `wait()`**: The `wait()` function returns the `pid` of the child that has terminated. If there are no child processes, it returns `-1`
5. This tells the parent process to pause and wait for **any child process** to terminate. The `NULL` argument means that the parent process is not interested in capturing the exit status of the child.`


1. [[Fork and exec (UNIX) vs CreateProcess(Windows)]]



### UNIX I/O facilities 

1. most have 3 os provided file descriptors 
	1. `stdin(0)` - connects to the keyboard 
	2. `stdout(1)` - connects to the console. - provides output
	3. `stderr(2)` - connects to the console. - throws error 
2.  ‘>’ redirects output (stdout) of ls to file tmp1
	1. `>` redirecting for stdout
	2. `<` redirecting for stdin
	3. `2>` for redirecting stderr 


### Pipe Command Syscall 

```bash 
sh < tests.sh | grep “fail” | wc -l
```

1. Kernel manages the flow
2. Unidirectional of data (bytes) from one process to another
3. **Signature** `pipe(int[2])`
```bash 
int pfd[2] ; 
pipe(pdf) ; # pdf[0] -> read end of pipe , pfd[1] -> write end of pipe
```

4. Inter process communication 
```bash
int pfd[2]; 
pipe(pfd); 
if ((pid = fork()) == 0) { 
	write(pfd[1], “Hello from child”, 16); 
	exit(0); 
} else (pid > 0) { 
	sz = read(pfd[0], buf, 100); // blocks until write is executed by child 
	write(1, buf, sz); 
	wait(0); 
}
```