s="""
		<tr class="row100 body">
		<td class="cell100 column1">{}</td>
		<td class="cell100 column2">{}</td>
		</tr>
"""
with open("html2.txt",mode="w",encoding="utf-8") as out:
    others=0
    with open("Emoji.txt",encoding="utf-8") as f:
        for ln in f:
            d=ln.split(" ")
            word=d[0]
            value=int(d[2].split("\n")[0])
            if(value<0):
                others+=value
            else:
                out.write(s.format(word,value))
    ##out.write(s.format("Any word <50",others))