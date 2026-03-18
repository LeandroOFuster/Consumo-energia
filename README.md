# ⚡ Calculadora de Consumo de Energia Elétrica

## 📌 Nome e Objetivo

> **Calculadora de Consumo de Energia Elétrica**

Este sistema foi desenvolvido em **Python** com o objetivo de ajudar o usuário a calcular o **consumo de energia elétrica** de qualquer aparelho doméstico, estimando o **custo mensal na conta de luz** de forma simples e rápida.

## 🐍 Linguagem Utilizada

<p>
  <img src="https://img.shields.io/badge/Python-Linguagem_Principal-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Versão-3.x-FFD43B?style=flat-square&logo=python&logoColor=blue"/>
</p>

O projeto utiliza apenas recursos nativos do Python, sem necessidade de instalar bibliotecas externas:

- 🔤 `input()` — leitura de dados do usuário
- 🔢 `float()` — conversão para número decimal
- 🖨️ `print()` com **f-string** — exibição formatada dos resultados

---

## 🔢 Fórmulas Utilizadas

| ⚙️ Cálculo | 📐 Fórmula |
|-----------|-----------|
| ⚡ Consumo Diário | `(Potência W × Horas) ÷ 1000` |
| 📅 Consumo Mensal | `Consumo Diário × 30 dias` |
| 💰 Custo Diário | `Consumo Diário × R$/kWh` |
| 🧾 Custo Mensal | `Consumo Mensal × R$/kWh` |

## 💻 Exemplo de Uso

💡 Calculadora Consumo de Energia Elétrica 💡

Digite o nome do Aparelho: Geladeira
Digite a Potência do Aparelho (em Watts): 150
Digite o Tempo de Uso Diário (em horas): 24

O consumo diário da Geladeira é: 3.60 kWh
O consumo mensal da Geladeira é: 108.00 kWh

Digite o Custo do kWh (em R$): 0.85

O custo diário da Geladeira é: R$ 3.06
O custo mensal da Geladeira é: R$ 91.80

## 🛠️ Tecnologias e Conceitos

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Tipo-float-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Formatação-f--string-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Entrada-input()-9cf?style=flat-square"/>
  <img src="https://img.shields.io/badge/Saída-print()-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Operadores-Aritméticos-red?style=flat-square"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/>
</p>

## 👤 Autor

Desenvolvido como projeto prático de introdução ao Python.