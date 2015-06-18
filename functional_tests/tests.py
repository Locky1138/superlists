from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

# Lets practice some end-to-end user story writing!
# now with 100% more LiveServerTestCase from django.test 

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # ok for now, will need explicit waits later

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Alice visits our site
        self.browser.get(self.live_server_url)

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
        alice_list_url = self.browser.current_url
        self.assertRegex(alice_list_url, '/lists/.+')

        time.sleep(5)

        self.check_for_row_in_list_table('1: Follow the white rabbit')

        # there is still a text box inviting her to add another item
        # she enters "obey the testing goat"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Obey the testing goat')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(5)
        # the page updates again and now shows both items on her list

        self.check_for_row_in_list_table('1: Follow the white rabbit')
        self.check_for_row_in_list_table('2: Obey the testing goat')

        # Now a new user, Bob, comes along to the site.

        ## We use a new browser session to make sure that no information of Alice's
        ## is comming through our cookies, etc.

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Bob visits the home page.
        # there is no sign of Alice's list

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Follow the white rabbit', page_text)
        self.assertNotIn('Ovey the testing goat', page_text)

        # Bob starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Bob gets his own unique URL
        bob_list_url = self.browser.current_url
        self.assertRegex(bob_list_url, '/lists/.+')
        self.assertNotEqual(bob_list_url, alice_list_url)
        
        # Again there is no trace of Alice's List
        page_text = self.browser.find_element_by_tag_name('body').text
        time.sleep(5)
        self.assertNotIn('Follow the white rabbit', page_text)
        self.assertIn('Buy milk', page_text)

        # satisfied, she moves on to other adventures, and he goes to bed


