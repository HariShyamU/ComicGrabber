from flask import Flask, render_template, request
import urllib, re,sys,requests
reload(sys)
sys.setdefaultencoding('utf8')
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
			source = urllib.urlopen('http://mangafox.me/manga/onepunch_man/').read()
			for link in re.findall('http://mangafox.me/manga/onepunch_man/v[0-9][0-9]/c\d\d\d', source):
				a.append(link)
			for link in re.findall('http://mangafox.me/manga/onepunch_man/vTBD/c\d\d\d', source):
				a.append(link)
	return render_template("result.html",result = a,reslen=len(a))

@app.route('/read',methods = ['POST' , 'GET'])
def read():
	if request.method == 'POST':
		lel = request.form['num']
		b=[]
		source=''
		source = requests.get('http://mangafox.me/manga/onepunch_man/').text
		for link in re.findall('http://mangafox.me/manga/onepunch_man/v[0-9][0-9]/c\d\d\d', source):
			b.append(link)
		for link in re.findall('http://mangafox.me/manga/onepunch_man/vTBD/c\d\d\d', source):
			b.append(link)
		for pno in range(1,16):
			aba=next((s for s in b if str(lel) in s), None)
			aba+='/'+str(pno)
			mpage=urllib.urlopen(aba).read()
			c=re.findall('http://l.mfcdn.net/store/manga/11362/[0-9].+', mpage)
        		d="".join(c)
			d=d[:119]
	return render_template("read.html",reads=source,ilag=c,page=aba,sc=mpage)
if __name__ == '__main__':
   app.run(debug = True)