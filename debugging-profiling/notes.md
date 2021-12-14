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
 - The profile is here.

```
 Timer unit: 1e-06 s

 Total time: 0.85625 s
 File: sorts.py
 Function: insertionsort at line 10

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                           @profile
    11                                           def insertionsort(array):
    12                                           
    13     25970      31600.0      1.2      3.7      for i in range(len(array)):
    14     24970      27984.0      1.1      3.3          j = i-1
    15     24970      28437.0      1.1      3.3          v = array[i]
    16    227360     271284.0      1.2     31.7          while j >= 0 and v < array[j]:
    17    202390     238407.0      1.2     27.8              array[j+1] = array[j]
    18    202390     228318.0      1.1     26.7              j -= 1
    19     24970      29089.0      1.2      3.4          array[j+1] = v
    20      1000       1131.0      1.1      0.1      return array

### It seems the while loop is the bottle neck

Total time: 0.469874 s
File: sorts.py
Function: quicksort at line 22

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    22                                           @profile
    23                                           def quicksort(array):
    24     34894     126081.0      3.6     26.8      if len(array) <= 1:
    25     17947      23315.0      1.3      5.0          return array
    26     16947      23583.0      1.4      5.0      pivot = array[0]
    27     16947      93791.0      5.5     20.0      left = [i for i in array[1:] if i < pivot]
    28     16947      91962.0      5.4     19.6      right = [i for i in array[1:] if i >= pivot]
    29     16947     111142.0      6.6     23.7      return quicksort(left) + [pivot] + quicksort(right)

Total time: 0.8908 s
File: sorts.py
Function: quicksort_inplace at line 31

### This is a recursive function. The base statement and the return statement are cumbersome.

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    31                                           @profile
    32                                           def quicksort_inplace(array, low=0, high=None):
    33     33114     110536.0      3.3     12.4      if len(array) <= 1:
    34        44         51.0      1.2      0.0          return array
    35     33070      38667.0      1.2      4.3      if high is None:
    36       956       3274.0      3.4      0.4          high = len(array)-1
    37     33070      38725.0      1.2      4.3      if low >= high:
    38     17013      18880.0      1.1      2.1          return array
    39                                           
    40     16057      18774.0      1.2      2.1      pivot = array[high]
    41     16057      18909.0      1.2      2.1      j = low-1
    42    121673     143856.0      1.2     16.1      for i in range(low, high):
    43    105616     124654.0      1.2     14.0          if array[i] <= pivot:
    44     54583      63975.0      1.2      7.2              j += 1
    45     54583      69021.0      1.3      7.7              array[i], array[j] = array[j], array[i]
    46     16057      21823.0      1.4      2.4      array[high], array[j+1] = array[j+1], array[high]
    47     16057     101338.0      6.3     11.4      quicksort_inplace(array, low, j)
    48     16057      99965.0      6.2     11.2      quicksort_inplace(array, j+2, high)
    49     16057      18352.0      1.1      2.1      return array
### This is the worst of three. The 'for loop' and the base statement of recursion are bottlenecks.
```

6. pycallgraph and graphviz
 - I put code to `fib.py`
 - install both... Done!
 - run the code `pycallgraph graphviz -- ./fib.py`
 - How many times is 'fib0' called? : 21
 - How many times is each 'fibN' called? : 1 for each.



7. find process which uses port 4444
 - I can't find port number 4444 but it's obvious the python program is what I have to kill. Is this okay??
 - I found the way to specify the port for 'lsof'
   `lsof -i:4444` (where the port number is 4444)

8. I can't install taskset on my Mac.

9. sniff "curl ipinfo.io"
    Destination address was "34.117.59.81"
    I did whois on the address and I found the server is owned by Google.


