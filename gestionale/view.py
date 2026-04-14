
import flet as ft

class View:

    def __init__(self, page):
        self._page = page #pagina in cui si vede tutto
        self._controller = None #controller da collegare
        self._page.title = "TdP 2025 - Software Gestionale" #titolo
        self._page.horizontal_alignment = "CENTER" #dice di centrare tutto ciò che è visibile
        self._page.theme_mode = ft.ThemeMode.LIGHT #modifica il tema da scuro a chiaro
        self.update_page() # "salva" le modifiche del titolo,tema, e centro

    def carica_interfaccia(self): #dove creiamo le cose visualizzate nella pagina

        #Prodotto
        #txtIn (TESTO in ENTRATA) significa che l'utente deve inserire qualcosa, dal flet importiamo TextField che sarebbe un rettangolo
        #di inserimento, label è il titolo del rettangolino, width la lunghezza(200 pixel)
        self._txtInNomeP = ft.TextField(label = "Nome prodotto", width=200)
        self._txtInPrezzo = ft.TextField(label = "Prezzo", width=200)
        self._txtInQuantita = ft.TextField(label = "Quantità", width=200)
        #ora che ho creato i rettangolini, li devo inserire in una riga, MainAxisAlignment.CENTER li mette al centro
        row1 = ft.Row(controls = [self._txtInNomeP, self._txtInPrezzo, self._txtInQuantita],
                      alignment = ft.MainAxisAlignment.CENTER)
        #qui abbiamo finito gli input utente per il prodotto, ora facciamo quello del cliente



        #Cliente
        #stessa cosa: creo 3 rettangolini(con nomi e lunghezze), li metto in una riga, e centriamo tutto
        self._txtInNomeC = ft.TextField(label = "Nome Cliente", width = 200)
        self._txtInMail = ft.TextField(label = "Mail", width = 200)
        self._txtInCategoria = ft.TextField(label = "Categoria", width = 200)
        row2 = ft.Row(controls = [self._txtInNomeC, self._txtInMail, self._txtInCategoria],
                      alignment = ft.MainAxisAlignment.CENTER)

        #Buttons
        # nell'esercizio: vogliamo 4 pulsanti, per aggiungere e processare un ordine
        #poi uno per processsarli tutti, e uno per stampare
        #nel nome mettiamo "btn" così sappiamo che è un pulsante

        #importiamo dal flet ElevatedButton, nel pulsante ci sarà scritto quello che scriviamo nel "text"
        #on_click servre per dire cosa vogliamo fare( nome della funzione che voglismo attivare), si ricorda
        #che la view NON comunica con model, quindi quello che devo chiamare lo devo fare dal controller,il
        #prof fa prima tutto il view (mette anche i nomi delle variabili su on_click) e poi completa gli altri
        #file, (come per esempio: crea i metodi dell'"on_click" su controller

        self._btnAdd = ft.ElevatedButton(text = "Aggiungi ordine",
                                         on_click = self._controller.add_ordine,
                                         width = 200)
        self._btnGestisciOrdine = ft.ElevatedButton(text = "Gestisci prox ordine",
                                         on_click = self._controller.gestisci_ordine,
                                         width = 200)
        self._btnGestisciAllOrdini = ft.ElevatedButton(text = "Gestisci tutti gli ordini",
                                         on_click = self._controller.gestisci_all_ordini,
                                         width = 200)
        self._btnStampaInfo = ft.ElevatedButton(text = "Stampa sommario",
                                         on_click = self._controller.stampa_sommario,
                                         width = 200)
        #anche qui si mettono su una riga, e si allineano.
        row3 = ft.Row(controls = [self._btnAdd, self._btnGestisciOrdine,
                                  self._btnGestisciAllOrdini,
                                  self._btnStampaInfo],
                      alignment = ft.MainAxisAlignment.CENTER)

        self._lvOut = ft.ListView(expand = True) #questa è la parte(espandibile, che vede l'utente,
                                                 # quando vogliamo comunicargli qualcosa

        #bisogna ricordarsi di salvare sempre le cose sennò l'utente non le vede
        self._page.add(row1, row2, row3, self._lvOut)
        # SOLO DOPO AVER COMPLETATO TUTTO QUESTO CARICA INTERFACCIA (forse all'esame è già fatto dal prof)
        # SI COMPLETA IL "CONTROLLER"


    def set_controller(self, c):
        self._controller = c

    def update_page(self):
        self._page.update()
