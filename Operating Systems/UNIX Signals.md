---
tags:
  - operatingsystem
---
1. limited form of inter-process communication
2. When a signal is sent, the operating system interrupts the target process's normal flow of execution to deliver a signal.
3. If the process has previously registered a signal handler, that routine is executed. Otherwise, the default signal handler is executed.
4. Examples:
    - Ctrl-C sends SIGINT; by default, this causes the process to terminate
    - Ctrl-Z sends SIGTSTP; by default, this causes the process to suspend execution
    - SIGCHLD signal is sent to a process when a child process terminates.
    - SIGFPE is the floating point exception (for example, on divide by zero)
    - SIGSEGV on segmentation fault
    - SIGUSR1 and SIGUSR2 are user-defined signals

1. **`kill(pid, signum)`**:
   - This function sends a specific signal (`signum`) to a process with a given `pid` (process ID). The `kill` function doesn't just "kill" processes; it can send any signal, such as `SIGTERM` (to terminate a process), `SIGHUP`, `SIGSTOP`, or custom-defined signals.
   
   - **Arguments**:
     - `pid`: The process ID to which the signal will be sent.
     - `signum`: The signal number that will be sent to the process. Signals can be predefined ones like `SIGTERM`, `SIGKILL`, or custom ones.
   
   - Example:
     ```c
     kill(1234, SIGTERM); // Sends the SIGTERM signal to the process with pid 1234
     ```

2. **`signal(signum, void (*handler)(int))`**:
   - This function sets up a signal handler for the process. A signal handler is a function that will be called automatically when a specific signal (`signum`) is received by the process.
   
   - **Arguments**:
     - `signum`: The signal number that you want to handle (e.g., `SIGINT`, `SIGTERM`).
     - `handler`: A pointer to the function that will be executed when the process receives the signal. This function should accept an integer argument, which will be the signal number.
   
   - Example:
     ```c
     void my_signal_handler(int signum) {
         printf("Received signal %d\n", signum);
     }
     
     signal(SIGINT, my_signal_handler); // Calls my_signal_handler when SIGINT is received (Ctrl+C)
     ```

In short:
- `kill(pid, signum)` sends a signal to a process.
- `signal(signum, handler)` allows you to define how a process responds to specific signals by associating the signal with a custom handler function.



**Example 2**

For example, if the current process ID (PID) of inetd is 4140, we would type:

`kill -SIGHUP 4140`

Another common use of signals is to stop a running process. To stop the inetd process completely, we would use this command:

`kill 4140`

By default, the kill command sends the SIGTERM signal. If SIGTERM fails, we can escalate to using the SIGKILL signal to stop the process:

`kill -9 4140`

**Because SIGKILL cannot be handled, stopping a process with SIGKILL is generally considered a bad idea. Using SIGKILL prevents a process from cleaning up after itself and exiting gracefully**

