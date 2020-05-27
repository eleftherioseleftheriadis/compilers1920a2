import re

def function(m): 
	if (m.group(0)=='&amp;'):
		return '&'
  
	elif (m.group(0)=='&gt;'):
		return '>'

	elif (m.group(0)=='&lt;'):
		return '<'

	else:
		return ' '	

a1 = re.compile('<title>(.+?)</title>') 
a2 = re.compile('<!--.*?-->',re.DOTALL) 
a3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL) 
a4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) 
a5_1 = re.compile(r'<.+?>|</.+?>',re.DOTALL) 
a5_2 = re.compile(r'<.+?/>',re.DOTALL) 
a6 = re.compile(r'&(amp|gt|lt|nbsp);') 
a7 = re.compile(r'\s+')

with open('testpage.txt','r') as fp:

	txt = fp.read() 
	m = a1.search(txt) 
	print(m.group(1)) 
	txt = a2.sub(' ',txt) 
	txt = a3.sub(' ',txt) 
	
	for m in a4.finditer(txt): 
		print('{} {}'.format(m.group(1),m.group(2))) 
	
	txt = a5_1.sub(' ',txt) 
	txt = a5_2.sub(' ',txt) 
	txt = a6.sub(function,txt) 
	txt = a7.sub(' ',txt)

	print(txt) 

