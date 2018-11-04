from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
import codecs
# from wordcloud import WordCloud
import wordcloud

f = open('iphonexcomments.txt','rt')
stoplist = {}.fromkeys([content.strip() for content in open("./stop_word.txt", encoding='UTF-8')])
text = f.read()
#本地存放字体
cut_text = ' '.join(jieba.lcut(text,cut_all= False))
cut_text = [word for word in list(cut_text) if word not in stoplist]

color_mask = imread("iphone.png")
file_write = codecs.open('./cut_text.txt', 'w', 'UTF-8')
for i in range(len(cut_text)):
    file_write.write(str(cut_text[i]) + '\n')
print("Write operation succeeded")
cloud = wordcloud.WordCloud(
    font_path='fzmw.ttf',
    background_color='white',
    mask=color_mask,
    max_words=200,
    max_font_size=5000
)
word_cloud = cloud.generate(cut_text)
plt.imshow(word_cloud)
plt.axis('off')
plt.show()