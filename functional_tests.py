from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith goes to check out the homepage
        self.browser.get('http://127.0.0.1:8000')

        # She notices that the header and page title mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She types "Buy peacock feathers" into a text box

        # When she hits enter the page lists "1: Buy peacock feathers"

        # There is still a textbox for another item. She types " Use peacock feathers to make a fly"

        # The page updates again and shows both items

        # She sees that the page has generated a unique URL for her and explanatory text.

        # She visits the URL and her list is still There

if __name__=='__main__':
    # checks if script is run from command line
    unittest.main(warnings='ignore')
