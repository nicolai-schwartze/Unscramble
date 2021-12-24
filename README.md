# Unscramble
Unscramble any word and discover anagrams based on a dictionary.

A comprehensive (although not complete) German wordlist can be found [here](https://gist.github.com/MarvinJWendt/2f4f4154b8ae218600eb091a5706b5f4). 

```python
from unscramble import *

if __name__ == "__main__":
    candidates = unscramble('Wollsokcen', 'wordlist-german.txt')
    print(candidates)
```
