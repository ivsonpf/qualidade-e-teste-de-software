import unittest
import mysql.connector
from mysql.connector import IntegrityError

class TestCadLivros(unittest.TestCase):
    
    # 1 - SETUP (Preparação)
    def setUp(self):
        # Conexão simulada com o banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sua_senha",
            database="sua_base"
        )
        # Inicia a transação (equivalente ao BEGIN TRANSACT do quadro)
        self.conexao.start_transaction()

    # 3 - TEARDOWN (Limpeza)
    def tearDown(self):
        # Desfaz qualquer inserção para não poluir o banco de dados
        self.conexao.rollback()
        self.conexao.close()

    # 2 - SEQUÊNCIA DE TESTES

    # RÉPLICA 1: Regra do Código Único
    def test_nao_deve_cadastrar_livro_com_codigo_duplicado(self):
        cursor = self.conexao.cursor()
        
        # Insere um livro válido primeiro para ocupar o código 100
        cursor.execute(
            "INSERT INTO livros (codigo, titulo, autor, quantidade) "
            "VALUES (100, 'Senhor dos Anéis', 'Tolkien', 5)"
        )
        
        # Tenta inserir outro livro com o MESMO código (100).
        # Espera-se que o banco dispare um IntegrityError (Chave Única/Primary Key).
        with self.assertRaises(IntegrityError):
            cursor.execute(
                "INSERT INTO livros (codigo, titulo, autor, quantidade) "
                "VALUES (100, 'O Hobbit', 'Tolkien', 3)"
            )

    # RÉPLICA 2: Regra do Título Obrigatório
    def test_nao_deve_cadastrar_livro_sem_titulo(self):
        cursor = self.conexao.cursor()
        
        # Tenta inserir um livro deixando o campo 'titulo' de fora (ou passando NULL).
        # Espera-se que o banco dispare um erro de restrição NOT NULL.
        with self.assertRaises(IntegrityError):
            cursor.execute(
                "INSERT INTO livros (codigo, autor, quantidade) "
                "VALUES (101, 'George Orwell', 10)"
            )

    # RÉPLICA 3: Regra da Quantidade >= 0
    def test_nao_deve_cadastrar_livro_com_quantidade_negativa(self):
        cursor = self.conexao.cursor()
        
        # Tenta inserir um livro com quantidade igual a -5.
        # Espera-se que o banco dispare um erro (assumindo que há uma restrição CHECK >= 0 na tabela).
        with self.assertRaises(IntegrityError):
            cursor.execute(
                "INSERT INTO livros (codigo, titulo, autor, quantidade) "
                "VALUES (102, '1984', 'George Orwell', -5)"
            )

if __name__ == '__main__':
    unittest.main()
