import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_contract_pdf(client_name, chosen_service, agreed_price):
    file_name = f"Contract_{client_name.replace(' ', '_')}.pdf"
    
    # 1. Read the external template file
    template_file = "contract_template.txt"
    if not os.path.exists(template_file):
        print(f"Error: Template file '{template_file}' missing!")
        return
        
    with open(template_file, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 2. Replace the placeholders with actual client data
    content = content.replace("[CLIENT_NAME]", client_name)
    content = content.replace("[SERVICE]", chosen_service)
    content = content.replace("[PRICE]", str(agreed_price))
    
    # 3. Initialize the PDF page
    pdf = canvas.Canvas(file_name, pagesize=letter)
    pdf.setTitle(f"Contract - {client_name}")
    
    # 4. Draw the content line by line on the PDF
    y_position = 700  # Starting high on the page
    lines = content.split("\n")
    
    for line in lines:
        # Simple formatting: make the first line bold and bigger (Title)
        if y_position == 700:
            pdf.setFont("Helvetica-Bold", 18)
            pdf.drawString(100, y_position, line)
            y_position -= 40  # Leave extra space after title
        else:
            pdf.setFont("Helvetica", 12)
            pdf.drawString(100, y_position, line)
            y_position -= 22  # Move down for the next line
            
    # Save the PDF file
    pdf.save()
    print(f"Successfully created: {file_name}")

def start_automation():
    excel_file = "client_data.xlsx"
    
    if not os.path.exists(excel_file):
        print(f"Error: Could not find the file '{excel_file}' in this folder!")
        return
        
    df = pd.read_excel(excel_file)
    print(f"Found {len(df)} rows in Excel. Starting contract generation...")
    
    for index, row in df.iterrows():
        name = row['name']
        service = row['service']
        price = row['price']
        create_contract_pdf(name, service, price)
        
    print("Process completed! Check your folder.")

if __name__ == "__main__":
    start_automation()
