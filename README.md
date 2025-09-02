# 🧪 Atividade de Teste de Mutação com Python Validators
Aplicação prática da técnica de **Teste de Mutação** para avaliar e aprimorar a suíte de testes da biblioteca [python-validators](https://github.com/kvesteri/validators).  
Projeto desenvolvido como parte da disciplina **Teste de Software** da **Universidade Federal de Sergipe (UFS)**.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![pytest](https://img.shields.io/badge/Tests-pytest-green)
![Mutation Testing](https://img.shields.io/badge/Mutation%20Testing-mutmut-orange)

---

## 👥 Autores
- Gustavo Henrique Marques  
- Henrique Rocha Valentim Bastos  
- Mariana Souza Nunes  
- Rafael Lauton Santos de Oliveira  

---

## 📖 Introdução
O **Teste de Mutação** é uma técnica avançada de verificação de software que avalia a eficácia de uma suíte de testes.  
A ideia é introduzir pequenas alterações no código (*mutantes*) e verificar se os testes são capazes de "matar" esses mutantes.  
Um mutante sobrevivente indica **fraqueza na suíte de testes** e aponta áreas para melhoria.

Este trabalho teve como objetivos:
1. Executar a suíte de testes original da biblioteca `python-validators` (baseline).  
2. Medir a cobertura de código com `pytest-cov`.  
3. Aplicar o `mutmut` para gerar e avaliar mutantes.  
4. Analisar os mutantes sobreviventes e identificar lacunas nos testes.  
5. Implementar novos casos de teste para aumentar a robustez da suíte.  

---

## 🛠️ Ferramentas Utilizadas
- **Python 3.12+** → Linguagem de programação.  
- **venv** → Criação de ambientes virtuais isolados.  
- **pytest** → Execução dos testes de unidade.  
- **pytest-cov** → Medição de cobertura de código.  
- **mutmut** → Ferramenta de Teste de Mutação.  

---

## ⚙️ Como Replicar a Análise

### 1️⃣ Clone o repositório
```bash
git clone <url_deste_repositorio>
cd <url_deste_repositorio>
```
### 2️⃣ Crie e ative um ambiente virtual
```
python3 -m venv .venv
source .venv/bin/activate
```
### 3️⃣ Instale as dependências
```
pip install pytest pytest-cov mutmut
```
### 4️⃣ Rode os testes unitários (baseline)
 ```
 pytest
 pytest --cov=validators 
   ```

### 5️⃣ Execute o teste de mutação

```
mutmut run
mutmut results
```
## 📊 Resultados Obtidos

- Cobertura de código inicial: 89%

- Mutantes gerados: 689

- Mutantes mortos (killed): 469

- Mutantes sobreviventes: 215

Após a adição de novos casos de teste:

- Mutantes mortos (killed): 496

- Mutantes sobreviventes: 193