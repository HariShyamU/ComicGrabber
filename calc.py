from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import urllib, re,requests
app = Flask(__name__)
a=[]
lol=1;
num=0
@app.route('/')
def student():
   return render_template('calc.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form['Manga']
		if result=="OPM":
			source = requests.get('http://mangafox.me/manga/onepunch_man/v01/c001/1.html')
			soup = BeautifulSoup(source.text)
			h=soup.findAll('option')
			l=[]
			t=[]
			source2 = requests.get('http://mangafox.me/manga/onepunch_man')
			soup2 = BeautifulSoup(source2.text)
			for div in soup2.findAll("ul", { "class" : "chlist" }):
				for h3 in div.findAll("h3"):
					for link in h3.select("a"):
						l.append(link['href'])
						t.append(link.contents[0])
			for div in soup2.findAll("ul", { "class" : "chlist" }):
				for h3 in div.findAll("h4"):
					for link in h3.select("a"):
						l.append(link['href'])
						t.append(link.contents[0])
			
			a = [str(r) for r in l]
			t = [str(r) for r in t]
	return render_template("result.html",chaplink = a,chapno=t,chaplen=len(t))

@app.route('/read/<clink>',methods = ['POST' , 'GET'])
def read(clink):
	source2 = requests.get('http://mangafox.me/manga/onepunch_man')
	soup2 = BeautifulSoup(source2.text)
	l=[]
	z=-2
	for div in soup2.findAll("ul", { "class" : "chlist" }):
		for h3 in div.findAll("h3"):
			for link in h3.select("a"):
				l.append(link['href'])
	for div in soup2.findAll("ul", { "class" : "chlist" }):
		for h3 in div.findAll("h4"):
			for link in h3.select("a"):
				l.append(link['href'])
			
			a = [str(r) for r in l]
	if 1==1:
		c=[]
		g=a[int(clink)][:-5]
		source = requests.get(g)
		soup = BeautifulSoup(source.text)
		for h in soup.findAll('select',{'class':'m'}):
			for i in h.findAll('option'):
				z=z+1
		z=z/2
		for i in range(0,z):
			j=g[:-1]
			j=j+str(i+1)+".html"
			source3 = requests.get(j)
			soup3 = BeautifulSoup(source3.text)
			b=soup3.find("img")
			c.append(b["src"])
		x=[str(r) for r in c]
	return render_template("read.html",imgl=x,pgno=z)
if __name__ == '__main__':
   app.run(debug = True)