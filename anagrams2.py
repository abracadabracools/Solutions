strs = ["eat","tea","tan","ate","nat","bat"]
#strs = ["",""]
from collections import defaultdict
output =[]
dict = defaultdict(list)
for i in strs:
    dict[''.join(sorted(i))].append(i)
print(list(dict.values()))