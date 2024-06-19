# Registry Trick

This trick is perhaps less 'OPSEC' and requires a lot of social engineering but I found it interesting. You can create a .reg file or play with the Windows registry to get a type of extension (.zip for example) to behave like .exe for example. You can also create your own.

The path to modify would be: HKEY_CURRENT_USER\Software\Classes\

- Disadvantages:

If you modify the behavior of an extension, all files with that extension on your computer will run with that new behavior.

If you want to use this as phishing, you need the user to first execute your .reg file and then your victim extension.

<video width="640" height="360" controls>
  <source src="images/video1.mp4" type="video/mp4">
</video>
