from django import urls
from django.test import LiveServerTestCase
from selenium.webdriver import Firefox


class BaseFunctionalTests(LiveServerTestCase):

    def setUp(self):
        self.driver = Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()

    def get_live_url(self, url_name):
        return f'{self.live_server_url}{urls.reverse(url_name)}'
