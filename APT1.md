# APT1 (Unit 61398, Comment Crew)

- Country: China
- Targets: All (IT, Telecommunications, Healthcare, Education, Financial, Public Administration etc.)
- Associated Malware: TROJAN.ECLTYS, BACKDOOR.BARKIOFORK, BACKDOOR.WAKEMINAP, TROJAN.DOWNBOT, BACKDOOR.DALBOT, BACKDOOR.REVIRD, TROJAN.BADNAME, BACKDOOR.WUALESS.

## Techniques:
- net localgroup,net user, and net group to find accounts on the system.
- GETMAIL and MAPIGET, to steal email. GETMAIL extracts emails from archived Outlook .pst files.
- The file name AcroRD32.exe, a legitimate process name for Adobe's Acrobat Reader, was used by APT1 as a name for malware.
- tasklist /v to list processes on the system.
- ipconfig /all for network information.
- RAR to compress files before moving them outside of the victim network.
- Batch script to perform a series of discovery techniques and saves it to a text file.
- Sent spearphishing emails containing hyperlinks to malicious files.
- Zero Day Exploits.
- Custom malware.
- Living-off-the-Land (LOL) Techniques.
- DNS Beaconing.
