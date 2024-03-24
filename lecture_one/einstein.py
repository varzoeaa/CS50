# tell the equivalent joules for kilogram input
def joules(mass):
    c_squared = 299792458 ** 2  
    joules = mass * c_squared
    return joules

def main():
    mass = float(input("Tell me the mass you want to convert to joules! (in kg) "))
    joule = joules(mass)
    print(f"{joule} joules")

main()