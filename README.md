# Vorpal: End-to-end Automated Testing Framework for Python
## Goals
Vorpal is an end-to-end automated testing framework designed to balance ease of development with performance and customizability.

## How to use Vorpal in a test project
### Requirements
* Python 3+

### First time setup
**Note:** While using a `virtualenv` is strongly recommended for Python projects, it isn't required. If you don't want to use `virtualenv` or have your own way of setting one up, feel free to skip to step **(4)**

0. If necessary, install the `virtualenv` package for Python
    * Command: `pip install virutalenv`
1. Create a virtual environment named `venv`
    * Command: `virtualenv venv`
2. If necessary, add `execute` permission for the current user to `./venv/bin/activate`
    * Command: `chmod u+x ./venv/bin/activate`
3. Activate the virtual environment
    * Command: `source ./venv/bin/activate`
4. Install the Vorpal framework via pip
    * Command: `pip install vorpal`
5. Install any other necessary dependencies for your project, like test runners (`pytest`, `nose`, etc.)
    * **Note:** You do _not_ need to separately install `selenium` since it is installed as a dependency of Vorpal
