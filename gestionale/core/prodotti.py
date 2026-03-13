# Scriviamo un codice python che modelli un semplice
# gestionale aziendale. Dovremo prvedere la possibilità di
# definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente
# scontati, ...
from dataclasses import dataclass

#CLASSE PRINCIPALE
class Prodotto:
    aliquota_iva = 0.22 #variabile di classe -- ovvero è la stessa per tutte le istanze che verranno create.

    def __init__(self, name: str, price: float, quantity: int, supplier = None):
        self.name = name
        self._price = None
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self._price*self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto*(1+self.aliquota_iva)
        return lordo

    @classmethod #metodo che vale per la singola classe:
    # in questo caso crea un prodotto automaticamente con quantità 1
    def costruttore_con_quantità_uno(cls, name: str, price: float, supplier: str):
        #cls=classe, non so se si deve mettere questo o il nome della classe
        cls(name, price, 1, supplier)

    @staticmethod #metodo che serve in generale non legato alla classe o alle sue istanze
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)

    #sono i getter e setter di python
    @property
    def price(self): # eq. getter
        return self._price
    @price.setter
    def price(self, valore):
        if valore < 0:
            raise ValueError("Attenzione, il prezzo non può essere negativo.")
        self._price = valore

#DUNDER METHODS (metodi speciali per le istanze(oggetti))
    def __str__(self): #dice all'oggetto come si deve stampare per l'utente
        return f"{self.name} - disponibili {self.quantity} pezzi a {self.price} $"

    def __repr__(self):#dice all'oggetto come si deve stampare per il programmatore
        return f"Prodotto(name = {self.name}, price = {self.price}, quantity = {self.quantity}, supplier = {self.supplier})"

    def __eq__(self, other: object): #confronta un'oggetto (self) con un altro (other:tipo_oggetto)

        if not isinstance(other, Prodotto): #se other non appartiene alla classe Prodotto
            return NotImplemented
        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)

    def __lt__(self, other: "Prodotto") -> bool: #"less then" dice al prodotto quando è minore di un altro
        #in questo caso si ordinano per prezzo crescente (utile nelle liste (sort))
        return self.price < other.price

    def prezzo_finale(self) -> float: #calcola il prezzo finale dell'istanza
        return self.price*(1+self.aliquota_iva)

#SOTTOCLASSE aggiunta di attributi
class ProdottoScontato(Prodotto): #si mette tra parentesi il padre
    #si definisce TUTTO quello che voglio che compaia (anche con altri nomi, si sistema dopo-> vedi Servizio)
    def __init__(self, name: str, price: float, quantity: int, supplier: str, sconto_percento: float):
        #Prodotto.__init__()
        super().__init__(name, price, quantity, supplier) #SOLO attributi del padre
        self.sconto_percento = sconto_percento
#OVERRIDE di un metodo, lo si scrive come se fosse nuovo, py se ne accorge da solo
    def prezzo_finale(self) -> float:
        return self.valore_lordo()*(1-self.sconto_percento/100)

#SOTTOCLASSE aggiunta,modifica,eliminazione di attributi
class Servizio(Prodotto):
    def __init__(self, name: str, tariffa_oraria: float, ore: int): #caratteristiche di Servizio
        super().__init__(name = name, price = tariffa_oraria, quantity=1, supplier=None) #si può cambiare nome o eliminare attributi
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.price * self.ore

#ALTRA CLASSE
class Abbonamento:
    def __init__(self, nome: str, prezzo_mensile: float, mesi: int):
        self.name = nome
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.prezzo_mensile*self.mesi


#METODO ALTERNATIVO PER CREARE CLASSI
#si deve importare e serve per non scrivere ogni volta Class.. def init ecc
@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float

    def __hash__(self):
        return hash((self.name, self.prezzo_unitario))

    def __str__(self):
        return f"{self.name} -- {self.prezzo_unitario}"

MAX_QUANTITA = 1000

def crea_prodotto_standard(nome: str, prezzo: float):
    return Prodotto(nome, prezzo, 1, None)

def _test_modulo(): #scrivo tutte le prove che mi servono per vedere se funziona il programma
    print("Sto testando il modulo prodotti.py")
    myproduct1 = Prodotto(name = "Laptop", price = 1200.0, quantity=12, supplier="ABC")

    print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

    print(f"Il totale lordo di myproduct1 è {myproduct1.valore_lordo()}") #uso un metodo di istanza
    p3 = Prodotto.costruttore_con_quantità_uno("Auricolari", 200.0, "ABC") #Modo per chiamare un metodo di classe.
    print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price, 0.15)}")#Modo per chiamare un metodo statico.

    myproduct2 = Prodotto("Mouse", 10, 25, "CDE")
    print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

    print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")
    Prodotto.aliquota_iva = 0.24
    print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")

    print(myproduct1)

    p_a = Prodotto("Laptop", price = 1200.0, quantity=12, supplier="ABC")
    p_b = Prodotto("Mouse ", 10, 14, "CDE")

    print("myproduct1 == p_a?", myproduct1 == p_a) #va a chiamare il metodo __eq__ appena implementato. Mi aspetto TRUE
    print("p_a == p_B?", p_a == p_b) # FALSE

    mylist = [p_a, p_b, myproduct1]
    mylist.sort(reverse=True)

    print("lista di prodotti ordinata")
    for p in mylist:
        print(f"- {p}")

if __name__ == "__main__": #da imparare a memo. significa: se il file è eseguito direttamente(non su altre finestre)
    #fai partire _test_modulo()
    _test_modulo()