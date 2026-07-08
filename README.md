# Supply-Chain-Inventory-Optimization-BigQuery
Data-driven inventory optimization project that utilizes cloud SQL analytics and Python to isolate stockout risks and capital inefficiencies in a supply chain framework.

# 📦 Supply Chain Optimization: Data-Driven Inventory Health Diagnosis

## 📌 Project Overview
This project focuses on transitioning macro-level sales data into actionable operational intelligence. Utilizing **SQL (Google BigQuery)** for data engineering and **Python (Pandas & Matplotlib)** for analytical processing and visualization, we diagnosed structural imbalances within the corporate inventory framework. 

Rather than relying on generic averages, this analysis applies specific supply chain logic to isolate financial risks associated with **Stockouts (Understock)** and **Capital Tied Up (Overstock)** across three primary product segments: Skincare, Haircare, and Cosmetics.

---

## 🛠️ Data Infrastructure & Pipeline
* **Data Warehouse:** Google BigQuery (Cloud Environment)
* **Processing Engine:** Python 3.13 within a dedicated virtual environment (`demo`)
* **Key Libraries:** `google-cloud-bigquery`, `pandas`, `matplotlib`, `pyarrow`, `db-dtypes`

---

## 📈 Analytical Breakdown & Table Interpretations

### 1. Commercial Performance & Revenue Aggregation (Macro View)
The initial phase required cleaning database fields (handling space-to-underscore conversions) and executing a baseline revenue performance query.

| Product Type | Average Price | Total Availability | Total Products Sold | Total Revenue ($) |
| :--- | :---: | :---: | :---: | :---: |
| **Skincare** | $55.88 | 1799 | 20731 | $388,717.93 |
| **Cosmetics** | $57.37 | 1515 | 11757 | $224,119.10 |
| **Haircare** | $55.16 | 1347 | 13611 | $174,455.39 |

* **Supply Chain Insight:** At a macro level, **Skincare** is the clear cash cow of the business, generating nearly **50% of total revenue**. However, aggregating data at this level creates a dangerous blind spot: high sales figures frequently mask severe underlying fulfillment and replenishment bottlenecks.

---

### 2. Operational Bottleneck & Lead Time Analysis
To bridge the gap between sales and operations, we evaluated the relationship between production volumes, manufacturing Lead Times, and available stock ratios.

* **Supply Chain Insight:** The analysis revealed that long **Production Lead Times** force operational managers into "panic ordering" behaviors. When lead times are volatile, companies artificially inflate their production volumes to prevent stockouts, inadvertently triggering localized overstocking while failing to secure a stable supply for high-turnover goods.

---

### 3. Inventory Health Matrix (The Core BI Asset)
To unlock true business value, we developed a portable SQL logical routing mechanism (`SUM(CASE WHEN)`) to categorize every single SKU into one of three operational states:
1.  **Understock Risk:** $Stock\ Levels < Order\ Quantities$ (Immediate threat of lost sales).
2.  **Overstock:** $Stock\ Levels > (Products\ Sold \times 1.5)$ (Tied-up capital and inflated holding costs).
3.  **Healthy:** Balanced inventory buffer.

#### **Distribution of Inventory States by Category**
* **Skincare:** 26 SKUs under Risk | 14 Healthy | 0 Overstock
* **Haircare:** 15 SKUs under Risk | 18 Healthy | 1 Overstock
* **Cosmetics:** 13 SKUs under Risk | 13 Healthy | 0 Overstock

### 🔍 Strategic BI Conclusions
The diagnostic matrix completely refutes the initial assumption of a generalized overstock issue. Instead, the business faces a systemic **Understock Crisis**:

* **The Skincare Vulnerability:** A staggering **65% of the Skincare catalog (26 out of 40 SKUs)** is operating under severe stockout risk. Because Skincare is our primary revenue driver, failing to fulfill demand directly impacts corporate EBITDA and compromises customer retention.
* **The Haircare Variance:** Haircare exhibits a highly volatile distribution. It contains the only literal instance of overstock in the dataset, yet simultaneously leaves **44% of its catalog unprotected** against desupply. This indicates a profound failure in SKU-level forecasting accuracy.
* **Cosmetics Imbalance:** Operating at a flat 50/50 split between healthy and at-risk stock, this segment requires immediate baseline replenishment adjustments before fulfillment rates decay.

---

## 🚀 Actionable Recommendations for Executive Management
1.  **Deploy Dynamic Safety Stock:** Transition away from static ordering patterns. Implement an automated Safety Stock formula that factors in the real variance of **Lead Times** specifically for the 26 critical Skincare SKUs.
2.  **Capital Realignment:** Liquidate the excess holding capital identified in the stagnant Haircare SKU and reallocate that budget to fund the immediate replenishment of high-turnover Understock items.
3.  **Supplier SLA Enforcement:** Negotiate strict Lead Time windows with suppliers. Every day reduced in manufacturing wait times directly lowers the required inventory buffer, freeing up corporate cash flow.
