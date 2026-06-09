import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginCarregamento(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://seventechsolucoes.com.br/selenium/login.php")

    def tearDown(self):
        self.driver.quit()

    def test_01_tela_de_login_carregada_com_sucesso(self):
        usuario = self.wait.until(
            EC.presence_of_element_located((By.NAME, "usuario"))
        )
        self.assertTrue(usuario.is_displayed())
        
        # Pausa para o professor ver a tela inicial estática carregada com sucesso
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()