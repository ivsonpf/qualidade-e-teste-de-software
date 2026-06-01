# 🧪 Qualidade e Teste de Software

Este repositório documenta meus avanços, estudos e atividades práticas desenvolvidas durante a disciplina de **Qualidade e Teste de Software**. O objetivo principal é aplicar técnicas de validação, automação de testes e garantia de qualidade em código.

## 🗂️ Estrutura do Repositório

Os códigos estão organizados por conceitos e técnicas aprendidas durante as aulas:

* 📁 **`/testes-caixa-branca`**: Atividades focadas na análise da estrutura interna do código (cobertura de caminhos lógicos, tratamento de exceções e `ifs`). Contém:
  * Sistema de cálculo de seguro de carga (`test_modulo_seguro.py`).
  * Sistema de cálculo de frete logístico ERP (`test_logistica.py`).

* 📁 **`/testes-integracao-bd`**: Testes focados na comunicação do Python com o banco de dados relacional. Avalia a integridade dos dados e as restrições do MySQL (como chaves únicas, campos `NOT NULL` e `CHECK`) utilizando controle de transações (`BEGIN` e `ROLLBACK`) para manter a base limpa. Contém:
  * Validação de regras de negócio para cadastro de livros (`test_cad_livros.py`).

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python 3
* **Framework de Teste:** `unittest` (Padrão do Python)
* **Banco de Dados:** MySQL (via biblioteca `mysql-connector-python`)

## 🚀 Como executar os testes
Para rodar os testes unitários, navegue até o diretório do arquivo pelo seu terminal e execute o comando abaixo substituindo pelo nome do arquivo desejado:

```bash
python -m unittest nome_do_arquivo_de_teste.py
