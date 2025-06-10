import requests
import json

# --- Tavo kodas (lieka nepakitęs) ---
model = "jobautomation/OpenEuroLLM-Lithuanian:latest"

try:
    with open('./anyksciai.txt', 'r', encoding='utf-8') as file:
        context = file.read()
    print("Sėkmingai nuskaitytas anyksciai.txt failas.")
    # print(context) # Atkomentuok, jei nori matyti visą kontekstą
except FileNotFoundError:
    print("KLAIDA: Failas './anyksciai.txt' nerastas. Įsitikink, kad jis yra toje pačioje direktorijoje kaip ir Python skriptas.")
    exit() # Nutraukiame programą, jei failas nerastas

user_prompt = input("Prašome užduoti klausimą apie Anykščius: ")

# --- Užklausos siuntimas (lieka nepakitęs) ---
try:
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": [
                # Geroji praktika yra sujungti sistemos pranešimus į vieną
                {"role": "system", "content": """Tu esi Anykščių turizmo informacijos centro specialistas.
                Tavo užduotys:
                1.  Siūlyti maršrutus, renginius, lankytinas vietas ir teikti praktinę informaciją turistams.
                2.  Atsakyti trumpai (1–3 sakiniais), pateikiant aiškų faktą arba rekomendaciją.
                3.  Bendrauti mandagiai, pozityviai ir paslaugiai.
                4.  Atsakyti tik lietuvių kalba, naudojant aiškią ir taisyklingą kalbą.
                """},
                {"role": "user", "content": f"Naudodamasis šiuo kontekstu: \"{context}\". Atsakyk į klausimą: \"{user_prompt}\""}
            ],
            "stream": False
        }
    )
    # Patikriname, ar užklausa buvo sėkminga (HTTP statuso kodas 200)
    response.raise_for_status()

    # --- Klaidų taisymas ir atsakymo apdorojimas ---

    # 1. Naudojame response.json() metodą, kad gautume Python žodyną
    duomenys = response.json()

    # 2. Išgauname tekstą pagal teisingą Ollama atsakymo struktūrą
    isgautas_tekstas = duomenys['message']['content']

    # Spausdiname rezultatą
    print("\n--- Atsakymas ---")
    print(isgautas_tekstas)

except requests.exceptions.RequestException as e:
    print(f"\nKLAIDA: Nepavyko prisijungti prie Ollama serverio (http://localhost:11434).")
    print("Patikrink, ar Ollama veikia tavo kompiuteryje ir ar nurodytas modelis yra įdiegtas.")
    print(f"Klaidos pranešimas: {e}")
except KeyError:
    print("\nKLAIDA: Gautas netikėtos struktūros atsakymas iš Ollama.")
    print("Gautas atsakymas:", duomenys)