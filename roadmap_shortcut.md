# First part: Basics

## Basic Linux/Bash commands
You need to be comfortable with the terminal and able to write some basic commands such as:

- ls; 
- mkdir; 
- cd; 
- touch; 
- chmod; 
- ssh; 
- And many more.

## SQL knowledge and Data modeling

What you need to master:

Constraints
CTEs
Window functions
Group by
Join
Normalization
Star schema
Snowflake schema

### Project 1

Pick a dataset on Kaggle, upload it to PostgreSQL, and answer some questions by querying it.

## Programming language: pick Python

Pandas, Polars: to manipulate data
SQLAlchemy: to interact with a database
Requests: to pull data from APIs
Logging
Pytest: for testing

### Project 2

Instead of manually uploading the dataset to PostgreSQL, use Python to apply some transformations, build the data model, and ingest the dataset into PostgreSQL. Then perform some queries.

## Docker

Now, you need to understand how to package your code with its dependencies so that you can easily move it from your local machine to another machine, without having the “it works on my machine” issue.

You need to understand Docker Image, Docker container, Volume, Networks.

Don’t go too deep; you just need some basic knowledge to get started.

### Project 3

Do you remember the first two projects? Now try to containerize your code and PostgreSQL instance.

## Intermediate

Job orchestration, scheduling: Airflow
Imagine you have many tasks that need to run: let’s say you pull data using Python from CSV files, APIs, apply some transformations, and load into a database/data warehouse, etc.

You need something that can orchestrate the whole process and dictate what needs to be run before what.

Learn about Airflow, and you can pick up a managed service like Astronomer.

### Project 4

Use Airflow on Project 3 to orchestrate the data ingestion and transformation.

Distributed systems: Spark, Snowflake, BigQuery
Imagine instead of simple CSV files, you need to work with TBs of data.

Here is where distributed systems come into place. Learn about it and for tools here is my advice:

DON’T LEARN THE THREE

In this part, you have to pick up a set of tools that you will use in your journey:

Spark: if you are more comfortable with Python. With Spark, you can also learn Databricks and Delta Lake.
Snowflake+dbt+DuckDB: if you like the SQL approach, pick these three and stick with it.
Cloud provider: AWS, GCP, Azure

### Project 5

Build a data pipeline that can be triggered with a simple UI (like Airflow) that takes some data from a data lake, transforms it to build a good model (with Spark or DBT+DuckDB), and loads back to the data lake in Delta format/or in a data warehouse like Snowflake or BigQuery.


## Advanced: Real-time streaming

This part is optional because in most cases, it is more worthwhile to concentrate all your effort on batch data pipelines or real-time pipelines, but not both at the same time. And most jobs today don’t require streaming knowledge.

This is more for advanced concepts. Here you need to focus on:

1. Kafka
2. Apache Flink

### Bonus:
Now you can add another tool to your toolkit: IaC (Infrastructure as Code). Pick up Terraform.