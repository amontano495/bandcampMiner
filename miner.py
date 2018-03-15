import os,re,urllib2,sys
from bs4 import BeautifulSoup

# Search by tag
basePage = 'https://bandcamp.com/tag/'

# Prompt for a tag
tag = sys.argv[1]

# URL for albums w/ this tag
albumsByTag = basePage + tag

page = urllib2.urlopen(albumsByTag)
soup = BeautifulSoup(page, 'html.parser')

albumURLs = soup.find_all('a',{'href': re.compile('/album/[a-zA-Z0-9]*')})


for i in range(5):
    print albumURLs[i]['href']
    command = 'soundscrape ' + albumURLs[i]['href'] + ' -b -f'
    os.system(command)

ignoreThis1 = 'mv ./miner.py ../'
ignoreThis2 = 'mv ./Pipfile ../'
makeDir = 'mkdir ~/Music/' + tag
moveEverything = 'mv * ~/Music/' + tag
bringBack1 = 'mv ../miner.py .'
bringBack2 = 'mv ../Pipfile .'

os.system(ignoreThis1)
os.system(ignoreThis2)
os.system(makeDir)
os.system(moveEverything)
os.system(bringBack1)
os.system(bringBack2)
