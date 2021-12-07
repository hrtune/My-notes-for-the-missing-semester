# Shell Tools and Scripting

```sh
$ foo=bar
$ echo $foo
foo
```
 - Don't put whitespace between '=' and a variable.

```sh
$ foo = bar

Command 'foo' not found, did you mean:
...
```

 - 'something' and "something" are different.
```sh
$ echo "Value is $foo"
bar
$ echo 'Value is $foo'
Value is $foo
```

- '$1','$2'... are arguments while '$0' is the command name itself.
- '$?' : the error code of the previous command.
- '$_' : the last argument of the previous command.

```sh
$ mkdir test
$ cd $_
$ pwd
(...)/test
```

 - !! : replaced with the previous command line.
 
 - The error code '0' shows no errors while '1' denotes there are errors.

 - `false` always has '1' error code.

```sh
$ false || echo "Oops fail"
Oops fail
$ true || echo "Will be not printed"
$
```
```sh
$ ture && echo "Things went well"
Things went well
$ false && echo "This will not be printed"
$
$ false ; echo "Sequence of commands"
Sequence of commands
```

 - store output to variable
```sh
$ foo=$(pwd)
$ echo $foo
/mnt/c/Users/hrtun/Documents/github/Notes-for-missing-semester/shell-tools/test
$ echo "The date is $(date)"
The date is Mon Dec  6 20:41:57 JST 2021
```

 - `$ cat <(ls) <(ls ..)` : concatenate two of `ls` outputs

 - `ls *.sh` : globbing

...


### Exercises

1. know `ls` options

```sh
$ ls -lat --block-size=M --color
```
2. marco and polo
(marco.sh)
```sh
# !/bin/bash
marco(){
    pwd > /tmp/marco.txt
}
marco
```

(polo.sh)
```sh
# !/bin/bash

polo(){
    cd $(cat /tmp/marco.txt) || echo 'Marco first.'
}

polo
```

3. run until fail
`inspect.sh`

4. 'xargs' is useful
```sh
$ ls | grep \.html$ | xargs --delimiter="\n" tar czf html.tar.gz
```
5. recursive find and sort by date
```sh
$ find /home/haruta/ -type f -printf "%T@ %Tc %p\n" | sort -n --reverse
```
(Sorry I googled that😕.)


