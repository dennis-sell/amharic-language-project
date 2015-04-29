#### Monolingual data
We were able to scrape 2.5 MB of (relatively) clean text from the amharic wikipedia. This required parsing the wikipedia text out of the xml dump available online, and then cleaning the wikipedia text, which is essentially a markup language at first.
 - amwiki-20150412-pages-articles.xml: data dump from wikipedia
 - amharic_wiki_unclean.txt: Wikitext extracted from  xml
 - amharic_wiki_clean.txt: Cleaned wikitext
 - xml_extractor.py: Initial attempt, gets unclean text
 - scrape.py: Script provided by friend. Cleans the wikipedia text


#### Transliteration
To start, I attempted to find bilingual data consisting of transliteration pairs. We extracted English-Amahric name pairs from [CCB's data](http://www.cis.upenn.edu/~ccb/data/transliteration/wikipedia\_names.gz), which were initially gathered from wikipedia. We extracted the english and amharic data and accounted for repeated data. This resulted in 86 name pairs, not enough for statistical transliteration model. We could not find other data sources, so we decided to make a simple non-statistical model from a informative source we found online (geez.xls). 
 - transliterate.py: The transliteration script. Pipe amharic text into the script to get transliterated text out.
 - geez.xls - Source on Amharic Abugida found online
 - en-am_titles.txt: English and Amharic versions of names extracted from wikipedia

The source contained a mapping from Amharic symbols to english syllables. We extraced and cleaned up the relevant data, replaced a few symbols from the IPA with english letters (i.e. "ʃ" ==> "sh"), etc. This is a simplistic method, but given the richness of Amharic syllables as compared to other Semitic writing systems like Arabic or Hebrew, this was sufficient.

Sample Output with Original English Names:
 - "Jerald Ford" ==> "Gerald Ford"
 - "Nelsen Mandela" ==> "Nelson Mandela"
 - "Hadis Alemajehu" ==> "Haddis Alemayehu"
 - "Jose Eduardo Dos Santos" ==> "Hoze Edwardo Dos Santos"


####Language Identification
 Due to the lack of large amounts of data available online for Amharic, it was not possible to write a language identification system using statistical methods. However, a very basic identifier, that primarily checks for correct characters was quite simple. The Ge'ez script used by Amharic is quite rare, and the only other languages that use it are Tigrinya, Tigre, and Blin (interestingly, some langauges, such as Oromo, used to use it, but have now switched to a Latin alphabet). Hence the obvious thing to do is to parse a given text and check that all, or nearly all, of the characters are of this alphabet. There are a handful of letter used in Tigrinya, Tigre, and Blin that are not used in Amharic, and so by looking for these characters it is possible to guess whether a Ge'ez text is Amharic, or one of the other three. The language_identifier.py script takes a text as input, and outputs 1 if the language is Amharic, 2 if it is Amharic-like (one of the other three Ge'ez language), and a 0 otherwise. The method used is obviously not perfect, as it is unable to determine if a given text is actually structured Amharic, or just a random sequence of Ge'ez characters. However, without enough data available, more advanced statistical language indentifier methods are not possible. 


####Twitter Presence
Users of Amharic are concentrated in two regions of the wrold: Amhara and the United States. Given this context, two Twitter stream scrapes were run:
#####Location Query
A location query was run on the bounding box NE: 13.77, 40.23; SW: 8.80, 35.27 over an 8 hour period on April 22 with the following [results](https://github.com/leejcw/amharic-data/blob/master/unicode.out) and their [metadata](https://github.com/leejcw/amharic-data/blob/master/scrape.json):

 - Number of tweets from region: 875
 - Lanuages tweeted in: Italian, Spanish, English, French, Korean, Arabic
 - Common topics: Justin Bieber, Italy (Milan/Sicily), Tunisia, Earth Day, Jonas Brothers
 - Tweets filtered out: none
These results seem to imply that Amharic speakers living in Ethiopia do not tweet often, and that the bulk of the traffic from the region were tourists from Europe and other places abroad. Unfortunately, there were no tweets in Amharic from Amhara within the time span of the scrape.

#####Alphabet Query
Though Twitter has a beta language recognition feature, it is not entirely reliable. Instead, a scrape was run in which the entire Amharic script was used as query tokens. This query was run for a 24 hour period from April 22 to April 23 with the following cleaned [results](https://github.com/leejcw/amharic-data/blob/master/amharic.out):

 - Number of tweets: 42
 - Languages tweeted in: Amharic, English
 - Common topics: Ethiopian politics, Earth Day
 - Tweets filtered out: Korean tweets that used Amharic characters for emojis

These results were almost entirely without location data, and those that had them indicated locations in the United States. It is worth noting from these results that while 42 tweets over a 24 hour period is already an abysmally low number, it is relatively high compared to the normal rate of <5 per day. This fortuitous spike appears to be the result of Earth Day in comjuntion with political activity and violence in Ethiopia.


