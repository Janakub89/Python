class Zvire:
   def __init__(self,jmeno:str,druh:str,vaha:int):
      self.jmeno = jmeno
      self.druh = druh
      self.vaha = vaha

   def __str__(self):
      return f'{self.jmeno}, je to {self.druh} a váží {self.vaha} kg.'
    
   def export_to_dict(self):
      novy={'jmeno':self.jmeno,'druh':self.druh,'vaha':self.vaha}
      return novy
   
    
class Zamestnanec:
   def __init__ (self,cele_jmeno:str,rocni_plat:int,pozice:str):
      self.cele_jmeno = cele_jmeno
      self.rocni_plat = rocni_plat
      self.pozice = pozice

   def __str__ (self):
      return f'{self.cele_jmeno} má na pozici {self.pozice} roční plat {self.rocni_plat} Kč.' 

   def ziskej_inicialy(self):
      jmeno,prijmeni=self.cele_jmeno.split(' ')
      return f'{jmeno[0].upper()}.{prijmeni[0].upper()}.'
  
   def export_to_dict(self):
      pridat_z = {'cele_jmeno':self.cele_jmeno, 'rocni_plat':self.rocni_plat, 'pozice':self.pozice}
      return pridat_z
   
  
class Reditel(Zamestnanec):
   def __init__(self, cele_jmeno, rocni_plat, oblibene_zvire: Zvire, pozice= 'Reditel'):
      super().__init__(cele_jmeno, rocni_plat,pozice)
      self.oblibene_zvire = oblibene_zvire

   def __str__(self):
      return super().__str__() + f'Jeho oblíbené zvíře je {self.oblibene_zvire}'  
   

class Zoo:
   def __init__(self,jmeno:str,adresa:str,reditel: Reditel,zamestnanci:Zamestnanec,zvirata:Zvire):
      self.jmeno = jmeno
      self.adresa = adresa
      self.reditel = reditel
      self.zamestnanci = zamestnanci
      self.zvirata = zvirata

   def vaha_vsech_zvirat_v_zoo(self):
      soucet=0
      for item in zvirata:
         soucet += item.vaha
      return soucet    

   def mesicni_naklady_na_zamestnance(self):
      rocni_naklady = reditel.rocni_plat
      for item in zamestnanci:
         rocni_naklady += item.rocni_plat
         mesicni_naklady=round(rocni_naklady/12,2)
      return mesicni_naklady
   
panda = Zvire('Růženka', 'Panda Velká',150)
vydra = Zvire('Vilda','Vydra Mořská',20)
tygr = Zvire('Matýsek','Tygr Sumaterský',300)
medved = Zvire('Karlík','Lední medvěd', 700)
zvirata =[panda,vydra,tygr,medved]

zvirata_dict=[]
for item in zvirata:
  pridat=item.export_to_dict()
  zvirata_dict.append(pridat)

tereza = Zamestnanec('Tereza Vysoka', 700_000,'Cvičitelka tygrů')
aneta = Zamestnanec('Anet Krasna', 600_000,'Cvičitelka vyder')
martin = Zamestnanec('Martin Veliky', 650_000,'Cvičitel ledních medvědů')
zamestnanci = [tereza, aneta, martin]

zamestnanci_dict= []  
for item in zamestnanci:
  pridat=item.export_to_dict()
  zamestnanci_dict.append(pridat)

zvire = Zvire('Adolf', 'Tarantule Velká', 0.1)
reditel = Reditel(cele_jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
assert reditel.pozice == 'Reditel'
assert isinstance(reditel.oblibene_zvire, Zvire)   

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, zamestnanci, zvirata)


print(panda)
print(medved.export_to_dict())
print(zvirata_dict)
print(tereza)
print(aneta)
print(martin)
print(tereza.ziskej_inicialy())
print(aneta.ziskej_inicialy())
print(martin.ziskej_inicialy())
print(zamestnanci_dict)
print(reditel)
print(zoo.reditel)
print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo(),'Kg.')
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance(),'Kč.')


# Zvire class
zvire = Zvire('Láďa', 'Koala', 15)
assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}

# Zamestnanec class
zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programator')
assert hasattr(zamestnanec, 'cele_jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.cele_jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
assert zamestnanec.ziskej_inicialy() =='P.N.'

# Reditel class
zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel('Jan Novotny', 80000, zvire)
assert isinstance(reditel.oblibene_zvire, Zvire)

# Zoo class
zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'jmeno')
assert hasattr(zoo, 'adresa')
assert hasattr(zoo, 'reditel')
assert hasattr(zoo, 'zamestnanci')
assert hasattr(zoo, 'zvirata')
assert isinstance(zoo.jmeno, str)
assert isinstance(zoo.adresa, str)
assert isinstance(zoo.reditel, Reditel)
assert isinstance(zoo.zamestnanci, list)
assert isinstance(zoo.zvirata, list)
assert zoo.vaha_vsech_zvirat_v_zoo() == 1170
