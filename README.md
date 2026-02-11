# Yelp Data Engineering Pipeline: S3 to Snowflake

## Project Overview
This project demonstrates a scalable data engineering pipeline designed to handle large-scale semi-structured data. I processed a **10GB Yelp Academic Dataset**, optimized it for cloud storage, and ingested it into **Snowflake** for high-performance analytical querying.

## Architecture
1.  **Data Processing:** Python script to partition a monolithic 10GB JSON file into 500MB chunks to bypass S3 upload limits and optimize Snowflake parallel loading.
2.  **Storage:** AWS S3 used as a Data Lake for staging raw JSON files.
3.  **Data Warehouse:** Snowflake configured with an External Stage and Storage Integration for secure data ingestion.
4.  **Analytics:** SQL transformation and querying of semi-structured (JSON) data.

## Tech Stack
* **Languages:** Python (Data Chunking), SQL (Data Transformation)
* **Cloud:** AWS S3
* **Data Warehouse:** Snowflake
* **Dataset:** Yelp Academic Dataset (JSON)

## How to Run
1.  **Split Data:** Run `python scripts/split_data.py` to prepare the files.
2.  **Upload to S3:** Upload the generated chunks to your AWS S3 bucket.
3.  **Snowflake Setup:** Execute the scripts in `snowflake_sql/setup_stage.sql` to connect Snowflake to your S3 bucket.
4.  **Ingest Data:** Use the `COPY INTO` command to load data into Snowflake tables.

## Key Learnings
* Managing large file uploads to cloud environments.
* Configuring secure IAM policies for Snowflake-S3 communication.
* Parsing nested JSON objects in Snowflake using `FLATTEN` and colon notation.
