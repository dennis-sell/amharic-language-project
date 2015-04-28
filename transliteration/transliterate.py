#!/usr/bin/env python3


translator_string = """ ሀ   ሁ   ሂ   ሃ   ሄ   ህ   ሆ
   ha  hu  hi  ha  he  h ho
   ለ   ሉ   ሊ   ላ   ሌ   ል   ሎ
   le  lu  li  la  le  l lo
   ሐ   ሑ   ሒ   ሓ   ሔ   ሕ   ሖ
   ha  hu  hi  ha  he  h ho
   መ   ሙ   ሚ   ማ   ሜ   ም   ሞ
   me  mu  mi  ma  me  m mo
   ሠ   ሡ   ሢ   ሣ   ሤ   ሥ   ሦ
   se  su  si  sa  se  s so
   ረ   ሩ   ሪ   ራ   ሬ   ር   ሮ
   re  ru  ri  ra  re  r ro
   ሰ   ሱ   ሲ   ሳ   ሴ   ስ   ሶ
   se  su  si  sa  se  s so
   ሸ   ሹ   ሺ   ሻ   ሼ   ሽ    ሾ
   ʃe  ʃu  ʃi  ʃa  ʃe  ʃ ʃo
   ቀ   ቁ   ቂ   ቃ   ቄ   ቅ    ቆ
   k’e k’u k’i k’a k’e k’ k’o
   በ   ቡ   ቢ   ባ   ቤ   ብ    ቦ
   be  bu  bi  ba  be  b bo
   ተ   ቱ   ቲ   ታ   ቴ   ት   ቶ
   te  tu  ti  ta  te  t to
   ቸ   ቹ   ቺ   ቻ   ቼ   ች    ቾ
   ʧe  ʧu  ʧi  ʧa  ʧe  ʧ ʧo
   ኀ   ኁ   ኂ   ኃ   ኄ   ኅ    ኆ
   ha  hu  hi  ha  he  h ho
   ነ   ኑ   ኒ   ና   ኔ   ን   ኖ
   ne  nu  ni  na  ne  n no
   ኘ   ኙ   ኚ   ኛ   ኜ   ኝ   ኞ
   ɲe  ɲu  ɲi  ɲa  ɲe  ɲ ɲo
   አ   ኡ   ኢ   ኣ   ኤ   እ   ኦ
   a  u  i  a  e  ə  o
   ከ   ኩ   ኪ   ካ   ኬ   ክ   ኮ
   ke  ku  ki  ka  ke  k ko
   ኸ   ኹ   ኺ   ኻ   ኼ   ኽ   ኾ
   he  hu  hi  ha  he  h    ho
   ወ   ዉ   ዊ   ዋ   ዌ   ው   ዎ
   we  wu  wi  wa  we  w    wo
   ዐ   ዑ   ዒ   ዓ   ዔ   ዕ   ዖ
   a  u  i  a  e   ʔ   o
   ዘ   ዙ   ዚ   ዛ   ዜ   ዝ   ዞ
   ze  zu  zi  za  ze  z    zo
   ዠ   ዡ   ዢ   ዣ   ዤ   ዥ   ዦ
   ʒe  ʒu  ʒi  ʒa  ʒe  ʒ    ʒo
   የ   ዩ   ዪ   ያ   ዬ   ይ   ዮ
   je  ju  ji  ja  je  j    jo
   ደ   ዱ   ዲ   ዳ   ዴ   ድ   ዶ
   de  du  di  da  de  d    do
   ጀ   ጁ   ጂ   ጃ   ጄ   ጅ   ጆ
   je  ju  ji  ja  je  j    jo
   ገ   ጉ   ጊ   ጋ   ጌ   ግ   ጎ
   ge  gu  gi  ga  ge  g    go
    ጠ   ጡ   ጢ   ጣ   ጤ   ጥ   ጦ
   t’e t’u t’i t’a t’e t’   t’o
   ጨ   ጩ   ጪ   ጫ   ጬ   ጭ   ጮ
   ʧ’e ʧ’u ʧ’i ʧ’a ʧ’e ʧ’   ʧ’o
   ጰ   ጱ   ጲ   ጳ   ጴ   ጵ   ጶ
   p’e p’u p’i p’a p’e p’   p’o
   ጸ   ጹ   ጺ   ጻ   ጼ   ጽ   ጾ
   ts’e    ts’u    ts’i    ts’a    ts’e    ts’  ts’o
   ፀ   ፁ   ፂ   ፃ   ፄ   ፅ   ፆ
   ts’e    ts’u    ts’i    ts’a    ts’e    ts’  ts’o
   ፈ   ፉ   ፊ   ፋ   ፌ   ፍ   ፎ
   fe  fu  fi  fa  fe  f    fo
   ፐ   ፑ   ፒ   ፓ   ፔ   ፕ   ፖ
   pe  pu  pi  pa  pe  p    po
   ቨ   ቩ   ቪ   ቫ   ቬ   ቭ   ቮ
   ve  vu  vi  va  ve  v    vo
   ቊ   ቋ   ቌ   ቍ   ኊ   ኋ   ኌ   ኍ   ኲ   ኳ   ኴ   ኵ   ጒ
   k’ʷi    k’ʷa    k’ʷe    k’ʷi    hʷi hʷa hʷe hʷi kʷi kʷa kʷe kʷi gʷi
   ጓ   ጔ   ጕ   ሏ   ቧ   ዟ   ጧ   ሟ   ቷ   ዧ   ጯ   ሯ   ቿ
   gʷa gʷe gʷi lʷa bʷa zʷa t’ʷa    mʷa tʷa ʒʷa ʧ’ʷa    rʷa ʧʷa
   ጇ   ጿ   ሷ   ኗ   ዷ   ፏ   ሿ   ኟ   ፘ   ፙ   ፚ   ኧ
   jʷa ts’ʷa   sʷa nʷa dʷa fʷa ʃʷa ɲʷa rʲa nʲa fʲa e"""

lines = translator_string.split("\n")
words = [line.split() for line in lines]

am_to_en = {' ': ' '}
en_to_am = {' ': ' '}
for x in range(int(len(words)/2)):
    amharic = words[2*x]
    english = words[2*x+1]
    for am, en in zip(amharic, english):
        am_to_en[am] = en
        en_to_am[en] = am


# Test this out
amharic_titles = [line.strip().split("\t")[1] for line in open("en-am_titles.txt", "r")]
for title in amharic_titles:
    english_word = "".join([am_to_en[c] if c in am_to_en else "*" for c in title])
    print(english_word)

