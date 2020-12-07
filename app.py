from flask import render_template                                                                                       
from flask import Flask                                                                                                 
from flask import request                                                                                               
import mariadb                                                                                                          
import os                                                                                                                                                                                                                                       
app = Flask(__name__)                                                                                                                                                                                                                           
conn = mariadb.connect(user='flask', password='pass', host='localhost', port=3306, database='zipCodes')                
curr = conn.cursor()                                                                                                                                                                                                                            
@app.route('/')                                                                                                         
def index():                                                                                                               
return render_template('index.html')                                                                                
@app.route('/zipCode')                                                                                                  
def zipcode():                                                                                                                                                                                                                                      
curr.execute("SELECT * FROM ZIPCodes WHERE zipcode= "+request.args.get("zipCode"))                                      
result = curr.fetchall()                                                                                                                                                                                                                       
return render_template('tables.html', Zipcode=result[0][0], City=result[0][1], State=result[0][2], Latitude=result[0][3], Longitude=result[0][4], Classification=result[0][5], Population=result[0][6])                                                                                                                                                            
if __name__ == '__main__':                                                                                                 
app.run(host= '0.0.0.0')  

