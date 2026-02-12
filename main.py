def check_temperature(temp):
    if temp < 18:
        return "Too cold"
    elif temp <= 24:
        return "Comfortable"
    else:
        return "Too hot"


temperature = float(input("Enter temperature: "))
result = check_temperature(temperature)
print(result)
