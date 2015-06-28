from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Alice goes to the home page and accidently tries to submit
        # an empty list item. she hits enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # she tries again with some text for the item, which now works

        # Perversely, she now decides to submit a second blank list item

        # she recieves a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
