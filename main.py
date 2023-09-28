import tkinter as tk
from tkinter import ttk
from tkinter import IntVar
from PIL import Image, ImageTk
from barcode import Code128
from barcode.writer import ImageWriter
import win32print
import os

def main():
    # A Tkinter ablak inicializálása
    root = tk.Tk()
    root.title("Címke Nyomtató")

    # Globális változók a címke mintaképének tárolására
    sample_image = None

    # Változó a példányszám tárolásához
    copies_var = IntVar()
    copies_var.set(1)  # Kezdetben 1 példány nyomtatása

    def generate_sample_image(label_text, label_width, label_height):
        try:
            # Vonalkód generálása a Code128 formátumban
            code = Code128(label_text, writer=ImageWriter())
            code_image = code.render()

            # Kép átméretezése a megadott szélességre és magasságra
            code_image = code_image.resize((int(label_width), int(label_height)))

            # Visszaadjuk a Code128 vonalkódot tartalmazó ImageTk.PhotoImage objektumot
            return ImageTk.PhotoImage(code_image)
        except Exception as e:
            print(f"Hiba a mintakép generálása során: {str(e)}")
            # Visszaadjuk egy üres képet, hogy elkerüljük az 'Expected type' hibát
            empty_image = Image.new("RGB", (int(label_width), int(label_height)))
            return ImageTk.PhotoImage(empty_image)

    # Hálózati,lokális nyomtatók listázása
    def list_network_printers():
        printer_list = []

        flags = win32print.PRINTER_ENUM_CONNECTIONS | win32print.PRINTER_ENUM_LOCAL
        printers = win32print.EnumPrinters(flags)

        for printer_info in printers:
            printer_name = printer_info[2]
            printer_list.append(printer_name)

        return printer_list

    # Az aktuális mintakép elkészítése
    def create_label():
        nonlocal sample_image

        label_text = label_text_entry.get()
        label_width = float(label_width_entry.get())
        label_height = float(label_height_entry.get())

        if sample_image:
            sample_image_label.config(image=None)
            sample_image_label.image = None

        sample_image = generate_sample_image(label_text, label_width, label_height)
        sample_image_label.config(image=sample_image)
        sample_image_label.image = sample_image

    # Nyomtatás
    def print_label():
        selected_printer = printer_combo.get()
        if not selected_printer:
            return  # Nincs kiválasztott nyomtató, nem nyomtatunk

        label_text = label_text_entry.get()
        label_width = float(label_width_entry.get())
        label_height = float(label_height_entry.get())
        copies = copies_var.get()  # Példányszám lekérdezése

        # Vonalkód generálása
        code = Code128(label_text, writer=ImageWriter())
        code_image = code.render()
        code_image = code_image.resize((int(label_width), int(label_height)))

        try:
            # Nyomtató kontextus létrehozása a kiválasztott nyomtatóhoz
            hprinter = win32print.OpenPrinter(selected_printer)
            pdc = win32print.GetPrinter(hprinter, 2)

            # PDF mentése
            pdf_file = "temp_code.pdf"
            code_image.save(pdf_file)

            # Nyomtatás beállítása
            for _ in range(copies):  # Megadott példányszámú nyomtatás
                os.startfile(pdf_file, "print")

            # Nyomtató kontextusok felszabadítása
            win32print.ClosePrinter(hprinter)
        except Exception as e:
            print(f"Hiba a nyomtatás során: {str(e)}")

    # Címke szöveg beviteli mező
    label_text_label = tk.Label(root, text="Címke Szöveg:", bg="black", fg="white")
    label_text_label.pack()
    label_text_entry = tk.Entry(root)
    label_text_entry.pack()
    label_text_entry.insert(0, "12345")  # Alapértelmezett szöveg

    # Címke szélesség beviteli mező
    label_width_label = tk.Label(root, text="Címke Szélesség (mm):", bg="black", fg="white")
    label_width_label.pack()
    label_width_entry = tk.Entry(root)
    label_width_entry.pack()
    label_width_entry.insert(0, "150")  # Alapértelmezett szélesség

    # Címke magasság beviteli mező
    label_height_label = tk.Label(root, text="Címke Magasság (mm):", bg="black", fg="white")
    label_height_label.pack()
    label_height_entry = tk.Entry(root)
    label_height_entry.pack()
    label_height_entry.insert(0, "100")  # Alapértelmezett magasság

    # Példányszám beállítása
    copies_label = tk.Label(root, text="Példányszám:", bg="black", fg="white")
    copies_label.pack()
    copies_entry = ttk.Combobox(root, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], textvariable=copies_var)
    copies_entry.pack()

    # Címke generálás gomb
    generate_button = tk.Button(root, text="Címke Generálás", command=create_label)
    generate_button.pack()

    # Nyomtató kiválasztás legördülő listával
    printer_label = tk.Label(root, text="Nyomtató kiválasztása:", bg="black", fg="white")
    printer_label.pack()
    printer_names = list_network_printers()
    printer_combo = ttk.Combobox(root, values=printer_names)
    printer_combo.pack()

    # Nyomtatás gomb
    print_button = tk.Button(root, text="Nyomtatás", command=print_label)
    print_button.pack()

    # Alapértelmezett címke megjelenítése
    sample_image = generate_sample_image("12345", 150, 100)
    sample_image_label = tk.Label(root, image=sample_image)
    sample_image_label.pack()

    # "B" felirat hozzáadása a jobb alsó sarokba
    b_label = tk.Label(root, text="B", font=("Arial", 13), bg="black", fg="white")
    b_label.place(relx=1.0, rely=1.0, anchor="se")

    root.configure(bg="black")  # A fő ablak háttere fekete lesz
    root.geometry("800x600")


    # A Tkinter ablak indítása
    root.mainloop()

if __name__ == "__main__":
    main()
