stromRichtg = {"Um":4,"Im":0.038,"RiA":3.3}
spannungsRichtg={}

if stromRichtg:
    Rm = round(stromRichtg["Um"]/stromRichtg["Im"],6)
    stromRichtg["Rm"] = Rm
    R = Rm-stromRichtg["RiA"]
    stromRichtg["R"] = R
    stromRichtg["F"] = stromRichtg["RiA"]
    stromRichtg["f"] = round((stromRichtg["RiA"]/R)*100,2)

print(stromRichtg)