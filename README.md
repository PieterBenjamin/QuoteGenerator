![raw text](https://github.com/PieterBenjamin/QuoteGenerator/blob/master/Quote%20Generator%20sample.png)  

This is a fun quote generator designed for anyone with a bash terminal. To get this working, clone the project, and edit the file `quotegenerator.py` 

https://github.com/PieterBenjamin/QuoteGenerator/blob/master/quote_generator/quotegenerator.py#L5-L7

so that the filepath (from your home directory to the file *quotes.txt) is correct.

From there, add the following two lines to your `.bash_profile`:  
`var=$(ls -1 ~/gitrepos/QuoteGenerator/quote_generator/TolkienQuotesJson | wc -l)
python ~/gitrepos/QuoteGenerator/quote_generator/quotegenerator.py $var`

*In a previous version of this project, 50 quotes were included in a single json file. These quotes were  
higher quality (with a source and all in English)*

This project was designed before, but with my [Goodreads-Scraper](https://github.com/PieterBenjamin/GoodReads-Scraper) in mind. As such, I have changed it to be easily usable with the scraper.
