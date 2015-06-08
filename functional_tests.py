from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

# Lets practice some end-to-end user story writing!
# now with 100% more unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # ok for now, will need explicit waits later

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Alice visits our site
        self.browser.get('http://localhost:8000')

        # she notices the page title and headder mention "To-Do" lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a to-do item immediately
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she types in "Follow the white rabbit" into a text box
        inputbox.send_keys('Follow the white rabbit')

        # when she hits 'Enter' the page updates, and now lists
        # "1: Follow the white rabbit" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Follow the white rabbit' for row in rows),
            "New to-do item did not appear in table"
        )

        # there is still a text box inviting her to add another item
        # she enters "obey the testing goat"
        self.fail('Finish the test!')

        # the page updates again and now shows both items on her list

        # Alice woners if the site will remember her list
        # she sees that the site has generated a unique URL for her
        # and there is some text explaining its use

        # she visits that URL and her list is there.

        # satisfied, she moves on to other adventures

if __name__ == '__main__':
    unittest.main()

