import requests
import time
import random

print("Online")

firstname = []
firstname_txt = open('firstnames.txt', 'r')
for firstnames in firstname_txt:
	firstnames = firstnames.strip('/n')
	firstname.append(firstnames)
firstname_txt.close()

lastname = []
lastname_txt = open('lastnames.txt', 'r')
for lastnames in lastname_txt:
	lastnames = lastnames.strip('/n')
	lastname.append(lastnames)
lastname_txt.close()

adjective = []
adjective_txt = open('adjectives.txt', 'r')
for adjectives in adjective_txt:
	adjectives = adjectives.strip('/n')
	adjective.append(adjectives)
adjective_txt.close()

noun = []
noun_txt = open('nouns.txt', 'r')
for nouns in noun_txt:
	nouns = nouns.strip('/n')
	noun.append(nouns)
noun_txt.close()

domainList = ["@lenovo.com", "@newegg.com", "@community.3ds.com", "@windows.com", "@cmail.att-mail.com", "@cdwemail.com", "@verkada.com", "@ra.rockwell.com", "@ecisolutions.com","@gop.org","@unitednations.org","@deeznutz.org","@gmail.com","@hotmail.com","@aol.com","@yahoo.com","@msn.com","@live.com","@verizon.net","@att.net","@bellsouth.net","@charter.net"]

while True:
	try:
		email = ""
		password = ""

		domain = random.choice(domainList)
		f = random.randint(0, (len(firstname) - 1))
		fn = firstname[f]
		l = random.randint(0, (len(lastname) - 1))
		ln = lastname[l]
		a1 = random.randint(0, (len(adjective) - 1))
		adj1 = adjective[a1]
		a2 = random.randint(0, (len(adjective) - 1))
		adj2 = adjective[a2]
		n1 = random.randint(0, (len(noun) - 1))
		noun1 = noun[n1]
		n2 = random.randint(0, (len(noun) - 1))
		noun2 = noun[n2]
		z = random.randint(0, 14)
		year = random.randint(1969, 1994)
		num = random.randint(22, 500)
		if z == 0:
			email = str(fn + ln + domain).lower()
		if z == 1:
			email = str(fn[0] + ln + domain).lower()
		if z == 2:
			email = str(fn + ln[0] + domain).lower()
		if z == 3:
			email = str(fn + ln[0] + str(year) + domain).lower()
		if z == 4:
			email = str(fn + ln[0] + str(num) + domain).lower()
		if z == 5:
			email = str(fn + ln + str(year) + domain).lower()
		if z == 6:
			email = str(fn + ln + str(num) + domain).lower()
		if z == 7:
			email = str(fn[0] + ln + str(year) + domain).lower()
		if z == 8:
			email = str(fn[0] + ln + str(num) + domain).lower()
		if z == 9:
			email = str(fn[0] + fn[1] + fn[2] + ln[0] + str(num) + domain).lower()
		if z == 10:
			email = str(adj1 + fn + str(num) + domain).lower()
		if z == 11:
			email = str(adj1 + fn + str(year) + domain).lower()
		if z == 12:
			email = str(adj1 + noun1 + noun2 + domain).lower()
		if z == 13:
			email = str(adj1 + noun1 + str(num) + adj2 + noun2 + domain).lower()
		if z == 14:
			email = str(fn + noun2 + str(num) + domain).lower()
		if z == 13:
			email = str(adj1 + noun1 + adj2 + noun2 + str(num) + domain).lower()

		pf = random.randint(0, (len(firstname) - 1))
		pfn = firstname[pf]
		pl = random.randint(0, (len(lastname) - 1))
		pln = lastname[pl]
		pa1 = random.randint(0, (len(adjective) - 1))
		padj1 = adjective[pa1]
		pa2 = random.randint(0, (len(adjective) - 1))
		padj2 = adjective[pa2]
		pn1 = random.randint(0, (len(noun) - 1))
		pnoun1 = noun[pn1]
		pn2 = random.randint(0, (len(noun) - 1))
		pnoun2 = noun[pn2]
		z = random.randint(0, 14)
		year = random.randint(1969, 1994)
		num = random.randint(22, 500)
		if z == 0:
			password = str(pfn + pln).lower()
		if z == 1:
			password = str(pfn[0] + pln).lower()
		if z == 2:
			password = str(pfn + pln[0]).lower()
		if z == 3:
			password = str(pfn + pln[0] + str(year)).lower()
		if z == 4:
			password = str(pfn + pln[0] + str(num)).lower()
		if z == 5:
			password = str(pfn + pln + str(year)).lower()
		if z == 6:
			password = str(pfn + pln + str(num)).lower()
		if z == 7:
			password = str(pfn[0] + pln + str(year)).lower()
		if z == 8:
			password = str(pfn[0] + pln + str(num)).lower()
		if z == 9:
			password = str(pfn[0] + pfn[1] + pfn[2] + pln[0] + str(num)).lower()
		if z == 10:
			password = str(padj1 + pfn + str(num)).lower()
		if z == 11:
			password = str(padj1 + pfn + str(year)).lower()
		if z == 12:
			password = str(padj1 + pnoun1 + pnoun2).lower()
		if z == 13:
			password = str(padj1 + pnoun1 + str(num) + padj2 + pnoun2).lower()
		if z == 14:
			password = str(pfn + pnoun2 + str(num)).lower()
		if z == 13:
			password = str(padj1 + pnoun1 + padj2 + pnoun2 + str(num)).lower()

		nemail = email.replace("\n", "")
		npass = password.replace("\n", "")

		referurl = str("https://billowing-poetry-4217.on.fleek.co/?answer="+nemail)
		password = str("pass.html?answer="+nemail+"&question="+npass)
		otherurl = str("https://billowing-poetry-4217.on.fleek.co/pass.html?answer="+nemail+"&question="+npass)

		headers = {
			"authority" : "billowing-poetry-4217.on.fleek.co",
			"method" : "GET",
			"path": password,
			"scheme" : "https",
			"accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-encoding" : "gzip, deflate, br",
			"accept-language" : "en-US,en;q=0.9",
			"referer" : referurl,
			"sec-ch-ua-mobile" : "?0",
			"sec-ch-ua-platform" : "Windows",
			"sec-fetch-dest" : "document",
			"sec-fetch-mode" : "navigate",
			"sec-fetch-site" : "same-origin",
			"sec-fetch-user" : "?1",
			"upgrade-insecure-requests" : "1",
			"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
			}
		getPage = requests.get(referurl, headers=headers, timeout=(60))
		print(getPage)
		getPage = requests.get(otherurl, headers=headers, timeout=(60))
		print(getPage)
		print(random.randint(10,99))
	except:
		print("IP POSSIBLY BANNED")

	
	time.sleep(0.1)
