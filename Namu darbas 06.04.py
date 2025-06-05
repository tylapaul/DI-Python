def registruoti_ir_apibendrinti_treniruotes():
    """
    Įrašo vartotojo savaitės treniruočių minutes, apskaičiuoja bendrą laiką,
    randa dieną su ilgiausia treniruote ir patikrina, ar pasiektas savaitės tikslas.
    """
    dienos = ["Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis", "Šeštadienis", "Sekmadienis"]
    treniruociu_minutes = []
    bendras_laikas = 0
    savaites_tikslas = 150  # Numatytasis savaitės tikslas minutėmis

    print("Įveskite kiekvienos dienos treniruočių minutes.\n")

    # 1. Duomenų įvedimas kiekvienai dienai
    for diena in dienos:
        while True:
            try:
                minutes = int(input(f"Kiek minučių sportavote {diena.lower()}? "))
                if minutes < 0:
                    print("Minučių skaičius negali būti neigiamas. Bandykite dar kartą.")
                else:
                    treniruociu_minutes.append(minutes)
                    break  # Išeiti iš while ciklo, jei įvestis teisinga
            except ValueError:
                print("Netinkama įvestis. Prašome įvesti skaičių.")

    # 2. Bendro laiko apskaičiavimas
    bendras_laikas = sum(treniruociu_minutes)

    # 3. Dienos su ilgiausia treniruote radimas
    if not treniruociu_minutes: # Jei sąrašas tuščias (nors neturėtų būti pagal logiką)
        ilgiausia_treniruote_minutes = 0
        geriausia_diena = "Nėra duomenų"
    else:
        ilgiausia_treniruote_minutes = 0
        geriausia_diena_indeksas = -1

        for i, minutes in enumerate(treniruociu_minutes):
            if minutes > ilgiausia_treniruote_minutes:
                ilgiausia_treniruote_minutes = minutes
                geriausia_diena_indeksas = i
        
        if geriausia_diena_indeksas != -1 and ilgiausia_treniruote_minutes > 0:
             geriausia_diena = dienos[geriausia_diena_indeksas]
        elif ilgiausia_treniruote_minutes == 0: # Visos treniruotės buvo 0 minučių
            geriausia_diena = "Nė vienos dienos (visos treniruotės 0 min)"
        else: # Neturėtų pasitaikyti, bet saugumo dėlei
            geriausia_diena = "Nėra duomenų"


    # 4. Savaitės tikslo tikrinimas
    ar_tikslas_pasiektas = bendras_laikas >= savaites_tikslas

    # 5. Rezultatų pateikimas
    print("\n--- Savaitės Treniruočių Apžvalga ---")
    print(f"📊 Bendras treniruočių laikas: {bendras_laikas} minučių")
    
    if ilgiausia_treniruote_minutes > 0:
        print(f"🥇 Diena su ilgiausia treniruote: {geriausia_diena} ({ilgiausia_treniruote_minutes} min.)")
    else:
        print("🥇 Šią savaitę treniruočių nebuvo.")

    if ar_tikslas_pasiektas:
        print(f"🎯 Savaitės tikslas ({savaites_tikslas} min.) pasiektas! Sveikiname! 🎉")
    else:
        print(f"🎯 Savaitės tikslas ({savaites_tikslas} min.) nepasiektas. Iki tikslo trūko {savaites_tikslas - bendras_laikas} min. 💪")

# Funkcijos iškvietimas, kad pamatytumėte, kaip ji veikia
if __name__ == "__main__":
    registruoti_ir_apibendrinti_treniruotes()