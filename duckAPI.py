import requests
import json

duckDump = requests.get('http://api.duckduckgo.com/?q=“presidents of the united states”&format=json')

#TEST: for keys in duckDump.json()['RelatedTopics'][0]:
#TEST:     print(keys)

duckSearchResults = []
for p in range(len((duckDump.json()['RelatedTopics']))):
    duckSearchResults.append(duckDump.json()['RelatedTopics'][p]['Text'])

#TEST: print(len(duckSearchResults))

presidents = {1: 'Washington', 2: 'Adams', 3: 'Jefferson', 4: 'Madison', 5: 'Monroe', 6: 'Quincy Adams',
              7: 'Jackson', 8: 'Van Buren', 9: 'Henry Harrison', 10: 'Tyler', 11: 'Polk', 12: 'Taylor',
              13: 'Fillmore', 14: 'Pierce', 15: 'Buchanan', 16: 'Lincoln', 17: 'Johnson', 18: 'Grant',
              19: 'Hayes', 20: 'Garfield', 21: 'Arthur', 22: 'Cleveland', 23: 'Benjamin Harrison',
              24: 'Cleveland', 25: 'McKinley', 26: 'Roosevelt', 27: 'Taft', 28: 'Wilson', 29: 'Harding',
              30: 'Coolidge', 31: 'Hoover', 32: 'Roosevelt', 33: 'Truman', 34: 'Eisenhower', 35: 'Kennedy',
              36: 'Johnson', 37: 'Nixon', 38: 'Ford', 39: 'Carter', 40: 'Raegan', 41: 'H. W. Bush',
              42: 'Clinton', 43: 'W. Bush', 44: 'Obama', 45: 'Trump', 46: 'Biden'}

for p in range(len(presidents)):
    for result in duckSearchResults:
        if presidents[p+1] in result:
            print(p+1, presidents[p+1])
            break
