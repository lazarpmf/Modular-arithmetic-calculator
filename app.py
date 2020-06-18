#import numpy as np

p=0
#Sabiranje
def press():
	xq=int(app.getEntry("prvi_sabirak"))
	yq=int(app.getEntry("drugi_sabirak"))
	zq=int(app.getEntry("mod_p"))
	# app.getEntry("prvi_sabirak")<1 or app.getEntry("drugi_sabirak")<1 or app.getEntry("mod_p")<1
	if(app.getEntry("prvi_sabirak")!=math.ceil(app.getEntry("prvi_sabirak")) or app.getEntry("prvi_sabirak")<1 or app.getEntry("drugi_sabirak")<1 or app.getEntry("drugi_sabirak")!=math.ceil(app.getEntry("drugi_sabirak")) or  app.getEntry("mod_p")!=math.ceil(app.getEntry("mod_p"))  or app.getEntry("mod_p")<1):
		app.warningBox("Greška u unosu", "Dozvoljen je unos samo pozitivnih cijelih brojeva!", parent=None)
	else:
		app.setLabel("x",(int(app.getEntry("prvi_sabirak"))+int(app.getEntry("drugi_sabirak")))%int(app.getEntry("mod_p")))
#Oduzimanje
	#app.setLabel("y",(int(app.getEntry("umanjenik"))-int(app.getEntry("umanjilac")))%int(app.getEntry("mod_m")))
def press_m():
	if(app.getEntry("umanjenik")!=math.ceil(app.getEntry("umanjenik")) or app.getEntry("umanjenik")<1 or app.getEntry("umanjilac")<1 or app.getEntry("umanjilac")!=math.ceil(app.getEntry("umanjilac")) or  app.getEntry("mod_m")!=math.ceil(app.getEntry("mod_m"))  or app.getEntry("mod_m")<1):
		app.warningBox("Greška u unosu", "Dozvoljen je unos samo pozitivnih cijelih brojeva!", parent=None)
	else:
		app.setLabel("y",(int(app.getEntry("umanjenik"))-int(app.getEntry("umanjilac")))%int(app.getEntry("mod_m")))
#Mnozenje
def press_t():
	if(app.getEntry("prvi_cinilac")!=math.ceil(app.getEntry("prvi_cinilac")) or app.getEntry("prvi_cinilac")<1 or app.getEntry("drugi_cinilac")<1 or app.getEntry("drugi_cinilac")!=math.ceil(app.getEntry("drugi_cinilac")) or  app.getEntry("mod_t")!=math.ceil(app.getEntry("mod_t"))  or app.getEntry("mod_t")<1):
		app.warningBox("Greška u unosu", "Dozvoljen je unos samo pozitivnih cijelih brojeva!", parent=None)
	else:
		app.setLabel("z",(int(app.getEntry("prvi_cinilac"))*int(app.getEntry("drugi_cinilac")))%int(app.getEntry("mod_t")))
def nzd_rek(a,b): 
    if a == 0: 
        return b 
    return int(nzd_rek(b % a, a))
def count_nzd():
    #treba sve da setujemo na empty string
    h=0
    for h in range(10):
        app.setLabel("post"+"_"+str(h)," ")			#cistimo redove

    i=7
    j=1
    k=0
    # p=0
    x=int(app.getEntry("prvi_nzd"))         #konvertujemo ih u integere
    y=int(app.getEntry("drugi_nzd"))
    if(x>0 and y>0):
    	app.setLabel("rez_NZD", str(nzd_rek(x,y)))
    else:
    	app.setLabel("rez_NZD", "NaN")
    #ne smije nijedan od unosa da bude 0
    if(x<=0 or y<=0):
    	# app.setLabel("post"+"_"+"0", "Nedozvoljen unos!")
    	# app.setLabel("post"+"_"+"1", "Molimo unesite")
    	# app.setLabel("post"+"_"+"2", "pozitivne vrijednosti!")
    	app.warningBox("Greška u unosu", "Dozvoljen je unos samo pozitivnih cijelih brojeva!")
    else:
    	if x>=y:
        
        	#x=y*q+r
        	r=x%y
        	q=int(x/y)
        	app.setLabel("post"+"_"+"0", "Postupak: ")
        	app.setLabel("post"+"_"+"1", str(x)+"="+str(y)+"*"+str(q)+"+"+str(int(r)))
        	ne=y
        	e=2
        	while r!=0:
        	    # e=2
        	    x=y
        	    y=r
        	    ne=r
        	    x_str=str(x)
        	    y_str=str(y)
        	    q_str=str(int(x/y))
        	    r_str=str(int(x%y))
        	    app.setLabel("post"+"_"+str(e), x_str+"="+y_str+"*"+q_str+"+"+r_str)
        	    k+=1
        	    i+=1
        	    e+=1
        	    r=x%y
        	    q=int(x/y)
        	app.setLabel("a",ne)
        	k+=1
        	i+=1
        #IDEJA: DA NAPRAVIM NEKIH 15 LABELA I DA IH ONDA SETUJEM
        
        #resetujemo brojace
        # i=7
        # j=1
        # k=0
        #app.addLabel("postupak_nzd_drugi"+"_"+str(k), x_str+"="+y_str+"*"+q_str+"+"+r_str,i,j)  
    	elif x<y:
    	    #y=x*q+r
    	    r=int(y%x)
    	    q=int(y/x)
    	    app.setLabel("post"+"_"+"0", "Postupak: ")
    	    app.setLabel("post"+"_"+"1", str(y)+"="+str(x)+"*"+str(q)+"+"+str(int(r)))
    	    #new=x
    	    e=2
    	    while r!=0:
    	        y=x
    	        x=r
    	        new=r
    	        x_str=str(x)
    	        y_str=str(y)
    	        q_str=str(int(x/y))
    	        r_str=str(int(x%y))
    	        app.setLabel("post"+"_"+str(e), y_str+"="+x_str+"*"+str(int(y/x))+"+"+str(int(y%x)))
    	        e+=1
    	        r=y%x
    	        q=int(y/x)
    	    app.setLabel("a",new)
    

def count_nzs():
	a=int(app.getEntry("prvi_nzs"))
	b=int(app.getEntry("drugi_nzs"))
	if(app.getEntry("prvi_nzs")<0 or app.getEntry("drugi_nzs")<0 or app.getEntry("prvi_nzs")!=math.ceil(app.getEntry("prvi_nzs")) or app.getEntry("drugi_nzs")!=math.ceil(app.getEntry("drugi_nzs"))):
		app.warningBox("Greška u unosu","Dozvoljen je unos samo pozitivnih cijelih brojeva!")
	else:
		nzd=nzd_rek(a,b)
		app.setLabel("result",int((a*b)/nzd)) 
#blankinship
def upper(matrix):
    while(matrix[0][0]!=0 and matrix[1][0]!=0):
    	#t=24
        if(matrix[0][0]>=matrix[1][0]):
            q=int(matrix[0][0]/matrix[1][0]) 
            matrix[0][0]=matrix[0][0]-q*matrix[1][0] #I-int(a/b)*II->I
            matrix[0][1]=matrix[0][1]-q*matrix[1][1]
            matrix[0][2]=matrix[0][2]-q*matrix[1][2]
            # app.setLabel("post_novi"+"_"+"1"+str(t), matrix)
            # t+=1
        else:
            r=int(matrix[1][0]/matrix[0][0])
            matrix[1][0]=matrix[1][0]-r*matrix[0][0] #II-int(b/a)*I->II
            matrix[1][1]=matrix[1][1]-r*matrix[0][1]
            matrix[1][2]=matrix[1][2]-r*matrix[0][2]
            # app.addLabel("b_result"+"_"+"1"+str(k), str(matrix), k+23,1)
            # k++
    print(matrix)
def blank():
	#treba ispitati da li ima rjesenja uopste
	
    a=int(app.getEntry("b_prvi"))
    b=int(app.getEntry("b_drugi"))
    matrix=[[a,1,0],[b,0,1]];
    upper(matrix)
    app.setLabel("b_result", str(matrix))   #treba da ljepse stampa
    if(matrix[0][0]>0):
    	app.setLabel("b_result_1", str(matrix[0][0])+'='+'('+str(matrix[0][1])+')'+'*'+str(a)+'+'+'('+str(matrix[0][2])+')'+'*'+str(b)) 
    else:
    	app.setLabel("b_result_1", str(matrix[1][0])+'='+'('+str(matrix[1][1])+')'+'*'+str(a)+'+'+'('+str(matrix[1][2])+')'+'*'+str(b))



#Ojlerova funkcija
def count_fi(n):
    n=int(app.getEntry("fi_first"))
    if(n>1000012337 or n<1 or math.ceil(app.getEntry("fi_first"))!=n):
        app.setLabel("fi_rezultat", "NaN")
        app.warningBox("Greška u unosu", "Dozvoljen je unos prirodnih brojeva u rasponu od 1 do 1000012336! Pokušajte ponovo!",parent=None)
    else:
        i=1
        num=0
        while(n+1!=i):
            if(nzd_rek(n,i)==1):
                num=num+1
            i=i+1
    app.setLabel("fi_rezultat", str(num))


#jna
def jn_a():
	#treba da ispitam da li ima rjesenje uopste
	#Ax=B(mod mod)
	#Treba prvo da ispitamo da li nzd(A,mod)|B
	#Rjesavamo Diofantovu jednacinu Ax-mod y=B
	#Neka je d=nzd(A,mod). Rjesavamo Ax1-mod y1=d
	#dobijemo x1 iz upper funkcije, pa je x=x1*k, gdje je k=B/d
	x=int(app.getEntry("j-na_A"))
	y=int(app.getEntry("j-na_drugi"))
	m=int(app.getEntry("j-na_mod"))
	nzd=nzd_rek(app.getEntry("j-na_A"),app.getEntry("j-na_mod"))
	a=int(x/nzd)
	b=int(y/nzd)
	mod=int(m/nzd)
	print(x)
	print(nzd)
	print("a= "+str(x/nzd))
	if(nzd_rek(a,mod)!=1 or app.getEntry("j-na_A")<1 or app.getEntry("j-na_drugi")<1 or app.getEntry("j-na_mod")<1 or math.ceil(app.getEntry("j-na_A"))!=app.getEntry("j-na_A") or app.getEntry("j-na_drugi")!=math.ceil(app.getEntry("j-na_drugi")) or app.getEntry("j-na_mod")!=math.ceil(app.getEntry("j-na_mod"))):
		#app.setLabel("j_na_rez", "Jednačina nema rješenje.")
		app.warningBox("Greška!", "Jednačina oblika Ax=B(mod m) ima rješenje akko je NZD(A,m)=1. \n Takođe, dozvoljen je unos samo pozitivnih cijelih brojeva.")
	else:
		if(a>=b):		#podesavanje matrice
			matrix=[[a,1,0],[mod,0,1]];
		else:
			matrix=[[mod,0,1],[a,1,0]];
		upper(matrix)		#Gausov metod za rjesavanje
		if(matrix[0][0]>0):
			app.setLabel("j_na_rez", str(((matrix[0][1]*int(int(y)/int(nzd)))%m)))
		else:
			app.setLabel("j_na_rez", str((matrix[1][1]*int((int(y)/int(nzd))))%m))

#inverzni element po modulu
def inverz():
	# a=app.getEntry("invAinput")
	# m=app.getEntry("invMODinput")
	# app.setLabel("invRez", a+m)
	x=int(app.getEntry("invAinput"))
	y=int(1)
	m=int(app.getEntry("invMODinput"))
	#nzd=nzd_rek(x,m)
	#a=int(x/nzd)
	#b=int(y/nzd)
	#mod=int(m/nzd)
	if(nzd_rek(x,m)!=1 or app.getEntry("invAinput")<1 or app.getEntry("invMODinput")<1 or math.ceil(app.getEntry("invAinput"))!=app.getEntry("invAinput") or app.getEntry("invMODinput")!=math.ceil(app.getEntry("invMODinput"))):
		#app.setLabel("j_na_rez", "Jednačina nema rješenje.")
		app.warningBox("Greška!", "Jednačina oblika Ax=B(mod m) ima rješenje akko je NZD(A,m)=1. \n Takođe, dozvoljen je unos samo pozitivnih cijelih brojeva.")
	else:
		
		if(x>=y):
			matrix=[[x,1,0],[m,0,1]];
		else:
			matrix=[[m,0,1],[x,1,0]];
		upper(matrix)
		if(matrix[0][0]>0):
			app.setLabel("invRez", str(((matrix[0][1]*int(y))%m)))
		else:
			app.setLabel("invRez", str((matrix[1][1]*(int(y)))%m))



def launch(win):
    app.showSubWindow(win)







from appJar import gui
import math

app=gui()


app.addLabel("title","Modularni Kalkulator", 0,0)
app.setLabelBg("title", "gray")

app.addNumericEntry("prvi_sabirak",1,0) #bilo 0,0
app.addLabel("plus","+",1,1)
app.addNumericEntry("drugi_sabirak",1,2)
app.addLabel("mod+","mod",1,3)
app.addNumericEntry("mod_p",1,4)

x=app.getEntry("prvi_sabirak")
y=app.getEntry("drugi_sabirak")
mod=app.getEntry("mod_p")


app.addLabel("subtitle","Rezultat", 1,6)  #bilo 1,0
app.setLabelBg("subtitle", "gray")

#app.addLabel("rezultat_sabiranje"," ", 1,1)

#app.addButton("jednako",mod_plus(x,y,mod))

#treba mi reakcija na dugme

app.addButton("jednako+",press, 1,5) 
# app.enableEnter(press)
app.addLabel("x","  ", 1,7)  #bilo 2,1
app.addLabel("empty", " ", 1,8)

#oduzimanje


app.addNumericEntry("umanjenik",2,0)
app.addLabel("minus","-",2,1)
app.addNumericEntry("umanjilac",2,2)
app.addLabel("mod-","modmin",2,3)
app.addNumericEntry("mod_m",2,4)

x=app.getEntry("umanjenik")
y=app.getEntry("umanjilac")
mod=app.getEntry("mod_m")

app.addLabel("podnaslov","Rezultat", 2,6) #bilo 2,0
app.setLabelBg("podnaslov", "gray")



app.addButton("jednako-",press_m, 2,5)
app.addLabel("y"," ", 2,7) #bilo 3,1

#mnozenje

app.addNumericEntry("prvi_cinilac",3,0)
app.addLabel("puta","*",3,1)
app.addNumericEntry("drugi_cinilac",3,2)
app.addLabel("mod*","modmul",3,3)
app.addNumericEntry("mod_t",3,4)

x=app.getEntry("prvi_cinilac")
y=app.getEntry("drugi_cinilac")
mod=app.getEntry("mod_t")

app.addLabel("podnaslov2","Rezultat", 3,6) #bilo 2,0
app.setLabelBg("podnaslov2", "gray")



app.addButton("jednako*",press_t, 3,5)
app.addLabel("z"," ", 3,7) #bilo 3,1
#nzd
app.addLabel("nzd", "NZD", 4,0)
app.setLabelBg("nzd","gray")

app.addLabel("nzd_tekst","NZD (",5,0)
app.addNumericEntry("prvi_nzd",5,1)
app.addLabel("zarez",",", 5,2)
app.addNumericEntry("drugi_nzd",5,3)
app.addLabel(")",")",5,4)
app.addButton("NZD",count_nzd, 5,5)
#app.addLabel("a"," ",5,6)
app.addLabel("rez_nzd", "Rezultat ", 5,6)
app.setLabelBg("rez_nzd", "grey")
app.addLabel("rez_NZD", " ", 5,7)

# #%%%%%%%%%%%%%%%%%
# app.addButton("Postupak", sub, 5,8)
# app.startSubWindow("Uputstvo za korišćenje aplikacije", modal=True)
# for w in range(10):
#     app.addLabel("post"+"_"+str(w), " ", 1+w, 1)

# app.stopSubWindow()


#app.addLabel("nthng", "  ", 5,9)
#Ideja gore napisana
for w in range(10):
    app.addLabel("post"+"_"+str(w), " ", 6+w, 1)
#ovu for petlju bi mozda trebalo da pozivam kad se pritisne dugme.

#########################Pokusati ponovo
# # these go in the main window
# #app.addButton("one", launch)
# app.addButton("two", show_algorithm)
# # this is a pop-up
# app.startSubWindow("one", modal=True)
# app.addLabel("labela", "Postupak Euklidovog algoritma")
# app.setLabelBg("labela","gray")
# for i in range(10):
#     app.addLabel("post_new"+"_"+str(i)," ",i+1,1)
# app.stopSubWindow()
############################Pokusati ponovo
app.addLabel("NZS","NZS",16,0) #bilo w+1
app.setLabelBg("NZS","gray")
app.addLabel("nzs_(", "NZS (", 20,0)
app.addNumericEntry("prvi_nzs", 20,1)
app.addLabel("zapeta", " , ", 20,2)
app.addNumericEntry("drugi_nzs", 20,3)
app.addLabel(")_closed",")", 20,4)
app.addButton("NZS", count_nzs, 20,5)
app.addLabel("result", " ", 20, 6)
#Blankinship metoda za NZD
app.addLabel("blankinship","Blankinship", 21,0)
app.setLabelBg("blankinship","gray")
app.addLabel("b_nzd", "NZD (", 22,0)
app.addNumericEntry("b_prvi", 22,1)
app.addLabel("b_zarez", ",", 22,2)
app.addNumericEntry("b_drugi", 22,3)
app.addLabel("b_closed", ")", 22,4)
app.addButton("Blankinship", blank, 22,5)
app.addLabel("b_result", " ", 23, 1)
app.addLabel("b_result_1", " ", 23, 2)
# for k in range(10):
# 	app.addLabel("post_novi"+"_"+"1"+str(k), " ", 24+k, 1)

#Ojlerova funkcija
app.addLabel("fi", "Ojlerova funkcija",25,0)
app.setLabelBg("fi", "grey")
app.addLabel("fi_znak", "Ф (", 26,0)
app.addNumericEntry("fi_first", 26,1)
app.addLabel("fi_closed",")", 26,2)
app.addButton("Ф(n)",count_fi, 26,3)
app.addLabel("fi_rez", "Rezultat ", 26,4)
app.setLabelBg("fi_rez", "grey")
app.addLabel("fi_rezultat", " ", 26,5)

#Ax (mod B)
app.addLabel("jednacina", "Ax=B (mod m)", 27,0)
app.setLabelBg("jednacina", "grey")
app.addLabel("j-na_prvi","A", 28,0)
app.addNumericEntry("j-na_A", 28, 1)		#unos
app.addLabel("x_jna", "X", 28,2)
app.addLabel("j-na_B", "B", 28,3)
app.addNumericEntry("j-na_drugi",28,4)		#unos
app.addLabel("jna_mod", "mod", 28,5)
app.addNumericEntry("j-na_mod",28,6)
app.addButton("riješi", jn_a, 28,7)
app.addLabel("rez_jna", "Rezultat", 29,2)
app.setLabelBg("rez_jna", "grey")
app.addLabel("j_na_rez", " ", 29,3)

#inverzni element za dati modulo
app.addLabel("inv", "Inverzni element za dati modulo", 30,0)
app.setLabelBg("inv", "grey")
app.addLabel("invA", "A", 31,1)
app.addNumericEntry("invAinput", 31,2)
app.addLabel("invMod", "mod", 31,3)
app.addNumericEntry("invMODinput", 31,4)
app.addButton("Inverz", inverz, 31,5)
app.addLabel("invRezName", "Rezultat", 31,6)
app.setLabelBg("invRezName", "grey")
app.addLabel("invRez", " ", 31,7)


#Uputstvo za korišćenje aplikacije
###################################
app.addButton("Uputstvo za korišćenje aplikacije", launch)
app.setButtonBg("Uputstvo za korišćenje aplikacije", "red")
app.startSubWindow("Uputstvo za korišćenje aplikacije", modal=True)
app.addLabel("naslov", "Uputstvo za korišćenje", 1, 2)
app.setLabelBg("naslov", "grey")
#kalkulator
app.addLabel("kalkulator", "Modularni kalkulator:", 2,0)
app.setLabelBg("kalkulator", "grey")
app.addLabel("kalkulator_tekst","Dozvoljen je unos pozitivnih cijelih brojeva.\nU polja za unos upišite pozitivne cijele brojeve i pritisnite dugme za računanje. \nDesno od labele \"Rezultat\" će se pojaviti rješenje. \nUkoliko unesete pogrešan unos, dobićete prozor sa upozorenjem.", 3)
#NZD
app.addLabel("nzd_", "Najveći zajednički djelilac (NZD):", 4,0)
app.setLabelBg("nzd_", "grey")
app.addLabel("nzd_tekst_","Dozvoljen je unos pozitivnih cijelih brojeva. ",5)
app.stopSubWindow()

app.go()