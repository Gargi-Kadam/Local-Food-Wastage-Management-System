# ============================
#  Streamlit App - With Add Provider & Receiver
# ============================

import streamlit as st
import pandas as pd
import sqlite3
import os

# ============================
# Database Setup
# ============================
DB_PATH = "food_wastage.db"

# Reset DB each time (for dev/demo)
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Match CSV schemas
c.execute('''CREATE TABLE IF NOT EXISTS providers
             (Provider_ID INTEGER PRIMARY KEY, Name TEXT, Type TEXT, City TEXT, Contact TEXT, Address TEXT, Provider_Type TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS receivers
             (Receiver_ID INTEGER PRIMARY KEY, Name TEXT, Type TEXT, City TEXT, Contact TEXT, Address TEXT, Receiver_Type TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS food_listings
             (Food_ID INTEGER PRIMARY KEY, Food_Name TEXT, Quantity INTEGER, Expiry_Date TEXT, Provider_ID INTEGER, Provider_Type TEXT, Location TEXT, Food_Type TEXT, Meal_Type TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS claims
             (Claim_ID INTEGER PRIMARY KEY, Food_ID INTEGER, Receiver_ID INTEGER, Status TEXT, Timestamp TEXT)''')

conn.commit()

# ============================
# Load CSVs into DB
# ============================
def load_csv_to_db(table_name, csv_file):
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        df.to_sql(table_name, conn, if_exists="replace", index=False)  # overwrite to match schema

load_csv_to_db("providers", "../Data/providers_data.csv")
load_csv_to_db("receivers", "../Data/receivers_data.csv")
load_csv_to_db("food_listings", "../Data/food_listings_data.csv")
load_csv_to_db("claims", "../Data/claims_data.csv")

# ============================
# Streamlit UI
# ============================
st.title("🍲 Local Food Wastage Management System")

menu = ["View Data", "Add Provider", "Add Receiver", "Add Food Listing", "Search", "Analysis"]
choice = st.sidebar.selectbox("Menu", menu)

# ----------------- View Data -----------------
if choice == "View Data":
    st.subheader("Providers Data")
    st.dataframe(pd.read_sql("SELECT * FROM providers", conn))

    st.subheader("Receivers Data")
    st.dataframe(pd.read_sql("SELECT * FROM receivers", conn))

    st.subheader("Food Listings Data")
    st.dataframe(pd.read_sql("SELECT * FROM food_listings", conn))

    st.subheader("Claims Data")
    st.dataframe(pd.read_sql("SELECT * FROM claims", conn))

# ----------------- Add Provider -----------------
elif choice == "Add Provider":
    st.subheader("Add Provider")
    with st.form("add_provider"):
        pid = st.number_input("Provider ID", step=1)
        name = st.text_input("Name")
        ptype = st.text_input("Type (e.g., Restaurant, NGO)")
        city = st.text_input("City")
        contact = st.text_input("Contact")
        address = st.text_area("Address")
        prov_type = st.selectbox("Provider Type", ["Individual", "Organization"])
        submitted = st.form_submit_button("Add Provider")

        if submitted:
            c.execute("INSERT INTO providers VALUES (?,?,?,?,?,?,?)",
                      (pid, name, ptype, city, contact, address, prov_type))
            conn.commit()
            st.success("✅ Provider added successfully!")

# ----------------- Add Receiver -----------------
elif choice == "Add Receiver":
    st.subheader("Add Receiver")
    with st.form("add_receiver"):
        rid = st.number_input("Receiver ID", step=1)
        name = st.text_input("Name")
        rtype = st.text_input("Type (e.g., Shelter, NGO)")
        city = st.text_input("City")
        contact = st.text_input("Contact")
        address = st.text_area("Address")
        recv_type = st.selectbox("Receiver Type", ["Individual", "Organization"])
        submitted = st.form_submit_button("Add Receiver")

        if submitted:
            c.execute("INSERT INTO receivers VALUES (?,?,?,?,?,?,?)",
                      (rid, name, rtype, city, contact, address, recv_type))
            conn.commit()
            st.success("✅ Receiver added successfully!")

# ----------------- Add Food Listing -----------------
elif choice == "Add Food Listing":
    st.subheader("Add Food Listing")
    with st.form("add_food"):
        food_id = st.number_input("Food ID", step=1)
        food_name = st.text_input("Food Name")
        qty = st.number_input("Quantity", step=1)
        expiry = st.date_input("Expiry Date")
        provider_id = st.number_input("Provider ID", step=1)
        provider_type = st.text_input("Provider Type")
        city = st.text_input("City")
        food_type = st.selectbox("Food Type", ["Vegetarian", "Non-Vegetarian", "Vegan"])
        meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snacks"])
        submitted = st.form_submit_button("Add Food")

        if submitted:
            c.execute("INSERT INTO food_listings VALUES (?,?,?,?,?,?,?,?,?)",
                      (food_id, food_name, qty, str(expiry), provider_id, provider_type, city, food_type, meal_type))
            conn.commit()
            st.success("✅ Food record added successfully!")

# ----------------- Search -----------------
elif choice == "Search":
    st.subheader("Search Food Listings by City")
    city = st.text_input("Enter City")
    if st.button("Search"):
        result = pd.read_sql(f"SELECT * FROM food_listings WHERE Location='{city}'", conn)
        st.dataframe(result)

# ----------------- Analysis -----------------
elif choice == "Analysis":
    st.subheader("📊 Food Listings by Type")
    df = pd.read_sql("SELECT Food_Type, COUNT(*) as count FROM food_listings GROUP BY Food_Type", conn)
    st.bar_chart(df.set_index("Food_Type"))
