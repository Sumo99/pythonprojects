from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import smtplib, ssl
opts = Options()
opts.add_argument("--headless")
browser = webdriver.Chrome(options=opts)

browser.get('https://edenprairiemn.infinitecampus.org/campus/portal/eden_prairie.jsp?status=login')
username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')
print(username.get_attribute("innerHTML"))
print(password.get_attribute("innerHTML"))
username.send_keys('redacted')
password.send_keys('********')
form = browser.find_element_by_id('form_signin')
form.submit()
browser.get('https://edenprairiemn.infinitecampus.org/campus/portal/portal.xsl?x=portal.PortalOutline&lang=en&X-XSRF-TOKEN=3c461b67-2cbe-4ead-90fb-0b09c6728e8b&personType=student&context=102036-467-627&personID=102036&studentFirstName=Sukalyan&lastName=Sinha%20Roy&firstName=Sukalyan&schoolID=13&calendarID=467&structureID=627&calendarName=18-19%20Central%20Middle%20School&mode=grades&x=portal.PortalGrades&X-XSRF-TOKEN=3c461b67-2cbe-4ead-90fb-0b09c6728e8b')
time.sleep(2)

geometry_grade=browser.find_element_by_xpath('//*[@id="section_866171_621_open"]/table/tbody/tr[4]/td[4]')
science_grade=browser.find_element_by_xpath('//*[@id="section_865953_621_open"]/table/tbody/tr[4]/td[4]')
soc_studies_grade=browser.find_element_by_xpath('//*[@id="section_866210_621_open"]/table/tbody/tr[4]/td[4]')
health_grade=browser.find_element_by_xpath('//*[@id="section_866148_621_open"]/table/tbody/tr[4]/td[4]')
english_grade=browser.find_element_by_xpath('//*[@id="section_866193_621_open"]/table/tbody/tr[4]/td[4]')

message="The geometry grade is "+geometry_grade.get_attribute("innerHTML")[:8].replace("<"," ")+"\n" #begin collecting the message to send as an email
message+="The science grade is "+science_grade.get_attribute("innerHTML")[:8].replace("<"," ")+"\n" 
message+="The social studies grade is "+soc_studies_grade.get_attribute("innerHTML")[:8].replace("<"," ")+"\n" 
message+="The health grade is "+health_grade.get_attribute("innerHTML")[:8].replace("<"," ")+"\n" 
message+="The english grade is "+english_grade.get_attribute("innerHTML")[:8].replace("<"," ")+"\n" 

print("The geometry grade is "+geometry_grade.get_attribute("innerHTML")[:8].replace("<"," "))
print("The science grade is "+science_grade.get_attribute("innerHTML")[:8].replace("<"," "))
print("The social studies grade is "+soc_studies_grade.get_attribute("innerHTML")[:8].replace("<"," "))
print("The health grade is "+health_grade.get_attribute("innerHTML")[:8].replace("<"," "))
print("The english grade is "+english_grade.get_attribute("innerHTML")[:8].replace("<"," ")) #the english grade does not exist yet!

port = 465  # For SSL
password ="***********"
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("***********@gmail.com", password)
    server.sendmail("jessyveux@gmail.com", "keltunontefonte@gmail.com", "cpucsr@gmail.com",message)
print("Emails sent!")

