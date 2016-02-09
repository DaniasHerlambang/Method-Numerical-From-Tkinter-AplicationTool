"""
Name             : Aplication absent from Tkinter version 1
Created By       : Rahmandani Herlambang (Danias) & Aldino Kemal Adi Gumawang (Kemal)
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/DaniasHerlambang13/Aplication-Metode-Numerik-From-Tkinter.git
Thanks to        : Python Tkinter - Mexico Tech - Newbie - LINUX 
"""

#****************************************** TK UNTUK DATA UTAMA ********************************************************************************
from Tkinter import*
import Tkinter as tk
from tkMessageBox  import*
import ttk
import time
import math
import os

'''
=====================================
|Contoh soal :                      |
|   x^3-7x+1 => ^ : pangkat         |
|                                   |
====================================='''
#****************************************** CLASS UNTUK TOOLTIP ******************************************************************

class CreateToolTip(object):

    def __init__(self, widget, text='tooltip'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        
        # membuat toplevel window baru
        self.tw = tk.Toplevel(self.widget)
        
        # menghilangkan kulit window tooltip
        self.tw.wm_overrideredirect(True)
        
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background='gold',fg='darkred', relief='solid', borderwidth=1,
                       font=('FreeSerif', "15", "normal"))
        label.pack(ipadx=1)
    def close(self, event=None):
        if self.tw:
            self.tw.destroy()
            
#****************************************** CLASS UNTUK KOMPONEN TAMPILAN AWAL PROGRAM******************************************************************

class Data(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(False, False)
        self.teksJam = StringVar()
        self.initUI()

        # suara pembuka aplikasi
        os.system("spd-say -l en -t female3 'welcome in aplication, informatic engenering, we are, cyber , no ,drag ,and ,drop ,area'")
##        os.system("spd-say -l id -t female3 'windows itu payah'")

     
    def initUI(self):
        
        self.datJam_menu = time.strftime("Newton Raphson VS Secant")
        # atur ukuran window
        # menempatkan window di tengah layar PC/Laptop
        lebar = 780
        tinggi = 660
 
        # ************************* penggunaan fungsi winfo_screenwidth()
        setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
        # ************************* penggunaan fungsi winfo_screenheight()
        setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
 
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY-35))
        # **************************************************************** 
        
        mainFrame = Frame(self.parent,bg='darkred',relief=RIDGE,bd=10 )
        mainFrame.pack(fill=BOTH, expand=YES)

        self.parent.title(self.datJam_menu)


        # ********************** MENUBAR ************************************** 
        
        self.menubar = Menu(self.parent)
        self.parent.config(menu = self.menubar)
        
        self.ums = PhotoImage(file='F.gif')
        fileMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = 'ABOUT PROGRAM...',compound='right',menu = fileMenu)
        fileMenu.add_command( label = 'LINUX TEAM NOT WINDOWS',image=self.ums,compound='top')


        # ********************** FRAME INTI ************************************** 
        
        self.fr_inti = Frame(mainFrame,bg='black')
        self.fr_inti.pack(expand=YES,side=BOTTOM)

        # ********************** KUMPULAN FRAME ATAS DAN INPUTAN ***************** 

        fr_input = Frame(self.fr_inti, bg = 'darkred')
        fr_input.pack(fill=X,pady=2,side=TOP)
        
        self.soal = Entry(fr_input,bg='white',relief=RIDGE,bd=7,font=('FreeSerif', 20))
        self.soal.pack(side=TOP ,fill=X, expand=YES)
        
        # tooltip ketika mouse berada di entry soal
        soal_ttp = CreateToolTip(self.soal, "MASUKAN SOAL SEKARANG")

        self.klik = Button(fr_input,bg='gray' , text ='EKSEKUSI', font=('FreeSerif', 13), cursor='hand2', command=self.cara_kerja)
        self.klik.pack(side=BOTTOM, expand=YES)

        # ********************** KUMPULAN FRAME TENGAH DAN HASIL ***************** 

        fr_tengah = Frame(self.fr_inti, bg = 'brown')
        fr_tengah.pack(fill=X,pady=2,side=TOP)

        fr_tengahkiri = LabelFrame(fr_tengah, bg = 'darkred')
        fr_tengahkiri.pack(pady=2,side=LEFT)

        fr_tengahkiriatas = Frame(fr_tengahkiri, bg = 'darkred')
        fr_tengahkiriatas.pack(fill=X,pady=2,side=TOP)        

        fr_tengahkanan = LabelFrame(fr_tengah, bg = 'darkred')
        fr_tengahkanan.pack(pady=2,side=RIGHT)

        fr_tengahkananatas = Frame(fr_tengahkanan, bg = 'darkred')
        fr_tengahkananatas.pack(fill=X,pady=2,side=TOP)        



        # ********************** LABEL NAMA NR vs SC & INPUT x0 , x1 *****************
        
        #-----------------------newtonraphson-------------------------------------------------
        
        self.newtownraphson= Label(fr_tengahkiriatas , text='Newton Raphson', bg='darkred' , fg='gold', bd=0, font=('FreeSerif', 13))
        self.newtownraphson.pack(pady=2,side=TOP)

        self.rumusNR= Label(fr_tengahkiriatas , text='  X0 ', bg='darkred' ,fg='gold', bd=0, font=('FreeSerif', 10))
        self.rumusNR.pack(pady=2,side=LEFT)

        self.x0_NR= Entry(fr_tengahkiriatas ,relief=RIDGE,bd=7, font=('Vijaya', 10))
        self.x0_NR.pack(fill=X,side=LEFT,expand=YES)

        # tooltip ketika mouse berada di entry x0 
        soal_ttp = CreateToolTip(self.x0_NR, "MASUKAN X0")

        #-----------------------secant-------------------------------------------------
        
        self.secant= Label(fr_tengahkananatas , text='Secant', bg='darkred' , fg='gold', bd=0, font=('FreeSerif', 13))
        self.secant.pack(pady=2,side=TOP)

        self.rumusSC1= Label(fr_tengahkananatas , text='  X0 ', bg='darkred' , fg='gold', bd=0, font=('FreeSerif', 10))
        self.rumusSC1.pack(pady=2,side=LEFT)

        self.x0_Sec= Entry(fr_tengahkananatas , relief=RIDGE, bd=7, font=('FreeSerif', 10), width=10)
        self.x0_Sec.pack(fill=X,side=LEFT,expand=YES)

        # tooltip ketika mouse berada di entry x0 
        soal_ttp = CreateToolTip(self.x0_Sec, "MASUKAN X0")

        self.rumusSC2= Label(fr_tengahkananatas , text='  X1 ',bg='darkred' , fg='gold', bd=0,font=('FreeSerif', 10))
        self.rumusSC2.pack(pady=2,side=LEFT)

        self.x1_Sec= Entry(fr_tengahkananatas ,relief=RIDGE,bd=7,font=('FreeSerif', 10),width=10)
        self.x1_Sec.pack(fill=X,side=LEFT,expand=YES)

        # tooltip ketika mouse berada di entry x1 
        soal_ttp = CreateToolTip(self.x1_Sec, "MASUKAN X1")
        

        # ************************* penggunaan listbox n scroll kiri
        
        self.listboxData1=Listbox(fr_tengahkiri, bg='turquoise',fg='black',width=40 , height=15)
        self.listboxData1.pack(fill=BOTH, side=RIGHT,expand=YES)
        s=ttk.Style()
        s.theme_use('classic')
        s.configure('TScrollbar', background='black')
        scrollbar = ttk.Scrollbar(fr_tengahkiri, orient=VERTICAL,
                                command=self.listboxData1.yview,cursor='hand2')
        scrollbar.pack(side=LEFT, fill=Y)
        self.listboxData1.config(yscrollcommand=scrollbar.set)

        # ************************* penggunaan listbox n scroll kanan
        
        self.listboxData2=Listbox(fr_tengahkanan, bg='turquoise',fg='black',width=40 , height=15)
        self.listboxData2.pack(fill=BOTH, side=LEFT,expand=YES)
        s=ttk.Style()
        s.theme_use('classic')
        s.configure('TScrollbar', background='black')
        scrollbar = ttk.Scrollbar(fr_tengahkanan, orient=VERTICAL,
                                command=self.listboxData2.yview,cursor='hand2')
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listboxData2.config(yscrollcommand=scrollbar.set)


        # ********************** KUMPULAN FRAME BAWAH DAN HASIL ***************** 

        fr_bawah = LabelFrame(self.fr_inti, bg = 'brown')
        fr_bawah.pack(fill=X,pady=2,side=BOTTOM)

        self.perbandingan= Label(fr_bawah , text='PERBANDINGAN',bg='darkred' , fg='gold', bd=0,font=('FreeSerif', 13))
        self.perbandingan.pack(fill=X,pady=2,side=TOP)

        # ************************* penggunaan listbox n scroll bawah
        
        self.listboxData3=Listbox(fr_bawah, bg='turquoise',fg='black',width=40 , height=13)
        self.listboxData3.pack(fill=BOTH, side=LEFT,expand=YES)
        s=ttk.Style()
        s.theme_use('classic')
        s.configure('TScrollbar', background='black')
        scrollbar = ttk.Scrollbar(fr_bawah, orient=VERTICAL,
                                command=self.listboxData3.yview,cursor='hand2')
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listboxData3.config(yscrollcommand=scrollbar.set)

    # ************************* function untuk mengkosongkan listbox dan entry
    
    def kosongan(self):
        self.listboxData1.delete(0,END)
        self.listboxData2.delete(0,END)
        self.listboxData3.delete(0,END)
        
        self.soal.delete(0, END)
        self.x0_NR.delete(0, END)
        self.x0_Sec.delete(0, END)
        self.x1_Sec.delete(0, END)

        self.klik.configure(text="EKSEKUSI", font=('FreeSerif', 13), cursor='hand2',command=self.cara_kerja)

#=========================================== Metode Newton Raphson ====================================================#
    #================ Memisah soal ==================#
    def split_soal_NR(self, soal):
        soal_split = []
        soal_pisah_per_bagian = ""
        for i in soal:
            if i == "+":
                soal_split.append(soal_pisah_per_bagian)
                soal_pisah_per_bagian = ""
            elif i == "-":
                soal_split.append(soal_pisah_per_bagian)
                soal_pisah_per_bagian = '-'
            else:
                soal_pisah_per_bagian += i
        soal_split.append(soal_pisah_per_bagian)
        if soal[0] == "-":
            soal_split.remove("")
        return soal_split

    #================ Turunan Soal ==================#
    def turunan_soal_NR(self, soal):
        turunan = []
        for i in soal:
            # print i
            for j in range(len(i)):
                if i[j] == "^":
                    pangkat = int(i[j+1:])
                    if len(i) <= 3:
                        angka_turunan = pangkat * 1
                        pangkat_turunan = pangkat - 1
                        turunan.append(str(angka_turunan)+"x^"+str(pangkat_turunan))
                    elif len(i) <= 4 and i[0] == "-":
                        angka_turunan = pangkat * 1
                        pangkat_turunan = pangkat - 1
                        turunan.append("-"+str(angka_turunan)+"x^"+str(pangkat_turunan))
                    else:
                        angka_turunan = pangkat * float(i[:j-1])
                        pangkat_turunan = pangkat-1
                        turunan.append(str(angka_turunan)+"x^"+str(pangkat_turunan))
                elif i[-1] == "x":
                        if (i[:-1])=='-':
                            turunan.append('-1')
                        else:
                            turunan.append(i[:-1])

                        break
        return turunan


    #================ Angka depan ==================#
    def angka_depan_NR(self, soal_terpisah):
        data_angka_depan = []
        for i in soal_terpisah:
            for j in range(len(i)):
                if i[j] == "x":
                    if i[:j] == "":
                        data_angka_depan.append(1)
                    elif i[:j] == "-":
                        data_angka_depan.append(-1)
                    else:
                        data_angka_depan.append(float(i[:j]))
                elif "x" not in i:
                    data_angka_depan.append(float(i))
                    break
        return data_angka_depan


    #================ Nilai Pangkat ==================#
    def pangkat_NR(self, soal_terpisah):
        data_pangkat = []
        for i in soal_terpisah:
            # print i
            for j in range(len(i)):
                if i[j] == "^":
                    data_pangkat.append(float(i[j+1:]))
                elif i[j] == "x" and i[-1] == "x":
                    data_pangkat.append(float(1))
            if "x" not in i:
                data_pangkat.append(float(1))
        return data_pangkat


    #================ Angka depan Turunan ==================#
    def angka_depan_turunan_NR(self, turunan_terpisah):
        data_angka_depan_turunan = []
        for i in turunan_terpisah:
            for j in range(len(i)):
                if i[j] == "x":
                    if i[:j] == "":
                        data_angka_depan_turunan.append(1)
                    elif i[:j] == "-":
                        data_angka_depan_turunan.append(-1)
                    else:
                        data_angka_depan_turunan.append(float(i[:j]))
                elif "x" not in i:
                    data_angka_depan_turunan.append(float(i))
                    break
        return data_angka_depan_turunan


    #================ Pangkat Turunan ==================#

    def pangkat_turunan_NR(self, turunan_terpisah):
        data_pangkat = []
        for i in turunan_terpisah:
            # print i
            for j in range(len(i)):
                if i[j] == "^":
                    data_pangkat.append(float(i[j+1:]))
                elif i[j] == "x" and i[-1] == "x":
                    data_pangkat.append(float(1))
            if "x" not in i:
                data_pangkat.append(float(1))
        return data_pangkat


    #================ Mencari Fx ==================#
    def Fx_nilai(self, x0):
        Fx = 0
        for i in range(len(self.soal_terpisah)):
            if "x" in self.soal_terpisah[i]:
                Fx += self.angka_depan_int[i] * (x0 ** self.pangkatX[i])
            else:
                Fx += self.angka_depan_int[-1]
        return Fx

    #================ Mencari F'x===============#
    def Fx_turunan_nilai(self, x0):
        Fx_turunan = 0
        for i in range(len(self.turunan_terpisah)):
            if "x" in self.turunan_terpisah[i]:
                Fx_turunan += self.angka_dpn_turunan[i] * (x0 ** self.pangkat_turunanX[i])
            else:
                Fx_turunan += self.angka_dpn_turunan[-1]
        return Fx_turunan


    #================ Nilai Xi+1 ===============#
    def x1_nilai(self, x0):
        x1 = x0 - (self.Fx / self.Fx_turunan)
        return x1



#=============================================== Metode Secant ========================================================#

    #================== Split soal Sekan ==================#
    def split_soal_sekan(self, soal):
        soal_split = []
        soal_pisah_per_bagian = ""
        for i in soal:
            if i == "+":
                soal_split.append(soal_pisah_per_bagian)
                soal_pisah_per_bagian = ""
            elif i == "-":
                soal_split.append(soal_pisah_per_bagian)
                soal_pisah_per_bagian = '-'
            else:
                soal_pisah_per_bagian += i
        soal_split.append(soal_pisah_per_bagian)
        if soal[0] == "-":
            soal_split.remove("")
        return soal_split


    #================== angka depan e Sekan ==================#
    def angka_depan_e_sekan(self, soal_terpisah):
        angka_dpn_sekan = []
        for i in soal_terpisah:
            if "e" in i:
                for j in range(len(i)):
                    if i[j] == "e":
                        if i[:j] == "-":
                            angka_dpn_sekan.append(-1)
                        elif i[:j] == "":
                            angka_dpn_sekan.append(1)
                        else:
                            angka_dpn_sekan.append(i[:j])
            else:
                angka_dpn_sekan.append(1)
        return angka_dpn_sekan


    #================== Angka depan ==================#
    def angka_depan_sekan(self, soal_terpisah):
        data_angka_depan = []
        for i in soal_terpisah:
            for j in range(len(i)):
                if i[j] == "x" and "e" not in i:
                    if i[:j] == "":
                        data_angka_depan.append(1)
                    elif i[:j] == "-":
                        data_angka_depan.append(-1)
                    else:
                        data_angka_depan.append(float(i[:j]))
                if "e" in i[j]:
                    if "-" in i:
                        data_angka_depan.append(0-math.exp(1))
                    else:
                        data_angka_depan.append(math.exp(1))
                elif "x" not in i:
                    data_angka_depan.append(float(i))
                    break

        return data_angka_depan


    #================== Nilai Pangkat ==================#
    def pangkat_sekan(self, soal_terpisah):
        data_pangkat = []
        for i in soal_terpisah:
            # print i
            for j in range(len(i)):
                if i[j] == "^" and "e" not in i:
                    data_pangkat.append(i[j+1:])
                elif i[j] == "^" and "e" in i:
                    data_pangkat.append("%f")
                elif i[j] == "x" and i[-1] == "x" and "e" not in i:
                    data_pangkat.append(1)

                # elif i[j] == "x" and i[-1] == "x" and "e" not in i:
                #     data_pangkat.append(1)

            if "x" not in i:
                data_pangkat.append(1)
        return data_pangkat


    #================== Nilai depan x pada pangkat e ==================#

    def angka_x_depan_e(self):
        angka_x_dpn_e = 0
        try:
            for i in self.soal_terpisah:
                for j in range(len(i)):
                    if "e" in i:
                        if i[j] == "^":
                            angka_x_dpn_e += float(i[j+1:-1])
        except ValueError:
            angka_x_dpn_e += 1.0
        return angka_x_dpn_e

    #================== Nilai Fx ==================#
    def Fx_nilai(self, x0):
        Fx = 0
        for K in range(len(self.soal_terpisah)):
            if "e" in self.soal_terpisah[K]:
                Fx += float(self.angka_depan_e_sekan(self.soal_terpisah)[K]) * (float(self.angka_depan_sekan(self.soal_terpisah)[K]) ** (float(self.pangkatX[K] % (x0)) * self.angka_x_dpn_e()))
            elif "e" not in self.soal_terpisah[K] and "x" not in self.soal_terpisah[K]:
                Fx += self.angka_depan_sekan(self.soal_terpisah)[-1]
            else:
                Fx += self.angka_depan_e_sekan(self.soal_terpisah)[K] * float(self.angka_depan_sekan(self.soal_terpisah)[K]) * (x0 ** float(self.pangkatX[K]))

        return Fx


    def x2_nilai(self, x1):
        # print "dalam def => x1=", x1
        # print "dalam def => self.Fx0=", self.Fx0
        # print "dalam def => self.Fx1=", self.Fx1
        # print "dalam def => self.x0_Sec_user=", self.x0_Sec_used
        Fx2_hasil = x1 - (self.Fx1 * (x1 - self.x0_Sec_used))/(self.Fx1 - self.Fx0)
        return Fx2_hasil


 #================ Mulai Kerja Newton Raphson================#
    def cara_kerja(self):
        try :
            self.klik.configure(text="ULANGI", font=('FreeSerif', 13), cursor='hand2',command=self.kosongan)
            self.soal_terpisah = self.split_soal_NR(self.soal.get())
            self.turunan_terpisah = self.turunan_soal_NR(self.soal_terpisah)
            self.angka_depan_int = self.angka_depan_NR(self.soal_terpisah)
            self.pangkatX = self.pangkat_NR(self.soal_terpisah)
            self.angka_dpn_turunan = self.angka_depan_turunan_NR(self.turunan_terpisah)
            self.pangkat_turunanX = self.pangkat_NR(self.turunan_terpisah)

            iterasi_NR = 0
            waktu_awal_NR = time.time()
            self.x0_NR_used = float(self.x0_NR.get())

            for i in range(1, 1000):
                # print "Iterasi ke-", i

                #iterasi pada GUI
                self.listboxData1.insert(END, "iterasi -"+str(i))

                iterasi_NR += 1
                self.Fx = self.Fx_nilai(self.x0_NR_used)

                # print "hasil F(x) :", self.Fx
                # hasil F(x) GUI
                self.listboxData1.insert(END, "F(x) : " + str(self.Fx))

                self.Fx_turunan = self.Fx_turunan_nilai(self.x0_NR_used)

                # print "Hasil F'(x) :", self.Fx_turunan
                # hasil F'(x) GUI
                self.listboxData1.insert(END, "F'(x) : " + str(self.Fx_turunan))

                # print "x0 =", self.x0_NR_used
                # x0 GUI
                self.listboxData1.insert(END, "x0 = " + str(self.x0_NR_used))

                self.x1_NR = self.x1_nilai(self.x0_NR_used)

                # print "x1 =", self.x1_NR
                self.listboxData1.insert(END, "x1 : " + str(self.x1_NR))

                if str(self.x0_NR_used) == str(self.x1_NR):
                    break
                elif self.x0_NR_used == self.x1_NR:
                    break
                elif self.x0_NR_used != self.x1_NR:
                    self.x0_NR_used = self.x1_NR
                # print "\n"
                self.listboxData1.insert(END, " ")


            waktu_ahir_NR = time.time()
            waktu_selesai_NR = waktu_ahir_NR - waktu_awal_NR
            # print "\nwaktu yang dibutuhkan (Newton Raphson) :", waktu_selesai_NR

            # print "\n\n"

    #================== Mulai kerja Secant ==================#

            self.x0_Sec_used = float(self.x0_Sec.get())
            self.x1_Sec_used = float(self.x1_Sec.get())
            self.soal_terpisah = self.split_soal_sekan(self.soal.get())
            self.angka_x_dpn_e = self.angka_x_depan_e()
            self.pangkatX = self.pangkat_sekan(self.soal_terpisah)


            iterasi_secant = 0
            waktu_awal_secant = time.time()
            for i in range(1, 100):
               try:
                    # print "Iterasi ke-", i
                    # Itrasi GUI
                    self.listboxData2.insert(END, "Iterasi ke- " + str(i))
                    iterasi_secant += 1

                    # print "x0 :", self.x0_Sec_used
                    # x0_sec GUI
                    self.listboxData2.insert(END, "x0 : " + str(self.x0_Sec_used))

                    # print "x1 :", self.x1_Sec_used
                    # x1_sec GUI
                    self.listboxData2.insert(END, "x1 : " + str(self.x1_Sec_used))

                    self.Fx0 = self.Fx_nilai(self.x0_Sec_used)
                    self.Fx1 = self.Fx_nilai(self.x1_Sec_used)
                    self.x2_Sec = self.x2_nilai(self.x1_Sec_used)
                    # print "hasil F(x0) :", self.Fx0
                    # F(x0)GUI
                    self.listboxData2.insert(END, "F(x0) : " + str(self.Fx0))

                    # print "hasil F(x1) :", self.Fx1
                    # F(x1) GUI
                    self.listboxData2.insert(END, "F(x1) : " + str(self.Fx1))

                    # print "hasil x2 :", self.x2_Sec
                    # x2 GUI
                    self.listboxData2.insert(END, "x2 : " + str(self.x2_Sec))

                    # print "\n"
                    self.listboxData2.insert(END, " ")

                    if self.x2_Sec != 0 and self.x1_Sec_used != 0:
                        self.x0_Sec_used = self.x1_Sec_used
                        self.x1_Sec_used = self.x2_Sec
                    else:
                        break
               except ZeroDivisionError:
                   # print "\n[+]Berhenti pada iterasi ke-", i-1
                   # print "[+]TIDAK DAPAT DIBAGI DENGAN 0\n"
                    self.listboxData2.insert(END, "[+]Berhenti pada iterasi ke-" + str(i-1))
                    self.listboxData2.insert(END, "[+]TIDAK DAPAT DIBAGI DENGAN 0")
                    break

            waktu_ahir_secant = time.time()
            waktu_total_secant = waktu_ahir_secant - waktu_awal_secant

            # print "waktu yang dibutuhkan (Secant) :", waktu_total_secant

    #================== Perbandingan ==================#
            # print "\n"
            # print 20*"=", "Perbandingan", 20*"="
            # print """\nWaktu :
            # \t[+]Newton Raphson = %s
            # \t[+]Secant         = %s""" % (str(waktu_selesai_NR), str(waktu_total_secant)),
            self.listboxData3.insert(END, "Waktu :")
            self.listboxData3.insert(END, "[+]Newton Raphson = %s" % (str(waktu_selesai_NR)))
            self.listboxData3.insert(END, "[+]Secant                = %s" % (str(waktu_total_secant)))


            if waktu_selesai_NR < waktu_total_secant:
                selisih_waktu = waktu_total_secant - waktu_selesai_NR
                # print "\n\t[+]Selisih waktu  =", selisih_waktu
                self.listboxData3.insert(END, "[+]Selisih waktu       = " + str(selisih_waktu))

                # print "\tNewton Raphson lebih cepat '%s' detik dari Secant" % (str(selisih_waktu))
                self.listboxData3.insert(END, "\tNewton Raphson lebih cepat %s detik dari Secant" % (str(selisih_waktu)))

            elif waktu_selesai_NR > waktu_total_secant:
                selisih_waktu = waktu_selesai_NR - waktu_total_secant
                # print "\n\t[+]Selisih waktu =", selisih_waktu
                self.listboxData3.insert(END, "[+]Selisih waktu       = " + str(selisih_waktu))

                # print "\tSecant lebih cepat '%s' detik dari Newton Raphson" % (str(selisih_waktu))
                self.listboxData3.insert(END, "\tSecant lebih cepat '%s' detik dari Newton Raphson" % (str(selisih_waktu)))

            else :
                print "\Newton Raphson dan sekan memiliki waktu yang sama yaitu %s detik" % (waktu_selesai_NR)
                self.listboxData3.insert(END, "\Newton Raphson dan sekan memiliki waktu yang sama yaitu %s detik" % (waktu_selesai_NR))

            # print "\t*Kecepatan program (waktu) tergantung dengan kecepatan PC*"
            self.listboxData3.insert(END, "\tKecepatan program (waktu) tergantung dengan kecepatan PC")

            print "\n"
            self.listboxData3.insert(END, " ")
            # print '''Iterasi :
            # \t[+]Newton Raphson = %d iterasi
            # \t[+]Secant         = %d iterasi ''' % (iterasi_NR, iterasi_secant-1)

            self.listboxData3.insert(END, "Iterasi :")
            self.listboxData3.insert(END, "[+]Newton Raphson = %d iterasi" % (iterasi_NR))
            self.listboxData3.insert(END, "[+]Secant                = %d iterasi" % (iterasi_secant-1))

            if iterasi_NR < iterasi_secant:
                selisih_iterasi = (iterasi_secant - 1) - iterasi_NR
                # print "\t[+]Selisih iterasi  =", selisih_iterasi
                self.listboxData3.insert(END, "[+]Selisih iterasi = " + str(selisih_iterasi))

                # print "\tNewton Raphson lebih cepat '%d' iterasi dari Secant" % (selisih_iterasi)
                self.listboxData3.insert(END, "\tNewton Raphson lebih cepat '%d' iterasi dari Secant" % (selisih_iterasi))

            elif iterasi_NR > iterasi_secant:
                selisih_iterasi = iterasi_NR - (iterasi_secant - 1)
                # print "\t[+]Selisih iterasi =", selisih_iterasi
                self.listboxData3.insert(END, "[+]Selisih iterasi = " + str(selisih_iterasi))

                # print "\tSecant lebih cepat '%d' iterasi dari Newton Raphson" % (selisih_iterasi)
                self.listboxData3.insert(END, "\tSecant lebih cepat '%d' iterasi dari Newton Raphsont" % (selisih_iterasi))
            else :
                print "\tSecant sama cepat dengan Newton Raphson sebanyak '%d' iterasi dari " %(iterasi_secant)

        except :
            showerror("KESALAHAN","Mohon isikan semua subjek dengan benar")
#----------------------------------------------------------------------------------------------------------------#
if __name__ =='__main__':
    root = Tk()
    app = Data(root)
    root.mainloop()


