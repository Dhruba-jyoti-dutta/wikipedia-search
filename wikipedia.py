from bs4 import BeautifulSoup
import requests
import string

i=input("search the wikipedia : ")
name=string.capwords(i)

lst=name.split()
fnl='_'.join(lst)
# print(fnl)
url="https://en.wikipedia.org/wiki/"+name
# html_text=requests.get(url).text
# print(html_text)
def wikibot(url):
    html_text=requests.get(url).text
    soup=BeautifulSoup(html_text,'html.parser')
    short_description=soup.find('div',class_='shortdescription nomobile noexcerpt noprint searchaux').text
    # long_description=soup.find('div',class_='mw-body-content mw-content-ltr').text
    # long_description=long_description.encode("utf8")
    #a=long_description[:2000]
    #print(a)
    # details=soup('table',class_='infobox')
    # for detail in details:
    #     h=detail.find_all('tr')
    #     for j in h:
    #         heading=j.find_all('th')
    #         description=j.find_all('td')
    #         #if heading is not None and description is not None:
    #         for x,y in zip(heading,description):
    #             print(f"{x.text} :: {y.text} \n")
    
    # for k in range(1,4):
    #     print(soup('p')[k].text)
    with open('F:/python/projects/ML/search results.txt','w', encoding="utf-8") as f:  #with write mode the txt file content gets deleted every time
        # i run the program but if we use append mode it doesnot get deleted   #encoding logaisu karon 
        f.write(f"{name} is a {short_description}\n")
        f.write("\n")
        details=soup.find_all('table',class_='infobox')  #or soup('table',class_='infobox') dileu kam kore
        for detail in details:
            h=detail.find_all('tr')
            for j in h:
                heading=j.find_all('th')
                description=j.find_all('td')
                #if heading is not None and description is not None:
                for x,y in zip(heading,description):
                    f.write(f"{x.text} :: {y.text} \n")
        for k in range(1,4):
            # a=soup.find_all('p')[k].text
            # l=100
            # a=a.insert(100,'\n')
            # # while i<len(a):
            f.writelines(f"{soup.find_all('p')[k].text}")
        # f.write(f" {name}: \n {long_description}\n")
        
    # dont_want1=soup.find('table',class_='infobox biography vcard').text
    # print(dont_want1)
    # dont_want2=soup.find('div',class_='hatnote navigation-not-searchable').text
    # # a=soup.long_description.p
    # print(long_description)
    # print(f" {name} is a {short_description}")



wikibot(url)