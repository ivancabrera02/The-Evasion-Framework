# Process Hollowing

Process Hollowing is an evasion technique commonly used by malware to inject malicious code into a legitimate operating system process. This method allows malicious code to run under the guise of a trusted process, making it more difficult to detect by security solutions.

Development of the technique:

- Process creation

The attacker creates a new process in a suspended state (using functions like CreateProcess on Windows). This process is usually a legitimate operating system application, such as explorer.exe or svchost.exe.

- 'Hollow out'

<img src="phollow3.png" >

Once the suspended process is created, the attacker hollows out the legitimate process. This is done by detaching or freeing the sections of memory that contain the legitimate code of the process. In technical terms, this is achieved using the Nt/ZwUnmapViewOfSection function

- Malicious Code Injection

The attacker then allocates a block of memory in the flushed process address space using VirtualAllocEx and writes the malicious code to that memory with WriteProcessMemory.

- Execution

 <img src="phollow4.png" >

The attacker modifies the process's Instruction Pointer to point to the start of the newly injected malicious code. This is done using the SetThreadContext function.

<img src="phollow2.png" >

- Resumption of the Process

Finally, the suspended process is resumed (using ResumeThread), but instead of executing the original, legitimate code, it now executes the malicious code that has been injected.

<img src="phollow1.png" >

