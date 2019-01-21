import re
import csv

source = "/Users/ickyv/PycharmProjects/QM/articles/UK_Publications 1-500 jan jun.HTML"
f = open(source, 'r')
s = f.read()

def stripHTMLTags(s):
    regex = '(?s)<style>(.*?)<\/style>'
    pattern = re.compile(regex)
    s = re.sub(pattern, "", s)

    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', s)

    # Replace &quot; with ''
    cleantext = cleantext.replace("&quot;", '"')
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
    cleantext = cleantext.replace("Edition 2; Scotland", "")
    cleantext = cleantext.replace("Second Edition", "")
    cleantext = cleantext.replace("First Edition", "")
    cleantext = cleantext.replace("Third Edition", "")
    cleantext = cleantext.replace("(London)", "")
    cleantext = cleantext.replace("(United Kingdom)", "")
    cleantext = cleantext.replace("(Norwich)", "")
    cleantext = cleantext.replace("(Scotland)", "")
    cleantext = cleantext.replace("- Daily Edition", "")
    cleantext = cleantext.replace("AM", "")
    cleantext = cleantext.replace("PM", "")
    cleantext = cleantext.replace("GMT", "")
    cleantext = cleantext.replace("EST", "")
    cleantext = cleantext.replace("BST", "")
    cleantext = cleantext.replace("12:00", "")
    cleantext = cleantext.replace("12:01", "")
    cleantext = cleantext.replace("3:59", "")
    cleantext = cleantext.replace("7:33", "")
    cleantext = cleantext.replace("7:50", "")
    cleantext = cleantext.replace("7:58", "")
    cleantext = cleantext.replace("5:00", "")
    cleantext = cleantext.replace("6:00", "")
    cleantext = cleantext.replace("6:03", "")
    cleantext = cleantext.replace("5:04", "")
    cleantext = cleantext.replace("6:04", "")
    cleantext = cleantext.replace("1:10", "")
    cleantext = cleantext.replace("6:51", "")
    cleantext = cleantext.replace("6:52", "")
    cleantext = cleantext.replace("10:08", "")
    cleantext = cleantext.replace("10:10", "")
    cleantext = cleantext.replace("10:13", "")
    cleantext = cleantext.replace("10:24", "")
    cleantext = cleantext.replace("10:51", "")
    cleantext = cleantext.replace("10:54", "")
    cleantext = cleantext.replace("10:58", "")
    cleantext = cleantext.replace("5:24", "")
    cleantext = cleantext.replace("12:45", "")
    cleantext = cleantext.replace("12:51", "")
    cleantext = cleantext.replace("12:55", "")
    cleantext = cleantext.replace("1:09", "")
    cleantext = cleantext.replace("1:12", "")
    cleantext = cleantext.replace("1:22", "")
    cleantext = cleantext.replace("1:30", "")
    cleantext = cleantext.replace("1:34", "")
    cleantext = cleantext.replace("8:25", "")
    cleantext = cleantext.replace("8:30", "")
    cleantext = cleantext.replace("8:01", "")
    cleantext = cleantext.replace("9:01", "")
    cleantext = cleantext.replace("2:01", "")
    cleantext = cleantext.replace("2:49", "")
    cleantext = cleantext.replace("4:07", "")
    cleantext = cleantext.replace("4:25", "")
    cleantext = cleantext.replace("9:40", "")
    cleantext = cleantext.replace("9:42", "")
    cleantext = cleantext.replace("9:43", "")
    cleantext = cleantext.replace("4:25", "")
    cleantext = cleantext.replace("3:13", "")
    cleantext = cleantext.replace("3:58", "")
    cleantext = cleantext.replace("3:41", "")
    cleantext = cleantext.replace("5:21", "")
    cleantext = cleantext.replace("12:25", "")
    cleantext = cleantext.replace("12:27", "")
    cleantext = cleantext.replace("10:14", "")
    cleantext = cleantext.replace("5:00", "")
    cleantext = cleantext.replace("5:16", "")
    cleantext = cleantext.replace("5:19", "")
    cleantext = cleantext.replace("6:00", "")
    cleantext = cleantext.replace("6:59", "")
    cleantext = cleantext.replace("10:12", "")
    cleantext = cleantext.replace("9:55", "")
    cleantext = cleantext.replace("4:20", "")
    cleantext = cleantext.replace("11:35", "")
    cleantext = cleantext.replace("11:36", "")
    cleantext = cleantext.replace("4:01", "")
    cleantext = cleantext.replace("2:31", "")
    cleantext = cleantext.replace("4:52", "")
    cleantext = cleantext.replace("3:10", "")
    cleantext = cleantext.replace("11:24", "")
    cleantext = cleantext.replace("10:03", "")
    cleantext = cleantext.replace("4:17", "")
    cleantext = cleantext.replace("3:22", "")
    cleantext = cleantext.replace("3:00", "")
    cleantext = cleantext.replace("8:43", "")
    cleantext = cleantext.replace("7:03", "")
    cleantext = cleantext.replace("8:01", "")
    cleantext = cleantext.replace("11:12", "")
    cleantext = cleantext.replace("5:41", "")
    cleantext = cleantext.replace("7:00", "")
    cleantext = cleantext.replace("3:01", "")
    cleantext = cleantext.replace("5:00", "")
    cleantext = cleantext.replace("4:09", "")
    cleantext = cleantext.replace("8:51", "")
    cleantext = cleantext.replace("2:27", "")
    cleantext = cleantext.replace("11:00", "")
    cleantext = cleantext.replace("6:31", "")
    cleantext = cleantext.replace("9:55", "")
    cleantext = cleantext.replace("11:45", "")
    cleantext = cleantext.replace("1:28", "")
    cleantext = cleantext.replace("5:01", "")
    cleantext = cleantext.replace("6:33", "")
    cleantext = cleantext.replace("11:41", "")
    cleantext = cleantext.replace("11:33", "")
    cleantext = cleantext.replace("11:17", "")
    cleantext = cleantext.replace("5:18", "")
    cleantext = cleantext.replace("10:42", "")
    cleantext = cleantext.replace("5:25", "")
    cleantext = cleantext.replace("9:01", "")
    cleantext = cleantext.replace("12:37", "")
    cleantext = cleantext.replace("11:10", "")
    cleantext = cleantext.replace("6:25", "")
    cleantext = cleantext.replace("8:52", "")
    cleantext = cleantext.replace("7:43", "")
    cleantext = cleantext.replace("6:04", "")
    cleantext = cleantext.replace("11:43", "")
    cleantext = cleantext.replace("11:34", "")
    cleantext = cleantext.replace("5:29", "")
    cleantext = cleantext.replace("6:00", "")
    cleantext = cleantext.replace("8:16", "")
    cleantext = cleantext.replace("10:21", "")
    cleantext = cleantext.replace("3:01", "")
    cleantext = cleantext.replace("10:56", "")
    cleantext = cleantext.replace("11:14", "")
    cleantext = cleantext.replace("1:15", "")
    cleantext = cleantext.replace("3:01", "")
    cleantext = cleantext.replace(" 0", "")
    cleantext = cleantext.replace("3:01", "")
    cleantext = cleantext.replace("12:30", "")
    cleantext = cleantext.replace("9:33", "")
    cleantext = cleantext.replace("1:17", "")
    cleantext = cleantext.replace("1:19", "")
    cleantext = cleantext.replace("10:02", "")
    cleantext = cleantext.replace("10:46", "")
    cleantext = cleantext.replace("4:29", "")
    cleantext = cleantext.replace("2:48", "")
    cleantext = cleantext.replace("12:18", "")
    cleantext = cleantext.replace("11:02", "")
    cleantext = cleantext.replace("12:06", "")
    cleantext = cleantext.replace("11:39", "")
    cleantext = cleantext.replace("1:17", "")
    cleantext = cleantext.replace("12:38", "")
    cleantext = cleantext.replace("10:04", "")
    cleantext = cleantext.replace("2:10", "")
    cleantext = cleantext.replace("2:10", "")
    cleantext = cleantext.replace("6:47", "")
    cleantext = cleantext.replace("2:17", "")
    cleantext = cleantext.replace("10:23", "")
    cleantext = cleantext.replace("11:20", "")
    cleantext = cleantext.replace("11:39", "")
    cleantext = cleantext.replace("4:38", "")
    cleantext = cleantext.replace("1:19", "")
    cleantext = cleantext.replace("8:05", "")
    cleantext = cleantext.replace("3:30", "")
    cleantext = cleantext.replace("2:43", "")
    cleantext = cleantext.replace("4:14", "")
    cleantext = cleantext.replace("8:09", "")
    cleantext = cleantext.replace("12:24", "")
    cleantext = cleantext.replace("10:23", "")
    cleantext = cleantext.replace("8:31", "")
    cleantext = cleantext.replace("10:33", "")
    cleantext = cleantext.replace("12:33", "")
    cleantext = cleantext.replace("7:10", "")
    cleantext = cleantext.replace("12:36", "")
    cleantext = cleantext.replace("2:28", "")
    cleantext = cleantext.replace("8:09", "")
    cleantext = cleantext.replace("7:16", "")
    cleantext = cleantext.replace("3:21", "")
    cleantext = cleantext.replace("12:16", "")
    cleantext = cleantext.replace("4:29", "")
    cleantext = cleantext.replace("12:13", "")
    cleantext = cleantext.replace("9:33", "")
    cleantext = cleantext.replace("10:46", "")
    cleantext = cleantext.replace("3:14", "")
    cleantext = cleantext.replace("11:39", "")
    cleantext = cleantext.replace("6:09", "")
    cleantext = cleantext.replace("1:19", "")
    cleantext = cleantext.replace("5:09", "")
    cleantext = cleantext.replace("6:56", "")
    cleantext = cleantext.replace("5:20", "")
    cleantext = cleantext.replace("4:21", "")
    cleantext = cleantext.replace("7:20", "")
    cleantext = cleantext.replace("12:23", "")
    cleantext = cleantext.replace("4:00", "")
    cleantext = cleantext.replace("6:56", "")
    cleantext = cleantext.replace("2:42", "")
    cleantext = cleantext.replace("9:22", "")
    cleantext = cleantext.replace("4:49", "")
    cleantext = cleantext.replace("8:50", "")
    cleantext = cleantext.replace("9:00", "")
    cleantext = cleantext.replace("1:19", "")
    cleantext = cleantext.replace("8:18", "")
    cleantext = cleantext.replace("5:14", "")
    cleantext = cleantext.replace("2:05", "")
    cleantext = cleantext.replace("5:31", "")
    cleantext = cleantext.replace("11:51", "")
    cleantext = cleantext.replace("12:16", "")
    cleantext = cleantext.replace("10:47", "")
    cleantext = cleantext.replace("2:11", "")
    cleantext = cleantext.replace("5:36", "")
    cleantext = cleantext.replace("1:56", "")
    cleantext = cleantext.replace("9:53", "")
    cleantext = cleantext.replace("8:23", "")
    cleantext = cleantext.replace("6:44", "")
    cleantext = cleantext.replace("12:09", "")
    cleantext = cleantext.replace("3:38", "")
    cleantext = cleantext.replace("9:51", "")
    cleantext = cleantext.replace("2:11", "")
    cleantext = cleantext.replace("8:55", "")
    cleantext = cleantext.replace("6:49", "")
    cleantext = cleantext.replace("12:52", "")
    cleantext = cleantext.replace("9:19", "")
    cleantext = cleantext.replace("5:51", "")
    cleantext = cleantext.replace("6:29", "")
    cleantext = cleantext.replace("11:11", "")
    cleantext = cleantext.replace("10:53", "")
    cleantext = cleantext.replace("9:58", "")
    cleantext = cleantext.replace("3:38", "")
    cleantext = cleantext.replace("2:04", "")
    cleantext = cleantext.replace("2:12", "")
    cleantext = cleantext.replace("12:41", "")
    cleantext = cleantext.replace("5:30", "")
    cleantext = cleantext.replace("5:34", "")
    cleantext = cleantext.replace("4:18", "")
    cleantext = cleantext.replace("6:43", "")
    cleantext = cleantext.replace("7:56", "")
    cleantext = cleantext.replace("9:45", "")
    cleantext = cleantext.replace("12:32", "")
    cleantext = cleantext.replace("8:41", "")
    cleantext = cleantext.replace("7:59", "")
    cleantext = cleantext.replace(".html-embed.component .quote.component{margin-left:0}.html-embed.component .quote.component .component-content{margin-right:16px}.quote__source, .quote__author {white-space: normal;}@media only screen and (min-width:730px){.html-embed.component .quote.component{margin-left:-60.83px}.html-embed.component .quote.component .quote__content:before{margin-left:-12px;padding-right:1px}}@media only screen and (min-width:1008px){.html-embed.component .quote.component{margin-left:-82.33px}}","")


    cleantext = removeDocumentNumber(cleantext)



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


def removeDocumentNumber(text):
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
        elif (line.find("BYLINE:") != -1):
            del textList[counter]
        else:
            line = line.strip()
            if(line != ""):
                s = s + line + '\n'
            counter = counter + 1


    return s


splitBy = "Hide XML section from browser"
articles = s.split(splitBy)

counter = 0

separator = "~"

header = ('"Publication"{}"Article Title"{}"Date"{}"Article Text"'
            .format(separator,separator,separator,separator))
print(header)

for post in articles:
    counter = counter + 1
    if counter >= 2:
        output = stripHTMLTags(post)
        if output != "":
            print('"' + getPublication(output) + '"' + separator, end="")
            print('"' + getArticleTitle(output) + '"' + separator, end="")
            print('"' + getDate(output) + '"' + separator, end="")
            print('"' + getArticleText(output) + '"')

