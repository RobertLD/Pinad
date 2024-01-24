# Pinad
Pinad is a simple python library that adds support for common Monads seen in other languages like Rust, and Haskell.

The source code is currently hosted on GitHub at:
https://github.com/RobertLD/pinad

## Installing Pinad

You can install Pinad through from PypI using Pip

```sh
# or PyPI
pip install pinad
```

## Supported Monads

The pinad library currently supports the following common monads:

   - Maybe - Used for values where None protection is important

Please use the issues page to suggest additional features.
https://github.com/RobertLD/pinad/issues
## Examples

```python
from pinad import Maybe

def echo(v):
    return v

x = None

>>> Maybe(x).orElse(1)
Maybe(1)

```


## Dependencies
None.

The goal of pinad is to add monad support with as few dependencies as possible
