# 🎶 Workshop 2: ETL Process Using Airflow 🎧

## 📝 Introduction
Welcome to **Workshop 2**, where we explore how to build an **ETL pipeline** using **Apache Airflow**. The goal is to extract information from multiple data sources (CSV files, APIs, and databases), transform it, and load it into a **PostgreSQL** database. Finally, we visualize the processed data using **Power BI**. 

Throughout this workshop, you'll learn how to manage data efficiently and create impressive visualizations. 

---

## 🚀 Getting Started

In this workshop, you'll use the **Spotify Tracks Dataset** and the **Grammy Awards Dataset**. Here's a quick overview of the process:

1. **Extract**:
   - Read data from a **CSV file** (Spotify dataset).
   - Load data into a **PostgreSQL database** (Grammy Awards dataset).
   - Optionally, pull data from an API (if desired).
   
2. **Transform**:
   - Merge the **Spotify dataset** with the **Grammy Awards** data.
   - Perform necessary transformations (e.g., cleaning, filtering, merging).

3. **Load**:
   - Load the transformed data back into the **PostgreSQL** database.
   - Optionally, export the final dataset to a **CSV file** for external use.

4. **Visualize**:
   - Create charts and dashboards using **Power BI** to gain insights from the merged data.

---

## 📊 What is Expected

You are expected to:
- Build a complete **ETL pipeline** using **Apache Airflow** to extract, transform, and load data.
- Store the processed data in a **PostgreSQL database**.
- Use **Power BI** to create meaningful visualizations.
- Ensure that your data visualizations are based on the data stored in the database, not directly from the CSV files.

---

## 🛠️ Technologies Used

This project leverages the following technologies:

- **Python** 🐍
- **Jupyter Notebook** 📓
- **Apache Airflow** 🌬️
- **PostgreSQL** 🐘 (via **Docker**)
- **CSV files** 📑
- **Power BI** 📊 (for data visualizations)

---

## 📂 Data Sources

Here are the datasets used in this project:

- **🎹 Spotify Tracks Dataset**: A dataset of Spotify songs with different genres and their audio features.
  - [Spotify Tracks Dataset on Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)

- **🏆 Grammy Awards Dataset**: Grammy Awards data from 1958 to 2019.
  - [Grammy Awards Dataset on Kaggle](https://www.kaggle.com/datasets/unanimad/grammy-awards)

---

## 🔄 ETL Pipeline Process

The following figure represents a high-level overview of the ETL pipeline:

1. **Extract**: 
   - Read data from the **Spotify Tracks CSV**.
   - Load the **Grammy Awards Dataset** into the **PostgreSQL** database.

2. **Transform**:
   - Merge both datasets based on relevant columns (e.g., `artist_name` from Spotify with `artist` from Grammy).
   - Filter the data to include only **Grammy winners**.

3. **Load**:
   - Load the transformed data into a **PostgreSQL table**.
   - Export the final dataset as a **CSV file** (optional).

4. **Visualize**:
   - Use **Power BI** to create interactive dashboards showcasing the key insights from the merged dataset.

---

## ⚙️ Setup Instructions

To get the project up and running on your machine, follow these steps:

### Prerequisites
- **Docker** 🐳 (for running PostgreSQL and Airflow)
- **Python** and **Pandas**
- **Power BI** (for visualizations)
  
### 1. Clone the Repository
```bash
git clone https://github.com/Johan901/workshop-002.git
cd workshop-002
```

### 2. Set Up Docker and PostgreSQL
Make sure you have **Docker** installed. Use the provided `docker-compose.yml` to spin up the necessary services (PostgreSQL, Airflow):

```bash
docker-compose up -d
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the ETL Pipeline in Airflow
```bash
Access Airflow via the browser at http://localhost:8090
```
### 5. Visualize with Power BI
Load the processed data from PostgreSQL into Power BI and create interactive dashboards.

## 📊 Visualizations
Using **Power BI**, we can create insightful visualizations such as:

- **Top Spotify Artists by Grammy Wins** 🏆
- **Audio Features of Grammy-Winning Tracks** 🎧
- **Trends Over Time in Grammy Awards and Popularity** 📈

These visualizations help showcase key insights from the merged Spotify and Grammy datasets.

---

## 💾 Final Output
The final dataset is stored in:

- **PostgreSQL database**: A table called `final_data` containing the merged data.
- Optionally, a **CSV file**: The merged data is also exported as a CSV file.

---

## 🌟 Conclusion
In this workshop, you built a complete ETL pipeline using **Apache Airflow** to extract, transform, and load data from multiple sources. You also used **PostgreSQL** to store the processed data and **Power BI** to visualize the results, showcasing your ability to manage and present data effectively.

---

## 🔗 Useful Links
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)

---

**Workshop 2: ETL Process Using Airflow** 💻🚀 | Made with 💙 by [Johan Hurtado Enríquez](https://github.com/Johan901) 👨‍💻
