"""
Module containing wrapper class for Selenium Web.
"""

class ExtendedWebElement:
    """
    Extends web elements with additional functionality.
    """

    def __init__(self, element):
        """
        Initializes ExtendedWebElement with Selenium WebElement.
        :param element: base Selenium WebElement
        """
        self.element = element

    # TODO: figure out if there's a more graceful way to delegate methods to element
    
    def __repr__(self):
        return self.element.__repr__

    @property
    def tag_name(self):
        """This element's ``tagName`` property."""
        return self.element.tag_name

    @property
    def text(self):
        """The text of the element."""
        return self.element.text

    def click(self):
        """Clicks the element."""
        self.element.click()

    def submit(self):
        """Submits a form."""
        self.element.submit()

    def clear(self):
        """Clears the text if it's a text entry element."""
        self.element.clear()

    def get_property(self, name):
        """
        Gets the given property of the element.
        :Args:
            - name - Name of the property to retrieve.
        Example::
            text_length = target_element.get_property("text_length")
        """
        return self.element.get_property(name)

    def get_attribute(self, name):
        """Gets the given attribute or property of the element.
        This method will first try to return the value of a property with the
        given name. If a property with that name doesn't exist, it returns the
        value of the attribute with the same name. If there's no attribute with
        that name, ``None`` is returned.
        Values which are considered truthy, that is equals "true" or "false",
        are returned as booleans.  All other non-``None`` values are returned
        as strings.  For attributes or properties which do not exist, ``None``
        is returned.
        :Args:
            - name - Name of the attribute/property to retrieve.
        Example::
            # Check if the "active" CSS class is applied to an element.
            is_active = "active" in target_element.get_attribute("class")
        """
        return self.element.get_attribute(name)

    def is_selected(self):
        """Returns whether the element is selected.
        Can be used to check if a checkbox or radio button is selected.
        """
        return self.element.is_selected

    def is_enabled(self):
        """Returns whether the element is enabled."""
        return self.element.is_enabled

    def find_element_by_id(self, id_):
        """Finds element within this element's children by ID.
        :Args:
         - id\_ - ID of child element to locate.
        :Returns:
         - WebElement - the element if it was found
        :Raises:
         - NoSuchElementException - if the element wasn't found
        :Usage:
            foo_element = element.find_element_by_id('foo')
        """
        return self.element.find_element_by_id(id_)

    def find_elements_by_id(self, id_):
        """Finds a list of elements within this element's children by ID.
        Will return a list of webelements if found, or an empty list if not.
        :Args:
         - id\_ - Id of child element to find.
        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not
        :Usage:
            elements = element.find_elements_by_id('foo')
        """
        return self.element.find_elements_by_id(id_)

    def find_element_by_name(self, name):
        """Finds element within this element's children by name.
        :Args:
         - name - name property of the element to find.
        :Returns:
         - WebElement - the element if it was found
        :Raises:
         - NoSuchElementException - if the element wasn't found
        :Usage:
            element = element.find_element_by_name('foo')
        """
        return self.element.find_element_by_name(name)

    def find_elements_by_name(self, name):
        """Finds a list of elements within this element's children by name.
        :Args:
         - name - name property to search for.
        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not
        :Usage:
            elements = element.find_elements_by_name('foo')
        """
        return self.element.find_elements_by_name(name)

    def find_element_by_link_text(self, link_text):
        """Finds element within this element's children by visible link text.
        :Args:
         - link_text - Link text string to search for.
        :Returns:
         - WebElement - the element if it was found
        :Raises:
         - NoSuchElementException - if the element wasn't found
        :Usage:
            element = element.find_element_by_link_text('Sign In')
        """
        return self.element.find_element_by_link_text(link_text)

    def find_elements_by_link_text(self, link_text):
        """Finds a list of elements within this element's children by visible link text.
        :Args:
         - link_text - Link text string to search for.
        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not
        :Usage:
            elements = element.find_elements_by_link_text('Sign In')
        """
        return self.element.find_elements_by_link_text(link_text)

    def find_element_by_partial_link_text(self, link_text):
        """Finds element within this element's children by partially visible link text.
        :Args:
         - link_text: The text of the element to partially match on.
        :Returns:
         - WebElement - the element if it was found
        :Raises:
         - NoSuchElementException - if the element wasn't found
        :Usage:
            element = element.find_element_by_partial_link_text('Sign')
        """
        return self.element.find_element_by_partial_link_text(link_text)

    def find_elements_by_partial_link_text(self, link_text):
        """Finds a list of elements within this element's children by link text.
        :Args:
         - link_text: The text of the element to partial match on.
        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not
        :Usage:
            elements = element.find_elements_by_partial_link_text('Sign')
        """
        return self.element.find_elements_by_partial_link_text(link_text)

    def find_element_by_tag_name(self, name):
        """Finds element within this element's children by tag name.
        :Args:
         - name - name of html tag (eg: h1, a, span)
        :Returns:
         - WebElement - the element if it was found
        :Raises:
         - NoSuchElementException - if the element wasn't found
        :Usage:
            element = element.find_element_by_tag_name('h1')
        """
        return self.element.find_element_by_tag_name(name)

    def find_elements_by_tag_name(self, name):
        """Finds a list of elements within this element's children by tag name.
        :Args:
         - name - name of html tag (eg: h1, a, span)
        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not
        :Usage:
            elements = element.find_elements_by_tag_name('h1')
        """
        return self.element.find_elements_by_tag_name(name)

    def find_element_by_xpath(self, xpath):
        """Finds element by xpath.
        :Args:
         - xpath - xpath of element to locate.  "//input[@class='myelement']"
        Note: The base path will be relative to this element's location.
        This will select the first link under this element.
        ::
            myelement.find_element_by_xpath(".//a")
        However, this will select the first link on the page.
        ::
            myelement.find_element_by_xpath("//a")
        :Returns:
         - WebElement - the element if it was found
        :Raises:
         - NoSuchElementException - if the element wasn't found
        :Usage:
            element = element.find_element_by_xpath('//div/td[1]')
        """
        return self.element.find_element_by_xpath(xpath)

    def find_elements_by_xpath(self, xpath):
        """Finds elements within the element by xpath.
        :Args:
         - xpath - xpath locator string.
        Note: The base path will be relative to this element's location.
        This will select all links under this element.
        ::
            myelement.find_elements_by_xpath(".//a")
        However, this will select all links in the page itself.
        ::
            myelement.find_elements_by_xpath("//a")
        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not
        :Usage:
            elements = element.find_elements_by_xpath("//div[contains(@class, 'foo')]")
        """
        return self.element.find_elements_by_xpath(xpath)

    def find_element_by_class_name(self, name):
        """Finds element within this element's children by class name.
        :Args:
         - name: The class name of the element to find.
        :Returns:
         - WebElement - the element if it was found
        :Raises:
         - NoSuchElementException - if the element wasn't found
        :Usage:
            element = element.find_element_by_class_name('foo')
        """
        return self.element.find_element_by_class_name(name)

    def find_elements_by_class_name(self, name):
        """Finds a list of elements within this element's children by class name.
        :Args:
         - name: The class name of the elements to find.
        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not
        :Usage:
            elements = element.find_elements_by_class_name('foo')
        """
        return self.element.find_elements_by_class_name(name)

    def find_element_by_css_selector(self, css_selector):
        """Finds element within this element's children by CSS selector.
        :Args:
         - css_selector - CSS selector string, ex: 'a.nav#home'
        :Returns:
         - WebElement - the element if it was found
        :Raises:
         - NoSuchElementException - if the element wasn't found
        :Usage:
            element = element.find_element_by_css_selector('#foo')
        """
        return self.element.find_element_by_css_selector(css_selector)

    def find_elements_by_css_selector(self, css_selector):
        """Finds a list of elements within this element's children by CSS selector.
        :Args:
         - css_selector - CSS selector string, ex: 'a.nav#home'
        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not
        :Usage:
            elements = element.find_elements_by_css_selector('.foo')
        """
        return self.element.find_elements_by_css_selector(css_selector)

    def send_keys(self, *value):
        """Simulates typing into the element.
        :Args:
            - value - A string for typing, or setting form fields.  For setting
              file inputs, this could be a local file path.
        Use this to send simple key events or to fill out form fields::
            form_textfield = driver.find_element_by_name('username')
            form_textfield.send_keys("admin")
        This can also be used to set file inputs.
        ::
            file_input = driver.find_element_by_name('profilePic')
            file_input.send_keys("path/to/profilepic.gif")
            # Generally it's better to wrap the file path in one of the methods
            # in os.path to return the actual path to support cross OS testing.
            # file_input.send_keys(os.path.abspath("path/to/profilepic.gif"))
        """
        self.element.send_keys(*value)

    # RenderedWebElement Items
    def is_displayed(self):
        """Whether the element is visible to a user."""
        return self.element.is_displayed()

    @property
    def location_once_scrolled_into_view(self):
        """THIS PROPERTY MAY CHANGE WITHOUT WARNING. Use this to discover
        where on the screen an element is so that we can click it. This method
        should cause the element to be scrolled into view.
        Returns the top lefthand corner location on the screen, or ``None`` if
        the element is not visible.
        """
        return self.element.location_once_scrolled_into_view

    @property
    def size(self):
        """The size of the element."""
        return self.element.size

    def value_of_css_property(self, property_name):
        """The value of a CSS property."""
        return self.element.value_of_css_property(property_name)

    @property
    def location(self):
        """The location of the element in the renderable canvas."""
        return self.element.location

    @property
    def rect(self):
        """A dictionary with the size and location of the element."""
        self.element.rect

    @property
    def screenshot_as_base64(self):
        """
        Gets the screenshot of the current element as a base64 encoded string.
        :Usage:
            img_b64 = element.screenshot_as_base64
        """
        return self.element.screenshot_as_base64

    @property
    def screenshot_as_png(self):
        """
        Gets the screenshot of the current element as a binary data.
        :Usage:
            element_png = element.screenshot_as_png
        """
        return self.element.screenshot_as_png

    def screenshot(self, filename):
        """
        Saves a screenshot of the current element to a PNG image file. Returns
           False if there is any IOError, else returns True. Use full paths in
           your filename.
        :Args:
         - filename: The full path you wish to save your screenshot to. This
           should end with a `.png` extension.
        :Usage:
            element.screenshot('/Screenshots/foo.png')
        """
        return self.element.screenshot

    @property
    def parent(self):
        """Internal reference to the WebDriver instance this element was found from."""
        return self.element.parent

    @property
    def id(self):
        """Internal ID used by selenium.
        This is mainly for internal use. Simple use cases such as checking if 2
        webelements refer to the same element, can be done using ``==``::
            if element1 == element2:
                print("These 2 are equal")
        """
        return self.element.id

    def __eq__(self, element):
        return self.element.__eq__(element)

    def __ne__(self, element):
        return self.element.__ne__(element)