import time
import sys

l = 19
counter = 0
print('#'*(l+1),end='')

while True:
    sys.stdout.flush()
    time.sleep(0.2)
    print('\r%s@%s' % ('#' * counter, '#' * (1-counter)), end='')
    counter += 1
    if counter > 1:
        counter = 0