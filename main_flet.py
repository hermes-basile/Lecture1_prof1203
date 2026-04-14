#questo main serve per fare comunicare view controller e gestoreordini
import flet as ft

from gestionale.controller import Controller
from gestionale.view import View


def main(page: ft.Page): #da imparare a memo;"al main passiamo la pagina"
    v = View(page)         #creo il view (da solo, non comunicante)
    c = Controller(v)       #creo il controller (collegato al view)
    #nel view so che ci sarà un metodo per settare il controller ->
    v.set_controller(c)
    v.carica_interfaccia() #siccome chiamiamo solo questo main, deve sapere dove caricare l'interfaccia (??)


ft.app(target = main) #chiamata al metodo app, dal flet,l'argomento è
                      # la funzione che regola l'applicazione grafica, che è il sopra (def main..)
