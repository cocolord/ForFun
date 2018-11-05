#encoding: utf-8
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
import codecs
from snownlp import SnowNLP
# from wordcloud import WordCloud
import wordcloud
#read text
f = open('iphonexcomments.txt','rt')
stoplist = {}.fromkeys([content.strip() for content in open("./stop_word.txt")])
text = f.read()

cut_text = ' '.join(jieba.lcut(text,cut_all = True))
cut_text = [word for word in list(cut_text) if word not in stoplist]

color_mask = imread("iphone.png")
####################
file_write = codecs.open('./cut_text.txt', 'w', 'utf-8')
for i in range(len(cut_text)):
    file_write.write(cut_text[i] + '\n')
print("Write operation succeeded")
####################
cloud = wordcloud.WordCloud(
    font_path='fzmw.ttf',
    background_color='white',
    mask=color_mask,
    max_words=200,
    max_font_size=5000
)

cut_text_str = ''.join(cut_text)
cut_text_str_nlp  = SnowNLP(cut_text_str)
cut_text_keywords = cut_text_str_nlp.keywords(limit=100)
cut_text_keywords_str = ''.join(cut_text_keywords)
word_cloud = cloud.generate(cut_text_str)
print (cut_text_str_nlp.summary(limit=20))
print (cut_text_keywords)
plt.imshow(word_cloud)
plt.axis('off')
plt.show()
