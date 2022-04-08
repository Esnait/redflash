from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import config
from selenium.common.exceptions import NoSuchElementException


def _find_element_(driver, element: tuple or list) -> WebElement:
    """
    Alternate method for finding web element

         Args:
            driver: accepts driver instance
            element: accepts only tuple or list having (locator type, locator string)

        Returns: identified web element
    """
    if type(element) == list:
        exceptions = []
        element_found = None

        for tuples in element:
            try:
                element_found = driver.find_element(*tuples)
                if not element_found is None:
                    return element_found

            except NoSuchElementException as E:
                exceptions.append(E)

        if len(exceptions) == len(element):
            raise Exception(exceptions)

    elif type(element) == tuple:
        return driver.find_element(*element)


class page:
    _accuracy_: int = config.accuracy_score

    driver: any
    _element_: tuple or list

    WIDTH: float
    HEIGHT: float
    LEFT: float
    TOP: float
    BOTTOM: float
    RIGHT: float

    def __init__(self, element: tuple or list):
        page._element_ = element
        self._set_dimension_()

    def _set_dimension_(self, ) -> None:
        """
        Sets the _width, height, x-offset, y-offset values by fetching actual element dimension
        """
        body_dimension = _find_element_(page.driver, (By.TAG_NAME, "Body")).rect

        dimension = _find_element_(page.driver, page._element_).rect
        page.WIDTH = round(dimension['width'], page._accuracy_)
        page.HEIGHT = round(dimension['height'], page._accuracy_)
        page.LEFT = round(dimension['x'], page._accuracy_)
        page.TOP = round(dimension['y'], page._accuracy_)
        page.BOTTOM = round(body_dimension['height'], page._accuracy_) - (round(dimension['y'], page._accuracy_) +
                                                                          round(dimension['height'], page._accuracy_))
        page.RIGHT = round(body_dimension['width'], page._accuracy_) - (round(dimension['x'], page._accuracy_) +
                                                                          round(dimension['width'], page._accuracy_))

    def is_width(self, expected_width: int or float, approx: int or float = 0, error_message: str = ""):
        """
        Asserts the width of the web element with expected width

            Args:
                expected_width: expected width for assertion, accepts only int or float values
                approx: approximate value defaults to 0 , accepts only int or float values and a range is defined by
                        adding and subtracting with the actual width to validate the expected width is within the
                        calculated range
                error_message: defaults to empty string, accepts user_defined error message as a string

            Returns: object of the inherited page to facilitate method chaining
        """

        page.driver.executeScript("arguments[0].setAttribute('style', 'border:2px solid red; background:yellow')",
                                 _find_element_(page.driver, page._element_));

        assert (expected_width - approx) <= page.WIDTH <= (
                expected_width + approx), f"Actual width Of {page._element_} '{page.WIDTH}' not in range" \
                                          f" {expected_width - approx}, {expected_width + approx}" if error_message == "" else error_message

        return self

    def is_height(self, expected_height: int or float, approx: int or float = 0, error_message: str = ""):
        """
        Asserts the height of the web element with expected width

            Args:
                expected_height: expected height for assertion, accepts only int or float values
                approx: approximate value defaults to 0 , accepts only int or float values and a range is defined by
                        adding and subtracting with the actual height to validate the expected height is within the
                        calculated range
                error_message: defaults to empty string, accepts user_defined error message as a string

            Returns: object of the inherited page to facilitate method chaining
        """
        assert (expected_height - approx) <= page.HEIGHT <= (
                expected_height + approx), f"Actual height Of {page._element_} '{page.HEIGHT}' not in range " \
                                           f"{expected_height - approx}, {expected_height + approx}" if error_message == "" else error_message

        return self

    def is_top(self, expected_top: int or float, approx: int or float = 0,
               inside: tuple = (By.TAG_NAME, "body"), error_message: str = ""):
        """
        Asserts the top of the web element with expected top
            Args:
                expected_top: expected top for assertion, accepts only int or float values
                approx: approximate value defaults to 0 , accepts only int or float values and a range is defined by
                        adding and subtracting with the actual top to validate the expected top is within the
                        calculated range
                error_message: defaults to empty string, accepts user_defined error message as a string

            Returns: object of the inherited page to facilitate method chaining
        """

        another_dimension = _find_element_(page.driver, inside).rect
        actual_top = page.TOP - round(another_dimension['y'], page._accuracy_)

        assert (expected_top - approx) <= actual_top <= (
                expected_top + approx), f"Actual top Of {page._element_} '{actual_top}' not in range " \
                                        f"{expected_top - approx}, {expected_top + approx}" if error_message == "" else error_message

        return self

    def is_left(self, expected_left: int or float, approx: int or float = 0,
                inside: tuple = (By.TAG_NAME, "body"), error_message: str = ""):
        """
        Asserts the left of the web element inside parent web element with expected left

            Args:
                expected_left: expected left for assertion, accepts only int or float values
                approx: approximate value defaults to 0 , accepts only int or float values and a range is defined by
                        adding and subtracting with the actual left to validate the expected left is within the
                        calculated range
                inside: acts as a parent element, defaults to the by locator of body as a tuple, accepts only tuple of (type of locator, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string

            Returns: object of the inherited page to facilitate method chaining
        """
        another_dimension = _find_element_(page.driver, inside).rect
        actual_left = page.LEFT - round(another_dimension['x'], page._accuracy_)

        assert (expected_left - approx) <= actual_left <= (
                expected_left + approx), f"Actual left Of {page._element_} '{actual_left}' not in range " \
                                         f"{expected_left - approx}, {expected_left + approx}" if error_message == "" else error_message

        return self

    def is_right(self, expected_right: int or float, approx: int or float = 0,
                 inside: tuple = (By.TAG_NAME, "body"), error_message: str = ""):

        """
        Asserts the right of the web element inside parent web element with expected right

            Args:
                expected_right: expected right for assertion, accepts only int or float values
                approx: approximate value defaults to 0 , accepts only int or float values and a range is defined by
                        adding and subtracting with the actual right to validate the expected right is within the
                        calculated range
                inside: acts as a parent element, defaults to the by locator of body as a tuple, accepts only tuple of (type of locator, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string

            Returns: object of the inherited page to facilitate method chaining
        """
        another_dimension = _find_element_(page.driver, inside).rect
        actual_right = round(another_dimension['width'], page._accuracy_) - (
            (page.LEFT - (round(another_dimension['x'], page._accuracy_)) + page.WIDTH))

        assert (expected_right - approx) <= actual_right <= (
                expected_right + approx), f"Actual right Of {page._element_} '{actual_right}' not in range" \
                                          f" {expected_right - approx}, {expected_right + approx}" if error_message == "" else error_message

        return self

    def is_bottom(self, expected_bottom: int or float, approx: int or float = 0,
                  inside: tuple = (By.TAG_NAME, "body"), error_message: str = ""):
        """
        Asserts the bottom of the web element inside parent web element with expected bottom

            Args:
                expected_bottom: expected bottom for assertion, accepts only int or float values
                approx: approximate value defaults to 0 , accepts only int or float values and a range is defined by
                        adding and subtracting with the actual bottom to validate the expected left is within the
                        calculated range
                inside: acts as a parent element, defaults to the by locator of body as a tuple, accepts only tuple of (type of locator, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string

            Returns: object of the inherited page to facilitate method chaining
        """

        another_dimension = _find_element_(page.driver, inside).rect
        actual_bottom = round(another_dimension['height'], page._accuracy_) - (
                (page.TOP - round(another_dimension['y'], page._accuracy_)) + page.HEIGHT)

        assert (expected_bottom - approx) <= actual_bottom <= (
                expected_bottom + approx), f"Actual bottom Of {page._element_} '{actual_bottom}' not in range" \
                                           f" {expected_bottom - approx}, {expected_bottom + approx}" if error_message == "" else error_message

        return self

    class compare:
        def __init__(self, operand_x, error: str):
            self.operand_x = operand_x
            self.error = error

        def is_less_than(self, operand: int or float, error_message: str = ""):
            """
            Asserts value passed to compare class as an argument is less than the operand passed

                Args:
                    operand: accepts only int or float values
                    error_message: user defined error message is passed as a string
            """
            assert self.operand_x < operand, self.error + f" less than {operand}" \
                if error_message == "" else error_message

        def is_greater_than(self, operand, error_message: str = ""):
            """
            Asserts value passed to compare class as an argument is greater than the operand passed

                Args:
                    operand: accepts only int or float values
                    error_message: user defined error message is passed as a string
            """
            assert self.operand_x > operand, self.error + f" greater than {operand}" \
                if error_message == "" else error_message

        def equals(self, operand, error_message: str = ""):
            """
            Asserts value passed to compare class as an argument is eqaul to the operand passed

                Args:
                    operand: accepts only int or float values
                    error_message: user defined error message is passed as a string
            """
            assert self.operand_x == operand, self.error + f" equals to {operand}" \
                if error_message == "" else error_message

        def is_greater_than_or_equals(self, operand, error_message: str = ""):
            """
            Asserts value passed to compare class as an argument is graeter than or equal to the operand passed

                Args:
                    operand: accepts only int or float values
                    error_message: user defined error message is passed as a string
            """
            assert self.operand_x >= operand, self.error + f" greater than or equals to {operand}" \
                if error_message == "" else error_message

        def is_less_than_or_equals(self, operand, error_message: str = ""):
            """
            Asserts value passed to compare class as an argument is lesser than or equal to the operand passed

                Args:
                    operand: accepts only int or float values
                    error_message: user defined error message is passed as a string
            """
            assert self.operand_x <= operand, self.error + f" lesser than or equals to {operand}" \
                if error_message == "" else error_message

    def check_width(self):
        """
        Passes required arguments for the comparision operations for width of the element to compare class

            Returns: compare class object to make use of compare functions
        """
        return page.compare(page.WIDTH, f"Actual width {page.WIDTH} of {page._element_} is not")

    def check_height(self):
        """
        Passes required arguments for the comparision operations for height of the element to compare class

            Returns: compare class object to make use of compare functions
        """
        return page.compare(page.HEIGHT, f"Actual height {page.HEIGHT} of {page._element_} is not")

    def check_top(self):
        """
        Passes required arguments for the comparision operations for top of the element to compare class

            Returns: compare class object to make use of compare functions
        """
        return page.compare(page.TOP, f"Actual top {page.TOP} of {page._element_} is not")

    def check_bottom(self):
        """
        Passes required arguments for the comparision operations for bottom of the element to compare class

            Returns: compare class object to make use of compare functions
        """
        body_height = round(_find_element_(page.driver, (By.TAG_NAME, "body")).size['height'], page._accuracy_)
        bottom = body_height - (page.TOP + page.HEIGHT)
        return page.compare(bottom, f"Actual bottom {bottom} of {page._element_} is not")

    def check_left(self):
        """
        Passes required arguments for the comparision operations for left of the element to compare class

            Returns: compare class object to make use of compare functions
        """
        return page.compare(page.LEFT, f"Actual left {page.LEFT} of {page._element_} is not")

    def check_right(self):
        """
        Passes required arguments for the comparision operations for right of the element to compare class

            Returns: compare class object to make use of compare functions
        """
        body_width = round(_find_element_(page.driver, (By.TAG_NAME, "body")).size['width'], page._accuracy_)
        right = body_width - (page.LEFT + page.HEIGHT)
        return page.compare(right, f"Actual right {right} of {page._element_} is not")

    def get_visibleport_dimension(self) -> dict:
        """
        Gets the dimension of visible portion of the page

            Returns: identified dimension as a dictionary
        """
        return {
            'y': page.driver.execute_script('return window.pageYOffset'),
            'x': page.driver.execute_script('return window.pageXOffset'),
            'width': page.driver.execute_script('return document.documentElement.clientWidth'),
            'height': page.driver.execute_script('return document.documentElement.clientHeight')}

    def is_left_of(self, element: tuple, error_message: str = "", aligned_all: bool = False):
        """
        Asserts the web element is in the left of element passed as an argument

            Args:
                element: accepts only tuple having (locator type, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string
                aligned_all: accepts boolean values only to verify web element is aligned left by all side
                                with element passed

            Returns: object of the inherited page to facilitate method chaining
        """
        another_dimension = _find_element_(page.driver, element).rect

        if aligned_all:
            assert page.TOP == round(another_dimension['y'], page._accuracy_) and \
                   page.TOP + page.HEIGHT == round(another_dimension['y'], page._accuracy_) + \
                   round(another_dimension['height']), f"{page._element_} is not aligned by all sides with {element}"

        assert page.LEFT < round(another_dimension['x'], page._accuracy_) and (
                page.LEFT + page.WIDTH) <= round(another_dimension['x'], page._accuracy_), \
            f"{page._element_} not in left of {element}" if error_message == "" else error_message

        return self

    def is_right_of(self, element: tuple, error_message: str = "", aligned_all: bool = False):
        """
        Asserts the web element is in the right of element passed as an argument

            Args:
                element: accepts only tuple having (locator type, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string
                aligned_all: accepts boolean values only to verify web element is aligned right by all side
                                with element passed

            Returns: object of the inherited page to facilitate method chaining

        """
        another_dimension = _find_element_(page.driver, element).rect

        if aligned_all:
            assert page.TOP == round(another_dimension['y'], page._accuracy_) and \
                   page.TOP + page.HEIGHT == round(another_dimension['y'], page._accuracy_) + \
                   round(
                       another_dimension['height']), f"{page._element_} is not aligned by all sides with {element}"

        assert page.LEFT >= round(another_dimension['x'], page._accuracy_) and (
                page.LEFT + page.WIDTH) > round(another_dimension['x'], page._accuracy_), \
            f"{page._element_} not in right of {element}" if error_message == "" else error_message

        return self

    def is_above(self, element: tuple, error_message: str = "", aligned_all: bool = False):
        """
        Asserts the web element is above the element passed as an argument

            Args:
                element: accepts only tuple having (locator type, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string
                aligned_all: accepts boolean values only to verify web element is aligned above by all side
                                with element passed

            Returns: object of the inherited page to facilitate method chaining

        """
        another_dimension = _find_element_(page.driver, element).rect

        if aligned_all:
            assert page.LEFT == round(another_dimension['x'], page._accuracy_) and \
                   page.LEFT + page.WIDTH == round(another_dimension['x'], page._accuracy_) + \
                   round(another_dimension['width']), f"{page._element_} is not aligned by all sides with {element}"

        assert page.TOP < round(another_dimension['y'], page._accuracy_) and \
               (page.TOP + page.HEIGHT) <= round(another_dimension['y'], page._accuracy_), \
            f"{page._element_} not above {element}" if error_message == "" else error_message

        return self

    def is_below(self, element: tuple, error_message: str = "", aligned_all: bool = False):
        """
        Asserts the web element is below the element passed as an argument

            Args:
                element: accepts only tuple having (locator type, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string
                aligned_all: accepts boolean values only to verify web element is aligned below by all side
                                with element passed

            Returns: object of the inherited page to facilitate method chaining

        """
        another_dimension = _find_element_(page.driver, element).rect

        if aligned_all:
            assert page.LEFT == round(another_dimension['x'], page._accuracy_) and \
                   page.LEFT + page.WIDTH == round(another_dimension['x'], page._accuracy_) + \
                   round(another_dimension['width']), f"{page._element_} is not aligned by all sides with {element}"

        assert page.TOP > round(another_dimension['y'], page._accuracy_) and (
                page.TOP + page.HEIGHT) >= round(another_dimension['y'], page._accuracy_), \
            f"{page._element_} not below {element}" if error_message == "" else error_message

        return self

    def is_inside(self, parent_element: tuple, error_message: str = ""):
        """
        Asserts the web element is inside the parent element passed as an argument

            Args:
                parent_element: accepts only tuple having (locator type, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string

            Returns: object of the inherited page to facilitate method chaining

        """
        if page._element_ == parent_element:
            raise Exception(f"Parent element  {parent_element} and nested element cannot be same")

        else:
            another_dimension = _find_element_(page.driver, parent_element).rect

            assert page.LEFT >= round(another_dimension['x'], page._accuracy_) and \
                   (page.LEFT + page.WIDTH) <= (round(another_dimension['x'], page._accuracy_) +
                                                round(another_dimension['width'],
                                                      page._accuracy_)) and page.TOP >= \
                   round(another_dimension['y'], page._accuracy_) and (page.TOP + page.HEIGHT) <= \
                   (round(another_dimension['y'], page._accuracy_) + round
                   (another_dimension['height'], page._accuracy_)), \
                f"{page._element_} is not inside {parent_element}" \
                    if error_message == "" else error_message

        return self

    def is_centered_vertically(self, inside: tuple = (By.TAG_NAME, "body"), error_message: str = ""):
        """
        Asserts the web element is centered vertically inside the element passed as an argument

            Args:
                inside: defaults to page-body locator,accepts only tuple having (locator type, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string

            Returns: object of the inherited page to facilitate method chaining
        """
        if page._element_ == inside:
            raise Exception(f"Parent element  {inside} and nested element cannot be same")

        else:
            another_dimension = _find_element_(page.driver, inside).rect
            actual_top = page.TOP - round(another_dimension['y'], page._accuracy_)
            actual_bottom = round(another_dimension['height'], page._accuracy_) - (page.HEIGHT + actual_top)
            assert actual_top == actual_bottom, f"{page._element_} is not centered vertically" if error_message == "" else error_message

        return self

    def is_centered_horizontally(self, inside: tuple = (By.TAG_NAME, "body"), error_message: str = ""):
        """
        Asserts the web element is centered horizontally inside the element passed as an argument

            Args:
                inside: defaults to page-body locator,accepts only tuple having (locator type, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string

            Returns: object of the inherited page to facilitate method chaining
        """
        if page._element_ == inside:
            raise Exception(f"Parent element  {inside} and nested element cannot be same")


        else:
            another_dimension = _find_element_(page.driver, inside).rect
            actual_left = page.LEFT - round(another_dimension['x'], page._accuracy_)
            actual_right = round(another_dimension['width'], page._accuracy_) - (page.WIDTH + actual_left)
            assert actual_left == actual_right, f"{page._element_} is not centered horizontally" if error_message == "" else error_message

        return self

    def is_centered(self, inside: tuple = (By.TAG_NAME, "body"), error_message: str = ""):
        """
        Asserts the web element is centered vertically and horizontally inside the element passed as an argument

            Args:
                inside: defaults to page-body locator,accepts only tuple having (locator type, locator string)
                error_message: defaults to empty string, accepts user_defined error message as a string

            Returns: object of the inherited page to facilitate method chaining
        """
        if page._element_ == inside:
            raise Exception(f"Parent element  {inside} and nested element cannot be same")

        else:
            another_dimension = _find_element_(page.driver, inside).rect
            nested_element_center = (page.LEFT + (page.WIDTH / 2)), (page.TOP + (page.HEIGHT / 2))
            parent_element_center = (round(another_dimension['x'], page._accuracy_) + (
                    round(another_dimension['width'], page._accuracy_) / 2)), (
                                            round(another_dimension['y'], page._accuracy_) + (
                                            round(another_dimension['height'], page._accuracy_) / 2))

            assert parent_element_center == nested_element_center, f"{page._element_} is not centered inside " \
                                                                   f"{inside}" if error_message == "" else error_message
