import requests
from bs4 import BeautifulSoup
allUniv = []
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r. text
    except:
        return""

def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)

        allUniv.append(singleUniv)

def printUnivList(name,rank):
    count = 0
    print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}{5:{0}^10}".format(chr(12288),"排名","学校","名称","省市","总分","培养规模"))
    for u in allUniv:
        if name in u[1]:
            print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}{5:{0}^10}".format(chr(12288),u[0],u[1],u[2],u[3],u[4]))
            count += 1
            if count == rank:
                break

def main(p,rank):
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html,'html.parser')
    fillUnivList(soup)
    printUnivList(p,rank)
main('交通',20)
