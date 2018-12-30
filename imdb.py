import urllib.request
import re
from bs4 import BeautifulSoup
def parseYear(year):
    regex = re.compile(r"(?<!\d)\d{4,7}(?!\d)") #match any run of four or more numbers
    return regex.search(year).group(0)
def removeTags(tags): #pretty things up by removing html tags
     result=re.sub('<[^>]*>','', tags)
     result =re.sub('\n',  ' ',result)
     result=re.sub('&lt', '<',result)
     result=re.sub('&gt', '>',result)
     return result
string=input("Enter the name of the IMDB movie you are looking for \n")
string=string.replace(" ","+") #format the string and replace the space with the plus
string_url="https://www.imdb.com/find?q="+string+"&s=tt" #the url where we can find the movie
print(string_url)
fetch=urllib.request.urlopen(string_url)
soup = BeautifulSoup(fetch, 'html.parser')
noResults=False #if the movie does not have any results
if(len(soup.find_all('div', class_="findNoResults"))>0):#this means that there are no results for the movie
    print("There are no movies with name "+string)
total=0
for link in soup.find_all(class_="result_text"):
    total=total+1
    url_to_visit="https://www.imdb.com"+link.a.get('href')
    fetch=urllib.request.urlopen(url_to_visit)
    soup = BeautifulSoup(fetch, 'html.parser') #begin looking at the new link
    for child in soup.find_all(class_="title_bar_wrapper"):
        print("The title is "+str(soup.find("h1").contents[0]))
        if(soup.find("div", class_="ratingValue") is not None): #for things yet to be released that do not have a rating
            print("The rating is "+ str(soup.find("div", class_="ratingValue").contents[1]["title"]))
            print() #for better formatting
        if(soup.find("div",class_="subtext") is not None):
           string=str(soup.find("div",class_="subtext"))
           string=removeTags(string).strip().replace(" ","").split("|") #remove the tags and whitespace and split into an an array
           print(string)
           print()
        if(len(soup.find("h1").contents)>1 ): 
            print("It was released in "+parseYear(str(soup.find("h1").contents[1]))+"\n")#the h1 element includes a date as well
            print()
        if(soup.find("div" ,class_="inline canwrap") is not None): #there is a plot description
           PlotSummary=str(soup.find("div" ,class_="inline canwrap").contents[1])[14:]
           print(removeTags(PlotSummary))
           print()
print("There are this many results: "+str(total)+ "for "+string )
