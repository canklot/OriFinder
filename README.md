# OriFinder
Origin of replication finder using python.
Thanks to hash tables its very fast

The origin of replication (also called the replication origin) is a particular sequence in a genome at which replication is initiated.



```
from collections import Counter
Cause of string.count() is slow and we have a HUGE dataset we need a faster method to search. Collections.Counter is a data type for counting data using hash tables which is very fast

In [9]:
def diveandconquer(s):
    maxcount = 0
    maxsubstring = ""
    for u in range(5, 20):
        allsubstrings = []
        for i in (range(len(s)-u+2)):
            allsubstrings.append(s[i:i+u])
        c = Counter(allsubstrings).most_common(1)
        if(c[0][1] >= maxcount):
            maxsubstring = c[0][0]
            maxcount = c[0][1]
    return maxsubstring + " " +str(maxcount)
We have two variables to store max number of occurances and most frequent substring. Then we have a list to store all possible substring. In the for loop we create 5 charecter long substrings by shift throug original string. Then we create a counter object with all possible substring and retrive the most common one and assign it to C. Counter object return two tupples in a list in this format [("theword"),(20)] first the word and the number of occurances. If the number of occurance is higher than previus maxcount value we assign current substring and count to maxcount and maxsubstring. The we itterate the same code with 5 to 20 charecters long substrings.

In [10]:
#f = open("vibrio_cholerae_light.txt", "r")
#f = open("vibrio_cholerae_med.txt", "r")
# = open("deneme.txt", "r")

f = open("vibrio_cholerae.txt", "r")
data = f.read()
f.close()
We read our dataset from a file and store it in a variable named data. I created 3 alternative datasets by deleting much of the original dataset to prevent memory errors and reduce the time taken by running the code while prototyping

In [11]:
sonuc = diveandconquer(data)
print(sonuc)
TTTTT 3193
And laslty we call our function and print it
```
