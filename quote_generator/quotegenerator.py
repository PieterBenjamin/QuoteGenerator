import os
import json
import random
import textwrap

path_to_file = '~/gitrepos/QuoteGenerator/quote_generator/tolkienquotesjson.txt'
json_data=open(str(os.path.expanduser(path_to_file))).read()

data = json.loads(json_data)

quoteIndex = random.randint(0, len(data) - 1)
print("")
quote = data[quoteIndex]['quote']
wrapped_quote = textwrap.wrap(quote[1 : len(quote) - 1], 80)

for quoteSegment in wrapped_quote:
    print(quoteSegment)

print("")
print("\t-" + data[quoteIndex]['author'] + ", " + data[quoteIndex]['source'])
print("")
