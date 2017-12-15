## Coded by SergentThomasKelly, started the 15th of December 2017 at 9:26 AM
# first version finished same day at 6:37 PM


# =========================== INITIALISATION ================================= #
# >>> IMPORTING ALL MODULES NEEDED <<<
from tkinter import *
import tkinter.messagebox
import wave
import math
import binascii
from tkinter.filedialog import *

# >>> PREPARING VARIABLES USED <<<
FrequencyMain = 0
IntensityMain = 0


# =========================== FUNCTIONS ====================================== #
# >>> UPDATE FREQUENCY WITH SCALE <<<
def updateFrequency(x):
    global FrequencyMain
    FrequencyMain = int(x)

# >>> UPDATE INTENSITY WITH SCALE <<<
def updateIntensity(x):
    global IntensityMain
    IntensityMain = int(x)

# >>> MAIN FUNCTION, CORE OF THE PROGRAM <<<
def demarrer():
    global FrequencyMain, IntensityMain
    if duree.get() != '':
        if FrequencyMain == 0:
            FrequencyMain=20
        if IntensityMain ==0:
            IntensityMain=3
        NomFichier = asksaveasfilename(defaultextension=".wav",
                parent=root, title="Where to save the created binaural sound ?", filetypes=[("WAV","*.wav")])
        if NomFichier == None or NomFichier == '':
            NomFichier = 'binaural.wav'
            tkinter.messagebox.showerror("Something went wrong", "You did not set the destination file...\nWill be saved where you executed this program.")
        ProcessingInfo= Label(root, text='Signal processing, please wait\nIt may take some time...', bg='snow3')
        ProcessingInfo.pack(padx=5, pady=5)
        tkinter.messagebox.showwarning("It's going to happen !", "The signal will take some time to be created !\nPlease don't panic !\nPress Ok when you're ready.")
        leSon = wave.open(NomFichier,'w')
        nbCanal = 2
        nbOctet = 1
        fech = 44100
        frequencel = FrequencyMain
        frequencer= FrequencyMain + IntensityMain
        niveau = 1
        dureeensecondes = duree.get()
        nbEchantillon = int(dureeensecondes) * fech
        amplitude = 127.5 * niveau
        parametres = (nbCanal, nbOctet, fech, nbEchantillon, 'NONE', 'not compressed')
        leSon.setparams(parametres)
        for i in range(nbEchantillon):
            valeurDataLeft = wave.struct.pack('B', int(128.0 + amplitude * math.sin( 2.0 * math.pi * frequencel * i/fech)))
            valeurDataRight = wave.struct.pack('B', int(128.0 + amplitude * math.sin( 2.0 * math.pi * frequencer * i/fech)))
            leSon.writeframes(valeurDataLeft)
            leSon.writeframes(valeurDataRight)
        leSon.close()
        ProcessingInfo.destroy()
        tkinter.messagebox.showinfo("That's all done !", "Finished")
    else:
        tkinter.messagebox.showerror("Something went wrong", "You did not set the duration !\nPlease be sure to give every required settings asked.")


# =========================== MAIN GUI AND WIDGETS =========================== #
root = Tk()
root.title("Create binaural sound easily!")
if os.path.isfile('iconBinaural.ico') == True:
    root.iconbitmap('iconBinaural.ico')
root.resizable(width=False, height=False)
root.configure(background='snow3')
LabelMain=Label(root, text='Create binaural sound easily !', bg='snow3').pack(padx=10, pady=5)
ChooseFrequency=Scale(root, orient='horizontal', from_=20, to=16020, resolution=20,
            tickinterval=4000, length=390, label='Frequency (Hz)',
            command=updateFrequency, bg='snow3').pack(padx=10, pady=10)
dureeLabel=Label(root, text="Time (s):", bg='snow3').pack()
duree=StringVar()
dureeEntry= Entry(root, textvariable=duree, width=10).pack()
ChooseIntensity=Scale(root, orient='horizontal', from_=1, to=5, resolution=1,
            tickinterval=1, length=390, label='Intensity level',
            command=updateIntensity, bg='snow3').pack(padx=10, pady=10)
startButton= Button (root, text='START!', command=demarrer, bg='lawn green').pack(side='right', padx=50, pady=5)
quitButton= Button (root, text='QUIT', command=root.destroy, bg='orange red').pack(side='left', padx=50, pady=5)
mainloop()

#END
