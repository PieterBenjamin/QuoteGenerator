![raw text](https://github.com/PieterBenjamin/QuoteGenerator/blob/master/Quote%20Generator%20sample.png)  

**Note: you will need python 3.0 installed**  
This is a fun quote generator designed for anyone with a bash terminal. To get this working, clone the project, and edit the file `quotegenerator.py` 

https://github.com/PieterBenjamin/QuoteGenerator/blob/master/quote_generator/quotegenerator.py#L5-L7

so that the filepath (from your home directory to the file *quotes.txt) is correct.

From there, add the following line to your `.bash_profile`:  
`python ~/gitrepos/QuoteGenerator/quote_generator/quotegenerator.py`

Upon opening a terminal window, you should be greeted with a random quote from the file. By default, 
I have included [50 quotes from Tolkien](https://pastebin.com/8PznRpXv) in JSON
format in the file [tolkienquotesjson.txt](https://github.com/PieterBenjamin/QuoteGenerator/blob/master/quote_generator/tolkienquotesjson.txt)  
*please note, I did not make this file and found it [from reddit](https://www.reddit.com/r/lotr/comments/4d5ss7/50_lotr_quotes_included_json_file/)*

Though only 50 quotes have been included to begin with, this project should be easily expandable so long as you provide
a JSON file, consisting of a single array of objects, each of which having a `quote`, `author`, and `source` field.
