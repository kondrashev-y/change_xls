import tkinter as tk
from tkinter import messagebox as mbox
import os
import sys
from tkinter import ttk
from change_cell_in_xl import ChangeCell


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Cell Changer App')
        self.style = ttk.Style()
        self.style.configure('ErrorLbl.TLabel', foreground='red')
        self.style.configure('BldLbl.TLabel', font=('Helvetica', 13, 'bold'), padding=(0, 10, 0, 10))
        self.style.configure('FrLbl.TLabel', padding=(20, 0, 0, 0))
        self['background'] = '#EBEBEB'
        self.geometry('800x250')
        self.resizable(width=False, height=False)
        # self.conf = {'padx': (5, 10), 'pady': 5}
        # self.bold_font = 'Helvetica 13 bold'
        self.info_status = 'Enter you params.'
        self.put_frames()
        self.put_menu()
        self.popup = Popup(self)

    def put_menu(self):
        self.config(menu=MainMenu(self))

    def put_frames(self):
        self.frame_info = InfoFrame(self).place(relx=0, rely=0, relwidth=1, relheight=0.4)
        self.frame_add_form = AddForm(self).place(relx=0, rely=0.4, relwidth=1, relheight=0.6)

    def refresh(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        self.put_frames()
        self.put_menu()

    # def quit(self):
    #     Popup(self)
    #     # self.destroy()


class InfoFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        """Create widgets"""
        self.greeting = ttk.Label(self, text='Hi! You can change some cell in your xl file.', style='BldLbl.TLabel')
        self.info = ttk.Label(self, text=self.master.info_status)

        self.greeting.pack(expand=True, padx=5, pady=5)
        self.info.pack(expand=True, padx=5, pady=5)


class AddForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.flag = True
        self.put_widgets()

    def chek_path(self) -> str:
        """Chek folder path"""
        input_path = self.input_path.get()
        if input_path == '':
            # input_path = os.path.join(os.path.abspath(os.path.dirname(__file__)))
            # input_path = sys.path[0]
            default_path = sys.path[0].split('/')
            input_path = '/'.join(default_path[:-5])
            print(input_path)
        return input_path

    def start_button(self):
        """start processing changing"""
        if not self.flag:
            self.master.info_status = 'Wrong path, input again'
            self.bell()
            self.master.refresh()
        else:
            print('!' * 20)
            path = self.chek_path()
            cell_number = self.input_cell.get()
            text_for_change = self.input_text.get()
            self.master.info_status = 'Processing...'
            self.master.refresh()
            changer = ChangeCell(path, cell_number, text_for_change)
            if changer.change_cell():
                self.master.info_status = 'Change successfully completed!'
                self.master.refresh()
                self.master.popup.show('success')
            else:
                self.bell()
                self.master.info_status = 'Error! Maybe you write wrong cell number.'
                self.master.refresh()

    def validate_amount(self, input_value: str) -> bool:
        """Chek validate input path"""
        # if os.path.exists(input_value) or input_value == '':
        if os.path.exists(input_value) or input_value == '':
            return True
        else:
            self.add_path['style'] = 'ErrorLbl.TLabel'
            self.flag = False
            self.bell()
            return False

    def put_widgets(self):
        """Create widgets"""
        self.add_path = ttk.Label(self, text='Enter folder path: ', style='FrLbl.TLabel')
        self.add_cell = ttk.Label(self, text='Enter cell number: ', style='FrLbl.TLabel')
        self.add_text = ttk.Label(self, text='Enter text for change: ', style='FrLbl.TLabel')
        self.add_btn = ttk.Button(self, text='Submit', command=self.start_button)
        self.input_path = ttk.Entry(self, text='input path', validate='focusout',
                                    validatecommand=(self.register(self.validate_amount), '%P'))
        self.input_cell = ttk.Entry(self, text='input cell')

        self.input_text = ttk.Entry(self, text='input text')
        self.add_path.grid(row=0, column=0)

        self.input_path.grid(row=0, column=1)
        self.add_cell.grid(row=1, column=0)

        self.input_cell.grid(row=1, column=1)
        self.add_text.grid(row=2, column=0)

        self.input_text.grid(row=2, column=1)

        self.add_btn.grid(row=3, column=0, columnspan=2)


class MainMenu(tk.Menu):
    def __init__(self, mainwindow):
        super().__init__(mainwindow)
        file_menu = tk.Menu(self)
        # options_menu = tk.Menu(self)
        help_menu = tk.Menu(self)

        file_menu.add_command(label="Refresh", command=mainwindow.refresh)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=lambda: mainwindow.popup.show('quit'))
        help_menu.add_command(label="About", command=lambda: mainwindow.popup.show('about_us'))
        help_menu.add_separator()
        help_menu.add_command(label="FAQ", command=lambda: mainwindow.popup.show('faq'))


        self.add_cascade(label='File', menu=file_menu)
        # self.add_cascade(label='Options', menu=options_menu)
        self.add_cascade(label='Help', menu=help_menu)


class Popup:
    def __init__(self, master):
        self.master = master

    def show(self, window_type):
        """Show popup window"""
        getattr(self, window_type)()

    def quit(self):
        """destroy program"""
        answer = mbox.askyesno('Quit', 'Are you sure?')
        if answer is True:
            self.master.destroy()

    def faq(self):
        """Show info faq"""
        mbox.showinfo('FAQ', 'This app change text in cell of file xl. You can enter path to'
                             ' a folder with files or leave the path empty if the program is located in a folder with '
                             'files. Enter number of cell and enter text for change.')

    def about_us(self):
        """Show info about us"""
        mbox.showinfo('About us', 'This application was developed by Yuri Kondrashev.')

    def success(self):
        """Show info success"""
        mbox.showinfo('Info', 'Changes completed!')


app = App()
app.mainloop()