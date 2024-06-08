# Process

The process is a management object that provides the information necessary to execute a program.
A process does not run or execute code, threads do that.
The process does not know or need the physical addresses of the memory, it only knows the virtual addresses and it is the memory manager of the operating system that does this translation.

A process contains:

- A private memory space.
- An amount of associated private physical memory (working set)
- The executable file, a link to the file on disk that contains the main function.
- A flag table of the kernel object handlers associated with it.
- A security token that contains the security descriptors of the process.
- Priority, that priority will be the one assigned to the threads of the process.

A process ends when:

- The threads calls ExitProcess(Win32)
- Threads calls TerminateProcess(Win32)
- All their threads end.

# Threads

# Handles

# Jobs
