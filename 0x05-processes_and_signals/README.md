# Process and Signals

### Process Management in Unix/Linux

## Table of Contents
1. [What is a PID?](#what-is-a-pid)
2. [What is a process?](#what-is-a-process)
3. [How to find a process' PID](#how-to-find-a-process-pid)
4. [How to kill a process](#how-to-kill-a-process)
5. [What is a signal?](#what-is-a-signal)
6. [What are the 2 signals that cannot be ignored?](#what-are-the-2-signals-that-cannot-be-ignored)

---

### What is a PID?

A PID, or Process IDentifier, is a unique numerical identifier assigned to each running process in an operating system. It is used to uniquely identify and manage processes. PIDs are essential for various process-related operations, such as monitoring, termination, and communication between processes.

### What is a process?

A process is a running instance of a program in an operating system. It represents the execution of a program's instructions in memory, along with its associated resources (e.g., CPU, memory, file handles). Each process is independent, isolated from other processes, and has its own PID.

### How to find a process' PID

To find a process's PID in Unix/Linux, you can use the `ps` command. For example:
```bash
ps aux | grep process_name
Replace process_name with the name of the process you want to find. This command will display information about the matching process, including its PID.
```

### How to kill a process
To terminate or kill a process in Unix/Linux, you can use the kill command. First, find the PID of the process using ps or other methods (as described above), and then execute:

```bash
kill PID
Replace PID with the actual process ID of the process you want to terminate.
```

### What is a signal?
A signal is a software interrupt delivered to a running process to notify it of a specific event or request. Signals are used for various purposes, such as process control, error handling, and communication between processes. They can trigger actions within a process, like terminating it or instructing it to perform a specific action.

### What are the 2 signals that cannot be ignored?
The two signals that cannot be ignored by a process are:

SIGKILL (signal number 9): This signal is used to forcefully terminate a process. It cannot be caught or blocked by the process, making it an effective way to stop a misbehaving or unresponsive process. However, it should be used with caution, as it can lead to data loss or corruption.

SIGSTOP (signal number 19): This signal is used to pause (suspend) a process's execution. Like SIGKILL, it cannot be ignored, but it allows the process to be resumed later using SIGCONT. SIGSTOP is often used for debugging and process management.
