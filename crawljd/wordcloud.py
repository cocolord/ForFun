from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
#import wordcloud

f = open('/home/dong/Documents/iphonexcomments.txt','rt')
text = f.read()
#本地存放字体
cut_text = ' '.join(jieba.lcut(text))
print(cut_text)
color_mask = imread("/home/dong/Downloads/iphone.png")
cloud = WordCloud(
    font_path='/home/dong/Downloads/fzmw.ttf',
    background_color='white',
    mask=color_mask,
    max_words=200,
    max_font_size=5000
)
word_cloud = cloud.generate(cut_text)
plt.imshow(word_cloud)
plt.axis('off')
plt.show()