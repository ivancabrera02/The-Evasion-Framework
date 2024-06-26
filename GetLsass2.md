# Read Lsass PID via NtQuerySystemInformation and doing Brute Force

The other day I found a script in Linux which performed brute force to find the Apache PID.

<img src="images/linuxlsass.png" />

The first thing I thought was... what if we do the same in Windows? So I put together the following script in powershell.

<img src="images/ps1lsass.png" />

<img src="images/ps1lsass2.png" />

It's not bad, but it's not very stealthy. I can do something better in Go.

<img src="images/ntbt.png" />

<img src="images/ntbt2.png" />

<img src="images/ntb3.png" />
