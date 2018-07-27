# Vorpal: End-to-end Web Automation Framework for Python
## Goals
Vorpal is an end-to-end browser and API automation framework designed to balance ease of development with performance
and customizability.

## How to use Vorpal
### Requirements
* Python 3+

### First time setup
**Note:** The venv module has been included for the standard library in Python 3.3 and higher. 

1. Create a virtual environment named `env`<sup>[1](#footnote1)</sup>
    * Command: `python3 -m venv env`
2. Activate the virtual environment
    * Command: `source env/bin/activate`
    * The following information obtained from: https://realpython.com/python-virtual-environments-a-primer/
    ** Notice how your prompt is now prefixed with the name of your environment (env, in this case)
    ** This is the indicator that env is currently active, which means the python executable will only use this
    environment’s packages and settings.
3. Install the Vorpal framework via pip
    * Command: `pip3 install vorpal`
4. Install any other necessary dependencies for your project
    * **Note:** Although Vorpal uses Selenium, you do _not_ need to separately install `selenium` - it is installed as
    a dependency of Vorpal

<a name="footnote1"><sup>1</sup></a> <i><small>The pyvenv command is a wrapper around the venv module and some users
have indicated we might want to consider avoiding the wrapper and just using the module directly. From Python 3.3 to 3.4
the recommended way to create a virtual environment was to use the pyvenv command-line tool that also comes included
with your Python 3 installation by default. But on 3.6 and above, python3 -m venv is the way to go.</small></i>
    
**Tip:** https://realpython.com/python-virtual-environments-a-primer/ 
This site seems to contain some useful tips about maintaining multiple environments and using a tool called
`virtualenvwrapper` to assist with this maintenance.

### How to use
#### Drivers
Drivers are what takes your scripts and turns them into actions on a page.
Vorpal is built using Selenium drivers, but wraps them in custom classes so users should not need to interact with
Selenium directly.

##### WebdriverFactory
Vorpal's `WebdriverFactory` class is the recommended class to use to create new webdriver instances for scripts.
By specifying the `browser` ('chrome', 'firefox', or 'IE') and `base_url` parameters in the constructor,
you will be able to easily generate new webdriver instances via the `get_webdriver_instance` method.

By setting the `remote` parameter to `True` and optionally specifying a `remote_url` you can have drivers
you create connect to a Selenium server or grid running either locally or a url you have access to.

The `get_webdriver_instance` accepts a `waiting_time` parameter, which defines the default time waited for elements
by the driver instance returned. This is equivalent to setting the implicit webdriver wait for a driver in Selenium,
meaning you will not need to tell the driver to wait for elements to appear after navigating to a new page unless
you want a different timeout for that page or element specifically.

##### CustomSeleniumDriver
The `CustomSeleniumDriver` class is Vorpal's wrapper for Selenium drivers. It implements most of the functionality
of the base Selenium driver, but adds a few bits of custom logic to improve quality of life.

The driver will return Vorpal's version of web elements as opposed to a Selenium web element. The differences between
Vorpal and Selenium web elements are covered in detail in the `Elements` section below.

#### Elements
Elements are basically HTML elements on the page. Vorpal uses a wrapped version of Selenium web elements, and while 
you can access the underlying Selenium element directly using the `element` property, almost all functionality available
in Selenium is also available in Vorpal.

TODO: Talk about lazy loading.

#### Page objects
It is often helpful to think of websites as collections of one or more pages.
TODO: Add more details.

#### APIs
Sometimes we can directly use site APIs to get the information we need.
TODO: Talk about built-in GET, POST, etc methods.



## Contributing to Vorpal
### Testing updates locally
Before pushing up changes, we want to test our changes locally. To do this, we use `pytest` to run test cases stored
in `test_local.py` and `test_page.py`. Run the `pytest` command from the command line at the project root to ensure
your changes haven't unexpectedly broken existing functionality, and update tests where appropriate if your changes
lead to different results.

If you're adding new functionality, please be sure to write well-targeted test cases that test the new feature in
isolation if at all possible. This makes it easier to track down any major breaking changes down the road.

If any of the existing test files start getting too big, or if your feature requires extensive testing, feel free to
make an additional test file (this was done in the case of `BasePage`, which led to `test_page.py`).
If you do, please update this documentation as part of your PR.

## Directions for Vorpal package owners/maintainers
### How to upload a new package version
As we build new features for Vorpal we will want to make them available on pypi.python.org.
To do this, we must complete the following steps:

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