import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs
import re

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

# Script generated for node Drop Duplicates
DropDuplicates_node1701736027619 = DynamicFrame.fromDF(
    AmazonS3_node1701734553332.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicates_node1701736027619",
)

# Script generated for node base_venda
base_venda_node1701734649497 = Filter.apply(
    frame=DropDuplicates_node1701736027619,
    f=lambda row: (bool(re.match("sale", row["negotiation_type"]))),
    transformation_ctx="base_venda_node1701734649497",
)

# Script generated for node base_aluguel
base_aluguel_node1701735835532 = Filter.apply(
    frame=DropDuplicates_node1701736027619,
    f=lambda row: (bool(re.match("rent", row["negotiation_type"]))),
    transformation_ctx="base_aluguel_node1701735835532",
)

# Script generated for node Amazon S3
AmazonS3_node1701734674262 = glueContext.getSink(
    path="s3://input-propriedades/processed/venda/",
    connection_type="s3",
    updateBehavior="LOG",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1701734674262",
)
AmazonS3_node1701734674262.setCatalogInfo(
    catalogDatabase="propriedades", catalogTableName="venda"
)
AmazonS3_node1701734674262.setFormat("csv")
AmazonS3_node1701734674262.writeFrame(base_venda_node1701734649497)
# Script generated for node Amazon S3
AmazonS3_node1701735860777 = glueContext.getSink(
    path="s3://input-propriedades/processed/aluguel/",
    connection_type="s3",
    updateBehavior="LOG",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1701735860777",
)
AmazonS3_node1701735860777.setCatalogInfo(
    catalogDatabase="propriedades", catalogTableName="aluguel"
)
AmazonS3_node1701735860777.setFormat("csv")
AmazonS3_node1701735860777.writeFrame(base_aluguel_node1701735835532)
job.commit()