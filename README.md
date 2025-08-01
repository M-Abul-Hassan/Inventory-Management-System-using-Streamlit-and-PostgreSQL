
# 🧾 Inventory Management System using Streamlit and PostgreSQL

This is a simple and interactive Inventory Management System built using **Streamlit** for the frontend and **PostgreSQL** (accessed via **PgAdmin 4**) for data storage. It allows users to add, view, and manage product inventory including details like product name, quantity, supplier, and reorder level.

---

## 📦 Features

- Add new inventory items
- Display inventory in a tabular format
- User-friendly UI with Streamlit
- PostgreSQL database integration
- Auto-refreshing inventory list
- Error-handling and input validation

---

## 🛠 Tech Stack

- Python 🐍
- Streamlit 📊
- PostgreSQL 🐘
- SQLAlchemy & Psycopg2 🔗

---

## 💾 Database Configuration
We will open the PgAdmin4, connect the server by putting password, after that database dashboard will be shown, we will create the database and its table by using SQL-Query.
### 🔸 Database Name: `feedback_db`  
### 🔸 Table Name: `inventory`

### 🧱 Table Structure (SQL Query)
```sql
CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INTEGER,
    supplier VARCHAR(100),
    reorder_level INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

