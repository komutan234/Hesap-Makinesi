import customtkinter

class Calculator(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hesap Makinesi")
        self.geometry("300x400")

        self.display = customtkinter.CTkEntry(self, width=280, height=50)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 1, 0
        for button_text in buttons:
            button = customtkinter.CTkButton(self, text=button_text, command=lambda t=button_text: self.click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, text):
        if text == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, customtkinter.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, customtkinter.END)
                self.display.insert(0, "Hata")
        else:
            self.display.insert(customtkinter.END, text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
