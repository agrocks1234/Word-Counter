import requests
from bs4 import BeautifulSoup
import operator
def wordcounter(maxpages):
    page=1
    wordlist=[]
    while page<=maxpages:
        url='https://thenewboston.com/forum/recent_activity.php?page='+str(page)
        source=requests.get(url).text
        soup=BeautifulSoup(source,'html.parser')
        for text in soup.findAll('a',{'class':'title text-semibold'}):
            content=text.string
            words = content.lower().split()
            for word in words:
                wordlist.append(word)
        page+=1
    cleanup_list(wordlist)


def cleanup_list(content):
    cleanlist=[]
    for word in content:
        symbol="!@#$%^&*()_+{}|:'<>?/.,;[]\"-='"
        for i in range(0,len(symbol)):
            word=word.replace(symbol[i],"")
        if len(word)>0:
            cleanlist.append(word)
    wordcount(cleanlist)

def wordcount(cleanlist):
    listcount={}
    for word in cleanlist:
        if word in listcount:
            listcount[word]+=1
        else:
            listcount[word]=1
    for key,value in sorted(listcount.items(),key=operator.itemgetter(1)):
        print key,':',value











