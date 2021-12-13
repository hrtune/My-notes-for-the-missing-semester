# Debugging and Profiling

 - /var/log

```sh
$ time curl https://missing.csail.mit.edu &> /dev/null
real    0m0.470s
user    0m0.016s  <- CPU user time
sys     0m0.094s  <- CPU kernel time
```

 - tac : print from the last line to the first line.
 - 


## Exercises

### Debugging

1. journalctl
> I think I can't use journalctl in my WSL environment, so later

2. pdb-tutorial (https://github.com/spiside/pdb-tutorial)

 - cloned the repo
 - cd to it
 - 2+3+2+3+5 = 15 so I entered 15
 - I entered 'y' to try again.
 - 5+4+3+1+4 = 17 right?
 - The answer is the same '5'.
 - To try again, I entered 'Y' instead of 'y', then it returns error.

Intro to pdb

 - I inserted 'import pdb; pdb.set_trace()' into the line 8.
 - run main.py and it works
 commands: l(ist), s(tep), n(ext), b(reak), r(eturn)
 - '<-' shows the current line on excution.
 ```sh
 def answer(self):
 total = 0
 for die in self.dice:
 total += 1
 return total 
 ```
 ```
 (Pdb) dir(die)
 ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'create_dice', 'roll', 'show', 'value']
 ```
 - There are a 'show' method and a 'value' object.
 - So I peeked them by `die.show()` and `die.value`
 - Obviously, the method just returns `len(self.dice)`

3. shellcheck
 - ran `shellcheck typical_script.sh` and fixed it

4. (skipped)

5. cProfile and line_profiler
 - install 'line_profiler'... 

6. pycallgraph and graphviz
 - I put code to `fib.py`
 - install both... 

7. find process which uses port 4444
 - 
