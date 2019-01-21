# Split by string -> "Hide XML section from browser"

import re


source = "/Users/ickyv/PycharmProjects/QM/articles/UK Publications 1-500 july-dec.HTML"
f = open(source, 'r')
s = f.read()

def stripHTMLTags(s):
    regex = '(?s)<style>(.*?)<\/style>'
    pattern = re.compile(regex)
    s = re.sub(pattern, "", s)

    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', s)

    # Replace reduntant characters and words with ''
    cleantext = cleantext.replace("&quot;" , '"')
    cleantext = cleantext.replace("<!--", "")
    cleantext = cleantext.replace("-->", "")
    cleantext = cleantext.replace("Read more\n", "")
    cleantext = cleantext.replace("&nbsp;", "")
    cleantext = cleantext.replace("&pound;", "£")
    cleantext = cleantext.replace("&bull;", "-")
    cleantext = cleantext.replace("Sunday", "")
    cleantext = cleantext.replace("Monday", "")
    cleantext = cleantext.replace("Tuesday", "")
    cleantext = cleantext.replace("Wednesday", "")
    cleantext = cleantext.replace("Thursday", "")
    cleantext = cleantext.replace("Friday", "")
    cleantext = cleantext.replace("Saturday", "")
    cleantext = cleantext.replace(", 2017", "")
    cleantext = cleantext.replace("Edition 1; Northern Ireland", "")
    cleantext = cleantext.replace("Edition 1; Scotland", "")
    cleantext = cleantext.replace("Edition 1; Ireland", "")
    cleantext = cleantext.replace("Edition 1; National Edition", "")
    cleantext = cleantext.replace("Edition 2; National Edition", "")
    cleantext = cleantext.replace("Edition 3; National Edition", "")
    cleantext = cleantext.replace("Second Edition", "")
    cleantext = cleantext.replace("First Edition", "")
    cleantext = cleantext.replace("Third Edition", "")
    cleantext = cleantext.replace("(London)", "")
    cleantext = cleantext.replace("(United Kingdom)", "")
    cleantext = cleantext.replace("- Daily Edition", "")
    cleantext = cleantext.replace("AM", "")
    cleantext = cleantext.replace("PM", "")
    cleantext = cleantext.replace("GMT", "")
    cleantext = cleantext.replace("EST", "")
    cleantext = cleantext.replace("BST", "")



    cleantext = removereduntantlines(cleantext)



    return cleantext

def getPublication(post):
    postList = post.split('\n')
    return postList[0];

def getArticleTitle(post):
    postList = post.split('\n')
    return postList[2];

def getDate(post):
    postList = post.split('\n')
    return postList[1];

def getArticleText(post):
    postList = post.split('\n')
    counter = 0
    s = ""
    for line in postList:
        if counter >= 6:
            s = s + line.replace("\n", "") + ""
        else:
            counter = counter + 1

    return(s)


def removereduntantlines(text):
    textList = text.split('\n')
    counter = 0
    s = ""
    for line in textList:
        if(line.find("of 500 DOCUMENTS") != -1):
            del textList[counter]
        elif(line.find("LOAD-DATE") != -1):
            del textList[counter]
        elif (line.find("LANGUAGE") != -1):
            del textList[counter]
        elif (line.find("PUBLICATION-TYPE") != -1):
            del textList[counter]
        elif (line.find("JOURNAL-CODE:") != -1):
            del textList[counter]
        elif (line.find("Copyright") != -1):
            del textList[counter]
        else:
            line = line.strip()
            if(line != ""):
                s = s + line + '\n'
            counter = counter + 1

    return s


#Setting the sentence that divides each of the articles from the others
splitBy = "Hide XML section from browser"
articles = s.split(splitBy)

counter = 0


#Setting the separator for the csv file
separator = "~"

header = ('"Publication"{}"Article Title"{}"Date"{}"Article Text"'
            .format(separator,separator,separator,separator))
print(header)
#Preparing the articles for saving into a csv file
for post in articles:
    counter = counter + 1
    if counter >= 2:
        output = stripHTMLTags(post)
        if output != "":
            print('"' + getPublication(output) + '"' + separator, end="")
            print('"' + getArticleTitle(output) + '"' + separator, end="")
            print('"' + getDate(output) + '"' + separator, end="")
            print('"' + getArticleText(output) + '"')
