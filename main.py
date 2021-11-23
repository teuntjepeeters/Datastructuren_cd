def main():
    studenten = {"Beau": [19, "HAVO"],
                 "Rosalie": [19, "HAVO"],
                 "Laura": [22, "HBO"],
                 "Zaki": {"Leeftijd":18, "Vooropleiding": "HAVO"},
                 "Pepijn": {"Leeftijd":17, "Vooropleiding":"HAVO"}}
    print(studenten)


    studenten_leeftijd = {19: ["Beau", "Rosalie"],
                          22: "Laura",
                          18: "Zaki",
                          17: "Pepijn"}
    #print(studenten_leeftijd[18])

    # print(studenten["Laura"][0])
    print(studenten["Pepijn"]["Vooropleiding"])
    print(studenten["Zaki"]["Leeftijd"])
    # print(studenten["Beau"][0])

    # Welke studenten zijn 18 jaar oud?
    # for k, v in studenten.items():
    #     if v == 18:
    #         print(k)
    #
    # print(studenten.keys())
    # print(studenten.values())


main()