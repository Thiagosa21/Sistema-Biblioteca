# 📚 Sistema de Gerenciamento de Biblioteca

## 📖 Sobre o projeto

Este projeto foi desenvolvido em **Python** com o objetivo de praticar os conceitos de **Programação Orientada a Objetos (POO)**.

A aplicação funciona pelo terminal e permite realizar o gerenciamento básico de uma biblioteca, possibilitando o cadastro de livros, consulta dos livros cadastrados, empréstimo e devolução.

Nesta primeira versão, todas as informações são armazenadas em memória durante a execução do programa. Ao encerrar a aplicação, os dados são perdidos.

---

## 🚀 Funcionalidades

* ✅ Cadastrar livros
* ✅ Listar livros cadastrados
* ✅ Empréstimo de livros por ID
* ✅ Devolução de livros por ID
* ✅ Geração automática de IDs para cada livro
* ✅ Controle de disponibilidade dos livros

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Programação Orientada a Objetos (POO)

---

## 📂 Estrutura do projeto

A classe `Livro` representa um livro da biblioteca, contendo:

* ID
* Nome
* Autor
* Status de empréstimo

O sistema permite:

* Criar novos livros
* Armazená-los em memória
* Consultar informações
* Alterar o status de empréstimo

---

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
```

2. Entre na pasta do projeto:

```bash
cd NOME-DO-REPOSITORIO
```

3. Execute o programa:

```bash
python nome_do_arquivo.py
```

---

## 📋 Menu da aplicação

```text
======================================================
|                Cadastro de Livros                  |
======================================================
|                1 - Cadastrar Livros                |
|                2 - Mostrar Livros Cadastrados      |
|                3 - Emprestar Livro                 |
|                4 - Devolver Livro                  |
|                5 - Sair                            |
======================================================
```

---

## 📌 Próximas melhorias

* Persistência de dados utilizando MySQL
* Classe `Biblioteca` para gerenciamento dos livros
* Pesquisa de livros por nome
* Pesquisa por autor
* Exclusão de livros
* Tratamento de erros com `try/except`
* Melhor organização do código

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido para praticar:

* Programação Orientada a Objetos
* Classes e Objetos
* Construtores (`__init__`)
* Atributos de instância e de classe
* Manipulação de listas de objetos
* Estruturas de repetição
* Estruturas condicionais
* Organização de código em funções

---

## 📈 Evolução do projeto

### Versão 1.0

* Sistema funcionando totalmente em memória.
* Cadastro, consulta, empréstimo e devolução de livros.

### Próxima versão

Integração com banco de dados MySQL para persistência dos dados e gerenciamento real da biblioteca.

---

## 👨‍💻 Autor

Desenvolvido por **Thiago Medeiros** como projeto de estudos em Python e Programação Orientada a Objetos.
