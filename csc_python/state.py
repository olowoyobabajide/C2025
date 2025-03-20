x = {"Abia":"Umuahia", "Adamawa":"Yola", "Akwa Ibom":"Uyo", "Anambra":"Awka", "Bauchi":"Bauchi", "Bayelsa":"Yenagoa", "Benue":"Makurdi", "Borno":"Maiduguri", "Cross River":"Calabar", "Delta":"Asaba", "Ebonyi":"Abakaliki", "Edo":"Benin City", "Ekiti":"Ado-Ekiti", "Enugu":"Enugu", "FCT":"Abuja", "Gombe":"Gombe", "Imo":"Owerri", "Jigawa":"Dutse", "Kaduna":"Kaduna", "Kano":"Kano", "Katsina":"Katsina", "Kebbi":"Birnin Kebbi", "Kogi":"Lokoja", "Kwara":"Ilorin", "Lagos":"Ikeja", "Nasarawa":"Lafia", "Niger":"Minna", "Ogun":"Abeokuta", "Ondo":"Akure", "Osun":"Osogbo", "Oyo":"Ibadan", "Plateau":"Jos", "Rivers":"Port Harcourt", "Sokoto":"Sokoto", "Taraba":"Jalingo", "Yobe":"Damaturu", "Zamfara":"Gusau"}


def state():
    y = str(input("Enter a state and get its capital ")).title()

    if y in x:
        print(f"The capital is {x[y]}. ")
    else:
        print("Invalid state, pls enter a correct state ")
        state()

state()
