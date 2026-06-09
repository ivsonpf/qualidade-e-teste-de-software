import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginInvalido(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://seventechsolucoes.com.br/selenium/login.php")

    def tearDown(self):
        self.driver.quit()

    def test_03_login_invalido(self):
        usuario = self.wait.until(EC.presence_of_element_located((By.NAME, "usuario")))
        senha = self.wait.until(EC.presence_of_element_located((By.NAME, "senha")))
        
        usuario.send_keys("aluno")
        senha.send_keys("senha_errada_123")
        
        # Pausa estratégica para evidenciar a tentativa com a senha incorreta
        time.sleep(2)
        
        botao_login = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'] | //input[@type='submit']"))
        )
        botao_login.click()

        botao_tentar_novamente = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[onclick="voltarLogin()"]'))
        )
        self.assertTrue(botao_tentar_novamente.is_displayed())
        
        # Pausa final para exibir a tela de erro e o botão de "Tentar Novamente" renderizado
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()