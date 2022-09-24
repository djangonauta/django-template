from django import test, urls
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class BaseFunctionalTests(test.LiveServerTestCase, test.TestCase):

    def setUp(self):
        super().setUp()
        self.driver = Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()
        super().tearDown()

    def get_live_url(self, url_name):
        return f'{self.live_server_url}{urls.reverse(url_name)}'

    def test_web(self):
        self.driver.get(self.get_live_url('index'))
        text = self.driver.find_element(By.TAG_NAME, 'h3').text
        self.assertEqual(text, 'working')
