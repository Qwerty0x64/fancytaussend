import questions
import random
import sys
import math
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

#Random Funktion fur Zufallszahl zwischen a und b einschliesslich
def iRandom(a, b):
	return int(random.random()*(b-a)+a)

def isPrime(n):
	if n < 2:
		return False
	for i in range(2, int(math.sqrt(n)+1)):
		if n % i == 0:
			return False
	return True

def isExponential(n, e):
	if n == 0:
		return True
	for i in range(0,int(n**(1.0/e)+2)):
		if i**e == n:
			return True
	return False

def twoRandoms(a, b):
	tmp = []
	randomB = iRandom(a, b)
	randomA = iRandom(a, randomB)
	tmp.append(randomA)
	tmp.append(randomB)
	return tmp

def getQuersumme(a):
	tmp = [int(j) for j in str(a)]
	summe = 0
	for zahl in tmp:
		summe = summe + zahl
	return summe

def printLine(a):
	for i in range(0,a):
		sys.stdout.write(u"\u2500")

def fib(a):
	if a == 1:
		return 0
	elif a == 2:
		return 1
	else:
		return fib(a-2)+fib(a-1)
	
cls()
#print tutorial
print ""
print ""
print ""
print u"\u250c",
printLine(51)
print u"\u2510"
print u"\u2502         Willkommen beim Fancy-Zahlenraten         \u2502"
print u"\u2514",
printLine(51)
print u"\u2518"
print ""
print ""
print "Ich versuche gleich deine Zahl zu erraten!"
print ""
print "Bei Ja und Nein Fragen gilt:"
print "0: Nein  -  1: Ja"
print "Ansonsten einfach die entsprechende Zahl antworten."
print ""
print "-1 kann benutzt werden, um Fragen zu ueberspringen."
print ""
print "Die Maximalgroesse des Suchraumes ist 50000. (langsam)"
print ""

#fibonacci-liste
fibzahlen = []
for i in range(1,26):
	fibzahlen.append(fib(i)) 

#2erpotenzen-liste
zweierpot = []
for i in range(0,16):
	zweierpot.append(int(math.pow(2,i)))

#setze zahlen-array
suchraum = input("Bitte gib die Groesse des Suchraumes an: ")
if suchraum < 1 or suchraum > 50000:
	print "Diese Angabe kann ich nicht akzeptieren... setze Suchraum auf 10001"
	suchraum = 10001
zahlen = range(0,suchraum)


#Errechne Grosse des Fragenpools
dicSize = len(questions.fragenDic)

bereitsGestellt = []
rnd = iRandom(0, dicSize)

print ""
print "Denk dir eine Zahl zwischen 0 und {} aus!".format(len(zahlen)-1)
print ""

while (len(zahlen) > 1):
	if (len(bereitsGestellt) == dicSize):
		if len(zahlen) > 10:
			rnd = 10
		else:
			rnd = 15
	else:
		while (bereitsGestellt.count(rnd) != 0):
			rnd = iRandom(0, dicSize)
		bereitsGestellt.append(rnd);

	if rnd == 10:
		tmpstr = questions.fragenDic[rnd]
		tmprnd = twoRandoms(zahlen[0], zahlen[len(zahlen)-1])
		tmpstr = tmpstr.replace("XX", str(tmprnd[0]))
		tmpstr = tmpstr.replace("YY", str(tmprnd[1]))
		print tmpstr
	elif rnd == 4:
		tmpstr = questions.fragenDic[rnd]
		tmprnd = iRandom(3,18)
		tmpstr = tmpstr.replace("ZZ", str(tmprnd))
		print tmpstr
	elif rnd == 5:
		tmpstr = questions.fragenDic[rnd]
		tmprnd = iRandom(0,10)
		tmpstr = tmpstr.replace("X", str(tmprnd))
		print tmpstr
	elif rnd == 15:
		tmpstr = questions.fragenDic[rnd]
		tmprnd = zahlen[iRandom(0,len(zahlen)-1)]
		tmpstr = tmpstr.replace("GG", str(tmprnd))
		print tmpstr
	elif rnd == 19:
		tmpstr = questions.fragenDic[rnd]
		tmpstr = tmpstr.replace("XX", str(suchraum-1))
		print tmpstr
	else:
		print questions.fragenDic[rnd]
	antwort = input("Antwort: ")
	print ""
	removelist = []
	#FRAGENKATALOG ABARBEITEN
	if rnd == 0: #primzahl?
		if antwort == 1:
			for i in zahlen:
				if not isPrime(i):
					removelist.append(i)
		else:
			for i in zahlen:
				if isPrime(i):
					removelist.append(i)
	elif rnd == 1: #geschlossener kreis in ziffer? 0123456789 04689
		for i in zahlen:
			tmp = [int(j) for j in str(i)]		
			if antwort == 1:
				if (tmp.count(0) + tmp.count(4) + tmp.count(6) + tmp.count(8) + tmp.count(9)) == 0:
					removelist.append(i)
			else:
				if (tmp.count(0) + tmp.count(4) + tmp.count(6) + tmp.count(8) + tmp.count(9)) > 0:
					removelist.append(i)

	elif rnd == 2: #quadratzahl?
		if antwort == 1:
			for i in zahlen:
				if not isExponential(i, 2):
					removelist.append(i)
		else:
			for i in zahlen:
				if isExponential(i, 2):
					removelist.append(i)

	elif rnd == 3: #palindrom?
		if antwort == 1:
			for i in zahlen:
				if str(i) != str(i)[::-1]:
					removelist.append(i)
		else:
			for i in zahlen:
				if str(i) == str(i)[::-1]:
					removelist.append(i)

	elif rnd == 4: #durch rnd teilbar?
		if antwort == 1:
			for i in zahlen:
				if i % tmprnd != 0:
					removelist.append(i)
		else:
			for i in zahlen:
				if i % tmprnd == 0:
					removelist.append(i)

	elif rnd == 5: #wieviele 7er?
		for i in zahlen:
			tmp = [int(j) for j in str(i)]
			if tmp.count(tmprnd) != antwort:
				removelist.append(i)	

	elif rnd == 6: #gerade?
		if antwort == 1:
			for i in zahlen:
				if i % 2 != 0:
					removelist.append(i)
		else:
			for i in zahlen:
				if i % 2 == 0:
					removelist.append(i)

	elif rnd == 7: # kubikzahl?
		if antwort == 1:
			for i in zahlen:
				if not isExponential(i, 3):
					removelist.append(i)
		else:
			for i in zahlen:
				if isExponential(i, 3):
					removelist.append(i)

	elif rnd == 8: #donnerstag?
		print "Das ist aber interessant..."

	elif rnd == 9: #single?
		print "Wir koennen ja mal einen Kaffee trinken gehen..."

	elif rnd == 10: # liegt in intervall?
		if antwort == 1:
			for i in zahlen:
				if i not in range(tmprnd[0], tmprnd[1]+1):
					removelist.append(i)
		else:
			for i in zahlen:
				if i in range(tmprnd[0], tmprnd[1]+1):
					removelist.append(i)

	elif rnd == 11: #wieviele stellen?
		for i in zahlen:
			tmp = [int(j) for j in str(i)]
			if len(tmp) != antwort:
				removelist.append(i)

	elif rnd == 12: #reim auf ei
		if antwort == 1:
			for i in zahlen:
				if i != 2 and i != 3 and i < 10:
					removelist.append(i)
				else:
					tmp = int(str(i)[len(str(i))-1])
					tmp2 = int(str(i)[len(str(i))-2])
					if not ((tmp == 2 or tmp == 3) and tmp2 == 0):
						removelist.append(i)
		else:
			for i in zahlen:
				if i == 2 or i == 3:
					removelist.append(i)
				elif i > 9:
					tmp = int(str(i)[len(str(i))-1])
					tmp2 = int(str(i)[len(str(i))-2])
					if (tmp == 2 or tmp == 3) and tmp2 == 0:
						removelist.append(i)

	elif rnd == 13: #quersumme
		for i in zahlen:
			if getQuersumme(i) != antwort:
				removelist.append(i)	

	elif rnd == 14: #iter. Quersumme
		for i in zahlen:
			tmp = getQuersumme(i)
			while (tmp) >= 10:
				tmp = getQuersumme(tmp)
			if tmp != antwort:
				removelist.append(i)		

	elif rnd == 15:	#12
		if antwort == 1:
			for i in zahlen:
				if i != tmprnd:
					removelist.append(i)
		else:
			removelist.append(tmprnd)

	elif rnd == 16:	#nachfolger:
		print "Das ist Ueberraschend!!"

	elif rnd == 17: #fib?
		if antwort == 1:
			for i in zahlen:
				if i not in fibzahlen:
					removelist.append(i)
		elif antwort == 0:
			for i in zahlen:
				if i in fibzahlen:
					removelist.append(i)	

	elif rnd == 18:	#2erpotenz
		if antwort == 1:
			for i in zahlen:
				if i not in zweierpot:
					removelist.append(i)
		elif antwort == 0:
			for i in zahlen:
				if i in zweierpot:
					removelist.append(i)	

	elif rnd == 19: #verdoppelt < als Suchraum
		if antwort == 1:
			for i in zahlen:
				if i*2 >= suchraum:
					removelist.append(i)
		if antwort == 0:
			for i in zahlen:
				if i*2 < suchraum:
					removelist.append(i)

	#Removelist abarbeiten
	if antwort != -1:
		for i in removelist:
			zahlen.remove(i)

	#Zwischenergebnis printen
	#print zahlen
	#print ""

try:
	print "Deine Zahl ist die {}. ".format(zahlen[0])
except IndexError as I:
	print "Luegen tuste, das biste!"


