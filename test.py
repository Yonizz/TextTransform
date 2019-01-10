,COMBINAISONS = [[[1,2,3],2],[[2,3,4],4],[[4,5,6],6],[[5,6]]]

buffer = []
for i in buffer:
    for j in i:
        buffer.append(j)

for i in buffer:
    for j in i:
        for w in j[0]:
            buffer.append(w)

[subelem for combinaison in COMBINAISONS for elem in combinaison for subelem in elem]

upper, lower = 1,2

COMBINAISONS = [[{Key.ctrl_l, Key.f1}, upper],
                [{Key.ctrl_l, Key.f2}, lower]]
,
    COMBINAISONS = [[{1,3},2],[{4,5,6},8],[{7,9,85,6,5},8]]

for combinaison in COMBINAISONS:
    for key in combinaison[0]:

[keys for combinaison in COMBINAISONS for keys in combinaison[0]]
