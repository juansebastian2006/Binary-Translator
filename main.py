import tkinter as tk
import pyperclip
import BinaryTranslator


class FirstWindow(tk.Tk):
    my_gray = "#B9B6B6"
    my_background = '#B0B9B9'
    code_format = ("Courier", 15)
    characters_color = "#15075F"

    def __init__(self):
        super().__init__()

        self.first_window = True
        self.resizable(False, False)
        self.title("First Window")
        self.geometry('850x600')

        self.configure(bg=self.my_background)

        self.label = tk.Label(self, bg=self.my_background, text='Binary Translator', font=('Helvetica', 30, 'bold'))
        self.label.place(relx=0.5, rely=0.1, anchor='center')

        self.textarea = tk.Text(self, bg="white",
                                width=31,
                                height=10,
                                font=("normal", 15),
                                highlightbackground="black",
                                highlightcolor="black",
                                highlightthickness=3, bd=0)

        self.textarea.place(relx=0.1, rely=0.3)

        self.result = tk.Text(self, bg='white', width=31, height=11,
                              font=self.code_format, highlightbackground='blue',
                              highlightcolor='blue', highlightthickness=3, bd=0)

        self.result.configure(state='disabled')
        self.result.place(relx=0.5, rely=0.3)

        self.text_1 = tk.Label(self, bg=self.my_background, text='Text input ASCII',
                               font="Verdana 18 bold italic", fg=self.characters_color)
        self.text_1.place(relx=0.1, rely=0.23)

        self.text_2 = tk.Label(self, bg=self.my_background, text='Result in Binary',
                               font=('Courier', 18), fg=self.characters_color)
        self.text_2.place(relx=0.5, rely=0.23)

        self.button_clear = tk.Button(self, width=10, height=2, text='clear',
                                      command=lambda: self.textarea.delete('1.0', tk.END))
        self.button_clear.place(relx=0.1, rely=0.7)

        self.button_convert = tk.Button(self, width=10, height=2, text='convert', command=self.ascii_to_b)
        self.button_convert.place(relx=0.3, rely=0.7)

        self.button_copy = tk.Button(self, width=10, height=2, text='copy', command=self.copy_result)
        self.button_copy.place(relx=0.5, rely=0.7)

        self.button_swap = tk.Button(self, width=10, height=2, text='swapping', command=self.swap_window2)
        self.button_swap.place(relx=0.7, rely=0.7)

        self.button_clear_everything = tk.Button(self, width=10, height=2, text='Clear All', command=self.clear_all)
        self.button_clear_everything.place(relx=0.1, rely=0.8)

    def clear_all(self):
        self.textarea.delete('1.0', tk.END)
        self.result.configure(state='normal')
        self.result.delete('1.0', tk.END)
        self.result.configure(state='disabled')

    def swap_window2(self):
        self.first_window = False

        if self.first_window is False:
            self.title("Second Window")
            self.button_swap.configure(command=self.swap_window1)
            self.clear_all()

            self.text_1.place_configure(relx=0.5, rely=0.23)
            self.text_2.place_configure(relx=0.1, rely=0.23)

            self.text_1.configure(text='Result in ASCII')
            self.text_2.configure(text='Text Input Binary')

            self.textarea.configure(font=self.code_format)
            self.result.configure(font=('normal', 15))

            self.textarea.configure(width=33, height=12)
            self.result.configure(width=31, height=11)

            self.button_convert.configure(command=self.binary_to_a)
            self.button_copy.configure(command=self.copy_result_second)

    def swap_window1(self):
        self.first_window = True
        if self.first_window:
            self.title("First Window")
            self.button_swap.configure(command=self.swap_window2)
            self.clear_all()

            self.text_1.place_configure(relx=0.1, rely=0.23)
            self.text_2.place_configure(relx=0.5, rely=0.23)

            self.text_1.configure(text='Text Input ASCII')
            self.text_2.configure(text='Result in Binary')

            self.textarea.configure(font=('normal', 15))
            self.result.configure(font=self.code_format)
            
            self.textarea.configure(width=31, height=10)
            self.result.configure(width=31, height=11)

            self.button_convert.configure(command=self.ascii_to_b)
            self.button_copy.configure(command=self.copy_result)

    def ascii_to_b(self):
        self.result.configure(state='normal')
        self.result.delete('1.0', tk.END)
        text = self.textarea.get("1.0", tk.END)
        self.result.insert('end', BinaryTranslator.binary_format(BinaryTranslator.ascii_to_binary(text.strip())))
        self.result.configure(state='disabled')

    def binary_to_a(self):
        self.result.configure(state='normal')
        self.result.delete('1.0', tk.END)
        text = self.textarea.get('1.0', tk.END)
        self.result.insert('end', BinaryTranslator.binary_to_ascii(text))
        self.result.configure(state='disabled')

    def copy_result(self):
        text = self.textarea.get("1.0", tk.END)
        pyperclip.copy(BinaryTranslator.ascii_to_binary(text.strip()))

    def copy_result_second(self):
        text = self.textarea.get('1.0', tk.END)
        pyperclip.copy(BinaryTranslator.binary_to_ascii(text))


if __name__ == "__main__":
    window = FirstWindow()
    window.mainloop()
