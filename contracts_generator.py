import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_contract_pdf(client_name, chosen_service, agreed_price):
    # Define the final file name (e.g., Contract_Mario_Rossi.pdf)
    file_name = f"Contract_{client_name.replace(' ', '_')}.pdf"
    
    # Initialize the PDF page
    pdf = canvas.Canvas(file_name, pagesize=letter)
    pdf.setTitle(f"Contract - {client_name}")
    
    # Write the standard contract text (using X and Y coordinates)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(100, 700, "STANDARD SERVICE PRESTATION CONTRACT")
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 650, "By means of this agreement, it is mutually agreed as follows:")
    pdf.drawString(100, 620, f"Between the undersigned Professional and the Client: {client_name}")
    
    pdf.drawString(100, 580, "1. Scope of Work: The professional agrees to perform the following")
    pdf.drawString(100, 560, f"   service: '{chosen_service}' for the benefit of the Client.")
    
    pdf.drawString(100, 520, "2. Compensation: For the services listed above, the Client shall pay")
    pdf.drawString(100, 500, f"   a total amount of {agreed_price} USD.")
    
    # Signature fields at the bottom
    pdf.drawString(100, 300, "Professional Signature: ______________________")
    pdf.drawString(100, 250, "Client Signature: ___________________________")
    
    # Close and save the PDF file
    pdf.save()
    print(f"Successfully created: {file_name}")

def start_automation():
    excel_file = "client_data.xlsx"
    
    # Safety check: verify if the Excel file actually exists
    if not os.path.exists(excel_file):
        print(f"Error: Could not find the file '{excel_file}' in this folder!")
        return
        
    # Read the Excel file using Pandas
    df = pd.read_excel(excel_file)
    
    print(f"Found {len(df)} rows in Excel. Starting contract generation...")
    
    # Loop through each row of the Excel sheet to extract data
    for index, row in df.iterrows():
        # Get data from the columns
        name = row['name']
        service = row['service']
        price = row['price']
        
        # Generate the specific PDF for this row
        create_contract_pdf(name, service, price)
        
    print("Process completed! Check your folder.")

# Tells Python to run the script
if __name__ == "__main__":
    start_automation()