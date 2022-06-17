strs = ["eat","tea","tan","ate","nat","bat"]
#strs = ["",""]
import collections
output =[]

for i in range(len(strs)):
    if any(strs[i] in k for k in output):
        continue
    inner =[strs[i]]
    for j in range(len(strs)):
        if i==j :
            continue
        #j= list(j)
        if collections.Counter(list(strs[i]))==collections.Counter(list(strs[j])):
            inner.append(strs[j])
    output.append(inner)

print(output)

