import datetime

def get_user_birthdate():
    while True:
        birthdate_str = input("Įveskite savo gimimo datą (formatu YYYY-MM-DD): ")
        try:
            birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()
            break  # Išeiname iš ciklo, jei data sėkmingai konvertuota
        except ValueError:
            print("Klaida: Neteisingas datos formatas. Bandykite dar kartą.")
    today = datetime.date.today()

    if birthdate > today:
        print("Klaida: Gimimo data negali būti ateityje.")
        return
    
def calculate_age(birth_date):
        # Amžiaus skaičiavimas
    # Apskaičiuojame skirtumą metais
    today = datetime.date.today()
    age = today.year - birthdate.year

    # Tiksliname amžių, jei šiais metais gimtadienis dar nebuvo
    # Tikriname, ar mėnuo yra ankstesnis arba tas pats mėnuo, bet diena ankstesnė
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    print(f"Jums yra {age} metai(-ų).")
    return age