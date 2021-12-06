# Course overview + the shell

 - ctrl + L : clear the shell
 - ctrl + R : look up history
 - `cd -` : move directory to the previous one

 ### Exercises
 
1. locate the shell

```
$ echo $SHELL
/bin/bash
```

2. create a directory

```
$ mkdir missing
$ ls
missing  remote-wsl-loc.txt
```

3. look up `touch`
`man touch`
 > Update the access and modification times of each FILE to the current time.
 > A FILE argument that does not exist is created empty, unless -c or -h is supplied.

4. create an empty file
```
$ cd missing
$ touch semester
$ ls
semester
```

5. write a script using redirection
```
$ echo '#!/bin/sh' > semester
$ echo 'curl --head --silent https://missing.csail.mit.edu' >> semester
$ cat semester
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu
```

6. figure out why I can't excute the script
```
$ ./semester
-bash: ./semester: Permission denied
```

 > Take a look at its info.

```
$ ls -l
total 0
-rw-r--r-- 1 haruta haruta 61 Dec  6 17:06 semester
```
 > Nobody can excute the file except for 'root'.

7. run the script with `sh`
```
$ sh semester
HTTP/2 200
server: GitHub.com
...
```
 > It worked.
8. read a man page of `chmod`
`$ man chmod`

9. change the file mode
```
$ chmod u+x semester
$ ls -l
total 0
-rwxr--r-- 1 haruta haruta 61 Dec  6 17:06 semester
```

10. get the 'last-modified' date
```
$ ./semester | grep 'last-modified' | cut -d ' ' -f 2- > last-modified.txt
$ cat last-modified.txt
Sat, 04 Dec 2021 10:20:09 GMT
```

11. read the battery's level from '/sys'
```
$ cat /sys/class/power_supply/battery/status
Full
```

DONE😀!

