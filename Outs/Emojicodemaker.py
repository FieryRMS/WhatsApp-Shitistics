from datetime import timedelta, date
import pickle
import regex
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
sd = date(2020, 8, 21)
ld = date(2021, 2, 25)
AllEmojis=["Less"]
with open("EmojiGraph.pkl","rb") as f:
    ds=pickle.load(f)

with open("Emoji.txt",encoding="utf-8") as f:
    for ln in f:
        data = regex.findall(r'\X', ln)
        if(not int(ln.split(" ")[2])<=30):
            AllEmojis.append(data[0])

Days=[]

DaysCnt=0
s1="data.addColumn('{}', '{}');\n"
s2="["+''.join([r"{},"]*(len(AllEmojis)+2))+"],\n"
print(s2)
for i in daterange(sd,ld):
    Days.append([0]*(len(AllEmojis)+1))
    if(i.strftime("%d-%m-%Y") in ds):
        for j in ds[i.strftime("%d-%m-%Y")]:
            if(j=="Total"):
                Days[DaysCnt][0]=ds[i.strftime("%d-%m-%Y")][j]
            else:
                if(j in AllEmojis):
                    Days[DaysCnt][AllEmojis.index(j)+1]=ds[i.strftime("%d-%m-%Y")][j]
                else:
                    Days[DaysCnt][1]=ds[i.strftime("%d-%m-%Y")][j]
        DaysCnt+=1
with open("EmojiGraphData.txt", "w", encoding="utf-8") as f:
    for i in AllEmojis:
        f.write(s1.format("number",i))
    f.write("\n\n")
    DayCnt=1
    for i in Days:
        f.write(s2.format(DayCnt,*i))
        DayCnt+=1