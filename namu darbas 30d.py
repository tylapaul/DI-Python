weight_txt = input("Ivesk svori (kg): ")  # imput komanda duoda teksta
weight = int(weight_txt)
height_txt = input("Ivesk ugi (cm): ")  # imput komanda duoda teksta
height = int(height_txt)
height_m = height/100
BMI = weight / (height_m ** 2)
BMI_r = round (BMI,2)
print ("Tavo MBI indexas: ", BMI_r)
if BMI < 18.5:
     print ("Underweight")
elif BMI >= 18.5 and BMI < 25 :
     print ("Normal")
elif BMI >= 25 and BMI < 30:
     print("Overweight")
elif BMI >= 30: 
     print("Obesity")