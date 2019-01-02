import urllib.request
import re
from bs4 import BeautifulSoup
import sys
import getopt
import itertools
def parseYear(year):
    regex = re.compile(r"(?<!\d)\d{4,7}(?!\d)") #match any run of four or more numbers
    return regex.search(year).group(0)
def removeTags(tags): #pretty things up by removing html tags
     result=re.sub('<[^>]*>','', tags)
     result =re.sub('\n',  ' ',result) #trim newlines
     result=re.sub('&lt', '<',result) 
     result=re.sub('&gt', '>',result)
     return result
Rating=0.0
TotalNumber=250
def main(argv): #provide a command line interface
    print("welcome to the imdb scraper")
    print("n is the number of movies you want to see, r is the minimum rating of the movie")
    opt=""
    try:
      global TotalNumber
      global Rating
      opts, args = getopt.getopt(sys.argv[1:] ,"hn:r:p:")
      TotalNumber=int(opts[0][1]) #update the global variable instead of the local variable
      Rating=float(opts[1][1])
    except Exception as e:
      print("n is the number of movies you want to see, r is the minimum rating of the movie")
string=input("Enter the name of the IMDB movie you are looking for \n")
string=string.replace(" ","+") #format the string and replace the space with the plus
string_url="https://www.imdb.com/find?q="+string+"&s=tt" #the url where we can find the movie
print(string_url)
fetch=urllib.request.urlopen(string_url)
soup = BeautifulSoup(fetch, 'html.parser')
main(sys.argv)
noResults=False #if the movie does not have any results
if(len(soup.find_all('div', class_="findNoResults"))>0):#this means that there are no results for the movie
    print("There are no movies with name "+string)
total=0
for link in itertools.islice(soup.find_all(class_="result_text"),0,TotalNumber):
    url_to_visit="https://www.imdb.com"+link.a.get('href')
    fetch=urllib.request.urlopen(url_to_visit)
    soup = BeautifulSoup(fetch, 'html.parser') #begin looking at the new link
    for child in soup.find_all(class_="title_bar_wrapper"):
        print("The title is "+str(soup.find("h1").contents[0]))
        if(soup.find("div", class_="ratingValue") is not None): #for things yet to be released that do not have a rating
            print("The rating is "+ str(soup.find("div", class_="ratingValue").contents[1]["title"]))
            rating_value=float(soup.find("div", class_="ratingValue").contents[1]["title"][0:3])
            if(rating_value<Rating): #if the rating is too low
               break
            print() #for better formatting
            total=total+1
        if(soup.find("div",class_="subtext") is not None):
           description_string=str(soup.find("div",class_="subtext"))
           subtext_string=removeTags(description_string).strip().replace(" ","").split("|") #remove the tags and whitespace and split into an an array
           print(str(subtext_string))
           print()
        if(len(soup.find("h1").contents)>1 ): 
            print("It was released in "+parseYear(str(soup.find("h1").contents[1]))+"\n")#the h1 element includes a date as well
            print()
        if(soup.find("div" ,class_="inline canwrap") is not None): #there is a plot description
           PlotSummary=str(soup.find("div" ,class_="inline canwrap").contents[1])[14:] 
           print(removeTags(PlotSummary))
           print()
print("There are this many results: "+ str(total)+" for the query "+string)

