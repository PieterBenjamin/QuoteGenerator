import os
import json
import random
from pprint import pprint

json_data=open(str(os.path.expanduser('~/gitrepos/QuoteGenerator/quote_generator/tolkienquotesjson.txt'))).read()

data = json.loads(json_data)

quoteIndex = random.randint(0, len(data))
print()
print(data[quoteIndex]['quote'])
print("-" + data[quoteIndex]['author'] + ", " + data[quoteIndex]['source'])
print()
