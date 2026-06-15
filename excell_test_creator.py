import pandas as pd
import random

# Mock lists to generate random english names, services, and prices
first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "David", "Emma", "Robert", "Olivia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]
services = ["Financial Consulting", "AI Software Development", "Social Media Marketing", "Logo Design", "Tax Auditing"]

data = []

# Generate 50 rows of mock data
for i in range(50):
    full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    service = random.choice(services)
    price = random.randint(500, 3500)
    
    data.append({
        "name": full_name,
        "service": service,
        "price": price
    })

# Convert list to Pandas DataFrame
df_test = pd.DataFrame(data)

# Save the Excel file
df_test.to_excel("client_data.xlsx", index=False)

print("File 'client_data.xlsx' with 50 mock clients generated successfully!")