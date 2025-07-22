# 📋 Project Overview: “Burn Aftercare Plan – Patient Intake”
The app is a Streamlit-based intake form for burn patients that captures essential clinical and personal information:

Inputs captured: age, burn area/location, severity (superficial/partial/full‑thickness), comorbidities, symptoms/pain level, and an optional wound photo.

On submission, the data is saved to:

A SQLite database (intake.db) using SQLAlchemy, with an Intake model that stores id, timestamp, age, burn area, severity, comorbidities, symptoms, and photo path.

Any uploaded photo is saved locally under a photos/ folder with a UUID-named PNG.

This setup enables you to record and persist structured patient intake data for future consultation or processing.

# 🛠️ How It Works (Simplified)
Streamlit UI: Presents an input form inside st.form() with validation controls.

Data Processing:

On click of Generate Plan, inputs are gathered.

The app saves data to intake.db via SQLAlchemy session.

Uploaded photo is saved to disk.

Backend:
**
Defines Intake as a SQLAlchemy model using SQLite**.

Uses Session() to insert and commit patient intake rows.

Optionally, separate script can query and print saved records.

# 🌟 Strengths & Capabilities
MVC-style separation: UI (Streamlit) and DB (SQLAlchemy) are cleanly decoupled.

UUID-based IDs/file names to avoid collisions.

Photo support, stored alongside structured intake data.

Portable SQLite backend—works locally or can be later scaled to cloud databases.

# 🔗 Context & Similar Solutions
University teams (e.g., Vanderbilt’s BurnCARE app) use neural networks and photos to assess burn wound severity for fluid resuscitation and treatment planning 
sciencedirect.com
bmcnurs.biomedcentral.com
engineering.vanderbilt.edu
.

Other projects, like smartphone/cloud-consult tools, enable sharing wound data from point-of-care to specialists 
journals.plos.org
.

Nurse-led aftercare programs collect structured patient intake data, conduct follow-ups, and track recovery 
bmcnurs.biomedcentral.com
.

Your tool aligns with these in terms of:

Data capture using forms + optional images.

Structured storage for later review or remote clinical workflows.

Being a foundational layer that can be extended with analytics, follow-ups, or machine learning.

# 🚀 Potential Next Steps
To bring this project further:

Generate care plans dynamically based on input—e.g., prescribing steps based on severity/comorbidities.

Add follow-up workflows: track symptom changes over time.

Integrate image analysis models to classify wound severity automatically (using ML).

Deploy on cloud or Heroku, and switch SQLite backend to a cloud database (PostgreSQL/MySQL).

Build data dashboards for clinicians to review intake logs visually.

Let me know if you'd like help extending this with ML, interactive dashboards, deployment, or remote care integration!
