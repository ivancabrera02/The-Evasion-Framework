# Lsass 

The Local Security Authority Subsystem Service (LSASS) is a process in Microsoft Windows operating systems, responsible for enforcing security policy on the system. Verify that users log on to a Windows computer or server, manage password changes, and create access tokens.

https://es.wikipedia.org/wiki/Servicio_de_Subsistema_de_Autoridad_de_Seguridad_Local

Performing a dump of this, in most cases, will generate alerts from the AV if we do not do it stealthily enough.

## Basic Ways to Dump Lsass.exe (NO OPSEC)

- ProcDump (Sysinternals) https://learn.microsoft.com/es-es/sysinternals/downloads/procdump
- Mimikatz or similar tools
- Task Manager GUI
- LoLBins like rundll32.exe, Adplus.exe, Createdump.exe, Dump64.exe, SQLdumper.exe, Dumpminitool.exe or rdrleakdiag.exe



