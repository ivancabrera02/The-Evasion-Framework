# Read Lsass PID from the Registry

First article in a series where we will see different ways to read the Lsass PID, avoiding the most common ones.

En la siguiente ruta encontramos el PID de lsass -> HKLM\SYSTEM\CurrentControlSet\Control\Lsa

<img src="images/lsasspid1.png" />

You could create a function in C or another language that obtains that value.
