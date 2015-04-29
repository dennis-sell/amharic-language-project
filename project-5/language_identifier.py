# must be run using python 3

# given a text file as input, outputs  1 if text is amharic, 2 if text is amharic-like and 0 if text is not amharic

import sys

char_string = """ ሀ   ሁ   ሂ   ሃ   ሄ   ህ   ሆ
   ለ   ሉ   ሊ   ላ   ሌ   ል   ሎ
   ሐ   ሑ   ሒ   ሓ   ሔ   ሕ   ሖ
   መ   ሙ   ሚ   ማ   ሜ   ም   ሞ
   ሠ   ሡ   ሢ   ሣ   ሤ   ሥ   ሦ
   ረ   ሩ   ሪ   ራ   ሬ   ር   ሮ
   ሰ   ሱ   ሲ   ሳ   ሴ   ስ   ሶ
   ሸ   ሹ   ሺ   ሻ   ሼ   ሽ    ሾ
   ቀ   ቁ   ቂ   ቃ   ቄ   ቅ    ቆ
   በ   ቡ   ቢ   ባ   ቤ   ብ    ቦ
   ተ   ቱ   ቲ   ታ   ቴ   ት   ቶ
   ቸ   ቹ   ቺ   ቻ   ቼ   ች    ቾ
   ኀ   ኁ   ኂ   ኃ   ኄ   ኅ    ኆ
   ነ   ኑ   ኒ   ና   ኔ   ን   ኖ
   ኘ   ኙ   ኚ   ኛ   ኜ   ኝ   ኞ
   አ   ኡ   ኢ   ኣ   ኤ   እ   ኦ
   ከ   ኩ   ኪ   ካ   ኬ   ክ   ኮ
   ኸ   ኹ   ኺ   ኻ   ኼ   ኽ   ኾ
   ወ   ዉ   ዊ   ዋ   ዌ   ው   ዎ
   ዐ   ዑ   ዒ   ዓ   ዔ   ዕ   ዖ
   ዘ   ዙ   ዚ   ዛ   ዜ   ዝ   ዞ
   ዠ   ዡ   ዢ   ዣ   ዤ   ዥ   ዦ
   የ   ዩ   ዪ   ያ   ዬ   ይ   ዮ
   ደ   ዱ   ዲ   ዳ   ዴ   ድ   ዶ
   ጀ   ጁ   ጂ   ጃ   ጄ   ጅ   ጆ
   ገ   ጉ   ጊ   ጋ   ጌ   ግ   ጎ
    ጠ   ጡ   ጢ   ጣ   ጤ   ጥ   ጦ
   ጨ   ጩ   ጪ   ጫ   ጬ   ጭ   ጮ
   ጰ   ጱ   ጲ   ጳ   ጴ   ጵ   ጶ
   ጸ   ጹ   ጺ   ጻ   ጼ   ጽ   ጾ
   ፀ   ፁ   ፂ   ፃ   ፄ   ፅ   ፆ
   ፈ   ፉ   ፊ   ፋ   ፌ   ፍ   ፎ
   ፐ   ፑ   ፒ   ፓ   ፔ   ፕ   ፖ
   ቨ   ቩ   ቪ   ቫ   ቬ   ቭ   ቮ
   ቊ   ቋ   ቌ   ቍ   ኊ   ኋ   ኌ   ኍ   ኲ   ኳ   ኴ   ኵ   ጒ
   ጓ   ጔ   ጕ   ሏ   ቧ   ዟ   ጧ   ሟ   ቷ   ዧ   ጯ   ሯ   ቿ
   ጇ   ጿ   ሷ   ኗ   ዷ   ፏ   ሿ   ኟ   ፘ   ፙ   ፚ   ኧ"""


lines = char_string.split("\n")
amh_lines = [line.split() for line in lines]

# characters used in other Ge'ez alphabets, but not amharic
other_geez = ['ቐ', 'ቘ', 'ⶓ', 'ጘ']

amharic_chars = []
for line in amh_lines:
    amharic_chars += line

total_count = 0
amharic_count = 0
amharicLike_count = 0

for line in sys.stdin:
    for char in line:
        if not char.isspace(): # only count actual character
            total_count += 1
        if char in amharic_chars:
            amharic_count += 1
        elif char in other_geez:
            amharicLike_count += 1


# check if more than 95% of input is writting with Ge'ez characters
if (amharic_count + amharicLike_count) / float(total_count) > .95:
    # if these characters are present, text is 'amharic-like' but not actual amharic
    if amharicLike_count > 0:
        sys.stdout.write("2\n")
    # text is amharic
    else:
        sys.stdout.write("1\n")

# not enough Ge'ez characters to be amharic
else:
    sys.stdout.write("0\n")


