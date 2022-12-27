from bs4 import BeautifulSoup
import requests
import string

def wikibot(url,inp2):
    html_text=requests.get(url).text
    soup=BeautifulSoup(html_text,'html.parser')
    short_description=soup.find('div',class_='shortdescription nomobile noexcerpt noprint searchaux').text
    with open(inp2,'w', encoding="utf-8") as f: 
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
        try:
            inp1=input("search the wikipedia : ")
            name=string.capwords(inp1)
            lst_name=name.split()
            fnl_name='_'.join(lst_name)
            url="https://en.wikipedia.org/wiki/"+fnl_name
            inp2=input('''enter the destination path where you want to store your data and file name in this format(F:/python/projects/ML/search results.txt):\n''')
            wikibot(url,inp2)
        except Exception as e:
            print(f'''The thing you are searching for is not on wikipedia.Please try searching another word Thank you''')
        finally:
            press_button=input("Press enter to search more (q to quit):\n")
            if press_button=='q':
                exit()
    