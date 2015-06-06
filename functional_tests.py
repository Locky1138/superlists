from selenium import webdriver

browser = webdriver.Firefox()

# Lets practice some end-to-end user story writing!

# Alice visits our site
browser.get('http://localhost:8000')

# she notices the page title and headder mention "To-Do" lists
assert 'To-Do' in browser.title

# she is invited to enter a to-do item immediately

# she types in "Follow the white rabbit" into a text box

# when she hits 'Enter' the page updates, and now lists
# "1: Follow the white rabbit" as an item in a to-do list

# there is still a text box inviting her to add another item
#she enters "obey the testing goat"

# the page updates again and now shows both items on her list

# Alice woners if the site will remember her list
# she sees that the site has generated a unique URL for her
# and there is some text explaining its use

# she visits that URL and her list is there.

# satisfied, she moves on to other adventures
browser.quit()
