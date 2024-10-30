import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode

# temel sistem fonksiyonu
def qrKodOlustur():

    url = urlGirdi.get()

    if url:
        qrUrl = pyqrcode.create(url)
        dosyaYolu = filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG DOSYALARI","*.svg")])

        if dosyaYolu:
            qrUrl.svg(dosyaYolu, scale=8)
            durumEtiketi.configure(text = "QR kodu olusturuldu ve kaydedildi")
        else:
            durumEtiketi.config(text="Dosya kaydedilmedi")

    else:

        durumEtiketi.config(text="Lütfen bir URL girin")

# arayuz tasarimi

uygulamaPenceresi = tk.Tk()

uygulamaPenceresi.title("Qr kod olusturucu")
uygulamaPenceresi.geometry("400x150")

#ekrandaki goruntu alani bu
label = tk.Label(uygulamaPenceresi,text = "url adresini girin:")

#tk.entry kullanicidan girdi almayi sagliyor
urlGirdi = tk.Entry(uygulamaPenceresi,width=40)

#fonksiyonu calistiracak buton
qrKodOlusturButonu = tk.Button(uygulamaPenceresi,text="olustur", command= qrKodOlustur,width=15)

#durum etiketi
durumEtiketi = tk.Label(uygulamaPenceresi,text = "")


label.grid(row=0,column=0,padx=10,pady=10)
urlGirdi.grid(row=0,column=1,padx=10,pady=10)
qrKodOlusturButonu.grid(row=2,column=1,padx=10,pady=10)
durumEtiketi.grid(row=3,column=1,padx=10,pady=10)


uygulamaPenceresi.mainloop()