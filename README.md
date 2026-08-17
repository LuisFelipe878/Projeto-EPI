# 🦺 Projeto-EPI

## Sistema de Identificação de Equipamentos de Proteção Individual

O **Projeto-EPI** é um sistema desenvolvido para auxiliar na identificação de Equipamentos de Proteção Individual (EPI) utilizados por profissionais em ambientes de trabalho.

O projeto utiliza **Python** e um modelo de visão computacional baseado em **YOLO/Ultralytics** para analisar imagens e identificar equipamentos como **capacete (helmet)** e **colete (vest)**.

## 🎯 Objetivo

Desenvolver uma primeira versão funcional de um sistema capaz de analisar uma imagem e verificar a presença de equipamentos de proteção individual.

O projeto faz parte de um trabalho de estágio escolar e também serve como estudo prático de programação, inteligência artificial e visão computacional.

## 🔎 Funcionamento

1. O usuário fornece uma imagem.
2. O sistema carrega o modelo treinado.
3. A imagem é analisada pelo modelo de visão computacional.
4. As detecções são processadas pelo programa.
5. O sistema informa quais EPIs foram detectados.

## 🧠 Modelo

O projeto utiliza um modelo treinado com **Ultralytics YOLO**.

Na versão atual, o sistema foi testado para identificar principalmente:

- 🪖 **helmet** — capacete
- 🦺 **vest** — colete

## ✅ Teste realizado

Em um teste realizado com uma imagem de referência, o modelo apresentou:

- 🪖 **helmet:** 74,65% de confiança
- 🦺 **vest:** 61,18% de confiança

O programa também confirmou a detecção dos dois equipamentos e terminou com **código de retorno 0**, indicando execução bem-sucedida.

> Os valores de confiança podem variar de acordo com a imagem utilizada.

## 📁 Estrutura do projeto

```text
Projeto-EPI/
├── modelos/
│   └── melhor.pt
├── src/
│   ├── main.py
│   ├── classes_epi.py
│   └── verificacao_epi.py
├── README.md
└── melhor (1).pt
