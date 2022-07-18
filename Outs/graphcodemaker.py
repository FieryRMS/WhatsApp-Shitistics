from datetime import timedelta, date
import pickle
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

sd = date(2020, 8, 21)
ld = date(2021, 2, 25)
Phone2Name={
    # "012345678910": "Jhon Doe"
}
Names=["Total"]
for i in Phone2Name:
    if(Phone2Name[i] not in Names):
        Names.append(Phone2Name[i])
with open("CharacterGraph.pkl","rb") as f:
    ds=pickle.load(f)
DayCnt=0

s1="data.addColumn('{}', '{}');\n"
s2="[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}],\n"
Days=[]
for i in daterange(sd,ld):
    Days.append([0]*26)
    if(i.strftime("%d-%m-%Y") in ds):
        for j in ds[i.strftime("%d-%m-%Y")]:
            if(j!='Total'):
                name=Phone2Name[j]
            else:
                name="Total"
            Days[DayCnt][Names.index(name)]+=ds[i.strftime("%d-%m-%Y")][j]
    DayCnt+=1
with open("ActivityGraphData.txt", "w", encoding="utf-8") as f:
    for i in Names:
        f.write(s1.format("number",i))
    f.write("\n\n")
    DayCnt=1
    for i in Days:
        f.write(s2.format(DayCnt,*i))
        DayCnt+=1