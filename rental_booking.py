import streamlit as st
from datetime import date

# --- CONFIGURATION ---
st.set_page_config(page_title="Hiab Rental Booking", layout="centered")

# --- DATA: Your Truck Inventory ---
# In a real app, this would come from a database (like AWS DynamoDB or SQL)
TRUCK_INVENTORY = {
    "Hiab 1: Small Lifter": {
        "model": "Hiab X-HiDuo 138",
        "reach": "10.6 meters",
        "lift_capacity": "3,800 kg",
        "daily_rate": 350,
        "image_url": "https://placehold.co/600x400?text=Small+Hiab+Truck"
    },
    "Hiab 2: Mid-Range Master": {
        "model": "Hiab X-HiPro 232",
        "reach": "15.1 meters",
        "lift_capacity": "5,600 kg",
        "daily_rate": 550,
        "image_url": "https://placehold.co/600x400?text=Medium+Hiab+Truck"
    },
    "Hiab 3: Heavy Lifter": {
        "model": "Hiab iX.2988",
        "reach": "22.0 meters",
        "lift_capacity": "10,000 kg",
        "daily_rate": 800,
        "image_url": "https://placehold.co/600x400?text=Heavy+Hiab+Truck"
    }
}

# --- SIDEBAR: Company Info ---
with st.sidebar:
    st.header("🏗️ Hiab Rentals Co.")
    st.write("Specialized lifting solutions for your site.")
    st.info("📞 Call us: +65 1234 5678")
    st.write("---")
    st.write("### Services")
    st.checkbox("Machine Moving", value=True, disabled=True)
    st.checkbox("Container Lifting", value=True, disabled=True)
    st.checkbox("Site Surveys", value=True, disabled=True)

# --- MAIN PAGE ---
st.title("🚛 Book a Hiab Truck")
st.write("Select a truck, check the specs, and request a quote instantly.")

# 1. Select Truck
st.subheader("1. Choose Your Equipment")
selected_truck_name = st.selectbox("Select Truck Model", list(TRUCK_INVENTORY.keys()))
truck = TRUCK_INVENTORY[selected_truck_name]

# Display Truck Details in Columns
col1, col2 = st.columns([1, 1])

with col1:
    st.image(truck["image_url"], caption=truck["model"])

with col2:
    st.markdown(f"**Model:** {truck['model']}")
    st.markdown(f"**Max Reach:** {truck['reach']}")
    st.markdown(f"**Max Lift:** {truck['lift_capacity']}")
    st.markdown(f"**Rate:** ${truck['daily_rate']} / day")
    
    # Simple Load Chart Logic (Visual warning)
    st.warning(f"⚠️ Note: Capacity drops as reach extends. Max lift at full reach is approx 20% of max capacity.")

st.divider()

# 2. Booking Details
st.subheader("2. Job Details")

with st.form("booking_form"):
    c1, c2 = st.columns(2)
    with c1:
        client_name = st.text_input("Your Name / Company")
        start_date = st.date_input("Start Date", min_value=date.today())
    with c2:
        contact_email = st.text_input("Email Address")
        duration = st.number_input("Rental Duration (Days)", min_value=1, value=1)

    location = st.text_area("Job Site Location & Access Details")
    
    # Calculate Total
    total_cost = truck["daily_rate"] * duration
    st.write(f"### Estimated Total: ${total_cost}")

    # Submit Button
    submitted = st.form_submit_button("Request Booking")

    if submitted:
        if not client_name or not contact_email:
            st.error("Please fill in your name and email.")
        else:
            # Here is where you would connect to AWS SES to send an email
            # or save to a database. For now, we simulate it.
            st.success(f"✅ Request Sent! We have received your booking for the {truck['model']}.")
            st.json({
                "Client": client_name,
                "Truck": truck['model'],
                "Days": duration,
                "Total Estimate": f"${total_cost}",
                "Status": "Pending Approval"
            })