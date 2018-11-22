import requests
from bs4 import BeautifulSoup
import webbrowser
from argparse import ArgumentParser

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-c', '--crawler', help="Craw the url", dest="myCrawler")
group.add_argument('-r', '--read', help="read Text File, Enter TXT Name", dest="myTxtFile")
args = parser.parse_args()

if args.myCrawler:
    myUrl = str(args.myCrawler)
    r = requests.get(myUrl)
# r = requests.get('https://forum.gamer.com.tw/C.php?page=25&bsn=32841&snA=5349&subbsn=0')
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')

    with open('out.txt', 'w', encoding='utf-8') as outfile:
        stories = soup.find_all('div', class_='c-article__content')
        for s in stories:
            outfile.write("內文： " + s.text)

    with open('url.txt', 'w', encoding='utf-8') as outfile:
        pict = soup.find_all('a', class_='photoswipe-image')
        for u in pict:
            outfile.write(u.get('href') + "\n")

    f = open('url.txt', 'r')
    result = list()
    for line in open('url.txt'):
        line = f.readline()
        webbrowser.open(line)


if args.myTxtFile:
    myFile = args.myTxtFile
    text = open(myFile, encoding='utf-8')
    print(text.read())



'''
回覆
<article class="reply-content__article c-article "><span>
已領~感謝大大^^</span></article>

內文
<div class="c-article__content">
請自取，謝謝
<a class="photoswipe-image" href="https://truth.bahamut.com.tw/s01/201811/379d14f281812c959a03dde7a643eaf3.JPG">
<img class="lazyload" data-src="https://truth.bahamut.com.tw/s01/201811/379d14f281812c959a03dde7a643eaf3.JPG"></a> 
</div>
</article>

https://forum.gamer.com.tw/C.php?page=25&bsn=32841&snA=5349&subbsn=0
https://forum.gamer.com.tw/C.php?page=26&bsn=32841&snA=5349&subbsn=0
'''
