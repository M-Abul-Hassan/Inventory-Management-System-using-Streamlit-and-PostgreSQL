import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Database configuration
db_url = "postgresql+psycopg2://postgres:12345@localhost:5432/feedback_db"
engine = create_engine(db_url)

# --- DATABASE FUNCTIONS ---

# Insert a new product
def add_product(name, qty, supplier, reorder):
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO inventory (product_name, quantity, supplier, reorder_level) VALUES (:name, :qty, :supplier, :reorder)"),
            {"name": name, "qty": qty, "supplier": supplier, "reorder": reorder}
        )
        conn.commit()

# Fetch all inventory items
def load_inventory():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM inventory ORDER BY product_name"))
        return pd.DataFrame(result.fetchall(), columns=result.keys())

# --- STREAMLIT UI ---

st.set_page_config(page_title="📦 Inventory Management System", layout="centered")
st.title("📦 Inventory Management System")

# Add product form
st.subheader("➕ Add New Product")
with st.form("add_form"):
    name = st.text_input("Product Name")
    qty = st.number_input("Quantity", min_value=0, step=1)
    supplier = st.text_input("Supplier")
    reorder = st.number_input("Reorder Level", min_value=0, step=1)
    submitted = st.form_submit_button("Add Product")

    if submitted:
        if name and supplier:
            add_product(name, qty, supplier, reorder)
            st.success(f"✅ '{name}' added successfully!")
        else:
            st.warning("⚠️ Please fill in all fields.")

st.write("---")

# View inventory
st.subheader("📋 Current Inventory")
df = load_inventory()

if not df.empty:
    st.dataframe(df)
else:
    st.info("📭 Inventory is currently empty.")
