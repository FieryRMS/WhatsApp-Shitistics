from emoji import UNICODE_EMOJI
import regex
def is_emoji(a):
    arr=[9760,128065,10084,9785,9733,9728]
    if(a in UNICODE_EMOJI["en"] or (a>="\U0001F1E6" and a<="\U0001F1FF") or ord(a[0]) in arr):
        return True
    return False
with open("emoji.txt",encoding='utf-8') as f:
    for ln in f:
        data = regex.findall(r'\X', ln)
        if(not is_emoji(data[0])):
            for i in data[0]:
                print(ord(i))