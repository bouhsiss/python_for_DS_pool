# ft_package

## Overview

`ft_package` is a Python package created by Bouhsiss Houda for demonstration purposes. It provides a simple function called `count_in_list` to count the occurrences of a specific item in a list.

## Installation

You can install `ft_package` from Test PyPI using pip:

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps ft_package_bouhsiss
```

### Usage

Once installed, you can use the `count_in_list` function in your Python projects:

```python
from ft_package_bouhsiss import count_in_list

# Example usage:
my_list = [1, 2, 3, 4, 1, 2, 1]
item = 1
count = count_in_list(my_list, item)
print(f"The count of {item} in the list is: {count}")
```

this will output: 

```bash
The count of 1 in the list is: 3
```

### License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/bouhsiss/python_for_DS_pool/tree/main/python_0/ex09/ft_package/LICENSE) file for details.

