import tkinter

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Tk, Radiobutton, DISABLED
import sysconfig
import tkinter as tk
import os
import time

ventana = Tk()#window global
ventana.geometry("1200x600")
ventana.title("Registro para jugar QUARTO  :)")
fondo1 = PhotoImage(file='tabla.png')
labelMain = Label(ventana, image=fondo1).place(x=0, y=0)


global variable

turno = 0
lisb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#This list is for update the radiobuttons
tab = []
misUsuarios = []
botones = []
puntaje = 0

jugador1 = 0 #Times won player 1
jugador2 = 0# Times won player 2
veces=0
informacion=[0,0,0,0,0,0]

turj = StringVar()

lf = ["NeGranHuR", 'NePequeHuR', 'NeGranR', 'NePequeR', 'NeGranHuC', 'NePequeHuC', 'NeGranC', 'NePequeC',
      'BlaPequeC', 'BlaGranHuR', 'BlaPequeHuR', 'BlaGranR', 'BlaPequeR', 'BlaGranHuC', 'BlaPequeHuC', 'BlaGranC']

empate = ['NePequeC','NePequeHuR', 'BlaGranC','NeGranHuC',
          'BlaGranHuC','NeGranC','BlaPequeHuR','BlaPequeC',
          'NeGranR','BlaPequeHuC',"NeGranHuR",'NePequeR',
          'BlaGranR', 'NePequeHuC', 'BlaPequeR','BlaGranHuR']

consulta33=[0,0,0,0,0,0,0,0,0]

# -----------------------------------MY NUMBER OF ITEMS ON THE FILE------------------------------------------------
def prueba():
    #numPartida = 0
    archivo = open('partidas.txt', 'r')
    for x in archivo.readlines():
        d = x.split(',')
        numeroP = int(d[0])
        var = int(numeroP)
    numPartida = int(var) + 1  # para que me incremente y vaya contando el numero de partidas
    return numPartida
#----------------------------------------------chronometer--------------------------------------------------------------
#FUNTION TO HAVE THE chronometer
class StopWatch(Frame):
    """ Implements a stop watch frame widget. """

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        """ Make the time label. """
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self):
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

    def Start(self):
        """ Start the stopwatch, ignore if running. """
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def get_elapsedtime(self):
        return self._elapsedtime

    def get_time(self):
        self.Stop()
        time = int(self._elapsedtime)
        minutes = int(time / 60)
        seconds = int(time - minutes * 60.0)
        hseconds = int((time - minutes * 60.0 - seconds) * 100)
        return '%02d:%02d:%02d' % (minutes, seconds, hseconds)

    def Stop(self):
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0
    def get_stop(self):
        return

    def Reset(self):
        """ Reset the stopwatch. """
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)

    def get_rese(self):
        return self._elapsedtime

#----------------------------------------PIECES-------------------------------------------------------------------------

class piecitas:  # My pieces
    def __init__(self):
        self.pieza = ''

    def mifigura(self, pieza):
        self.pieza = pieza

clase = piecitas()

#----------------------------------------My Window Principal-----------------------------------------------------------
#THIS FUNTION CALL THE ALL IMAGES AND RADIOBUTTONS
#HAVE IMAGE FONT

def ventanaPrincipal():
    Tk.update(ventana) #UDDATE THE WINDOW

    ventana.title('---------------Datos----------------')

    Label(ventana, image=fondo1).place(x=0, y=0)#fond of window

    casilla1 = StringVar()
    casilla2 = StringVar()
    casilla3 = StringVar()
    casilla4 = StringVar()
    casilla5 = StringVar()
    casilla6 = StringVar()
    casilla7 = StringVar()
    casilla8 = StringVar()

    #Alls my radiobuttons
    selecciona1 = tk.Radiobutton(ventana, text='Pieza1', value='NeGranHuR', variable=casilla1, indicatoron=0,
                                 command=lambda: rb_command(selecciona1, casilla1),background='sandy brown',cursor="X_cursor")
    selecciona1.place(x=668, y=120)

    selecciona2 = tk.Radiobutton(ventana, text='Pieza2', value='NePequeHuR', variable=casilla2, indicatoron=0,
                                 command=lambda: rb_command(selecciona2, casilla2),background='sandy brown',cursor="X_cursor")
    selecciona2.place(x=724, y=120)

    selecciona3 = tk.Radiobutton(ventana, text='Pieza3', value='NeGranR', variable=casilla3, indicatoron=0,
                                 command=lambda: rb_command(selecciona3, casilla3),background='sandy brown',cursor="X_cursor")
    selecciona3.place(x=780, y=120)
    selecciona4 = tk.Radiobutton(ventana, text='Pieza4', value='NePequeR', variable=casilla4, indicatoron=0,
                                 command=lambda: rb_command(selecciona4, casilla4),background='sandy brown',cursor="X_cursor")
    selecciona4.place(x=837, y=120)

    selecciona5 = tk.Radiobutton(ventana, text='Pieza5', value='NeGranHuC', variable=casilla5, indicatoron=0,
                                 command=lambda: rb_command(selecciona5, casilla5),background='sandy brown',cursor="X_cursor")
    selecciona5.place(x=895, y=120)

    selecciona6 = tk.Radiobutton(ventana, text='Pieza6', value='NePequeHuC', variable=casilla6, indicatoron=0,
                                 command=lambda: rb_command(selecciona6, casilla6),background='sandy brown',cursor="X_cursor")
    selecciona6.place(x=953, y=120)

    selecciona7 = tk.Radiobutton(ventana, text='Pieza7', value='NeGranC', variable=casilla7, indicatoron=0,
                                 command=lambda: rb_command(selecciona7, casilla7),background='sandy brown',cursor="X_cursor")
    selecciona7.place(x=1010, y=120)

    selecciona8 = tk.Radiobutton(ventana, text='Pieza8', value='NePequeC', variable=casilla8, indicatoron=0,
                                 command=lambda: rb_command(selecciona8, casilla8),background='sandy brown',cursor="X_cursor")
    selecciona8.place(x=1070, y=120)

    casilla9 = StringVar()
    casilla10 = StringVar()
    casilla11 = StringVar()
    casilla12 = StringVar()
    casilla13 = StringVar()
    casilla14 = StringVar()
    casilla15 = StringVar()
    casilla16 = StringVar()

    selecciona9 = tk.Radiobutton(ventana, text='Pieza9', value='BlaPequeC', variable=casilla9, indicatoron=0,
                                 command=lambda: rb_command(selecciona9, casilla9),background='sandy brown',cursor="X_cursor")
    selecciona9.place(x=670, y=250)
    selecciona10 = tk.Radiobutton(ventana, text='Pieza10', value='BlaGranHuR', variable=casilla10, indicatoron=0,
                                  command=lambda: rb_command(selecciona10, casilla10),background='sandy brown',cursor="X_cursor")
    selecciona10.place(x=720, y=250)
    selecciona11 = tk.Radiobutton(ventana, text='Pieza11', value='BlaPequeHuR', variable=casilla11, indicatoron=0,
                                  command=lambda: rb_command(selecciona11, casilla11),background='sandy brown',cursor="X_cursor")
    selecciona11.place(x=774, y=250)
    selecciona12 = tk.Radiobutton(ventana, text='Pieza12', value='BlaGranR', variable=casilla12, indicatoron=0,
                                  command=lambda: rb_command(selecciona12, casilla12),background='sandy brown',cursor="X_cursor")
    selecciona12.place(x=830, y=250)
    selecciona13 = tk.Radiobutton(ventana, text='Pieza13', value='BlaPequeR', variable=casilla13, indicatoron=0,
                                  command=lambda: rb_command(selecciona13, casilla13),background='sandy brown',cursor="X_cursor")
    selecciona13.place(x=890, y=250)
    selecciona14 = tk.Radiobutton(ventana, text='Pieza14', value='BlaGranHuC', variable=casilla14, indicatoron=0,
                                  command=lambda: rb_command(selecciona14, casilla14),background='sandy brown',cursor="X_cursor")
    selecciona14.place(x=950, y=250)
    selecciona15 = tk.Radiobutton(ventana, text='Pieza15', value='BlaPequeHuC', variable=casilla15, indicatoron=0,
                                  command=lambda: rb_command(selecciona15, casilla15),background='sandy brown',cursor="X_cursor")
    selecciona15.place(x=1007, y=250)
    selecciona16 = tk.Radiobutton(ventana, text='Pieza16', value='BlaGranC', variable=casilla16, indicatoron=0,
                                  command=lambda: rb_command(selecciona16, casilla16),background='sandy brown',cursor="X_cursor")
    selecciona16.place(x=1063, y=250)
    #Alls my images of game

    botimage1 = PhotoImage(file='botoncirculohueco.png')
    labelMain = Label(ventana, image=botimage1).place(x=665, y=60)

    botimage2 = PhotoImage(file='botoncirculohuecoP.png')
    labelMain = Label(ventana, image=botimage2).place(x=720, y=60)

    botimage3 = PhotoImage(file='botoncirculorelleno.png')
    labelMain = Label(ventana, image=botimage3).place(x=775, y=60)

    botimage4 = PhotoImage(file='botoncirculorellenoP.png')
    labelMain = Label(ventana, image=botimage4).place(x=830, y=60)

    botimage5 = PhotoImage(file='botoncuadradohueco.png')
    labelMain = Label(ventana, image=botimage5).place(x=890, y=60)

    botimage6 = PhotoImage(file='botoncuadradohuecoP.png')
    labelMain = Label(ventana, image=botimage6).place(x=950, y=60)

    botimage7 = PhotoImage(file='botoncuadradorelleno.png')
    labelMain = Label(ventana, image=botimage7).place(x=1000, y=60)

    botimage8 = PhotoImage(file='botoncuadradorellenoP.png')
    labelMain = Label(ventana, image=botimage8).place(x=1060, y=60)

    #SECOND BAND OF IMAGES.
    botimage9 = PhotoImage(file='botoncuadradorellenoPB.png')
    labelMain = Label(ventana, image=botimage9).place(x=665, y=200)
    botimage10 = PhotoImage(file='circulohuecoB.png')
    labelMain = Label(ventana, image=botimage10).place(x=720, y=200)
    botimage11 = PhotoImage(file='circulohuecoPB.png')
    labelMain = Label(ventana, image=botimage11).place(x=775, y=200)
    botimage12 = PhotoImage(file='circulorellenoB.png')
    labelMain = Label(ventana, image=botimage12).place(x=830, y=200)
    botimage13 = PhotoImage(file='circulorellenoPB.png')
    labelMain = Label(ventana, image=botimage13).place(x=890, y=200)
    botimage14 = PhotoImage(file='cuadradohuecoB.png')
    labelMain = Label(ventana, image=botimage14).place(x=950, y=200)
    botimage15 = PhotoImage(file='cuadradohuecoPB.png')
    labelMain = Label(ventana, image=botimage15).place(x=1007, y=200)
    botimage16 = PhotoImage(file='cuadradorellenoB.png')
    labelMain = Label(ventana, image=botimage16).place(x=1060, y=200)

    #The buttons(matriz)

    b0 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(0))
    lisb[0]=b0
    b0.place(x=20, y=50)

    b1 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(1))
    lisb[1]=b1
    b1.place(x=100, y=50)
    b2 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(2))
    lisb[2]=b2
    b2.place(x=180, y=50)
    b3 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(3))
    lisb[3]=b3
    b3.place(x=260, y=50)
    # ------------------------------------------------------------------
    b4 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(4))
    lisb[4]=b4
    b4.place(x=20, y=120)
    b5 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(5))
    lisb[5]=b5
    b5.place(x=100, y=120)
    b6 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(6))
    lisb[6]=b6
    b6.place(x=180, y=120)
    b7 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(7))
    lisb[7]=b7
    b7.place(x=260, y=120)
    # ---------------------------------------------------------------------
    b8 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(8))
    lisb[8]=b8
    b8.place(x=20, y=190)
    b9 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(9))
    lisb[9]=b9
    b9.place(x=100, y=190)
    b10 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(10))
    lisb[10]=b10
    b10.place(x=180, y=190)
    b11 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(11))
    lisb[11]=b11
    b11.place(x=260, y=190)

    # ----------------------------------------------------------------------
    b12 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(12))
    lisb[12]=b12
    b12.place(x=20, y=260)
    b13 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(13))
    lisb[13]=b13
    b13.place(x=100, y=260)
    b14 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(14))
    lisb[14]=b14
    b14.place(x=180, y=260)
    b15 = Button(ventana, width=9, height=3, relief=SOLID, cursor="pencil", command=lambda: cambiaTurno(15))
    lisb[15]=b15
    b15.place(x=260, y=260)


    tkinter.Label(ventana, text="Si el radiobutton está en blanco es que ya se Uso!!!",bg='lightblue').place(x=700, y=30)

    global sw #global clock
    sw = StopWatch(ventana)#TIME

    sw.pack(side=TOP)#POSITION

    Label(ventana, text= 'Intrucciones del Juego:\n 1. Ingrese los Nombres al iniciar el Juego\n'
                       '2. Juego de acuerdo al turno.\n'
                       '------------------------------------------------------------------------------\n'
                       '- Si le toca a X, entonces juega pone la piesa . Automaticamente se cambia de turno\n'
                       'X selecciona previamente la piesa que quiere que use el contrincante Y. Viceversa\n'   
                       '+ Hay un ganador y se guarda la informacion:\n'
                       'La puede consultar en Estadisticas\n').place(x=700,y=400)


    Label(ventana,textvariable=turj).place(x=140,y=10)
    Button(ventana, bg='blue', fg='white', text='Iniciar juego', cursor="sizing", width=15, height=3,
                  command=iniciandoJuego).place(x=130, y=360)

    Button(ventana, bg='red', fg='white', text='Gané', cursor="sizing", width=15, height=3,
                  command=lambda:jugadas()).place(x=280, y=360)

    Button(ventana, text='REVANCHA', bg='turquoise',command=lambda :llamaIniciandojuego(),background='LimeGreen').place(x=450, y=150)


    #button = Button(ventana, text="REINICIAR JUEGO", command=lambda: ventanaPrincipal(),background='DarkOrchid', cursor="X_cursor").place(x=200, y=450)

    bloq()
    prueba()
    # global numPartida
    # np = str(numPartida)
    # Label(ventana, text=str(np), width=2, height=1).place(x=600, y=400)
    #actualizaPartida()

    ventana.mainloop()

def rb_command(radio_button, str_var):#This funtion disable the radiobutton after to be used
    radio_button.config(state=DISABLED)
    clase.mifigura(str_var.get())

def actualizaPartida():
    archivo = open('partidas.txt', 'r')#read the archive
    for x in archivo.readlines():
        d = x.split(',')
        numeroP = int(d[0])
        var = int(numeroP)
    numPartida = int(var) + 1  # for to grow and count the number game

    np = str(numPartida)
    Label(ventana, text=str(np), width=2, height=1).place(x=600, y=400)

    abreArchi = open('partidas.txt', 'a+') #add the number to archive
    hora = sw.get_time()
    numeAgrego = str(np) + ',' + str(hora) + ',' + '\n'
    abreArchi.write(numeAgrego)
    abreArchi.close()


def reiniciar():#update the radiobuttons and  we can use again

    casilla1 = StringVar()
    casilla2 = StringVar()
    casilla3 = StringVar()
    casilla4 = StringVar()
    casilla5 = StringVar()
    casilla6 = StringVar()
    casilla7 = StringVar()
    casilla8 = StringVar()

    selecciona1 = tk.Radiobutton(ventana, text='Pieza1', value='NeGranHuR', variable=casilla1, indicatoron=0,
                                 command=lambda: rb_command(selecciona1, casilla1))
    selecciona1.place(x=668, y=120)

    selecciona2 = tk.Radiobutton(ventana, text='Pieza2', value='NePequeHuR', variable=casilla2, indicatoron=0,
                                 command=lambda: rb_command(selecciona2, casilla2))
    selecciona2.place(x=724, y=120)

    selecciona3 = tk.Radiobutton(ventana, text='Pieza3', value='NeGranR', variable=casilla3, indicatoron=0,
                                 command=lambda: rb_command(selecciona3, casilla3))
    selecciona3.place(x=780, y=120)
    selecciona4 = tk.Radiobutton(ventana, text='Pieza4', value='NePequeR', variable=casilla4, indicatoron=0,
                                 command=lambda: rb_command(selecciona4, casilla4))
    selecciona4.place(x=837, y=120)

    selecciona5 = tk.Radiobutton(ventana, text='Pieza5', value='NeGranHuC', variable=casilla5, indicatoron=0,
                                 command=lambda: rb_command(selecciona5, casilla5))
    selecciona5.place(x=895, y=120)

    selecciona6 = tk.Radiobutton(ventana, text='Pieza6', value='NePequeHuC', variable=casilla6, indicatoron=0,
                                 command=lambda: rb_command(selecciona6, casilla6))
    selecciona6.place(x=953, y=120)

    selecciona7 = tk.Radiobutton(ventana, text='Pieza7', value='NeGranC', variable=casilla7, indicatoron=0,
                                 command=lambda: rb_command(selecciona7, casilla7))
    selecciona7.place(x=1010, y=120)

    selecciona8 = tk.Radiobutton(ventana, text='Pieza8', value='NePequeC', variable=casilla8, indicatoron=0,
                                 command=lambda: rb_command(selecciona8, casilla8))
    selecciona8.place(x=1070, y=120)

    casilla9 = StringVar()
    casilla10 = StringVar()
    casilla11 = StringVar()
    casilla12 = StringVar()
    casilla13 = StringVar()
    casilla14 = StringVar()
    casilla15 = StringVar()
    casilla16 = StringVar()

    selecciona9 = tk.Radiobutton(ventana, text='Pieza9', value='BlaPequeC', variable=casilla9, indicatoron=0,
                                 command=lambda: rb_command(selecciona9, casilla9))
    selecciona9.place(x=670, y=250)
    selecciona10 = tk.Radiobutton(ventana, text='Pieza10', value='BlaGranHuR', variable=casilla10, indicatoron=0,
                                  command=lambda: rb_command(selecciona10, casilla10))
    selecciona10.place(x=720, y=250)
    selecciona11 = tk.Radiobutton(ventana, text='Pieza11', value='BlaPequeHuR', variable=casilla11, indicatoron=0,
                                  command=lambda: rb_command(selecciona11, casilla11))
    selecciona11.place(x=774, y=250)
    selecciona12 = tk.Radiobutton(ventana, text='Pieza12', value='BlaGranR', variable=casilla12, indicatoron=0,
                                  command=lambda: rb_command(selecciona12, casilla12))
    selecciona12.place(x=830, y=250)
    selecciona13 = tk.Radiobutton(ventana, text='Pieza13', value='BlaPequeR', variable=casilla13, indicatoron=0,
                                  command=lambda: rb_command(selecciona13, casilla13))
    selecciona13.place(x=890, y=250)
    selecciona14 = tk.Radiobutton(ventana, text='Pieza14', value='BlaGranHuC', variable=casilla14, indicatoron=0,
                                  command=lambda: rb_command(selecciona14, casilla14))
    selecciona14.place(x=950, y=250)
    selecciona15 = tk.Radiobutton(ventana, text='Pieza15', value='BlaPequeHuC', variable=casilla15, indicatoron=0,
                                  command=lambda: rb_command(selecciona15, casilla15))
    selecciona15.place(x=1007, y=250)
    selecciona16 = tk.Radiobutton(ventana, text='Pieza16', value='BlaGranC', variable=casilla16, indicatoron=0,
                                  command=lambda: rb_command(selecciona16, casilla16))
    selecciona16.place(x=1063, y=250)


#--------------------------------------------------------STATISTICS-------------------------------------------------
def estadistica():# Funtion to show the information
    Tk.update(ventana)
    contador=1

    ventana.title('---------------Datos----------------')

    Label(ventana, image=fondo1).place(x=0, y=0)
    Button(ventana, text="Volver", command=lambda: ventanaPrincipal(),background="CadetBlue").place(x=1050, y=550)

    #--------------------------Consulta1--------------------------------------------
    contador=60
    archivo = open('partidas.txt', 'r')

    Label(ventana, text='Numero de partida',background='coral').place(x=30,y=30)
    Label(ventana, text='Tiempo',background='coral').place(x=160,y=30)
    for i in archivo:
        a = i.strip('\n').split(',')

        Label(ventana, text=a[0]).place(x=60,y=contador)
        Label(ventana, text=a[1]).place(x=160,y=contador)
        contador += 35

    #---------------------------Consulta2----------------------------------
    contador2=60
    #SHOW IN WINDOW LABELS
    archivo2=open('jugadores.txt', 'r')
    Label(ventana,text= "Jugador 1",background='gold').place(x=350,y=30)
    Label(ventana,text='Ganadas_1',background='gold').place(x=450,y=30)
    Label(ventana, text= 'Jugador 2',background='gold').place(x=550,y=30)
    Label(ventana,text='Ganadas_2',background='gold').place(x=650,y=30)
    Label(ventana,text='V.Jugadas',background='gold').place(x=750,y=30)
    Label(ventana, text='Tiempo',background='gold').place(x=850,y=30)
    Label(ventana, text='F_usadas1', background='gold').place(x=950, y=30)
    Label(ventana, text='F_usadas2', background='gold').place(x=1050, y=30)

    for i in archivo2:
        a = i.strip('\n').split(',')

        Label(ventana, text=a[0]).place(x=350,y=contador2)#SHOW IN WINDOW THE INFORMATION (ARCHIVE)
        Label(ventana, text=a[1]).place(x=450, y=contador2)
        Label(ventana, text=a[2]).place(x=550,y=contador2)
        Label(ventana, text=a[3]).place(x=650, y=contador2)
        Label(ventana, text=a[5]).place(x=750,y=contador2)
        Label(ventana, text=a[4]).place(x=850, y=contador2)
        Label(ventana, text=a[6]).place(x=950, y=contador2)
        Label(ventana, text=a[7]).place(x=1050, y=contador2)

        contador2+=50
#-------------------------------------------------------REINICIO DE JUEGO------------------------------------
def llamaIniciandojuego():# Restart the game
    reinicioorevancha[0] = 1

    iniciandoJuego()#call again the play

# ------------------------------------ITEMS AND STARTING GAME------------------------------------------------------------
global sw

def partidas(numPartida):#Funtion to save the number played
    #global numPartida
    np = str(numPartida)
    Label(ventana, text=str(np), width=2, height=1).place(x=600, y=400)

    abreArchi = open('partidas.txt', 'a+')
    hora = sw.get_time()
    numeAgrego = str(np) + ',' + str(hora) + ',' + '\n'
    abreArchi.write(numeAgrego)
    abreArchi.close()

for i in range(0, 16):
    tab.append("N")

def bloq():#block the bottons
    for i in range(0, 16):
        lisb[0].config(state="disable")
reinicioorevancha = [0]

# 0 is equal to restart and 1 is equal to arevancha is 0 zero by default so always ask for the names

#----------------------------------------------------------INICIA JUEGO------------------------------------------------
def iniciandoJuego():#is for can play

    for i in range(0, 16):
        lisb[i].config(state="normal")
        lisb[i].config(bg="lightgray")
        lisb[i].config(text="")
        tab[i] = "N"
    cero = 0
    uno = 1

    if cero in reinicioorevancha:
            sw.Start()
            global nomj1, nomj2 #names of all players

            nomj1 = simpledialog.askstring("Jugador", "Escribe el nombre del jugador 1: ")#receive the name1
            informacion[0]=nomj1
            consulta33[0]=nomj1

            nomj2 = simpledialog.askstring("Jugador", "Esribe el nombre del jugador 2: ")#receiive the name2
            informacion[1]=nomj2
            consulta33[2]=nomj2

            turj.set("Turno: " + str(nomj1))  # aqui se le está asignando al primer jugador

            if nomj1 == '':
                iniciandoJuego()
            elif nomj2 == '':
                iniciandoJuego()

    if uno in reinicioorevancha:#RESET THE GAME
        #actualizaPartida()
        reiniciar()
        sw.Reset()
        sw.Start()
        turj.set("Turno: " + str(nomj1))  # aqui se le está asignando al primer jugador

        if nomj1 == '':
            iniciandoJuego()
        elif nomj2 == '':
            iniciandoJuego()

    # # vecesjugadas = informacion[2]
    # n  = vecesjugadas +1
    # informacion[2] = n
    #
    # print(informacion)

#-------------------------------------------------------CAMBIA TURNO----------------------------------------------------
piesasUsadas1 = []
piesasUsadas2 = []

def cambiaTurno(num):#to change the player when play

    print(num)
    global turno, nomj1, nomj2
    pieza = clase.pieza  # me importa las piezas

    if tab[num] == "N" and turno == 0:
        lisb[num].config(text=pieza)
        lisb[num].config(bg="white")
        tab[num] = pieza
        turno = 1
        turj.set("Turno:" + nomj2)#name of the one who is playing

        piesasUsadas1.append(nomj2)

    elif tab[num] == "N" and turno == 1:
        lisb[num].config(text=pieza)
        lisb[num].config(bg="lightblue")
        tab[num] = pieza
        turno = 0
        turj.set("Turno: " + nomj1)#name of the one who is playing

        piesasUsadas2.append(nomj1)

    lisb[num].config(state="disable")

    print('Usadas por',nomj2 ,':',piesasUsadas1,'Cantidad:',len(piesasUsadas1))
    global global1
    global1= len(piesasUsadas1)


    print('Usadas por',nomj1 ,':',piesasUsadas2,'Cantidad:',len(piesasUsadas2))
    global global2
    global2 = len(piesasUsadas2)

    #usadas()

#Save all in the archive players
def CapturelRegistry(name, name2, puntos1, puntos2,veces,global1,global2):

    archivo = open("jugadores.txt", "a")
    hora = sw.get_time()
    registro = name + "," + str(puntos1) + ',' + name2 + ',' + str(puntos2) + ',' + str(hora) + ',' +str(veces)+','+str(global1)+','+str(global2)+','+"\n"
    consulta33[1]=puntos1
    consulta33[3]=puntos2
    consulta33[4]=veces
    consulta33[5]=hora
    consulta33[6]=global1
    consulta33[7]=global2
    print(consulta33)
    archivo.write(registro)
    archivo.close()


#----------------------------------------------------------------MIS JUGADAS--------------------------------------------
#ALL MY PIECES

coloresBlack = ['NeGranHuR', 'NePequeHuR', 'NeGranR', 'NePequeR', 'NeGranHuC', 'NeGranC', 'NePequeC', 'NePequeHuC']
coloresWhite = ['BlaPequeC', 'BlaGranHuR', 'BlaPequeHuR', 'BlaGranR', 'BlaPequeR', 'BlaGranHuC', 'BlaPequeHuC',
                'BlaGranC']
tamanoG = ['NeGranHuR', 'NeGranR', 'NeGranC', "BlaGranHuR", 'NeGranHuC', 'BlaGranR', 'BlaGranHuC', 'BlaGranC']
tamanoP = ['NePequeHuR', 'NePequeR', 'NePequeHuC', 'NePequeC', 'BlaPequeC', 'BlaPequeHuR', 'BlaPequeR', 'BlaPequeHuC']
formaR = ['NeGranHuR', 'NePequeHuR', 'NeGranR', 'NePequeR', 'BlaGranHuR', 'BlaPequeHuR', 'BlaGranR', 'BlaPequeR']
formaC = ['NeGranHuC', 'NePequeHuC', 'NeGranC', 'NePequeC', 'BlaGranHuC', 'BlaPequeHuC', 'BlaGranC', 'BlaPequeC']
huecas = ['NeGranHuR', 'NePequeHuR', 'NeGranHuC', 'NePequeHuC', 'BlaGranHuR', 'BlaPequeHuR', 'BlaGranHuC','BlaPequeHuC']
NoHuecas = ['NeGranR', 'NePequeR', 'NeGranC', 'NePequeC', 'BlaGranR', 'BlaPequeR', 'BlaGranC', 'BlaPequeC']


def jugadas():#WAYS TO WIN
    Tk.update(ventana)
    global jugador1, jugador2,veces,global1,global2
    # -----------------------------------First session Verify in Horizontal-------------------------------------------
    if (tab[0] in coloresBlack and tab[1] in coloresBlack and tab[2] in coloresBlack and tab[3] in coloresBlack) or (
            tab[4] in coloresBlack and tab[5] in coloresBlack and tab[6] in coloresBlack and tab[
        7] in coloresBlack) or (
            tab[8] in coloresBlack and tab[9] in coloresBlack and tab[10] in coloresBlack and tab[
        11] in coloresBlack) or (
            tab[12] in coloresBlack and tab[13] in coloresBlack and tab[14] in coloresBlack and tab[
        15] in coloresBlack):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal")
            jugador1 += 1# increases counter

        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal")
            jugador2 += 1# increases counter
        veces+=1

        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in coloresWhite and tab[1] in coloresWhite and tab[2] in coloresWhite and tab[3] in coloresWhite) or (
            tab[4] in coloresWhite and tab[5] in coloresWhite and tab[6] in coloresWhite and tab[
        7] in coloresWhite) or (
            tab[8] in coloresWhite and tab[9] in coloresWhite and tab[10] in coloresWhite and tab[
        11] in coloresWhite) or (
            tab[12] in coloresWhite and tab[13] in coloresWhite and tab[14] in coloresWhite and tab[
        15] in coloresWhite):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3  \n Ganó de forma Horizontal")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal")
            jugador2 +=1# increases counter
        veces+=1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in tamanoG and tab[1] in tamanoG and tab[2] in tamanoG and tab[3] in tamanoG) or (
            tab[4] in tamanoG and tab[5] in tamanoG and tab[6] in tamanoG and tab[7] in tamanoG) or (
            tab[8] in tamanoG and tab[9] in tamanoG and tab[10] in tamanoG and tab[11] in tamanoG) or (
            tab[12] in tamanoG and tab[13] in tamanoG and tab[14] in tamanoG and tab[15] in tamanoG):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in tamanoP and tab[1] in tamanoP and tab[2] in tamanoP and tab[3] in tamanoP) or (
            tab[4] in tamanoP and tab[5] in tamanoP and tab[6] in tamanoP and tab[7] in tamanoP) or (
            tab[8] in tamanoP and tab[9] in tamanoP and tab[10] in tamanoP and tab[11] in tamanoP) or (
            tab[12] in tamanoP and tab[13] in tamanoP and tab[14] in tamanoP and tab[15] in tamanoP):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in formaR and tab[1] in formaR and tab[2] in formaR and tab[3] in formaR) or (
            tab[4] in formaR and tab[5] in formaR and tab[6] in coloresWhite and tab[7] in formaR) or (
            tab[8] in formaR and tab[9] in formaR and tab[10] in formaR and tab[11] in formaR) or (
            tab[12] in formaR and tab[13] in formaR and tab[14] in formaR and tab[15] in formaR):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in formaC and tab[1] in formaC and tab[2] in formaC and tab[3] in formaC) or (
            tab[4] in formaC and tab[5] in formaC and tab[6] in formaC and tab[7] in formaC) or (
            tab[8] in formaC and tab[9] in formaC and tab[10] in formaC and tab[11] in formaC) or (
            tab[12] in formaC and tab[13] in formaC and tab[14] in formaC and tab[15] in formaC):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma Horizontal")
            jugador2 += 1# increases counter
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)
    elif (tab[0] in huecas and tab[1] in huecas and tab[2] in huecas and tab[3] in huecas) or (
            tab[4] in huecas and tab[5] in huecas and tab[6] in huecas and tab[7] in huecas) or (
            tab[8] in huecas and tab[9] in huecas and tab[10] in huecas and tab[11] in huecas) or (
            tab[12] in huecas and tab[13] in huecas and tab[14] in huecas and tab[15] in huecas):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Huecas")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma Huecas")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)


    elif (tab[0] in NoHuecas and tab[1] in NoHuecas and tab[2] in NoHuecas and tab[3] in NoHuecas) or (
            tab[4] in NoHuecas and tab[5] in NoHuecas and tab[6] in NoHuecas and tab[7] in NoHuecas) or (
            tab[8] in NoHuecas and tab[9] in NoHuecas and tab[10] in NoHuecas and tab[11] in NoHuecas) or (
            tab[12] in NoHuecas and tab[13] in NoHuecas and tab[14] in NoHuecas and tab[15] in NoHuecas):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Nohuecas")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma Nohuecas")
            jugador2 += 1# increases counter
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    # ------------------------------------------------Diagonales----------------------------------------------------
    elif (tab[0] in coloresBlack and tab[5] in coloresBlack and tab[10] in coloresBlack and tab[
        15] in coloresBlack) or (
            tab[3] in coloresBlack and tab[6] in coloresBlack and tab[9] in coloresBlack and tab[12] in coloresBlack):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Diagonal ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Diagonal ")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in coloresWhite and tab[5] in coloresWhite and tab[10] in coloresWhite and tab[
        15] in coloresWhite) or (
            tab[3] in coloresWhite and tab[6] in coloresWhite and tab[9] in coloresWhite and tab[12] in coloresWhite):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Diagonal ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Diagonal ")
            jugador2 += 1# increases counter
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in tamanoG and tab[5] in tamanoG and tab[10] in tamanoG and tab[15] in tamanoG) or (
            tab[3] in tamanoG and tab[6] in tamanoG and tab[9] in tamanoG and tab[12] in tamanoG):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Diagonal ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Diagonal ")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in tamanoP and tab[5] in tamanoP and tab[10] in tamanoP and tab[15] in tamanoP) or (
            tab[3] in tamanoP and tab[6] in tamanoP and tab[9] in tamanoP and tab[12] in tamanoP):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Diagonal ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Diagonal ")
            jugador2 += 1# increases counter
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in formaR and tab[5] in formaR and tab[10] in formaR and tab[15] in formaR) or (
            tab[3] in formaR and tab[6] in formaR and tab[9] in formaR and tab[12] in formaR):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Diagonal ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Diagonal ")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in formaC and tab[5] in formaC and tab[10] in formaC and tab[15] in formaC) or (
            tab[3] in formaC and tab[6] in formaC and tab[9] in formaC and tab[12] in formaC):
        bloq()

        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3\n Ganó de forma Diagonal  ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Diagonal ")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in huecas and tab[5] in huecas and tab[10] in huecas and tab[15] in huecas) or (
            tab[3] in huecas and tab[6] in huecas and tab[9] in huecas and tab[12] in huecas) :
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma huecas")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma huecas")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)


    elif (tab[0] in NoHuecas and tab[5] in NoHuecas and tab[10] in NoHuecas and tab[15] in NoHuecas) or (
            tab[3] in NoHuecas and tab[6] in NoHuecas and tab[9] in NoHuecas and tab[12] in NoHuecas):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Nohuecas 70")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma Nohuecas")
            jugador2 += 1# increases counter

        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    # ----------------------------------------------VERTICALS------------------------------------------------
    elif (tab[0] in coloresBlack and tab[4] in coloresBlack and tab[8] in coloresBlack and tab[12] in coloresBlack) or (
            tab[1] in coloresBlack and tab[5] in coloresBlack and tab[9] in coloresBlack and tab[
        13] in coloresBlack) or (
            tab[2] in coloresBlack and tab[6] in coloresBlack and tab[10] in coloresBlack and tab[
        14] in coloresBlack) or (
            tab[3] in coloresBlack and tab[7] in coloresBlack and tab[11] in coloresBlack and tab[15] in coloresBlack):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Vertical")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3 \n Ganó de forma Vertical")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in coloresWhite and tab[4] in coloresWhite and tab[8] in coloresWhite and tab[12] in coloresWhite) or (
            tab[1] in coloresWhite and tab[5] in coloresWhite and tab[9] in coloresWhite and tab[
        13] in coloresWhite) or (
            tab[2] in coloresWhite and tab[6] in coloresWhite and tab[10] in coloresWhite and tab[
        14] in coloresWhite) or (
            tab[3] in coloresWhite and tab[7] in coloresWhite and tab[11] in coloresWhite and tab[15] in coloresWhite):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3 \n Ganó de forma Vertical")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Vertical")
            jugador2 += 1# increases counter

        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in tamanoG and tab[4] in tamanoG and tab[8] in tamanoG and tab[12] in tamanoG) or (
            tab[1] in tamanoG and tab[5] in tamanoG and tab[9] in tamanoG and tab[13] in tamanoG) or (
            tab[2] in tamanoG and tab[6] in tamanoG and tab[10] in tamanoG and tab[14] in tamanoG) or (
            tab[3] in tamanoG and tab[7] in tamanoG and tab[11] in tamanoG and tab[15] in tamanoG):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3\n Ganó de forma Vertical ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Vertical")
            jugador2 += 1# increases counter

        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in tamanoP and tab[4] in tamanoP and tab[8] in tamanoP and tab[12] in tamanoP) or (
            tab[1] in tamanoP and tab[5] in tamanoP and tab[9] in tamanoP and tab[13] in tamanoP) or (
            tab[2] in tamanoP and tab[6] in tamanoP and tab[10] in tamanoP and tab[14] in tamanoP) or (
            tab[3] in tamanoP and tab[7] in tamanoP and tab[11] in tamanoP and tab[15] in tamanoP):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3\n Ganó de forma Vertical ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Vertical")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in formaR and tab[4] in formaR and tab[8] in formaR and tab[12] in formaR) or (
            tab[1] in formaR and tab[5] in formaR and tab[9] in formaR and tab[13] in formaR) or (
            tab[2] in formaR and tab[6] in formaR and tab[10] in formaR and tab[14] in formaR) or (
            tab[3] in formaR and tab[7] in formaR and tab[11] in formaR and tab[15] in formaR):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3\n Ganó de forma Vertical ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Vertical")
            jugador2 += 1# increases counter

        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in formaC and tab[4] in formaC and tab[8] in formaC and tab[12] in formaC) or (
            tab[1] in formaC and tab[5] in formaC and tab[9] in formaC and tab[13] in formaC) or (
            tab[2] in formaC and tab[6] in formaC and tab[10] in formaC and tab[14] in formaC) or (
            tab[3] in formaC and tab[7] in formaC and tab[11] in formaC and tab[15] in formaC):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3\n Ganó de forma Vertical ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma Vertical")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in huecas and tab[4] in huecas and tab[8] in huecas and tab[12] in huecas) or (
            tab[1] in huecas and tab[5] in huecas and tab[9] in huecas and tab[13] in huecas) or (
            tab[2] in huecas and tab[6] in huecas and tab[10] in huecas and tab[14] in huecas) or (
            tab[3] in huecas and tab[7] in huecas and tab[11] in huecas and tab[15] in huecas):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3\n Ganó de forma Hueca ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma hueca")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] in NoHuecas and tab[4] in NoHuecas and tab[8] in NoHuecas and tab[12] in NoHuecas) or (
            tab[1] in NoHuecas and tab[5] in NoHuecas and tab[9] in NoHuecas and tab[13] in NoHuecas) or (
            tab[2] in NoHuecas and tab[6] in NoHuecas and tab[10] in NoHuecas and tab[14] in NoHuecas) or (
            tab[3] in NoHuecas and tab[7] in NoHuecas and tab[11] in NoHuecas and tab[15] in NoHuecas):
        bloq()
        if turno == 1:
            messagebox.showinfo("Ganaste" + nomj1, "Puntaje Obtenido: 3\n Ganó de forma NoHuecas ")
            jugador1 += 1# increases counter
        elif turno == 0:
            messagebox.showinfo("Ganaste" + nomj2, "Puntaje Obtenido: 3\n Ganó de forma NoHuecas")
            jugador2 += 1# increases counter
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2,veces,global1,global2)

    elif (tab[0] ==empate[0] and tab[1]==empate[1] and tab[2]==empate[2] and tab[3]==empate[3])or(
        tab[4]==empate[4] and tab[5]==empate[5] and tab[6]==empate[6] and tab[7]==empate[7])or(
        tab[8]==empate[8] and tab[9]==empate[9] and tab[10]==empate[10] and tab[11]==empate[11])or(
        tab[12]==empate[12] and tab[13]==empate[13] and tab[14]==empate[14] and tab[15]==empate[15]):

        messagebox.showinfo('Perdedores:)','Se ha producido un empate')
        veces += 1
        partidas(prueba())
        CapturelRegistry(nomj1, nomj2, jugador1, jugador2, veces,global1,global2)

    else:

        messagebox.showinfo('MAL!!','Se le restan 2 puntos')
        partidas(prueba())
#-------------------------FUNCTION CALLS THE FIRST WINDOW--------------------------------------------------------------

def main(): #Window principal
    Tk.update(ventana)
    Label(ventana, image=fondo1).place(x=0, y=0)

    barramenu = Menu(ventana)
    menuarchi = Menu(barramenu)
    menuarchi.add_command(label= 'Estadistica',command=lambda: estadistica())
    menuarchi.add_command(label='Salir', command=quit)
    ventana.config(menu=menuarchi)

    Button(ventana, text=" INGRESAR ", font="Elephant", heigh=1, width=10, bg="#696969", fg="#FFF",
                           activebackground="#808080",
                           activeforeground="#FFF", command=lambda: ventanaPrincipal()).place(x=550, y=250)
    ventana.mainloop()

main()