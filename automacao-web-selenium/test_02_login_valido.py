import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginValido(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://seventechsolucoes.com.br/selenium/login.php")

    def tearDown(self):
        self.driver.quit()

    def test_02_login_valido(self):
        usuario = self.wait.until(EC.presence_of_element_located((By.NAME, "usuario")))
        senha = self.wait.until(EC.presence_of_element_located((By.NAME, "senha")))
        
        usuario.send_keys("aluno")
        senha.send_keys("123456")
        
        # Pausa estratégica para dar tempo de ler os campos preenchidos antes do clique
        time.sleep(2)
        
        botao_login = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'] | //input[@type='submit']"))
        )
        botao_login.click()

        self.wait.until(EC.url_changes("https://seventechsolucoes.com.br/selenium/login.php"))

        botao_logout = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="logout.php"]'))
        )
        self.assertTrue(botao_logout.is_displayed())
        
        # Pausa para o professor confirmar visualmente que o login deu certo e o painel abriu
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()