from emoji import UNICODE_EMOJI
import regex
import pickle
Phone2Name={
    # "012345678910": "Jhon Doe"
}
TotalMsgCnt=0
DelMsgCnt=0
RepMsgCnt=0
EmojiCnt=0
CharacterCnt=0
EmojisUsed={}
Emoji={}
Word={}
Activity={}
RepTo={}
Reps={}
Del={}
Character={}
ActivityGraph={}
EmojiGraph={}
DelGraph={}
CharacterGraph={}

def is_emoji(a):
    arr=[9760,128065,10084,9785,9733,9728]
    if(a in UNICODE_EMOJI["en"] or (a>="\U0001F1E6" and a<="\U0001F1FF") or ord(a[0]) in arr):
        return True
    return False
def main():
    global TotalMsgCnt, DelMsgCnt, RepMsgCnt, EmojiCnt, CharacterCnt, Emoji, Word, Activity
    global RepTo, Reps, Del, Character, ActivityGraph, EmojiGraph, DelGraph, CharacterGraph
    # https://github.com/B16f00t/whapa
    with open(r"whapa output.txt",encoding="utf-8") as f:
        for Ln in f:
            if(Ln=="\n" or Ln==""):
                continue
            Line=f.readline()
            if(Line[:5]=="Error"):
                continue
            From=f.readline()
            Msg=""
            Temp=""
            RepliedTo=""
            Date=""
            flag=0
            RepFlag=0
            while(1):
                Temp=f.readline()
                if(Temp[:9]=="Message: "):
                    flag=1
                    Temp=Temp[9:]
                elif(Temp[:13]=="Replying to: "):
                    RepliedTo=Temp.split(" ")[2]
                    RepFlag=1
                elif(Temp[:11]=="Timestamp: "):
                    break
                if(flag):
                    Msg+=Temp
            if(Temp.find("System message")==-1):
                if(From[5]=="M"):
                    From="Me"
                else:
                    From=From.partition("participant ")[2].split(" ")[0]
                Date=Temp.split(" ")[1]


                ##From, Msg, RepliedTo, Date
                TotalMsgCnt+=1
                if(From not in Activity):
                    Activity[From]=1
                else:
                    Activity[From]+=1
                if(Date not in ActivityGraph):
                    ActivityGraph[Date]={}
                    ActivityGraph[Date]["Total"]=1
                    ActivityGraph[Date][From]=1
                else:
                    ActivityGraph[Date]["Total"]+=1
                    if(From not in ActivityGraph[Date]):
                        ActivityGraph[Date][From]=1
                    else:
                        ActivityGraph[Date][From]+=1
                if(Msg=="Message deleted for all participants\n"):
                    DelMsgCnt+=1
                    if(From not in Del):
                        Del[From]=1
                    else:
                        Del[From]+=1
                    if(Date not in DelGraph):
                        DelGraph[Date]={}
                        DelGraph[Date]["Total"]=1
                        DelGraph[Date][From]=1
                    else:
                        DelGraph[Date]["Total"]+=1
                        if(From not in DelGraph[Date]):
                            DelGraph[Date][From]=1
                        else:
                            DelGraph[Date][From]+=1
                    continue
                if(RepFlag):
                    RepMsgCnt+=1
                    if(RepliedTo not in RepTo):
                        RepTo[RepliedTo]=1
                    else:
                        RepTo[RepliedTo]+=1
                    if(From not in Reps):
                        Reps[From]=1
                    else:
                        Reps[From]+=1
                data = regex.findall(r'\X', Msg)
                Wrd=""
                BrokenFlag=0
                Breaks=[" ", ",", ".", "\n", "!","(",";",":",")","?"]
                Ignore=["_", "*", "~","`",'"',"'","-"]
                for Char in data:
                    CharacterCnt+=1
                    if(From not in Character):
                        Character[From]=1
                    else:
                        Character[From]+=1
                    if(Date not in CharacterGraph):
                        CharacterGraph[Date]={}
                        CharacterGraph[Date]["Total"]=1
                        CharacterGraph[Date][From]=1
                    else:
                        CharacterGraph[Date]["Total"]+=1
                        if(From not in CharacterGraph[Date]):
                            CharacterGraph[Date][From]=1
                        else:
                            CharacterGraph[Date][From]+=1
                    if(is_emoji(Char)):
                        EmojiCnt+=1
                        if(Char not in Emoji):
                            Emoji[Char]=1
                        else:
                            Emoji[Char]+=1
                        if(From not in EmojisUsed):
                            EmojisUsed[From]=1
                        else:
                            EmojisUsed[From]+=1
                        BrokenFlag=1
                        if(Date not in EmojiGraph):
                            EmojiGraph[Date]={}
                            EmojiGraph[Date]["Total"]=1
                            EmojiGraph[Date][Char]=1
                        else:
                            EmojiGraph[Date]["Total"]+=1
                            if(Char not in EmojiGraph[Date]):
                                EmojiGraph[Date][Char]=1
                            else:
                                EmojiGraph[Date][Char]+=1
                    if(Char in Breaks):
                        BrokenFlag=1
                    if(BrokenFlag):
                        if(Wrd!=""):
                            if(Wrd not in Word):
                                Word[Wrd]=1
                            else:
                                Word[Wrd]+=1
                            Wrd=""
                        BrokenFlag=0
                    elif(Char not in Ignore and Char.find('\u200c')==-1):
                        Wrd+=Char
                if(Wrd!=""):
                    if(Wrd not in Word):
                        Word[Wrd]=1
                    else:
                        Word[Wrd]+=1
                    Wrd=""
def exportCustom():
    global TotalMsgCnt, DelMsgCnt, RepMsgCnt, EmojiCnt, CharacterCnt, Emoji, Word, Activity, EmojisUsed
    global RepTo, Reps, Del, Character, ActivityGraph, EmojiGraph, DelGraph, CharacterGraph
    with open(r".\Outs\Count.txt", mode="w", encoding="utf-8") as f:
        f.write("TotalMsg: {}\nDelMsg: {}\nRepMsg: {}\nCharCnt: {}\nEmojiCnt:{}\nTotal@ : 2480".format(TotalMsgCnt,DelMsgCnt,RepMsgCnt,CharacterCnt,EmojiCnt))

    Emoji=dict(sorted(Emoji.items(), key=lambda item: item[1], reverse=True))
    with open(r".\Outs\Emoji.txt", mode="w", encoding="utf-8") as f:
        for i in Emoji:
            f.write(i+" - "+str(Emoji[i])+"\n")

    EmojisUsed=dict(sorted(EmojisUsed.items(), key=lambda item: item[1], reverse=True))
    with open(r".\Outs\EmojisUsed.txt", mode="w", encoding="utf-8") as f:
        for i in EmojisUsed:
            f.write(i+" - "+str(EmojisUsed[i])+"\n")

    with open(r".\Outs\EmojiGraph.pkl", mode="wb") as f:
        pickle.dump(EmojiGraph,f)

def export():
    global TotalMsgCnt, DelMsgCnt, RepMsgCnt, EmojiCnt, CharacterCnt, Emoji, Word, Activity, EmojisUsed
    global RepTo, Reps, Del, Character, ActivityGraph, EmojiGraph, DelGraph, CharacterGraph
    with open(r".\Outs\Count.txt", mode="w", encoding="utf-8") as f:
        f.write("TotalMsg: {}\nDelMsg: {}\nRepMsg: {}\nCharCnt: {}\nEmojisUsed:{}".format(TotalMsgCnt,DelMsgCnt,RepMsgCnt,CharacterCnt,EmojiCnt))

    Emoji=dict(sorted(Emoji.items(), key=lambda item: item[1], reverse=True))
    with open(r".\Outs\Emoji.txt", mode="w", encoding="utf-8") as f:
        for i in Emoji:
            f.write(i+" - "+str(Emoji[i])+"\n")

    Word=dict(sorted(Word.items(), key=lambda item: item[1], reverse=True))
    with open(r".\Outs\Word.txt", mode="w", encoding="utf-8") as f:
        for i in Word:
            f.write(i+" - "+str(Word[i])+"\n")

    Activity=dict(sorted(Activity.items(), key=lambda item: item[1], reverse=True))
    with open(r".\Outs\Activity.txt", mode="w", encoding="utf-8") as f:
        for i in Activity:
            f.write(i+" - "+str(Activity[i])+"\n")

    RepTo=dict(sorted(RepTo.items(), key=lambda item: item[1], reverse=True))
    with open(r".\Outs\RepTo.txt", mode="w", encoding="utf-8") as f:
        for i in RepTo:
            f.write(i+" - "+str(RepTo[i])+"\n")

    Reps=dict(sorted(Reps.items(), key=lambda item: item[1], reverse=True))
    with open(r".\Outs\Reps.txt", mode="w", encoding="utf-8") as f:
        for i in Reps:
            f.write(i+" - "+str(Reps[i])+"\n")

    Del=dict(sorted(Del.items(), key=lambda item: item[1], reverse=True))
    with open(r".\Outs\Del.txt", mode="w", encoding="utf-8") as f:
        for i in Del:
            f.write(i+" - "+str(Del[i])+"\n")

    Character=dict(sorted(Character.items(), key=lambda item: item[1], reverse=True))
    with open(r".\Outs\Character.txt", mode="w", encoding="utf-8") as f:
        for i in Character:
            f.write(i+" - "+str(Character[i])+"\n")

    EmojisUsed=dict(sorted(EmojisUsed.items(), key=lambda item: item[1], reverse=True))
    with open(r".\Outs\EmojisUsed.txt", mode="w", encoding="utf-8") as f:
        for i in EmojisUsed:
            f.write(i+" - "+str(EmojisUsed[i])+"\n")

    with open(r".\Outs\ActivityGraph.pkl", mode="wb") as f:
        pickle.dump(ActivityGraph,f)

    with open(r".\Outs\EmojiGraph.pkl", mode="wb") as f:
        pickle.dump(EmojiGraph,f)
    
    with open(r".\Outs\DelGraph.pkl", mode="wb") as f:
        pickle.dump(DelGraph,f)
    
    with open(r".\Outs\CharacterGraph.pkl", mode="wb") as f:
        pickle.dump(CharacterGraph,f)
main()
exportCustom()














