#### Monolingual data
We were able to scrape 2.5 MB of (relatively) clean text from the amharic wikipedia. This required parsing the wikipedia text out of the xml dump available online, and then cleaning the wikipedia text, which is essentially a markup language at first.
 - amwiki-20150412-pages-articles.xml: data dump from wikipedia
 - amharic_wiki_unclean.txt: Wikitext extracted from  xml
 - amharic_wiki_clean.txt: Cleaned wikitext
 - xml_extractor.py: Initial attempt, gets unclean text
 - scrape.py: Script provided by friend. Cleans the wikipedia text

#### Bilingual Data
We scraped the Amharic bible from [here](https://bible.org/foreign/amharic/). I built a scraper using BeautifulSoup, which you can see in project-2/scrape.py. I also took the English bible from [here](http://www.vatican.va/archive/bible/genesis/documents/bible_genesis_en.html). There is a cleaning script that helps to align the lines. I could not find an English bible that was as well formatted as this one, so I decided this was sufficient for proof of concept for bible scraping. The cleaned files are in am_clean and eng_clean, which are Amharic and English respectively. 

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

#### Interlinear Glosses
Taken from:
Introductory Grammar of Amharic. Leslau, Wolf. Harrassowitz Verlag, 2000

Scraped freely available parts from partial preview of book at http://books.google.com/books?id=FwGRQChZ91oC

#####Methodology
 It was extremely difficult to find online sources. There are copious amounts of resources in print which contain interlinear glosses, but it is difficult to scrape them. Even getting the glosses out of this book proved to be very challenging. In order to get the characters, I used an Optical Character recognition system provided at http://ocr.ethiocloud.com/ .

However, this was not ideal for three large reasons. First, OCR is inherently noisy. It is especially noisy for Amharic due to the nature of the alphabet. The scans are often not high quality, so it is difficult for the system to differentiate between similar characters. There were two major errors I saw. The system was often unable to see the small inflections on characters. For example, ል would be read as ለ. These types of character differences are integral to the Amharic alphabet, which contributes to the difficulty of a high quality OCR system. the other common mistake was between similar characters such as ሥ and ማ. The "tops" would get cut off of the latter. This applies to all morphologies of these characters. These are the two that were obvious to a non speaker of Amharic, so there were many other errors that I may not have seen. I verified each sentence myself after the OCR and attempted to correct it, but it is certainly necessary to have some understanding of the alphabet to be able to see the nuances. It would be an interesting exercise to crowdsource this type of correction for native Amharic speakers.  

The second main issue was that this OCR system could not read mixed English and Amharic. This greatly limited the speed of scraping. I had to individually crop images to only get the Amharic and feed it into the OCR system: if you had any English in it, the system would crash. If this were availble, it would be far more feasible to scrape entire dictionaries and language books at once. 
The third issue was that this system limited you to 5 queries per day. Obviously, this created issues. 

It is good to note that there has been some reasearch into Amharic OCR. A paper published in 2007 by Million Meshesha and C.V. Jawahar outlines work they have put into building a better system. They were able to achieve high accuracy (~90%) for their test sets, which seems to be better than what I got from this free system.  

If there was a good OCR system such as this, it would be far easier to extract data such as this from the various sources available. 


Optical Character Recognition of Amharic Documents. African Journal of Information and Communication Technology, Vol. 3, No. 2, June 2007



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


