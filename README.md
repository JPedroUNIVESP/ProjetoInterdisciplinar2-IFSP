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
##### A análise exploratória dos dados revelou o seguinte:
* A maioria dos imóveis que se encontram na região Oeste e Sul, possui uma média de preços, tanto aluguel quanto venda, superior as demais regiões;
* Os valores de condominio nas regiões Oeste e Sul, são maiores em relação as demais regiões. O mesmo comportamento visto no preço dos imóveis. Isso era de se esperar: imóveis mais caros, estão em melhores localizações e possuem maior "infraestrutura", aumentando assim seu custo final;
* Há uma relação direta entre o tamanho do imóvel e seu preço. Imóveis maiores, custam mais caro. O que já era esperado;
* A média nas regiões centro, leste e norte estão bem próximas de 2 banheiros, mas na zona Oeste e Sul, a média está mais próximo de 3. Como a média de quartos é maior nessa região, é de se esperar que o número de banheiros também seja para comportar os moradores;
* As regiões Centro, Leste e norte, a maioria dos imóveis não possui suites;
* Em imóveis maiores, com mais quartos, o número de moradores tende a ser maior, logo é de se esperar a necessidade de mais vagas de estacionamento para imóveis maiores. Vemos que as regiões Oeste e Sul, por possuirem imóveis maiores, também tem uma oferta maior de imóveis com mais vagas, como esperado.
* Podemos observar que mesmo em regiões mais caras, a maioria dos imóveis não possui elevador. Essa informação surpreendeu. É de se esperar que em imóveis mais caros, por se tratar de apartamentos, deva ter elevador. Uma suposição para essa ausência de elevadores é uma quantidade pequena de andares no imóvel (inferior a 4 andares), o que explicaria esse comportamento;
* Em todas as regiões vemos que mais de 77% delas não está mobiliada;
* Notamos que para as regiões em que os preços dos aluguéis e venda são mais altos (Zona Oeste e Sul), o percentual de imóveis que possuem piscina são maiores que os que não possuem. O destaque foi para a região norte que possui mais de 70% das casas a venda com piscina;
* Na base, a grande maioria dos imóveis não são novos. Pode ser que essa informação não seja interessante para o modelo visto que há concentração em um valor.





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
