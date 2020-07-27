from flask import Flask, render_template, request, g
import sqlite3 
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
app = Flask(__name__)
 
con = sqlite3.connect("links.db")  
con.row_factory = sqlite3.Row
c = con.cursor()
#print("Database opened successfully")  
#con.execute("create table links (id INTEGER PRIMARY KEY AUTOINCREMENT, links TEXT NOT NULL)")  
#print("Table created successfully")  

myurl = 'https://www.vinted.fr/'

#Opening the connection and grabing the page
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")


#grabs each link
def data_entry():
    for hi in page_soup.find_all('a', href=True):
        link_text = hi['href']
        links = ("Found the URL:"+ link_text)
        c.execute("INSERT INTO links (links) VALUES (?)", (links))
        con.commit()  

def data_entry2():
    for bi in page_soup.find_all('link', href=True):
        link_text1 = bi['href']
        links1 = ("Found the URL:"+ link_text1)
        c.execute("INSERT INTO links (links) VALUES (?)", (links1))
        con.commit()    

@app.route("/")  
def view():
    con = sqlite3.connect("links.db")  
    con.row_factory = sqlite3.Row
    c = con.cursor()  
    c.execute("select * from links")  
    rows = c.fetchall()  
    c.close
    con.close()
    return render_template("view.html",rows = rows)   

c.close
con.close()

if __name__ == '__main__':
   app.run(debug = True)