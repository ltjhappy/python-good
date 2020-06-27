import jieba
import wordcloud
c = wordcloud.WordCloud(font_path='STFANGSO.TTF')
c.generate("李琳 李天军 陈心怡 艾春伶 SenseTime Love 2016")
c.to_file("love.png")