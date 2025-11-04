dd = {"Park" : {"age" : 25 , "blood" : "B"} ,
      "Kim" : {"age" : 37 , "blood" : "A"}}

print(dd["Park"]) # {"age" : 25 , "blood" : "B"}
print(dd["Park"]["age"]) 

for name in dd: # name = "Park" , "Kim"
    for info in dd[name]: # info = "age" , "blood"
        print(dd[name][info])
        # dd["Park"] -> {"age" : 25 , "blood" : "B"}
        # info -> age , blood
        # dd["Kim"] ->  {"age" : 37 , "blood" : "A"}}
        # info -> age , blood

ld = [{"name" : "Park" , "age" : 25 , "blood" : "B"} ,
      {"name" : "Park" , "age" : 37 , "blood" : "A"}]
print(ld[0])
print(ld[0]["name"]) # ld[인덱스][key]


for i in ld: # i = {"name" : "Park" , "age" : 25 , "blood" : "B"}
    for key in i: # key 에는 key 값만 담김!!!!!
        print("{} : {}".format(key, i[key]))

































