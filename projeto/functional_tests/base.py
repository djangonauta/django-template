from django import test, urls
from django.conf import settings
from selenium.webdriver import Chrome


class BaseFunctionalTests(test.LiveServerTestCase):
    available_apps = settings.INSTALLED_APPS

    def setUp(self):
        super().setUp()
        self.browser = Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(7)

    def tearDown(self):
        self.browser.close()
        super().tearDown()

    def get_live_url(self, url_name):
        return f"{self.live_server_url}{urls.reverse(url_name)}"
