import os
import sys
import json
import random
import textwrap
from termcolor import colored, cprint


# Put the absolute (or relative) pathway to the json quote file.
path_to_json_file = '~/gitrepos/QuoteGenerator/quote_generator/TolkienQuotesJson/TolkienQuotes-%s.json' % str(random.randint(1, int(sys.argv[1])))
# Python handles opening up the json
json_data   = open(str(os.path.expanduser(path_to_json_file))).read()
quote_data  = json.loads(json_data)
# Variable which specifies how many characters to include in
# the quote before wrapping.
quote_width = 80

# Random selection
quote_index = random.randint(0, len(quote_data) - 1)
print("")
quote = quote_data[quote_index]
wrapped_quote = textwrap.wrap(quote[1 : len(quote) - 1], quote_width)

# Printing the actual quote.
for quoteSegment in wrapped_quote:
    cprint(quoteSegment, 'cyan', attrs=['bold'])
# Printing the author/source.
print("")
