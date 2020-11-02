from collections import Counter

def diveandconquer(s):
    maxcount = 0
    maxrepeat = ""
    for u in range(5, 20):
        news = []
        for i in (range(len(s)-u+2)):
            news.append(s[i:i+u])
        c = Counter(news).most_common(1)
        if(c[0][1] >= maxcount):
            maxrepeat = c[0][0]
            maxcount = c[0][1]
    return maxrepeat + " " +str(maxcount) 



# --- Open file ----
#f = open("vibrio_cholerae.txt", "r")
#f = open("vibrio_cholerae_light.txt", "r")
#f = open("vibrio_cholerae_med.txt", "r")
f = open("deneme.txt", "r")
data = f.read()
f.close()

# -----Main----

sonuc = diveandconquer(data)
print(sonuc)
