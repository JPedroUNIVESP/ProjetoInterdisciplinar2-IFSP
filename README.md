# Projeto Interdisciplinar - IFSP - Câmpus Campinas
## Projeto Interdisciplinar - 2o. Semestre
## Ciência de Dados
### Alunos: 

[Evandro Costa Ferreira (CP3021947)](https://github.com/evandrocf4)<br>
[Jaqueline Jana da Silva (CP3021891)](https://github.com/JaquelineJana)<br>
[João Pedro de Oliveira Ferreira (CP3021696)](https://github.com/JPedroUNIVESP)


---


### Base de Dados
* A base de dados utilizada neste projeto se encontra no seguinte link do [Kaggle](https://www.kaggle.com/datasets/argonalyst/sao-paulo-real-estate-sale-rent-april-2019)
<!-- O dataset se refere a 13 mil propriedades à venda ou para alugar na cidade de São Paulo, Brasil.-->
* O conjunto de dados inclui aproximadamente 13.000 apartamentos disponíveis para venda e locação na cidade de São Paulo. As informações foram coletadas de diversas fontes, com destaque para sites de classificados de imóveis. Sendo uma versão menor e anonimizada de um conjunto de dados que foram utilizados na startup OpenImob.
* O objetivo do trabalho é prever o preço das propriedades tanto para venda como para aluguel.
---
### Estrutura das pastas
* [.ipynb_checkpoints](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/tree/main/.ipynb_checkpoints): esta pasta contém o código utilizado para avalidar 3 modelos: __regressão linear__, __xgboost__ e __lgbm__;

* [pickles](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/tree/main/pickles): esta pasta contém os dois arquivos _.pickles_ para os modelos escolhidos para previsão de preço de aluguel e de venda;

* [Glue-Jobs](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/tree/main/Glue-Jobs): esta pasta contém o script utilizado no Glue Job para o pré processamento;

* [Queries-SQL](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/tree/main/Queries-SQL): esta pasta contém todas as queries SQLs utilizadas no trabalho.

---
### Análise Exploratória
*
*
*
---
### Análise dos Modelos
*
*
*
---

### Diagrama da Arquitetura de dados:
![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/AWS1.jpg)
----
### Detalhe do Glue Job
![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/Glue-Job.jpg)
_Pré-processamento de Dados com Visual ETL_

Utilizamos o Visual ETL para realizar o pré-processamento dos dados. Inicialmente, adicionamos um nó para acessar o bucket que contém os dados de entrada.

Em seguida, implementamos um nó de transformação para eliminar linhas duplicadas. Posteriormente, paralelizamos dois nós: um para filtrar dados e gerar a base de vendas, e outro para criar a base de aluguel.

Ao finalizar o processamento, os dois arquivos .csv resultantes são salvos no mesmo bucket, mas em pastas distintas.

O script gerado está disponível neste [link](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/Glue-Jobs/glue-job.py)

---
### Queries
* As consultas se encontram nesta [pasta](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/tree/main/Queries-SQL)

### Conclusão
*
*
*
