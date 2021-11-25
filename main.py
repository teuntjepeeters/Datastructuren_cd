import pickle


def demo_dictionary():
    studenten = {"Beau": [19, "HAVO"],
                 "Rosalie": [19, "HAVO"],
                 "Laura": [22, "HBO"],
                 "Zaki": {"Leeftijd": 18, "Vooropleiding": "HAVO"},
                 "Pepijn": {"Leeftijd": 17, "Vooropleiding": "HAVO"}}
    print(studenten)

    studenten_leeftijd = {19: ["Beau", "Rosalie"],
                          22: "Laura",
                          18: "Zaki",
                          17: "Pepijn"}
    # print(studenten_leeftijd[18])

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


def demo_sets():

    lievelingseten = set(["pasta", "pasta", "sushi", "broccoli", "pizza", "tiramisu"])
    gezondeten = set(["broccoli", "wortel", "soep", "appel", "sla"])

    lievelingseten.add("kapsalon")

    #print(lievelingseten)

    #print(gezondeten)

    # Union
    # print(lievelingseten.union(gezondeten))

    # Intersection
    # print(gezondeten.intersection(lievelingseten))

    # Difference
    # print(lievelingseten.difference(gezondeten))
    # print(gezondeten.difference(lievelingseten))

    # Symmetric difference
    #print(lievelingseten.symmetric_difference(gezondeten))

    set1 = set([1, 2, 3, 4])
    set2 = set([4, 1])
    print(set2)
    print(set2.issubset(set1))
    print(set2.issuperset(set1))
    print(set1.issuperset(set2))


def demo_pickling():
    studenten = {"Beau": [19, "HAVO"],
                 "Rosalie": [19, "HAVO"],
                 "Laura": [22, "HBO"],
                 "Zaki": {"Leeftijd": 18, "Vooropleiding": "HAVO"},
                 "Pepijn": {"Leeftijd": 17, "Vooropleiding": "HAVO"}}
    
    inFile = open("demo_pickle", "wb")
    pickle.dump(studenten, inFile)
    inFile.close()

    inFile = open("demo_pickle", "rb")
    stud = pickle.load(inFile)
    print(stud)
    inFile.close()



def main():
    demo_pickling()



main()