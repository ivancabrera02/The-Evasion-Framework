# APT28 (Tsar Team, Fancy Bear)

- Country: Russia
- Targets:  European countries, NATO and other European security organizations and defense firms.
- Associated Malware: CHOPSTICK, SOURFACE

## Techniques:
- Google Drive for C2.
- Used compromised Office 365 service accounts with Global Administrator privileges to collect email from user inboxes.
- Rundll32 to execute .dlls.
- UEFI rootkit known as LoJax.
- Routed traffic over Tor and VPN servers to obfuscate their activities.
- Spearphishing emails containing malicious Microsoft Office and RAR attachments.
- ntdsutil.exe utility to export the Active Directory database for credential access.
- Dumped the LSASS process memory using the MiniDump function.
- Performed timestomping on victim files.
- Saved files with hidden file attributes.
- CVE-2014-4076, CVE-2015-2387, CVE-2015-1701, CVE-2017-0263 to escalate privileges.
- COM hijacking for persistence by replacing the legitimate MMDeviceEnumerator object with a payload.
- Downloads and executes PowerShell scripts and performs PowerShell commands.
- Trojan adds the Registry key HKCU\Environment\UserInitMprLogonScript to establish persistence.
