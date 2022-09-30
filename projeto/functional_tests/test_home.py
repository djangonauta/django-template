from django.contrib.auth import get_user_model
from selenium.webdriver.common.by import By

from .base import BaseFunctionalTests


class TestMarcarConsulta(BaseFunctionalTests):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.cliente = get_user_model().objects.create_user(
            username='usuario', email='usuario@domain.com', password='senha',
        )

    def test_marcar_consulta(self):
        self.browser.get(self.get_live_url('index'))
        self.assertTrue(get_user_model().objects.get().is_default())
        self.assertEqual(
            self.browser.find_element(By.TAG_NAME, 'h3').text,
            'Bem vindo',
        )
