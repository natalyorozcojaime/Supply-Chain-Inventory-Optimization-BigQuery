# 📦 BigQuery Supply Chain: Inventory Optimization & Safety Stock Analytics

[![BigQuery](https://img.shields.io/badge/Google_BigQuery-SQL-4285F4?style=flat&logo=googlecloud&logoColor=white)](https://cloud.google.com/bigquery)
[![Analytics](https://img.shields.io/badge/Domain-Supply_Chain_Analytics-008080?style=flat)](https://github.com/natalyorozcojaime)
[![Status](https://img.shields.io/badge/Project_Status-Production_Ready-brightgreen?style=flat)](#)

## 📌 Executive Summary & Business Problem

In global supply chains, stockouts lead to immediate revenue loss, while overstocking ties up working capital and increases holding costs. Standard inventory management models often fail to adjust dynamically to fluctuations in demand and lead-time variability across diverse product lines.

This project delivers an **end-to-end BigQuery SQL pipeline** designed to optimize stock levels, automate ABC inventory classification, and dynamically calculate **Safety Stock ($SS$)** and **Reorder Points ($ROP$)**. 

By querying raw transaction logs and inventory tables directly in the cloud, this framework reduces manual reporting overhead, identifies high-risk SKU bottlenecks, and optimizes inventory holding costs.

---

## 🛠️ Data Architecture & Tech Stack

```text
[ Raw Sales & Logistics Data ] 
              │
              ▼
    [ Google Cloud Storage ] 
              │
              ▼
     [ Google BigQuery ] ──(SQL Window Functions & CTEs)──► [ Inventory Optimization Engine ]
                                                                        │
                                                                        ▼
                                                                  [ Power BI ]
