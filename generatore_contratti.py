import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def crea_pdf_contratto(nome_cliente, servizio_scelto, prezzo_pattuito):
    # Definiamo il nome del file finale (es: Contratto_Mario_Rossi.pdf)
    nome_file = f"Contratto_{nome_cliente.replace(' ', '_')}.pdf"
    
    # Inizializziamo il foglio PDF
    pdf = canvas.Canvas(nome_file, pagesize=letter)
    pdf.setTitle(f"Contratto - {nome_cliente}")
    
    # Scriviamo il testo del contratto standard (usando le coordinate X e Y del foglio)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(100, 700, "CONTRATTO STANDARD DI PRESTAZIONE SERVIZI")
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 650, f"Con la presente scrittura, si conviene e si stipula quanto segue:")
    pdf.drawString(100, 620, f"Tra il sottoscritto professionista e il Cliente: {nome_cliente}")
    
    pdf.drawString(100, 580, f"1. Oggetto del contratto: Il professionista si impegna a svolgere il servizio")
    pdf.drawString(100, 560, f"   di '{servizio_scelto}' a favore del Cliente.")
    
    pdf.drawString(100, 520, f"2. Corrispettivo: Per le prestazioni sopra indicate, il Cliente corrisponderà")
    pdf.drawString(100, 500, f"   la cifra totale di euro {prezzo_pattuito} €.")
    
    # Spazio per le firme in fondo alla pagina
    pdf.drawString(100, 300, "Firma del Professionista: ______________________")
    pdf.drawString(100, 250, "Firma del Cliente: ___________________________")
    
    # Chiudiamo e salviamo il file PDF
    pdf.save()
    print(f"Creato con successo: {nome_file}")

def avvia_automazione():
    file_excel = "dati_clienti.xlsx"
    
    # Controllo di sicurezza: verifichiamo se l'Excel esiste davvero
    if not os.path.exists(file_excel):
        print(f"Errore: Non trovo il file '{file_excel}' in questa cartella!")
        return
        
    # Leggiamo il file Excel con Pandas
    df = pd.read_excel(file_excel)
    
    print(f"Trovate {len(df)} righe nell'Excel. Inizio la generazione dei contratti...")
    
    # Cicliamo su ogni riga dell'Excel per estrarre i dati
    for indice, riga in df.iterrows():
        # Prendiamo i dati dalle colonne
        nome = riga['nome']
        servizio = riga['servizio']
        prezzo = riga['prezzo']
        
        # Generiamo il PDF specifico per questa riga
        crea_pdf_contratto(nome, servizio, prezzo)
        
    print("Processo completato! Controlla la cartella.")

# Questo dice a Python di avviare lo script
if __name__ == "__main__":
    avvia_automazione()