import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from awsglue import DynamicFrame
from pyspark.sql import functions as SqlFuncs
import re


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1701734553332 = glueContext.create_dynamic_frame.from_catalog(
    database="propriedades",
    table_name="raw",
    transformation_ctx="AmazonS3_node1701734553332",
)

# Script generated for node SQL Query
SqlQuery0 = """
SELECT
    raw.*,
    CASE 
        WHEN district IN ('Artur Alvim/São Paulo', 'Belém/São Paulo', 'Cangaíba/São Paulo', 'Carrão/São Paulo',
						    'Cidade Líder/São Paulo', 'Cidade Tiradentes/São Paulo', 'Ermelino Matarazzo/São Paulo',
							'Iguatemi/São Paulo', 'Itaim Paulista/São Paulo', 'Itaquera/São Paulo', 'Jardim Helena/São Paulo',
							'José Bonifácio/São Paulo', 'Lajeado/São Paulo', 'Parque do Carmo/São Paulo', 'Penha/São Paulo',
							'Ponte Rasa/São Paulo', 'Sapopemba/São Paulo', 'São Lucas/São Paulo', 'São Mateus/São Paulo',
							'São Miguel/São Paulo', 'São Rafael/São Paulo', 'Tatuapé/São Paulo', 'Vila Curuçá/São Paulo',
							'Vila Formosa/São Paulo', 'Vila Jacuí/São Paulo', 'Vila Matilde/São Paulo', 'Vila Prudente/São Paulo',
							'Mooca/São Paulo', 'Brás/São Paulo', 'Pari/São Paulo', 'Água Rasa/São Paulo', 'Aricanduva/São Paulo',
							'Guaianazes/São Paulo') THEN 'Leste'
        WHEN district IN ('Cambuci/São Paulo', 'Bela Vista/São Paulo', 'Bom Retiro/São Paulo', 'Consolação/São Paulo',
							'Liberdade/São Paulo','República/São Paulo', 'Santa Cecília/São Paulo',
							'Sé/São Paulo') THEN 'Centro'
        WHEN district IN ('Campo Belo/São Paulo', 'Campo Grande/São Paulo', 'Campo Limpo/São Paulo', 'Capão Redondo/São Paulo',
							'Cidade Ademar/São Paulo', 'Cidade Dutra/São Paulo', 'Cursino/São Paulo', 'Grajaú/São Paulo',
							'Ipiranga/São Paulo', 'Jabaquara/São Paulo', 'Jardim Ângela/São Paulo', 'Moema/São Paulo',
							'Pedreira/São Paulo', 'Sacomã/São Paulo', 'Santo Amaro/São Paulo',
							'Saúde/São Paulo', 'Socorro/São Paulo', 'Vila Andrade/São Paulo', 'Vila Mariana/São Paulo',
							'Jardim São Luis/São Paulo', 'Brooklin/São Paulo') THEN 'Sul'
        WHEN district IN ('Itaim Bibi/São Paulo', 'Jardim Paulista/São Paulo', 'Pinheiros/São Paulo', 'Vila Sônia/São Paulo',
							'Alto de Pinheiros/São Paulo', 'Jaguaré/São Paulo', 'Lapa/São Paulo', 'Perdizes/São Paulo',
							'Rio Pequeno/São Paulo', 'Vila Leopoldina/São Paulo', 'Barra Funda/São Paulo', 'Raposo Tavares/São Paulo',
							'Vila Madalena/São Paulo', 'Vila Olimpia/São Paulo', 'Morumbi/São Paulo', 'Butantã/São Paulo') THEN 'Oeste'
        WHEN district IN ('Anhanguera/São Paulo', 'Brasilândia/São Paulo', 'Cachoeirinha/São Paulo', 'Freguesia do Ó/São Paulo',
							'Jaraguá/São Paulo', 'Limão/São Paulo', 'Pirituba/São Paulo', 'Tremembé/São Paulo','São Domingos/São Paulo',
							'Tucuruvi/São Paulo', 'Vila Guilherme/São Paulo', 'Vila Maria/São Paulo', 'Medeiros/São Paulo',
							'Jaçanã/São Paulo', 'Mandaqui/São Paulo', 'Santana/São Paulo', 'Casa Verde/São Paulo', 'Perus/São Paulo') THEN 'Norte'
        ELSE NULL  -- ou algum valor padrão para distritos que não estão mapeados
    END AS district_zone
FROM
    raw;
"""
SQLQuery_node1701817104205 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={"raw": AmazonS3_node1701734553332},
    transformation_ctx="SQLQuery_node1701817104205",
)

# Script generated for node Drop Duplicates
DropDuplicates_node1701736027619 = DynamicFrame.fromDF(
    SQLQuery_node1701817104205.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicates_node1701736027619",
)

# Script generated for node Drop Fields
DropFields_node1701875258244 = DropFields.apply(
    frame=DropDuplicates_node1701736027619,
    paths=["longitude", "latitude", "district"],
    transformation_ctx="DropFields_node1701875258244",
)

# Script generated for node base_venda
base_venda_node1701734649497 = Filter.apply(
    frame=DropFields_node1701875258244,
    f=lambda row: (bool(re.match("sale", row["negotiation_type"]))),
    transformation_ctx="base_venda_node1701734649497",
)

# Script generated for node base_aluguel
base_aluguel_node1701735835532 = Filter.apply(
    frame=DropFields_node1701875258244,
    f=lambda row: (bool(re.match("rent", row["negotiation_type"]))),
    transformation_ctx="base_aluguel_node1701735835532",
)

# Script generated for node base_full
base_full_node1701875168173 = glueContext.write_dynamic_frame.from_options(
    frame=DropDuplicates_node1701736027619,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://input-propriedades/processed/full/",
        "compression": "snappy",
        "partitionKeys": [],
    },
    transformation_ctx="base_full_node1701875168173",
)

# Script generated for node Amazon S3
AmazonS3_node1701734674262 = glueContext.write_dynamic_frame.from_options(
    frame=base_venda_node1701734649497,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://input-propriedades/processed/venda/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1701734674262",
)

# Script generated for node Amazon S3
AmazonS3_node1701735860777 = glueContext.write_dynamic_frame.from_options(
    frame=base_aluguel_node1701735835532,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://input-propriedades/processed/aluguel/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1701735860777",
)

job.commit()