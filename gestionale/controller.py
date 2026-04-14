import flet as ft

from gestionale.gestoreOrdini import GestoreOrdini


class Controller:
    def __init__(self, v):
        self._view = v
        self._model = GestoreOrdini()

#dopo aver creato la view, con già tutti i nomi, dobbiamo creare le funzioni del controller
# ( che hanno appunto i nomi copiati dal view)

    #tutte le funzioni che sono collegate a pulsanti per regola hanno 2 argomenti, "self" ed "e", se non li mettiamo
    #non funziona niente.

    def add_ordine(self, e): #per esempio questa funzione è quella creata negli "on_click"
        #Prodotto
        # da quello che ho capito l'obbiettivo è quello di far creare a python un Prodotto, che è qurllo che
        #che abbiamo definito all'inizio del corso, siccome lo abbiamo creato noi, sappiamo ciascun campo
        #che tipo di dato si aspetta: per esempio sappiamo che il nome è una stringa, il prezzo un float, la quantità
        #un intero.
        #siccome dal txtIn (del view) noi riceviamo solo stringhe, dobbiamo fare il "parse" e trasformare da
        #stringhe, a quello che ci serve.
        #per non perdere punti all'esame dobbiamo farlo con il "try", in modo da avvertire l'utente se ha messo un
        #dato non trasformabile (Es: "Pc" nel riquadro quantità)


        #il nome è una stringa: niente controllo,
        # lo prendiamo accedendo dal controller,view,il riquadrino della view, il value (che è il contenuto)
        nomePstr = self._view._txtInNomeP.value

        #il prezzo è un float: trasformiamo da stringa a float
        # se funziona (try) tutto ok, se non funziona lanciamo l'eccezione except ValueError **
        try:
            prezzo = float(self._view._txtInPrezzo.value)
        except ValueError:
            #** se l'utente ha sbagliato ad inserire il dato, dobbiamo comunicarlielo, attraverso la ListView
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! il prezzo deve essere un numero.",
                        color = "red")
            )
            self._view.update_page()
            return
        try:
            quantita = int(self._view._txtInQuantita.value)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! la quantità deve essere un intero.",
                        color="red")
            )
            self._view.update_page()
            return

        #Cliente
        nomeC = self._view._txtInNomeC.value
        mail = self._view._txtInMail.value
        categoria = self._view._txtInCategoria.value

        ordine = self._model.crea_ordine(nomePstr, prezzo,
                                         quantita, nomeC,
                                         mail, categoria)
        self._model.add_ordine(ordine)

        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzo.value = ""
        self._view._txtInQuantita.value = ""
        self._view._txtInNomeC.value = ""
        self._view._txtInMail.value = ""
        self._view._txtInCategoria.value = ""

        self._view._lvOut.controls.append(
            ft.Text("Ordine correttamente inserito.",
                    color="green"))
        self._view._lvOut.controls.append(
            ft.Text("Dettagli dell'ordine:")
        )
        self._view._lvOut.controls.append(
            ft.Text(ordine.riepilogo())
        )

        self._view.update_page()



    def gestisci_ordine(self, e):
        pass

    def gestisci_all_ordini(self, e):
        pass

    def stampa_sommario(self, e):
        pass