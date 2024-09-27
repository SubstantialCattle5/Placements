---
tags:
  - operatingsystem
---
In the shell, backgrounding a process (with `&`) involves forking the process and detaching it from the terminal so it can run independently in the background while the shell continues to accept and execute new commands.

### **How does the shell implement backgrounding (`&`)?**

1. **Forking**: When you issue a command like `compute &`, the shell creates a child process using the `fork()` system call. The child process is responsible for executing the `compute` command.
   
2. **Running in Background**: The key part of the backgrounding process (`&`) is that the parent shell does not wait for the child process to finish. This means the shell can immediately accept and execute the next command without being blocked by the background process.
   - The shell typically calls `fork()` to create a child process and then calls `exec()` to replace the child process's memory space with the command.
   - The shell does **not** call `wait()` on the child process right away. Instead, the child runs independently, and the shell continues running.

3. **Process Grouping**: 
	1. The background process is typically assigned to a different process group so that it is not tied to the terminal’s job control mechanism. 
	2. This prevents the shell from suspending or stopping it when handling foreground jobs.

5. **Shell Prompt**: The shell immediately returns the prompt to the user and keeps track of the background processes (often listing the job number and process ID).

### **What if a background process exits while the shell waits for a foreground process?**

The shell uses signal handling to deal with background processes. Specifically:

- When a background process terminates (either by completion or by receiving a signal), the shell receives a `SIGCHLD` signal, which informs it that a child process has terminated.
  
- The shell can handle this in different ways:
  - It might log the termination in the background without interrupting the current foreground process.
  - Some shells print a message after the current foreground command finishes to inform you of the termination of the background process (e.g., `[1]+  Done`).
  
- If the shell is waiting for a foreground process when a background process terminates, it typically doesn’t handle the background process termination immediately but records the event to be handled after the foreground process finishes.

### **Lists of commands, separated by `";"`**

When multiple commands are separated by a semicolon (`;`), the shell executes them sequentially in the current shell environment:
- The shell parses the entire command string, splits the commands at the semicolons, and executes each command in the order it appears.
- Each command is run in the same shell instance, meaning any changes to the environment (e.g., variable assignments) persist across commands.

For example, `touch a; ls`:
1. The shell first executes `touch a`, creating the file `a`.
2. After `touch a` completes, the shell moves to the next command, `ls`, and lists the contents of the current directory.

### **Subshells implemented using `(` and `)`**

Subshells are a way to run commands in a separate child shell process. The commands inside a subshell have their own environment, which is isolated from the parent shell.

- When the shell encounters parentheses `()`, it creates a subshell (using `fork()`) to execute the enclosed commands.
- Changes made to the environment within the subshell (e.g., modifying variables or changing directories) do not affect the parent shell.
- After the commands inside the subshell finish executing, the subshell terminates, and the parent shell continues execution from the next command after the closing parenthesis.

Example:
```sh
COMMAND1;
COMMAND2;
(
  PATH=/bin
  COMMAND3
  COMMAND4
);
COMMAND5
```
Here:
1. `COMMAND1` and `COMMAND2` execute in the current shell.
2. `COMMAND3` and `COMMAND4` execute in a subshell with the modified `PATH` environment variable.
3. `COMMAND5` executes in the parent shell, unaffected by the environment changes made inside the subshell.

### **Summary of Shell Functionalities**:
- **Backgrounding (`&`)**: Fork a child process and continue execution without waiting for it to finish.
- **Handling background process exit**: The shell handles background process exits via signal handling, specifically using `SIGCHLD`.
- **Command lists (`;`)**: Execute commands sequentially in the current shell.
- **Subshells (`(` and `)`)**: Fork a subshell where commands run in an isolated environment, and any changes made don't affect the parent shell.

