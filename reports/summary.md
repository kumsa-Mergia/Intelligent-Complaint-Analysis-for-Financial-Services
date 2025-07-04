# 📊 Task 1 Summary – EDA & Preprocessing

## 🗂️ Dataset Overview

I explored the **Consumer Financial Protection Bureau (CFPB)** complaint dataset, which contains **9+ million** consumer complaints. Each record includes:

- A `Product` category describing the type of financial product.
- A `Consumer complaint narrative` field with free-text descriptions of consumer issues.

---

## 🔍 Key Findings

### 1️⃣ Distribution of Complaints by Product

Complaint volume is heavily concentrated in a few categories:

- 🥇 **Credit reporting / Personal consumer reports**: \~4.8 million complaints
- 🥈 **Debt collection** and 🥉 **Mortgage** also represent large volumes
- 📉 Categories I focused on—**Credit card**, **Personal loan**, **Buy Now, Pay Later**, **Savings account**, and **Money transfers**—make up a smaller but meaningful subset

---

### 2️⃣ Narrative Availability

| Type                          | Count     |
| ----------------------------- | --------- |
| Complaints with narratives    | 2,980,756 |
| Complaints without narratives | 6,629,041 |

⚠️ **\~75% of the dataset lacks consumer-written narratives**, so these were excluded from further analysis.

---

### 3️⃣ Narrative Word Count Distribution

- 📝 Most narratives contain **20–200 words**
- 🧵 A small number exceed **1000 words**
- 📐 This supports the need for **chunking** during the embedding stage to handle long entries effectively

---

## 🧹 Data Filtering & Preprocessing

To prepare the dataset for embedding and modeling, I performed the following steps:

1. **Filtered** the dataset to include only the following product categories:

   - 💳 Credit card
   - 💸 Personal loan
   - 🛍️ Buy Now, Pay Later
   - 🏦 Savings account
   - 🌐 Money transfers

2. **Removed** complaints without a narrative

3. **Cleaned** the text by:

   - Lowercasing
   - Removing special characters and noise

📁 **Output file saved at:**
`data/processed/filtered_complaints.csv`
