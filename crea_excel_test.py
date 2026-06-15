import pandas as pd
import random

# Liste di parole per inventare nomi, servizi e prezzi realistici
nomi_finti = ["Mario", "Luigi", "Elena", "Giulia", "Francesco", "Alessandro", "Sofia", "Chiara", "Davide", "Roberta"]
cognomi_finti = ["Rossi", "Ferrari", "Russo", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco", "Bruno"]
servizi_finti = ["Consulenza Finanziaria", "Sviluppo Software AI", "Social Media Marketing", "Design Logo", "Revisione Contabile"]

dati = []

# Generiamo 50 righe di dati finti
for i in range(50):
    # Combina un nome e un cognome a caso
    nome_completo = f"{random.choice(nomi_finti)} {random.choice(cognomi_finti)}"
    servizio = random.choice(servizi_finti)
    prezzo = random.randint(500, 3500) # Prezzo a caso tra 500 e 3500 euro
    
    dati.append({
        "nome": nome_completo,
        "servizio": servizio,
        "prezzo": prezzo
    })

# Trasformiamo la lista in un DataFrame Pandas
df_test = pd.DataFrame(dati)

# Salviamo l'Excel nella stessa cartella
df_test.to_excel("dati_clienti.xlsx", index=False)

print("File 'dati_clienti.xlsx' con 50 clienti finti generato con successo!")