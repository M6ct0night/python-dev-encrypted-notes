import tkinter as tk
from tkinter import messagebox
import base64

ekran=tk.Tk()
ekran.title("encrypted notes")
ekran.configure(bg="white")
ekran.minsize(height=900,width=500)

def tt():
    messagebox.showinfo("Bilgilendirme", "Bu bir uyarı penceresidir!")


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save_note():
    title = baslik.get()
    note_content = note.get("1.0", tk.END).strip()
    mst=masterkey.get()


    if not title or not note_content or not mst:
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun!")
        return


    enote = encode(mst, note_content)

    try:
        with open("notes.txt", "a")as file:
            file.write(f"Başlık: {title}\n")
            file.write(f"Not: {enote}\n")
            file.write("-" * 20 + "\n")
        messagebox.showinfo("Başarılı", "Not başarıyla kaydedildi!")

        # Alanları temizle
        baslik.delete(0, tk.END)
        note.delete("1.0", tk.END)
        masterkey.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Hata", f"Not kaydedilemedi!\n{e}")
        mst = masterkey.get()

def decodeation():
    note_content = note.get("1.0", tk.END).strip()
    mst = masterkey.get()

    if not note_content or not mst:
        messagebox.showwarning("hata",f"gerekli alanları doldurunuz")
        return

    try:
        deco=decode(mst,note_content)
        note.delete("1.0", tk.END)  # Tüm metni sil
        note.insert(tk.END, f"{deco}")  # Yeni mesajı ekle
    except Exception as e:
        messagebox.showerror("Hata", f"çevrilemedi!\n{e}")

resim = tk.PhotoImage(file="hck.png")
etiket = tk.Label(ekran, image=resim)
etiket.configure(height=150,width=150,padx=5,pady=300)
etiket.grid(row=1,column=2)

bosluk=tk.Label(ekran,text="gizli",fg="white",bg="white",width=15)
bosluk.grid(column=1, row=1)


yazi1=tk.Label(ekran,text="başlık",fg="black",bg="white")
yazi1.grid(row=2,column=2,padx=5,pady=5)

baslik=tk.Entry(ekran,bg="light grey",)
baslik.grid(row=3,column=2,padx=5,pady=5)

yazi2=tk.Label(ekran,text="notunuzu yazınız",bg="white",fg="black")
yazi2.grid(row=4,column=2,padx=5,pady=5)

note=tk.Text(ekran,width=30,bg="light grey",fg="black")
note.grid(row=5,column=2)

yazi3=tk.Label(ekran,text="enter masterkey",bg="white",fg="black")
yazi3.grid(row=6,column=2,padx=5,pady=5)

masterkey=tk.Entry(ekran,bg="light grey",)
masterkey.grid(row=7,column=2,padx=5,pady=5)

dugme = tk.Button(ekran, text="save and encrypt", command=save_note, bg="light grey",)
dugme.grid(row=8,column=2,padx=7,pady=7)

dugme = tk.Button(ekran, text="decrypt", width=6, command= decodeation , bg="light grey",)
dugme.grid(row=9,column=2,padx=7,pady=7)

ekran.mainloop()
