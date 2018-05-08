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

## Directions for Vorpal package owners/maintainers
### How to upload a new package version
As we build new features for Vorpal we will want to make them available on pypi.python.org. To do this, we must complete the following steps:

1. Update the `version` argument in `setup.py`
    * We use semantic versioning, so please follow [semantic versioning guidelines]:
        * Bug fixes and minor changes increment the third digit (`1.0.0 => 1.0.1`)
        * New features that don't break existing functionality increment the second digit (`1.0.0 => 1.1.0`)
        * Changes that break backward compatibility increment the first digit (`1.0.0 => 2.0.0`)
2. Build a `wheel`
    * Vorpal is built exclusively for Python3, so we want to build a ['pure' Python wheel]
    * To build a wheel, we need to install the `wheel` package, so run `pip install wheel` if you haven't already
    * We build the wheel by running `python setup.py bdist_wheel` from the project root
3. Upload to PyPI
    * Install `twine` via `pip install twine` if you haven't already
    * Run `twine upload dist/*` in the project root and enter your PyPI username and password when prompted

['pure' Python wheel]: https://packaging.python.org/tutorials/distributing-packages/#pure-python-wheels]

[semantic versioning guidelines]: https://docs.npmjs.com/getting-started/semantic-versioning#semver-for-publishers

And that's all there is to it!