n=int(input('dati numarul de elemente din vector:'))
a=[]
print('introduceti ',n,' elemente pentru vectorul creat')
if n<10:
    for i in range(0,n):
        x=int(input('dati elementul:'))
        a.extend([x])
    print(a)
else:
    print('CITESTE ATENT CONDITIA!')
#a)afişează pe ecran componentele tabloului la un interval de 5 poziţii
pa=a[0:5]
print('a)componenta tabloului la un interval de 5 pozitii:', pa)
#b)afişează pe ecran numerele în ordinea inversă a introducerii în calculator
pb=a[::-1]
print('b)numerele in ordinea inversa a introducerii in calculator:',pb)
#c)sortează componentele tabloului în ordine descrescătoare
pc=sorted(a)
pc.sort(reverse=True)
print('c)sortarea componentelor in ordine descrescatoare:',pc)
#d)afişează pe ecran doar componentele pare
pd=[]
for p in range(0,len(a)):
    if a[p]%2==0:
        ay=a[p]
        pd.extend([ay])
print('d)componentele pare:',pd)
#e) afişează pe ecran media aritmetică a componentelor pare
pe=sum(pd)/len(pd)
print('e)media aritmetica a componentelor pare:',pe)
#f)afişează pe ecran doar componentele impare
pf=[]
for q in range(0,len(a)):
    if a[q]%2!=0:
        z=a[q]
        pf.extend([z])
print('f)componentele impare:',pf)
#g)afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y 
x=int(input('introduceti un numar:'))
y=int(input('introduceti un numar:'))
pg=[]
for i in range(0,len(a)):
    if a[i]>x and a[i]%y!=0:
        w=a[i]
        pg.append(w)
print('g)componentele mai mari ca x şi nu sunt divizibile cu y:',pg)
#h)afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y 
ph=[]
for m in range(0,len(a)):
    if a[m]>x and a[m]<y:
        l=a[m]
        ph.append(l)
print('h)componentele mai mari ca x şi mai mici decât y:',ph)
#i)afişează pe ecran poziţiile componentelor impare negative
pi=[]
for i in pf:
    if i<0:
        pi.extend([a.index(i)])
print('i)poziţiile componentelor impare negative',pi)
#j)afişează pe ecran poziţiile componentelor ce conţin doar două cifre semnificative
#for fn in a:
   # if(a[fn]>9 and a[fn]<100):
      #  print('j)poziţiile componentelor ce conţin doar două cifre semnificative',a.index(fn) )
   # elif a[fn]<-9 and a[fn]>-100:
        #print('j)poziţiile componentelor ce conţin doar două cifre semnificative',a.index(fn) )
#k)înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv
pk=a.copy()
pk[0]=min(pk)
print('k)prima componentă a tabloului inlocuita cu componenta de valoare minimă din tabloul respectiv:',pk)
#l)înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia
pl=a.copy()
pl[pl.index(min(pl))]=pl[0]
print('l)componenta de valoare minimă din tabloul inlocuita cu prima componentă a acestuia:',pl)
#m)creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură
pm=pd
print('m)tablou format doar din componentele pare ale tabloului introdus de la tastatură:',pm)
#n)creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură
pn=[]
for i in range(0,len(a)):
    if a[i]%3==0:
        z=a[i]
        pn.extend([z])
print('n)tablou format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură:',pn)
#o)creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori
po=[]
for i in a:
    if i>0:
        k=0
        for j in range(1,i+1):
            if (i%j==0):
               k+=1
        if k<=4:
            po.extend([i])
print('o)tablou format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori',po)
