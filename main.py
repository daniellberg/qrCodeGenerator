from tkinter import *
import qrcode
from PIL import Image, ImageDraw, ImageTk
from tkinter import messagebox, Tk, Label, Entry, Button

# cria funções 

def gera_qrCode():
    url = website_entry.get()

    if len(url) == 0:
        messagebox.showinfo(
            title="Ops, ocorreu um erro!",
            message="Por favor insira uma URL válida")
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"O endereço URL é \n "
            f"Endereço: {url} \n"
            f"Pronto para salvar?")
        
        if opcao_escolhida:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img.save('qrExport.png')

#create GUI
if __name__ == '__main__':
    window = Tk()
    window.iconbitmap('icon.png') #not working
    window.title('Gerador de QR Code')
    window.config(padx=10, pady= 100)

    iconPhoto = ImageTk.PhotoImage(Image.open("icon.png")) #falta usar a imagem
    

    website_label = Label(text="URL:")
    website_label.grid(row=2, column=0)

    website_entry = Entry(width=35)
    website_entry.grid(row=2, column=1, columnspan=2)
    website_entry.focus()
    add_button = Button(text="Gerar QR Code", width=35, command=gera_qrCode)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()