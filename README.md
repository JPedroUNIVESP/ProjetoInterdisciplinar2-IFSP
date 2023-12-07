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

* [img](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/tree/main/img): esta pasta contém todas as imagens utilizadas no trabalho.

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
* Optou-se por separar a base entre aluguel e venda, visto que o valor a ser previsto (preço) variava muito entre essas categorias;
* Foram treinados 6 modelos: Regressão Linear, XGBoost e LightGBM. Abaixo é mostrado a performance do treino e na validação de cada modelo:

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/metricas.jpg)

</div>

* O modelo de regressão linear foi o que apresentou os maiores erros nas bases de aluguel e venda. Tal comportamento pode ser devido a simplicidade do modelo e pelo fato de algumas propriedades não terem necessariamente uma relação linear e de não termos aplicado nenhum tipo de regularização. Já quando partimos para o Boosting e o LGBM os erros foram menores. O LGBM se mostrou mais estável em relação as diferenças de erros entre as bases de treino e teste. Como os erros foram na mesma ordem de grandeza, não consideramos que houve overfit ou underfit.

---

### Diagrama da Arquitetura de dados:
<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/AWS1.jpg)

</div>

### Verificação de permissionamento IAM:

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/iam.png)
</div>

Antes de realizar o _ETL_ checamos todos os serviços disponíveis para o role _LabRole_, e
verificamos que os serviços que utilizariamos estavam liberados: _S3_, _Athena_, _SageMaker_, _EC2_, _Glue_.

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/LabRole.png)
</div>

----
### Processo de ETL com AWS Glue:

#### 1. Criação de Bucket S3:
Primeiramente, foram criados dois buckets no Amazon S3, um para armazenar os dados de entrada (input) e outro para a saida do modelo (output).

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/Buckets.png)
</div>

###### _input-propriedades_
Dentro do bucket de input, _**input-propriedades**_, criados 2 pastas: _raw_ e _processed_

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/input-propriedades.png)
</div>

* __raw__: Nesta pasta inserimos apenas os dados brutos, ou seja, a base crua extraída do [Kaggle](https://www.kaggle.com/datasets/argonalyst/sao-paulo-real-estate-sale-rent-april-2019).

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/input-propriedades-raw.png)
</div>

* __processed__: Nesta inserimos os dados processados, e para melhor organização separamos em 3 pastas:

    * __aluguel__: Arquivos _.csv_ contendo todos os dados de imóveis que estão para locação. Esses dados foram populados via Job.
    
    * __venda__: Da mesma forma que a base de aluguel, temos os arquivos _.csv_ contendo todos os dados de imóveis que estão para venda, e foram populados via Job.

    * __full__: Base intermediária contendo todos os dados de input, sem nenhum filtro, com um mapeamento aplicado de regiões. Utilizados esse mapeamento para clusterizar imóveis de acordo com a zona que o mesmo pertence, dentro da cidade de são paulo, ao invés de utilizar a informação de distrito.

<div align="center">

  ![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/input-propriedades-processed.png)
</div>

###### _output-modelo_
Neste bucket de output inserimos os pickles gerados via SageMaker, após o processamento dos modelos.

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/output-modelo.png)
</div>

---

#### 2. Detalhamento do Glue Job

Utilizamos o **Visual ETL** para realizar o pré-processamento dos dados. 

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/Job-Input-Dados.png)
</div>

Inicialmente, adicionamos um nó para acessar o bucket que contém os dados de entrada (_input-propriedades/raw/_).

Em seguida, implementamos um nó de transformação via SQL query no qual criou uma coluna (district_zone) atráves de um mapeamento de _bairro -> região_. 
Para eliminar linhas duplicadas, adicionamos na sequência outro nó de transformação que capturou apenas as linhas únicas da base.
Posteriormente, paralelizamos dois nós: um para salvar a base de input com a adição da coluna district_zone em _input-propriedades/raw/full/_ , e outro para a retirada de colunas que não usaremos nos modelos.
Com outro nó de transformação filtramos os dados e geramos as bases de vendas e de aluguel.
Por fim, salvamos os arquivos _.csv_ gerados em _input-propriedades/raw/venda/_ e _input-propriedades/raw/aluguel/_, respectivamente.

O script gerado está disponível neste [link](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/Glue-Jobs/glue-job.py)
<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/Glue-Job.png)
</div>

---

#### 3. Configuração do Crawler Glue para criação de tabelas

Foram criados crawlers para analisarem os dados nos buckets de input e output, e criar metadados e tabelas no AWS Glue DataCatalog.
<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/Glue-Tables.png)
</div>

Após a rodada de cada um, conseguimos visualizar os dados via AWS Athena.

---

#### 4. Refinamento do Glue DataCatalog
Após a criação das tabelas, editamos o schema de cada uma para ajustar o nome e o tipo das colunas, além da adição do comentário com um breve descritivo de cada coluna.

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/Schema-Aluguel.png)
</div>

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/Schema-Venda.png)
</div>

---
#### 5. Validação de dados com Athena

Uma vez que as tabelas foram criadas no Glue DataCatalog, utilizamos o *Amazon Athena* para executar consultas SQL diretamente nos dados processados (_aluguel, venda e full_).
Essas consultas auxiliaram no pré-processamento dos dados e refinamento do _Job_.

##### _Queries_
* As consultas utilizadas se encontram nesta [pasta](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/tree/main/Queries-SQL)


#### 6. SageMaker

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/notebook_instance.png)
</div>


Utilizando o SageMaker, provisionamos uma instância EC2 (_ml.c5.xlarge_: 4 vCPUs e 8GB de memória) para executar um notebook que desenvolvemos 
para treinar três modelos distintos: _Regressão Linear_, _Boosting_ e _LGBM_. 

<div align="center">

![](https://github.com/JPedroUNIVESP/ProjetoInterdisciplinar2-IFSP/blob/main/img/create_notebook_instance.png)
</div>

Ao final desse processo, geramos 2 arquivos no formato .pkl contendo as informações e parâmetros resultantes dos modelos selecionados.


---

#### 7. Conclusão
* O LightGBM se mostrou como modelo mais eficiente em prever o preço dos imóveis em aluguel e venda, não apresentando _overfit_ ou _underfit_ e possuiu performance melhor que a Regressão Linear e o XGBoost;
* O ambiente Cloud Amazon AWS se mostrou eficiente e escalável em armazenar dados e realizar ETL. Também se mostrou eficiente em oferecer um ambiente para treinamento e realização de deploy de modelos.