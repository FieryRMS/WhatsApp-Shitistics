s="""
    {{
    type: 'number',
    label: '{}',
    color: '{}',
    disabledColor: '{}',
    visible: true
    }},
"""
colors=[
    "#0000FF",
    "#8A2BE2",
    "#7FFF00",
    "#DC143C",
    "#008B8B",
    "#B8860B",
    "#006400",
    "#8B008B",
    "#8B0000",
    "#FF1493",
    "#228B22",
    "#6A9C79",
    "#7CFC00",
    "#20B2AA",
    "#800000",
    "#0000CD",
    "#191970",
    "#000080",
    "#FFA500",
    "#808000",
    "#FF4500",
    "#663399",
    "#595959",
    "#A0522D",
    "#008080",
    "#009400",
]
Fader=0.7
Phone2Name={
    # "012345678910": "Jhon Doe"
}

AllEmojis=["Total","Emojis with<=30ocr"]
import regex
with open("Emoji.txt",encoding="utf-8") as f:
    for ln in f:
        data = regex.findall(r'\X', ln)
        if(not int(ln.split(" ")[2])<=30):
            AllEmojis.append(data[0])

with open("emojicolumns.txt",'w') as f:
    for i in range(len(AllEmojis)):
        R=int("0x"+colors[i%len(colors)][1:3],16)
        G=int("0x"+colors[i%len(colors)][3:5],16)
        B=int("0x"+colors[i%len(colors)][5:],16)
        R+=int((255-R)*Fader)
        G+=int((255-G)*Fader)
        B+=int((255-B)*Fader)
        disColor="#{:0>2}{:0>2}{:0>2}".format(hex(R)[2:],hex(G)[2:],hex(B)[2:])

        f.write(s.format(AllEmojis[i],colors[i%len(colors)],disColor))
