

# python_project_setup

- This repository is a simple guideline of Python project setup.
- It will introduce the most common practice in setuping a development python package.
  1. System path (`sys.path` / `PYTHONPATH`)
  2. `setuptools` (`setup.py`)
  3. `pyproject.toml`

## 1. Virtual Environment setup (Windows Environment)
- Create a virtual environment (Python 3.10) for testing

```bash
conda create -y -n project_setup python==3.10
conda activate project_setup
pip install -r requirements.txt
```

- Remark
  - Only `numpy==1.26.4` is listed in `requirements.txt`and installed.
  - When creating new virtual environment, `setuptools` is installed by default, which will be introduced in **Section 3.2**

![image](meta/create_virtual_env.jpg)

## 2. Background
- Python has numerous external open-source packages. 
  - The packages will be installed via `pip install <package>` or `conda install <package>`
  - And during Python project development, different external packages will be imported via `import <package>`
  - Example: [import_external_package.py](import_external_package.py)

```bash
pip install numpy==1.26.4
```

```python
import numpy
import numpy as np
from numpy import mean

# python import_external_package.py
# -----------------------------------
# Mean   of [1, 2, 4]: 2.33
# Median of [1, 2, 4]: 2.00
```

- However, if a Python project is in development phase like codes under `src/demo` folder, how to use the same `import` command to import the related variables/functions/classes.
  - Example: [import_internal_package.py](import_internal_package.py)

```
# Folder structure
├── src
│   ├── demo
│   │   ├── utils.py
└── import_internal_package.py
```

```python
from demo.utils import mean, median

# python import_internal_package.py
# ---------------------------------------------------------------------------------
# Traceback (most recent call last):
#   File "python_project_setup\import_internal_package.py", line 1, in <module>    
#     from demo.utils import mean, median
# ModuleNotFoundError: No module named 'demo'
```

- To tackle the above issue and smoothen the Python development flow, below are 3 popular methods to `import` the required packages correctly.
  1. System path (`sys.path` / `PYTHONPATH`)
  2. `setuptools` (`setup.py`)
  3. `pyproject.toml`

## 3.1. System path (`sys.path` / `PYTHONPATH`)
- Append the code folder path to system path so Python knows where to import the related variables.
- There are 2 methods to append the path.

### 3.1.1. By command line: `export PYTHONPATH="<code folder path>"`

```bash
export PYTHONPATH="./src"

echo $PYTHONPATH
# ./src

python import_internal_package.py
# Mean   of [1, 2, 4]: 2.33
# Median of [1, 2, 4]: 2.00
```

### 3.1.2. Edit the sys.path within the script (Example: [syspath_3.1.py](syspath_3.1.py))

```python
import sys
sys.path.append("<code folder path>")
```

```python
# Example: syspath_3.1.py
import sys
sys.path.append("./src")

from demo.utils import mean, median

# python syspath_3.1.py
# ------------------------------
# Mean   of [1, 2, 4]: 2.33
# Median of [1, 2, 4]: 2.00
```

## 3.2. `setuptools` (`setup.py`)
- 

## 3.3. `pyproject.toml`
-

## 4. Conclusion
- 
