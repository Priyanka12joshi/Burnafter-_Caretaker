# Add these lines to ensure Python can find the db folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the db module
import streamlit as st
from db.db import Session, Intake, pathlib, uuid

st.title("Burn Aftercare Plan – Patient Intake")

with st.form("patient_form"):
    age = st.number_input("Age", 0, 120, step=1)
    burn_area = st.text_input("Burn area / location")
    severity = st.selectbox("Severity", ["Superficial", "Partial-thickness", "Full-thickness"])
    comorbidities = st.text_area("Comorbidities (e.g., diabetes, COPD)")
    symptoms = st.text_area("Current symptoms / pain level")
    photo = st.file_uploader("Optional wound photo", type=["jpg", "png"])

    submitted = st.form_submit_button("Generate Plan")

if submitted:
    # Save patient data and optional photo to database
    session = Session()

    photo_path = None
    if photo:
        path = pathlib.Path("photos")
        path.mkdir(exist_ok=True)
        photo_path = path / f"{uuid.uuid4()}.png"
        photo_path.write_bytes(photo.read())

    # Store the data in the database
    row = Intake(
        id=str(uuid.uuid4()), age=age, area=burn_area,
        severity=severity, comorbidities=comorbidities,
        symptoms=symptoms, photo_path=str(photo_path)
    )
    session.add(row)
    session.commit()

    st.success(f"Saved! Record ID {row.id}")
