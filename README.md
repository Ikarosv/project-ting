# project‑ting

**Repositório**: ferramentas para gerenciamento de arquivos e buscas de palavras.

## 🧾 Sobre

Projeto em **Python** que simula um sistema de processamento e análise de arquivos. Possui módulos para:

* **Gerenciamento de arquivos**
* **Busca de palavras-chave**
* **Leitura controlada em fila**

É voltado para fins didáticos e estruturado com boas práticas de testes, cobertura e formatação de código.

## ⚙️ Tecnologias e bibliotecas usadas

* **Python 3.8+**
* [pytest](https://docs.pytest.org/en/7.1.x/) – execução de testes
* [pytest-cov](https://pytest-cov.readthedocs.io/) – cobertura dos testes
* [pytest-json](https://pypi.org/project/pytest-json/) – relatório de testes em JSON
* [pytest-dependency](https://github.com/RKrahl/pytest-dependency) – controle de dependência entre testes
* [flake8](https://flake8.pycqa.org/) – verificação de estilo
* [black](https://black.readthedocs.io/en/stable/) – formatação automática de código

## 📁 Estrutura do projeto

```
.
├── ting_file_management/     # Módulo de gerenciamento de arquivos
├── ting_word_searches/       # Módulo de busca de palavras
├── tests/                    # Testes automatizados
├── requirements.txt
├── dev-requirements.txt
├── setup.py
├── setup.cfg
├── pyproject.toml
└── README.md
```

## 🚀 Instalação

Clone o projeto e instale as dependências:

```bash
git clone https://github.com/Ikarosv/project-ting.git
cd project-ting

# Instala dependências principais
pip install .

# Instala dependências de desenvolvimento
pip install -r dev-requirements.txt
```

## 🧪 Executando os testes

Para rodar os testes:

```bash
pytest
```

Para gerar relatório de cobertura:

```bash
pytest --cov=ting_file_management --cov=ting_word_searches
```

Para gerar um relatório JSON:

```bash
pytest --json-report
```

## 🧼 Padronização de código

Verifique erros de estilo com `flake8`:

```bash
flake8
```

Formate o código com `black`:

```bash
black .
```

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 📄 Licença

Este projeto não possui licença definida.
