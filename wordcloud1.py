from wordcloud import WordCloud
import matplotlib.pyplot as plt

#https://github.com/amueller/word_cloud

positive = open('neutral_bridge.txt', "r").read()


# Generating word cloud
wc = WordCloud(background_color="black", max_font_size=50, min_font_size=10, max_words=10000).generate(positive)

# Display the generated image
plt.figure(figsize=[10,10])
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# Save the image in the img folder
wc.to_file("/Users/ickyv/PycharmProjects/QM/twitter/wordcloud/London bridge attack/neutral_wordcloud.png")


