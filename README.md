# 🪖 Projeto-EPI

## Sistema de Identificação de Equipamentos de Proteção Individual

Projeto desenvolvido por **Luis Felipe**, estudante do **Instituto Federal de Goiás (IFG)**, com o objetivo de desenvolver um sistema de visão computacional capaz de auxiliar na identificação do uso de Equipamentos de Proteção Individual (EPIs) por profissionais em ambientes de trabalho.

---

## 📌 Sobre o projeto

O **Projeto-EPI** tem como proposta utilizar **Inteligência Artificial e Visão Computacional** para analisar imagens e, posteriormente, vídeos de ambientes de trabalho.

O sistema deverá ser capaz de identificar profissionais presentes na imagem e verificar a presença de determinados equipamentos de proteção, como:

* 🪖 Capacete de segurança
* 🦺 Colete de segurança
* 🥽 Óculos de proteção
* 🧤 Luvas
* 👢 Calçados de segurança
* 😷 Máscara de proteção

O projeto está sendo desenvolvido de forma gradual, começando por um protótipo para processamento de imagens.

---

## 🎯 Objetivos

### Objetivo geral

Desenvolver um protótipo de sistema de visão computacional capaz de auxiliar na identificação do uso de Equipamentos de Proteção Individual em ambientes profissionais.

### Objetivos específicos

* Processar imagens de ambientes de trabalho;
* Identificar pessoas presentes nas imagens;
* Detectar equipamentos de proteção individual;
* Associar os EPIs identificados aos profissionais detectados;
* Apresentar os resultados de forma visual;
* Posteriormente, realizar testes com vídeos;
* Desenvolver uma interface simples para facilitar a utilização do sistema.

---

## 🧠 Tecnologias

As principais tecnologias previstas para o desenvolvimento são:

* **Python** — linguagem de programação;
* **YOLO** — modelo de detecção de objetos;
* **OpenCV** — processamento de imagens e vídeos;
* **Pillow** — manipulação de imagens;
* **Git e GitHub** — controle e armazenamento do código-fonte.

As tecnologias poderão ser ajustadas durante o desenvolvimento do projeto.

---

## 📂 Estrutura do projeto

```text
Projeto-EPI/
│
├── data/
│   └── images/
│
├── results/
│
├── src/
│   └── main.py
│
└── README.md
```

### Diretórios

**`data/images/`**
Armazena as imagens utilizadas nos testes.

**`results/`**
Armazena os resultados gerados pelo sistema.

**`src/`**
Contém o código-fonte principal do projeto.

---

## 🚧 Status do projeto

**Em desenvolvimento — Etapa 1**

Atualmente, o projeto possui:

* [x] Repositório criado no GitHub
* [x] Estrutura inicial do projeto
* [x] Primeiro programa em Python
* [x] Diretório para imagens de teste
* [x] Diretório para resultados
* [ ] Processamento automatizado de imagens
* [ ] Implementação do modelo de detecção de objetos
* [ ] Detecção específica de EPIs
* [ ] Testes com vídeos
* [ ] Interface gráfica
* [ ] Geração de relatórios

---

## 🔬 Metodologia

O desenvolvimento será realizado de maneira incremental.

### Etapa 1 — Protótipo

Criar a estrutura inicial do projeto e realizar o processamento básico de imagens.

### Etapa 2 — Visão computacional

Integrar ferramentas de processamento e detecção de objetos.

### Etapa 3 — Detecção de EPIs

Utilizar um modelo adequado para identificar diferentes tipos de equipamentos de proteção.

### Etapa 4 — Análise de profissionais

Relacionar os equipamentos identificados às pessoas presentes na imagem.

### Etapa 5 — Vídeos

Expandir o sistema para trabalhar com vídeos e, futuramente, com transmissões em tempo real.

### Etapa 6 — Interface e resultados

Desenvolver uma interface para facilitar o uso do sistema e apresentar os resultados das análises.

---

## ⚠️ Limitações

O Projeto-EPI é um **protótipo acadêmico em desenvolvimento**.

Os resultados produzidos pelo sistema não devem ser considerados, isoladamente, como uma certificação de conformidade ou substituição da avaliação realizada por profissionais responsáveis pela segurança do trabalho.

A precisão do sistema dependerá da qualidade das imagens, do modelo utilizado e dos dados empregados em seu treinamento e avaliação.

---

## 🎓 Finalidade acadêmica

Este projeto está sendo desenvolvido como parte da formação acadêmica de **Luis Felipe**, estudante do **Instituto Federal de Goiás (IFG)**, com finalidade de aprendizado, pesquisa e apresentação em contexto de estágio escolar.

---

## 👨‍💻 Autor

**Luis Felipe**

Estudante do **Instituto Federal de Goiás (IFG)**

GitHub: [LuisFelipe878](https://github.com/LuisFelipe878)

---

## 📄 Licença

Este projeto ainda não possui uma licença definida.
