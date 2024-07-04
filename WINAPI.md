# Offensive Windows APIs

## Enumeration
- CreateToolhelp32Snapshot

```
HANDLE CreateToolhelp32Snapshot(
  [in] DWORD dwFlags,
  [in] DWORD th32ProcessID
);
``` 
https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-createtoolhelp32snapshot

- EnumProcesses

```
BOOL EnumProcesses(
  [out] DWORD   *lpidProcess,
  [in]  DWORD   cb,
  [out] LPDWORD lpcbNeeded
);
```
https://learn.microsoft.com/es-es/windows/win32/api/psapi/nf-psapi-enumprocesses

- EnumProcessModules
```
BOOL EnumProcessModules(
  [in]  HANDLE  hProcess,
  [out] HMODULE *lphModule,
  [in]  DWORD   cb,
  [out] LPDWORD lpcbNeeded
);
```
https://learn.microsoft.com/en-us/windows/win32/api/psapi/nf-psapi-enumprocessmodules

- EnumDeviceDrivers
```
BOOL EnumDeviceDrivers(
  [out] LPVOID  *lpImageBase,
  [in]  DWORD   cb,
  [out] LPDWORD lpcbNeeded
);
```
https://learn.microsoft.com/es-es/windows/win32/api/psapi/nf-psapi-enumdevicedrivers

## Injection
- CreateRemoteThread
```
HANDLE CreateRemoteThread(
  [in]  HANDLE                 hProcess,
  [in]  LPSECURITY_ATTRIBUTES  lpThreadAttributes,
  [in]  SIZE_T                 dwStackSize,
  [in]  LPTHREAD_START_ROUTINE lpStartAddress,
  [in]  LPVOID                 lpParameter,
  [in]  DWORD                  dwCreationFlags,
  [out] LPDWORD                lpThreadId
);
```
https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread

- CreateRemoteThreadEx
```
HANDLE CreateRemoteThreadEx(
  [in]            HANDLE                       hProcess,
  [in, optional]  LPSECURITY_ATTRIBUTES        lpThreadAttributes,
  [in]            SIZE_T                       dwStackSize,
  [in]            LPTHREAD_START_ROUTINE       lpStartAddress,
  [in, optional]  LPVOID                       lpParameter,
  [in]            DWORD                        dwCreationFlags,
  [in, optional]  LPPROC_THREAD_ATTRIBUTE_LIST lpAttributeList,
  [out, optional] LPDWORD                      lpThreadId
);
```
https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethreadex

- VirtualAlloc
```
LPVOID VirtualAlloc(
  [in, optional] LPVOID lpAddress,
  [in]           SIZE_T dwSize,
  [in]           DWORD  flAllocationType,
  [in]           DWORD  flProtect
);
```
https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc

- VirtualProtect
```
BOOL VirtualProtect(
  [in]  LPVOID lpAddress,
  [in]  SIZE_T dwSize,
  [in]  DWORD  flNewProtect,
  [out] PDWORD lpflOldProtect
);
```
https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect
## Evasion
- SleepEx
```
DWORD SleepEx(
  [in] DWORD dwMilliseconds,
  [in] BOOL  bAlertable
);
```
https://learn.microsoft.com/es-es/windows/win32/api/synchapi/nf-synchapi-sleepex

- Sleep
```
void Sleep(
  [in] DWORD dwMilliseconds
);
```
https://learn.microsoft.com/es-es/windows/win32/api/synchapi/nf-synchapi-sleep

- IcmpSendEcho
```
IPHLPAPI_DLL_LINKAGE DWORD IcmpSendEcho(
  [in]           HANDLE                 IcmpHandle,
  [in]           IPAddr                 DestinationAddress,
  [in]           LPVOID                 RequestData,
  [in]           WORD                   RequestSize,
  [in, optional] PIP_OPTION_INFORMATION RequestOptions,
  [out]          LPVOID                 ReplyBuffer,
  [in]           DWORD                  ReplySize,
  [in]           DWORD                  Timeout
);
```
https://learn.microsoft.com/es-es/windows/win32/api/icmpapi/nf-icmpapi-icmpsendecho

- SetTimer
```
UINT_PTR SetTimer(
  [in, optional] HWND      hWnd,
  [in]           UINT_PTR  nIDEvent,
  [in]           UINT      uElapse,
  [in, optional] TIMERPROC lpTimerFunc
);
```
https://learn.microsoft.com/es-es/windows/win32/api/winuser/nf-winuser-settimer

## Dump
- MiniDumpWriteDump

```
BOOL MiniDumpWriteDump(
  [in] HANDLE                            hProcess,
  [in] DWORD                             ProcessId,
  [in] HANDLE                            hFile,
  [in] MINIDUMP_TYPE                     DumpType,
  [in] PMINIDUMP_EXCEPTION_INFORMATION   ExceptionParam,
  [in] PMINIDUMP_USER_STREAM_INFORMATION UserStreamParam,
  [in] PMINIDUMP_CALLBACK_INFORMATION    CallbackParam
);
```
https://learn.microsoft.com/en-us/windows/win32/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump

- RtlReportSilentProcessExit

```
NTSTATUS(NTAPI* RtlReportSilentProcessExit_func) (
	_In_     HANDLE                         ProcessHandle,
	_In_     NTSTATUS						            ExitStatus
	);
```
I have not found official Microsoft documentation

https://www.hexacorn.com/blog/2019/09/19/silentprocessexit-quick-look-under-the-hood/
