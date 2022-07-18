Phone2Name={
    # "012345678910": "Jhon Doe"
}
Data={}

with open("Activity.txt",encoding="utf-8") as  f:
    for Ln in f:
        d=Ln.split(" ")
        number=Phone2Name[d[0]]
        value=d[2].split("\n")[0]
        if(number not in Data):
            Data[number]=[0,0,0,0,0,0,0]
        Data[number][0]+=int(value)

with open("Character.txt",encoding="utf-8") as  f:
    for Ln in f:
        d=Ln.split(" ")
        number=Phone2Name[d[0]]
        value=d[2].split("\n")[0]
        if(number not in Data):
            Data[number]=[0,0,0,0,0,0,0]
        Data[number][1]+=int(value)

with open("EmojisUsed.txt",encoding="utf-8") as  f:
    for Ln in f:
        d=Ln.split(" ")
        number=Phone2Name[d[0]]
        value=d[2].split("\n")[0]
        if(number not in Data):
            Data[number]=[0,0,0,0,0,0,0]
        Data[number][2]+=int(value)

with open("Ats.txt",encoding="utf-8") as  f:
    for Ln in f:
        d=Ln.split(" ")
        number=Phone2Name[d[0][1:]]
        value=d[2].split("\n")[0]
        if(number not in Data):
            Data[number]=[0,0,0,0,0,0,0]
        Data[number][3]+=int(value)

with open("Reps.txt",encoding="utf-8") as  f:
    for Ln in f:
        d=Ln.split(" ")
        number=Phone2Name[d[0]]
        value=d[2].split("\n")[0]
        if(number not in Data):
            Data[number]=[0,0,0,0,0,0,0]
        Data[number][4]+=int(value)

with open("RepTo.txt",encoding="utf-8") as  f:
    for Ln in f:
        d=Ln.split(" ")
        number=Phone2Name[d[0]]
        value=d[2].split("\n")[0]
        if(number not in Data):
            Data[number]=[0,0,0,0,0,0,0]
        Data[number][5]+=int(value)

with open("Del.txt",encoding="utf-8") as  f:
    for Ln in f:
        d=Ln.split(" ")
        number=Phone2Name[d[0]]
        value=d[2].split("\n")[0]
        if(number not in Data):
            Data[number]=[0,0,0,0,0,0,0]
        Data[number][6]+=int(value)
Data=dict(sorted(Data.items(), key=lambda item: item[0]))
s="""
								<tr class="row100 body">
									<td class="cell100 column1">{}</td>
									<td class="cell100 column2">{}</td>
									<td class="cell100 column3">{}</td>
									<td class="cell100 column4">{}</td>
									<td class="cell100 column5">{}</td>
                                    <td class="cell100 column6">{}</td>
                                    <td class="cell100 column7">{}</td>
                                    <td class="cell100 column8">{}</td>
								</tr>
"""
with open("htmlout.txt",mode="w",encoding="utf-8") as f:
    cnt=0
    for i in Data:
        cnt+=1
        nem=i
        if(i in Phone2Name):
            nem=Phone2Name[i]
        f.write(s.format(nem,Data[i][0],Data[i][1],Data[i][2],Data[i][3],Data[i][4],Data[i][5],Data[i][6]))
    print(cnt)





