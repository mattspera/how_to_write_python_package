
# Writing Libraries and Packages

Maturity model level 3 demonstrates competance in transforming your standalone scripts/projects into re-distributable, installable packages, which in turn, can be imported as modules (libraries) and utilised within subsequent scripts developed.

For demonstration purposes, this tutoral will focus on creating minimal Python packages however the same or similar methodology should apply to other scripting/programming languages.

## Why write libraries?

Writing code with a focus on writing libraries rather than standalone scripts can provide mulitple advantages. Some of the most significant advantages gained through writing libraries include:

- **Reusability:** Functionality defined in a single module or package (collection of modules) can be easily reused in other scripts, eliminating the need to recreate duplicate code.
- **Distribution:** Once packaged, your code can be distributed to and installed on multiple platforms and can be even be made publically available, allowing anyone to install and utilise the library like you would with an oridinary Python pip package.
- **Maintainability:** Versioning can be applied to your created package, allowing changes to any modules within to be bundled into the package and pushed up to a packaging repository such as pip, where users can then upgrade their currently installed version. This also allows tracing of enhancements, bug fixes and any other changes to your code.

## What makes up a Python package?

A package is a collection of Python modules. While a Python module is single file (`.py` extension), a package is a directory of Python modules containing an additional `__init__.py` file, which forces Python to treat the directory as a package.

Packages can also incorporate *tests*, which leverages unit testing to validate each function/method embedded within modules perform as designed. Tests are highly recommended to be included as a component of your package.

## Creating a simple Python package

Within this directory, I've created `example_project`, which is an example of a distributable, installable Python package. The following tutorial will detail the steps taken to create this package as well as the steps required to install and ultimately use this package within other scripts.

### 1. Creating the package directory structure

Todo...

```
example_project/
    example_project/
        __init__.py
        module_1.py
        module_2.py
        module_3.py
    tests/
        __init__.py
        test_module_1.py
        test_module_2.py
        test_module_3.py
    setup.py
```

### 2. `setup.py`

Todo...

### 3. Compiling your package

Todo...

`python setup.py sdist bdist_wheel`

### 4. Installing your package (via pip)

Todo...

`pip install dist/<.whl>`

### 5. Using you package

Todo...

```python
# you can import your entire Python package like so
import example_project

# alternatively, you can import specific Classes from your Python package
from example_project.caps import Capitals
```
