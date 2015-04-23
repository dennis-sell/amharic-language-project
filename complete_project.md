Amharic 
======= 
####CIS 526 Language Project
######Joyce Lee, Adnaan Mukadam, Dennis Sell, Evelyn Yeung

####Language Features - Syntax and Morphology  
The Amharic language has the order SOV (Subject, Object, Verb). Hence, to say “Ethiopia is in Africa.”, a speaker of Amharic would say what literally translates to “Ethiopia Africa inside is.” Additionally, adjectives, demonstratives, and numerals come before the nouns which they modify. The order of words in Amharic appears to be mostly fixed.

There is a large amount of inflection used in the language. Most inflections appear at the end of words, taking on the form of a suffix. Verbs must agree with their subject in person, number, and gender through the verbs inflection. Verbs can also have suffixes to indicate the object(s). The rules for how to put together the verb vary depending on their usage. For example, the subject agreement is expressed through suffixes alone in the perfect and gerund category, and it uses a mix of both prefixes and suffixes for the imperfect and imperative. Amharic is considered to be a null subject language, which means that it does not require an explicit subject, and often only uses personal pronouns as subjects for emphasis.

Additionally, nouns often take on suffixes for various reasons. Nouns can have inflections to show possession. There is a suffix corresponding to each of the pronouns in Amharic. For example,  -wa is the suffix for “her” and would be placed onto the end of the end of a noun to indicate the noun belongs to an unspecified female (or feminine noun). Nouns will usually take on the suffix -očč to be made plural (which is referred to as the normal method), although there is another way to make it plural by changing the end of the root of the word. For example, bet 'house' becomes bet-očč 'houses'. Showcasing the second method of pluralization, wäyzäro 'lady' can take the normal plural, yielding wäyzär-očč, but it can also become wäyzazər.
 
Genders in Amharic in many ways resemble the genders in Romance languages. There are exactly two genders and all nouns have genders. Certain nouns use suffixes to change the gender - such as the suffix  -it. For example, the word for “child“ or “boy” - “lǝǧ-it” - is altered to become “girl” - “lǝǧ-it”. 

As for pronouns, they distinguish between number (singular vs plural) and person (first, second, or third). Additionally, certain pronouns distinguish for the two genders and have a formal form. Specifically, he/she and you sg. female and male versions. The pronouns which have a form for politeness are you (for any gender and number) and he/she. The total list of pronouns in Amharic, ordered by person, is:  

  - I, we
  - you (male, singular), you (female, singular), you (polite),  you (plural)
  - he, she, he/she (polite), they 

####Language Demographics

Amharic is the language of the Amhara people, an ethnic group from the highlands of Ethiopia. According to a census in 2013, there are almost 22 million native speakers and 4 million second language speakers. 21.6 million of them reside in Ethiopia, where it is still commonly used. There are also emigrants in Egypt, Israel, and the USA which comprise the rest of the population of speakers.  

Though Amharic is the official language of Ethiopia, it is the second most commonly known language in the country, second to Oromo, in a country where over 90 individual languages are spoken. Because it was developed in the capital Addis Ababa and the Amhara region for use as the official language, there exist few dialects. It was the lingua franca, the method for trade and everyday communique since the 1600s. Influences on the language were exerted by those of the Cushitic family in its lexicon, syntax, and typography.  
The people of Ethiopia who are able to afford higher education are bilingual. Though primary schools once were taught only in Amharic, they are now taught in local languages such as Oromo and Tingrinya. All higher education, including secondary school and universities, are taught in English. Exposure to other languages is minimal outside of an academic setting.  
The range percentage of Amharic speakers throughout the regions of Ethiopia varies greatly. Amhara has 74% of all Amharic speakers, and 93% of the region speak the language. Regions like Tigray and Somali have very low percentages of Amharic speakers, less that 1%. Other regions like Benishangul-Gumuz , Dire Dawa, and Harari have few people who speak Amaharic, but the speakers form a quarter of their population.

![alt text](http://mapping.febinfo.org/peoples/map_amh.gif "Amharic speakers in the world")  
Sources:  
aboutworldlanguages.com/amharic  
http://mapping.febinfo.org/peoples/map_amh.gif  
http://www.languagesgulper.com/eng/Amharic.html


####Writing System

The Amharic script is an abugida / alphasyllabary (consonant-vowel sequences are written together as one unit, as opposed to a full alphabet where vowels and consonants are written separately). The characters of the system are called fidel, and a font that supports Amharic, such as GF Zemen Unicode, is needed to see fidel on modern computers. The basic shape of each character is determined by the consonant sound in it. So for example, the l-vowel family of characters is:

ለ  - represents the sound ‘lə’  
ሉ - represents ‘lu’  
ሊ - represents ‘li’  
ላ - represents ‘la’  
ሌ - represents ‘le’  


Originally written from right to left like other Semitic languages, Amharic eventually switched to a left to right system. Changing consonant length (gemination) in Amharic can change the meaning of words, for example “ala” means “he said”, but “alla” means “there is”. Gemination is, however, not indicated in Amharic orthography, and readers must infer meaning from context. 

Ethiopia has a literacy rate of 39%, so it can probably be assumed that an even smaller fraction is able to write Amharic. There are several software systems than enable Amharic to be typed on a computer, and Google has added it to its Language Tools, allowing it to be typed without an Amharic keyboard. 

The bible has been translated into Amharic, and the most famous novel in the language is Fiqir Iske Meqabir (english title is roughly “Love unto Crypt”).

####Existing Systems for Transliteration/Translation of Amharic 

Machine Translation of Amharic

There is one online machine transliteration system, annotated with:

Note: The image above represents one of many possible "transliterations" of the given text into Amharic characters. We do not guarantee its accuracy, it is provided for entertainment purposes only.

An example output of the Wikipedia sentence:

    Amharic is a Semitic language spoken in Ethiopia. It is the second-most spoken Semitic language in the world.

transliterates into  
![alt text](http://www.stwing.upenn.edu/~fifi/amharic.png "Amharic Transliteration using Google")  

It is important to note that the above is a transliteration of the input and not an actual translation.

Transliteration tool: http://www.google.com/intl/am/inputtools/try/

#####Analyzing Amharic: 

There is a group that has attempted to create extensible dependency grammar (XDG) graphs for the language. This means they analyze a sentence at multiple dimensions, such as the syntactic or semantic dimensions.   
http://www.cs.indiana.edu/~gasser/Research/software.html   

Run morphological parser to stem all words in sentence, since there are so many different morphologies. This parser returns root, and all possible grammatical analyses based on the structure. This morphological parser is the foundation for their XDG builder, which offers many insights into the structure of the sentence, including parts of speech.  


The amount of verb morphologies, including the lack of explicit subjects presents a problem, similar to issues that came up in alignment.. Building an XDG relies on explicit inputs, so they used “empty nodes” in the syntactic dimension, like the null token in alignment. They have various rules based on the information returned from the parser.  


There is much discussion in the paper about rules they impose while building the graph that reflect the language. One interesting example is their method of modeling a relative clause by making the sentence a directed acyclic graph in which “the shared noun has multiple verb heads.”  
![alt text](http://www.stwing.upenn.edu/~fifi/sexy_xdg_dag.png "XDG relative clause")  
Gasser, Figure 5: Syntactic analysis of a sentence with a relative clause 


Papers:  

http://mt-archive.info/LREC-2006-Amsalu-2.pdf  
http://www.mica.edu.vn/sltu2012/files/proceedings/8.pdf (this one is stat MT)  
http://www.cs.indiana.edu/~gasser/AfLaT12/#(1) (this one is syntax)  
http://www.mt-archive.info/10/LREC-2010-Gasser.pdf  

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