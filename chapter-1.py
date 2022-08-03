from nltk.book import *

print('\n\n concordance in text1')
text1.concordance('monstrous')
print('\n\n concordance in text2')
text2.concordance('monstrous')
print('\n\n similiar in text1')
text1.similar('monstrous')
print('\n\n common_contexts in text1 for \'monstrous\', \'curious\'')
text1.common_contexts(['monstrous', 'curious'])