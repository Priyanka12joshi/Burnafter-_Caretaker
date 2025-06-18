from db.db import Session, Intake

# Create a session to interact with the database
session = Session()

# Query all the rows from the 'intakes' table
records = session.query(Intake).all()

# Check if there are any records
if records:
    for record in records:
        # Print the saved data for each record
        print(f"ID: {record.id}")
        print(f"Timestamp: {record.ts}")
        print(f"Age: {record.age}")
        print(f"Burn Area/Location: {record.area}")
        print(f"Severity: {record.severity}")
        print(f"Comorbidities: {record.comorbidities}")
        print(f"Symptoms: {record.symptoms}")
        print(f"Photo Path: {record.photo_path}")
        print("-" * 50)  # Just a separator for readability
else:
    print("No records found.")

# Close the session
session.close()
