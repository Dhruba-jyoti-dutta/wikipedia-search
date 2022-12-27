from bs4 import BeautifulSoup
import requests
import string
def wikibot(url,inp):
    html_text=requests.get(url).text
    soup=BeautifulSoup(html_text,'html.parser')
    short_description=soup.find('div',class_='shortdescription nomobile noexcerpt noprint searchaux').text
    with open(inp,'w', encoding="utf-8") as f: 
        f.write(f"{name} is a {short_description}\n")
        f.write("\n")
        details=soup.find_all('table',class_='infobox') 
        for detail in details:
            h=detail.find_all('tr')
            for j in h:
                heading=j.find_all('th')
                description=j.find_all('td')
                for x,y in zip(heading,description):
                    f.write(f"{x.text} :: {y.text} \n")
        for k in range(1,4):
            f.writelines(f"{soup.find_all('p')[k].text}")
if __name__=="__main__":
    while True:
        i=input("search the wikipedia : ")
        name=string.capwords(i)
        lst=name.split()
        fnl='_'.join(lst)
        url="https://en.wikipedia.org/wiki/"+name
        inp=input('''enter the destination path where you want to store your
    data and file name in this format(F:/python/projects/ML/search results.txt):\n''')
        wikibot(url,inp)

        #try wikipedia 
        # except