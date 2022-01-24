#working on nested dictionary

family={"Mother":"Sara",
        "Father":"Imran",
        "Siblings":{1:"Maham",2:"Yahya",3:"Umar",4:"Umama"}}
for k,v in family.items():
    print(k,":",v)

grandfamily={"Maternal":{"Grandfather":"Rasheed",
                         "Grandmother":"Muzaffari",
                         "Uncle":["Amir","Ahmed"]},
             "Paternal": {"Grandfather": "Tauqeer",
                          "Grandmother": "Ahmedi",
                          "Aunts": {1:"Shahana", 2:"Farzana"}}}
#del family["Siblings"]
#in order to delete a particular value of a key, we have to first index it as shown below, and when we index it, we will change [] to
del family["Siblings"][4]
del grandfamily["Maternal"]["Uncle"]
del grandfamily["Paternal"]["Aunts"][2]
grandfamily["Paternal"]["Aunts"][1]="Rubina"


family.update(grandfamily)
for k,v in family.items():
    print(k,":",v)


















