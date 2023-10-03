whole_numbers = {
    0: "Eber",
    1: "Hal",
    2: "Labo",
    3: "Saddex",
    4: "Afar",
    5: "Shan",
    6: "Lix",
    7: "Tadabbo",
    8: "Sideed",
    9: "Sagaal",
    10: "Toban",
    20: "Lawaatan",
    30: "Soddan",
    40: "Afartan",
    50: "Kontan",
    60: "Lexdan",
    70: "Tadawaatan",
    80: "Sideetan",
    90: "Sagaashan",
    100: "Baqol",
}


def number_to_text_somali(number):
    if number < 0 or number > 1000000:
        return "ma ugu talagalin number 1 million ka badan ama la eg"

    if number in whole_numbers:
        return f"{whole_numbers[number]}"
    elif number < 100:
        taban = number // 10 * 10
        ones = number % 10
        return f"{whole_numbers[taban]} iyo {whole_numbers[ones]}"
    elif number < 1000:
        boqol = number // 100
        hare = number % 100
        return f"{whole_numbers[boqol]} boqol iyo {number_to_text_somali(hare)}"
    elif number < 1000000:
        kun = number // 1000 # 1
        hare = number % 1000 # 927
        return f"{number_to_text_somali(kun)} kun {number_to_text_somali(hare)}"


print(number_to_text_somali(19652))
