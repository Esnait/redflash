from selenium.webdriver.common.by import By

import config

approximate_value = config.APPROXIMATION


class properties:
    def __init__(self, driver, locator):
        self.driver = driver
        self.element = locator

    def get_window_size(self):
        """
        Gets current window size

            Returns: dictionary having identified height and width in pixels
        """
        return self.driver.get_window_size()

    def get_dimension(self):
        """
        Gets dimension of the element

            Returns: dictionary having height, width, x and y offsets in pixels
        """
        return self.driver.find_element(*self.element).rect

    def get_size(self):
        """
        Gets size of the element

            Returns: dictionary having height and width in pixels
        """
        return self.driver.find_element(*self.element).size

    def get_width(self):
        """
        Gets width of the element

            Returns: numeric value of identified width in pixels
        """
        return self.driver.find_element(*self.element).size['width']

    def get_height(self):
        """
        Gets height of the element

            Returns: numeric value of identified height in pixels
        """
        return self.driver.find_element(*self.element).size['height']

    def get_location(self):
        """
        Gets x and y offsets of the element

            Returns: dictionary having identified x and y offsets in pixels
        """
        return self.driver.find_element(*self.element).location

    def get_Xoffset(self):
        """
        Gets x-offset of the element

            Returns: numeric value of identified x-offset in pixels
        """
        return self.driver.find_element(*self.element).location['x']

    def get_Yoffset(self):
        """
        Gets y-offset of the element

            Returns: numeric value of identified y-offset in pixels
        """
        return self.driver.find_element(*self.element).location['y']

    def get_visible_port_dimension(self):
        """
        Gets dimension of visible part of the page

            Returns: dictionary having height, width, x and y offsets in pixels
        """
        return {
            'y': self.driver.execute_script('return window.pageYOffset'),
            'x': self.driver.execute_script('return window.pageXOffset'),
            'width': self.driver.execute_script('return document.documentElement.clientWidth'),
            'height': self.driver.execute_script('return document.documentElement.clientHeight')}

    def get_visible_port_Xoffset(self):
        """
        Gets x-offset of the visible part of the page

            Returns: numeric value of identified x-offset in pixels
        """
        return self.driver.execute_script('return window.pageXOffset')

    def get_visible_port_Yoffset(self):
        """
        Gets y-offset of the visible part of the page

            Returns: numeric value of identified y-offset in pixels
        """
        return self.driver.execute_script('return window.pageYOffset')

    def get_visible_port_width(self):
        """
        Gets width of the visible part of the page

            Returns: numeric value of width in pixels
        """
        return self.driver.execute_script('return document.documentElement.clientWidth')

    def get_visible_port_height(self):
        """
        Gets height of the visible part of the page

            Returns: numeric value of height in pixels
        """
        return self.driver.execute_script('return document.documentElement.clientHeight')

    def is_inside_visible_port(self):
        """
        Asserts the position of element is inside the visible parts of the page

            Returns: object of the inherited page to facilitate method chaining
        """
        elem_left_bound = self.get_Xoffset()
        elem_top_bound = self.get_Yoffset()
        elem_width = self.get_width()
        elem_height = self.get_height()
        elem_right_bound = elem_left_bound + elem_width
        elem_lower_bound = elem_top_bound + elem_height

        win_upper_bound = self.get_visible_port_Yoffset()
        win_left_bound = self.get_visible_port_Xoffset()
        win_width = self.get_visible_port_width()
        win_height = self.get_visible_port_height()
        win_right_bound = win_left_bound + win_width
        win_lower_bound = win_upper_bound + win_height

        try:
            if not (win_left_bound <= elem_left_bound and win_right_bound >= elem_right_bound and win_upper_bound <= elem_top_bound and win_lower_bound >= elem_lower_bound):
                raise AssertionError(f"{self.element} is not visible inside the window")
        except AssertionError as E:
            print(E)
        return self

    def get_left_from(self, element):
        """
        Gets the x and y offsets of element from another element identified from the object passed as element argument

            Args:
                element: object of the inherited page to facilitate method chaining

            Reurns: dictionary having identified x and y offsets in pixels
        """
        return {
            'x': self.get_Xoffset() - element.get_Xoffset(),
            'y': self.get_Yoffset() - element.get_Yoffset()}

    def get_right_bottom_offset(self):
        """
        Gets the x, y offsets of right bottom corner of the element

            Returns: dictionary having identified x and y offsets in pixels
        """
        return {
            'x': self.get_Xoffset() + self.get_width(),
            'y': self.get_Yoffset() + self.get_height()}

    def is_left_of(self, element):
        """
        Asserts current element is in the left of element identified from the object passed as element argument

            Args:
                element: object of the inherited page to facilitate method chaining

            Reurns: object of the inherited page to facilitate method chaining
        """
        try:
            if not (self.get_Xoffset() < element.get_Xoffset() and self.get_right_bottom_offset()[
                'x'] <= element.get_Xoffset()):
                raise AssertionError(f"{self.element} is not left of {element.element}")
        except AssertionError as E:
            print(E)
        return self

    def is_right_of(self, element):
        """
        Asserts current element is in the right of element identified from the object passed as element argument

            Args:
                element: object of the inherited page to facilitate method chaining

            Reurns: object of the inherited page to facilitate method chaining
        """
        try:
            if not (self.get_Xoffset() >= element.get_get_Xoffset() and self.get_right_bottom_offset()['x'] >
                    element.get_Xoffset()):
                raise AssertionError(f"{self.element} is not right of {element.element}")
        except AssertionError as E:
            print(E)
        return self

    def is_below(self, element):
        """
        Asserts current element is below the element identified from the object passed as element argument

            Args:
                element: object of the inherited page to facilitate method chaining

            Reurns: object of the inherited page to facilitate method chaining
        """
        try:
            if self.get_Yoffset() + self.get_height() < element.get_Yoffset():
                raise AssertionError(f"{self.element} is not below {element.element}")
        except AssertionError as E:
            print(E)
        return self

    def is_above(self, element):
        """
        Asserts current element is left of another element identified from the object passed as element argument

            Args:
                element: object of the inherited page to facilitate method chaining

            Reurns: object of the inherited page to facilitate method chaining
        """
        try:
            if self.get_Yoffset() + self.get_height() > element.get_Yoffset():
                raise AssertionError(f"{self.element} is not above {element.element}")
        except AssertionError as E:
            print(E)
        return self

    def get_text(self):
        """
        Gets the text from the element

            Returns: identified text as string
        """
        return self.driver.find_element(*self.element).text

    def is_text(self, text):
        """
        Asserts actual text of the element is equal to the text passed

            Args:
                text: string of expected result

            Reurns: object of the inherited page to facilitate method chaining
        """
        try:
            if self.get_text() != text:
                raise AssertionError(f"Actual text in {self.element} : '{self.get_text()}', got '{text}")
        except AssertionError as E:
            print(E)
        return self

    def get_font_size(self):
        """
        Gets the css property font-size of the element

            Returns: identified font size in pixels as string
        """
        return str(self.driver.find_element(*self.element).value_of_css_property('font-size'))

    def get_font_style(self):
        """
        Gets css property font-style of the element

            Returns: identified font style as string
        """
        return self.driver.find_element(*self.element).value_of_css_property('font-style')

    def get_rgba_font_color(self):
        """
        Gets css property color of the element in rgba code

            Returns: identified rgba code
        """
        color = self.driver.find_element(*self.element).value_of_css_property('color')
        return color

    def get_font_weight(self):
        """
        Gets css property font weight of the element

            Returns: identified font weight as string
        """
        return self.driver.find_element(*self.element).value_of_css_property('font-weight')

    def get_font_family(self):
        """
        Gets css property font family of the element

            Return: dictionary having identified font family
        """
        return self.driver.find_element(*self.element).value_of_css_property('font-family')

    def is_font_style(self, font_style):
        """
        Asserts actual css font style of the element is equal to the font style passed as string

            Args:
                font_style: expected font style passed as a string

            Returns: Oobject of the inherited page to facilitate method chaining
        """
        try:
            if self.get_font_style() != font_style:
                raise AssertionError(f"Actual font style in {self.element} : '{self.get_font_style()}', got '{font_style}")
        except AssertionError as E:
            print(E)
        return self

    def is_font_size(self, font_size):
        """
        Asserts actual css font size of the element is equal to the font size passed as string

            Args:
                font_size: expected font size passed as a string

            Returns: Oobject of the inherited page to facilitate method chaining
        """
        try:
            if self.get_font_size() != font_size:
                raise AssertionError(f"Actual font size in {self.element} : '{self.get_font_size()}', got '{font_size}")
        except AssertionError as E:
            print(E)
        return self

    def is_selected(self):
        """
        Asserts the property of the element selected is true

            Returns: Oobject of the inherited page to facilitate method chaining
        """
        try:
            if not self.driver.find_element(*self.element).is_selected():
                raise AssertionError(f"{self.element} is not selected")
        except AssertionError as E:
            print(E)
        return self

    def is_displayed(self):
        """
        Asserts the property of the element displayed is true

            Returns: Oobject of the inherited page to facilitate method chaining
        """
        try:
            if not self.driver.find_element(*self.element).is_displayed():
                raise AssertionError(f"{self.element} is not displayed")
        except AssertionError as E:
            print(E)
        return self

    def is_enabled(self):
        """
        Asserts the enabled property of the element is true

            Returns: object of the inherited page to facilitate method chaining
        """
        try:
            if not self.driver.find_element(*self.element).is_enabled():
                raise AssertionError(f"{self.element} is not enabled")
        except AssertionError as E:
            print(E)
        return self

    def to_get_property(self, property_name):
        """
        Gets the property value of the element for passed property name

            Args:
                property_name: name of the desired property of the element passed as string

            Returns: identified property value as string
        """
        return self.driver.find_element(*self.element).get_property(property_name)

    def is_property(self, property_name, property_value):
        """
        Asserts the actual property value for the passed property name is same as the expected property value passed

            Args:
                property_name: name of the desired property of the element passed as a string
                property_value: expected property value for the passed property name passed as a string

            Returns:
                object of the inherited page to facilitate method chaining
        """
        try:
            if self.to_get_property(property_name) != property_value:
                raise AssertionError(f"Actual property of {self.element} is {property_name} : {self.to_get_property(property_name)}, but got {property_name} : {property_value}")
        except AssertionError as E:
            print(E)
        return self

    def get_attribute(self, attribute_name):
        """
        Gets the attribute value of the element for passed attribute name

            Args:
                attribute_name: name of the desired attribute of the element passed as string

            Returns: identified attribute value as string
        """
        return self.driver.find_element(*self.element).get_attribute(attribute_name)

    def is_attribute(self, attribute_name, attribute_value):
        """
        Asserts the actual attribute value for the passed attribute name is same as the expected attribute value passed

            Args:
                attribute_name: name of the desired attribute of the element passed as a string
                attribute_value: expected attribute value for the passed attribute name passed as a string

            Returns:
                object of the inherited page to facilitate method chaining
        """
        try:
            if self.get_attribute(
                attribute_name) != attribute_value:
                raise AssertionError(f"Actual property of {self.element} is {attribute_name} : {self.get_property(attribute_name)}, but got {attribute_name} : {attribute_value}")
        except AssertionError as E:
            print(E)
        return self

    def is_width(self, width, approx=None):
        """
        Asserts actual width with the expected width passed as string based on the operator or string passed with the
        numeric values in the string of expected width

            Args: width: takes only specific kind of strings
                        "27"     -  asserts width is in the rage of actual (width - approximate value passed),
                                    (width + approximate value passed)
                        "1 to 5" -  asserts actual width is in the range of 1 to 5
                        ">5"     -  asserts actual width is greater than 5
                        "<5"     -  asserts actual width is lesser than
                        5 ">=7"  -  asserts actual width is greater than or equals to 5
                        "<=19"   -  asserts actual width is lesser than or equals 5
                approx: takes the value of APPROXIMATION
                            from config file by default and takes the value passed if any value passed as integer

            Returns: object of the inherited page to facilitate method chaining
        """
        if approx is None:
            approx = approximate_value

        operation = ''.join([i for i in width if not i.isdigit()]).strip()
        actual_width = self.get_width()

        if operation == "to":
            flag = False
            width = width.split("to")
            if int(width[0]) <= actual_width <= int(width[1]):
                flag = True
            try:
                if not flag:
                    raise AssertionError(f"Actual width {actual_width} is not in range of {int(width[0])} to {int(width[1])}")
            except AssertionError as E:
                print(E)

        elif operation == ">":
            width = int(width.replace('>', ''))
            try:
                if actual_width <= width:
                    raise AssertionError(f"Actual width {actual_width} is not greater than {width}")
            except AssertionError as E:
                print(E)

        elif operation == "<":
            width = int(width.replace('<', ''))
            try:
                if actual_width >= width:
                    raise AssertionError(f"Actual width {actual_width} is not lesser than {width}")
            except AssertionError as E:
                print(E)

        elif operation == ">=":
            width = int(width.replace('>=', ''))
            try:
                if actual_width < width:
                    raise AssertionError(f"Actual width {actual_width} is lesser than {width}")
            except AssertionError as E:
                print(E)

        elif operation == "<=":
            width = int(width.replace('<=', ''))
            try:
                if actual_width > width:
                    raise AssertionError(f"Actual width {actual_width} is greater than {width}")
            except AssertionError as E:
                print(E)

        elif width.strip().isnumeric():
            width = int(width)
            try:
                if not actual_width - approx <= width <= actual_width + approx:
                    raise AssertionError(f"Actual width is {actual_width}, got {width}")
            except AssertionError as E:
                print(E)

        else:
            try:
                raise Exception(f'{width} unsupported operation for width')
            except Exception as E:
                print(E)
        return self

    def is_height(self, height, approx=None):
        """
        Asserts actual width with the expected width passed as string based on the operator or string passed with the
        numeric values in the string of expected width

            Args:
                height: takes only special kind of strings
                        "27"     -  asserts height is in the rage of actual (height - approximate value passed),
                                    (height + approximate value passed)
                        "1 to 5" -  asserts actual height is in the range of 1 to 5
                        ">5"     -  asserts actual height is greater than 5
                        "<5"     -  asserts actual height is lesser than 5
                        ">=7"    -  asserts actual height is greater than or equals to 5
                        "<=19"   -  asserts actual height is lesser than or equals 5
                 approx: defaults to value mentioned in config, can be overridden by passing values

            Returns: object of the inherited page to facilitate method chaining
        """
        if approx is None:
            approx = approximate_value

        operation = ''.join([i for i in height if not i.isdigit()]).strip()
        actual_height = self.get_height()

        if operation == "to":
            flag = False
            height = height.split("to")
            if int(height[0]) <= actual_height <= int(height[1]):
                flag = True
            try:
                if not flag:
                    raise AssertionError(f"Actual width {actual_height} is not in range of {int(height[0])} to {int(height[1])}")
            except AssertionError as E:
                print(E)

        elif operation == ">":
            height = int(height.replace('>', ''))
            try:
                if actual_height <= height:
                    raise AssertionError(f"Actual width {actual_height} is not greater than {height}")
            except AssertionError as E:
                print(E)

        elif operation == "<":
            height = int(height.replace('<', ''))
            try:
                if actual_height >= height:
                    raise AssertionError(f"Actual width {actual_height} is not lesser than {height}")
            except AssertionError as E:
                print(E)

        elif operation == ">=":
            height = int(height.replace('>=', ''))
            try:
                if actual_height < height:
                    raise AssertionError(f"Actual width {actual_height} is lesser than {height}")
            except AssertionError as E:
                print(E)

        elif operation == "<=":
            height = int(height.replace('<=', ''))
            try:
                if actual_height > height:
                    raise AssertionError(f"Actual width {actual_height} is greater than {height}")
            except AssertionError as E:
                print(E)

        elif height.strip().isnumeric():
            height = int(height)
            try:
                if not actual_height - approx <= height <= actual_height + approx:
                    raise AssertionError(f"Actual width is {actual_height}, got {height}")
            except AssertionError as E:
                print(E)

        else:
            try:
                raise Exception(f'{height} unsupported operation for height')
            except Exception as E:
                print(E)
        return self

    # -----------------------------------To assert exact height and width-----------------------------------------------
    def is_size(self, height, width):
        """
        Asserts the actual height and actual width is as same as height and width passed

            Args:
                height: numeric value of expected height of the element
                width: numeric value of expected width of the element

            Returns:
                object of the inherited page to facilitate method chaining
        """
        size = height, width
        element_size = self.get_size()
        actual_size = element_size['height'], element_size['width']
        try:
            if size != actual_size:
                raise AssertionError(f"Actual size is {actual_size}, got {size}")
        except AssertionError as E:
            print(E)
        return self

    # -----------------------------------To assert positioned vertically---------------------------------------
    def is_positioned_horizontally(self):
        """
        Asserts the width of element is higher than the height of the same element

            Returns:
                object of the inherited page to facilitate method chaining
        """
        size = self.get_size()
        try:
            if size['width'] <= size['height']:
                raise AssertionError(f"{self.element} is not positioned horizontally")
        except AssertionError as E:
            print(E)
        return self

    def is_positioned_vertically(self):
        """
        Asserts the height of element is higher than the width of the same element

            Returns:
                object of the inherited page to facilitate method chaining
        """
        size = self.get_size()
        try:
            if size['height'] <= size['width']:
                raise AssertionError(f"{self.element} is not positioned vertically")
        except AssertionError as E:
            print(E)
        return self

    def is_squared(self):
        """
        Asserts the width and height of the same element are same

            Returns: object of the inherited page to facilitate method chaining
        """
        size = self.get_size()
        try:
            if size['height'] != size['width']:
                raise AssertionError(f"{self.element} is not squared in dimension")
        except AssertionError as E:
            print(E)
        return self

    def is_almost_squared(self):
        """
        Asserts the width and height of the same element are same by reducing the accuracy by 10%

            Returns: object of the inherited page to facilitate method chaining
        """
        size = self.get_size()
        try:
            if size['height'] < size['width']:
                if (size['height'] / size['width']) * 100 > 10:
                    raise AssertionError(f"{self.element} is not squared")
            if size['width'] < size['height']:
                if (size['width'] / size['height']) * 100 > 10:
                    raise AssertionError(f"{self.element} is not squared")
        except AssertionError as E:
            print(E)
        return self

    def is_location(self, x, y):
        """
        Asserts the actual x, y offsets of the element are same as the expected x, y offsets passed

            Args:
                x: expected x offset of the element is passed as a numeric value
                y: expected y offset of the element is passed as a numeric value

            Returns: object of the inherited page to facilitate method chaining
        """
        location = x, y
        element_location = self.get_location()
        actual_location = element_location['x'], element_location['y']
        try:
            if actual_location != location:
                raise AssertionError(f"Actual location is {actual_location},got {location}")
        except AssertionError as E:
            print(E)
        return self

    def is_centered_horizontally(self, approx=None, inside=None):
        """
        Asserts the top and bottom pixels between the current element and the element identified from the object
        passed as the inside argument are approximately same, if no object passed as inside argument asserts element
        with the body of the page approximately

            Args:
                approx: defaults to value mentioned in config, can be overridden by passing values
                inside: takes the object of the inherited page

            Returns: object of the inherited page to facilitate method chaining

        """
        if approx is None:
            approx = approximate_value

        horizontal_loction = self.get_Xoffset()
        nested_element_width = self.get_width()

        try:
            if inside is None or inside == 'screen':
                inside = 'screen'
                parent_element_width = self.driver.find_element(By.TAG_NAME, "body").size['width']

            elif type(inside.element) is tuple:
                parent_element_width = inside.get_width()

            try:
                if not (parent_element_width - (
                        horizontal_loction + nested_element_width) - approx) <= horizontal_loction <= \
                       (parent_element_width - (horizontal_loction + nested_element_width) + approx):
                    raise AssertionError(f"{self.element} is not centered horizontally inside {inside} " if inside == 'screen' else f"{self.element} is not centered horizontally inside {inside.element}")
            except AssertionError as E:
                print(E)

        except AttributeError as E:
            try:
                raise Exception(f'{inside}:- is unsupported for this operation')
            except Exception as e:
                print(e)
        return self

    def is_centered_vertically(self, approx=None, inside=None):
        """
        Asserts the left and right pixels between the current element and the element identified from the object
        passed as the inside argument are approximately same, if no object passed as inside argument asserts element
        with the body of the page approximately

            Args:
                approx: defaults to value mentioned in config, can be overridden by passing values
                inside: takes the object of the inherited page

            Returns: object of the inherited page to facilitate method chaining

        """
        if approx is None:
            approx = approximate_value

        vertical_location = self.get_Yoffset()
        nested_element_height = self.get_height()

        try:
            if inside is None or inside == 'screen':
                inside = 'screen'
                parent_element_height = self.driver.find_element(By.TAG_NAME, "body").size['height']
            elif type(inside.element) is tuple:
                parent_element_height = inside.get_height()

            try:
                if not parent_element_height - (
                        vertical_location + nested_element_height) - approx <= vertical_location <= \
                       parent_element_height - (vertical_location + nested_element_height) + approx:
                    raise AssertionError(f"{self.element} is not centered vertically inside {inside} " if inside == 'screen' else f"{self.element} is not centered vertically inside {inside.element}")
            except AssertionError as E:
                print(E)

        except AttributeError as E:
            try:
                raise Exception(f'{inside}:- is unsupported for this operation')
            except Exception as e:
                print(e)
        return self

    def get_edges(self):
        """
        Gets x, y offsets and offsets of right bottom corner of the element

            Returns: x, y and right bottom corner offsets of the element as a tuple
        """
        inst_element_loc = self.get_dimension()
        coordinates = (inst_element_loc['x'], inst_element_loc['y'], inst_element_loc['x'] + inst_element_loc['width'],
                       inst_element_loc['y'] + inst_element_loc['height'])
        return coordinates

    def is_inside(self, parent=None):
        """
        Asserts the element is inside the element idenfied from the object passed as the parent argument, asserts with the body of the page if no object passed as parent argument

            Args:
                parent: object of the inherited page is passed to facilitate method chaining
        """
        child_loc = self.get_edges()

        if parent is None:
            parent_loc = self.get_edges((By.TAG_NAME, "body"))
        else:
            parent_loc = parent.get_edges()
        try:
            if not (child_loc[0] >= parent_loc[0] and child_loc[1] >= parent_loc[1] and child_loc[2] <= parent_loc[
                2] and child_loc[3] <= parent_loc[
                        3]):
                raise AssertionError(f"{self.element} is not inside screen" if parent is None else f"{self.element} is not inside {parent.element}")
        except AssertionError as E:
            print(E)
        return self

    def is_centered_all(self, inside=None, approx=None):
        """
        Asserts the x, y offsets of the center of element is approximately equal to the element identified from the
        object passed as inside argument, asserts with the body of the page if inside argument is not passed :param

            Args:
                inside: object of the inherited page is passed to facilitate method chaining
                approx: defaults to value mentioned in config, can be overridden by passing values

            Return: object of the inherited page to facilitate method chaining
        """
        if approx is None:
            approx = approximate_value

        child_loc = self.get_dimension()
        if inside is None:
            parent_loc = self.driver.find_element(By.TAG_NAME, "body").rect
        else:
            parent_loc = inside.get_dimension()

        child_loc = (child_loc['x'] + child_loc['width'] / 2), (child_loc['y'] + child_loc['height'] / 2)
        parent_loc = (parent_loc['x'] + parent_loc['width'] / 2), (parent_loc['y'] + parent_loc['height'] / 2)
        try:
            if not (parent_loc[0] - approx <= child_loc[0] <= parent_loc[0] + approx) & \
                   (parent_loc[1] - approx <= child_loc[1] <= parent_loc[1] + approx):
                raise AssertionError(f"{self.element} is not centered inside screen" if inside is None else f"{self.element} is not centered inside {inside.element}")
        except AssertionError as E:
            print(E)
        return self
