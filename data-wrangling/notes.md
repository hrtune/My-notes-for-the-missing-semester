# Data Wrangling

 - (data) | sed -E 's/(Regular expressions)/(replacement)/'
 - sed : stream editor
 - awk : a column based stream processor
 - awk '{print $2}' (print the second column)
 - bc : a calculator on command line
 - R : a stream processor for statistics
 - sort : sort the data
 - uniq : tool for omitting duplication
 - xargs : takes lines of input and pass as arguments

### Exercises

1. solve problems on regexone.com
  - done Lesson 14 ... (lesson 15: https://regexone.com/lesson/misc_meta_characters?)
  - Completed! (Further more problems here: https://regexone.com/lesson/end?)

2. perform regex on /usr/share/dict/words

output words contains at least three as to `more-as.txt`
```sh
$ cat /usr/share/dict/words | perl -pe "s/.*\'s$//" | perl -pe 's/^([^a]*a){0,2}[^a]*$//i' > more-as.
txt
```

What are the most common last two letters?
```sh
$ cat more-as.txt | grep -o "..$" | sort | uniq -c | sort -k1,1 | tail -n 3
```

How many of those two-letters combinations?
> Use `wc -l` in addition to `uniq`
```
$ cat more-as.txt | grep -o "..$" | sort | uniq | wc -l
```

Which combinations do not occur?

 - generate all possible two-letters combinations 
   ```sh
   $ crunch 2 2 -t @@ > two-lowers.txt
   ```

 - concatenate two files of `two-lowers` and the last two-letters combs of `more-as.txt`
   then, do the `uniq`
   ```sh
   $ cat more-as.txt | grep -o "..$" > last-two.txt
   $ cat last-two.txt two-lowers.txt | sort | uniq -u
   ```

3. Why is it bad idea?
For example...
```sh
$ echo "abc" > abc.txt
$ cat abc.txt | sed "s/abc/hello/"  <-- convention
hello
$ sed "s/abc/hello/" abc.txt        <-- Okay
hello
% sed "s/abc/hello/" abc.txt > abc.txt
$ cat abc.txt
$                                   <-- deleted content
```

...
