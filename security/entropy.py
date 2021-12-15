# Just print how many bits of entropy the passwords have.

import math

words = 4 # correcthorsebatterystaple
letters = 8 # rg8Ql34g

dict_size = 100000
alphanumeric_size = 26 + 26 + 10 # A-Z, a-z, 0-9


entropy = 1
for i in range(words):
    entropy *= dict_size

print('four words: ', math.log(entropy, 2))
print('It takes {:.2e} seconds to break this.\n'.format(entropy / 10000))
entropy = 1
for i in range(letters):
    entropy *= alphanumeric_size 

print('8 character:', math.log(entropy, 2))
print('It takes {:.2e} seconds to break this.\n'.format(entropy / 10000))