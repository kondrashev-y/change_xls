import tkinter as tk
import os
from tkinter import ttk
from change_cell_in_xl import ChangeCell


window = tk.Tk()
window.title('Cell changer App')
window.geometry('400x300')
window.resizable(width=False, height=False)

frame_info = tk.Frame(window, width=200, height=200, bg='red')
frame_add_form = tk.Frame(window, width=400, height=200, bg='green')

# frame_add_form.grid(row=0, column=0)
# frame_info.grid(row=0, column=1)
frame_info.place(relx=0, rely=0, relwidth=1, relheight=0.3)
frame_add_form.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)


# chk = ttk.Checkbutton(frame_add_form, text='Change in folder')
l_tempo_frame_add_path = ttk.Label(frame_add_form, text='Enter folder path: ')
l_tempo_frame_add_cell = ttk.Label(frame_add_form, text='Enter cell number: ')
l_tempo_frame_add_text = ttk.Label(frame_add_form, text='Enter text for change: ')


def chek_path():
    input_path = l_input_path.get()
    if input_path == '':
        input_path = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    if not os.path.exists(input_path):
        return 'Wrong path, input again', False
    return input_path, True


l_greeting = ttk.Label(frame_info, text='Hi! You can change some cell in your xl file.')
l_info = ttk.Label(frame_info, text='Enter you params.')

l_greeting.pack(expand=True, padx=5, pady=5)
l_info.pack(expand=True, padx=5, pady=5)


def start_button():
    path, status = chek_path()
    if not status:
        l_info.configure(text=path)
    else:
        cell_number = l_input_cell.get()
        text_for_change = l_input_text.get()
        changer = ChangeCell(path, cell_number, text_for_change)
        l_info.configure(text=changer.change_cell())

# change = ChangeCell(path, cell_number, text_for_change)
# change.change_cell()


l_tempo_frame_add_btn = ttk.Button(frame_add_form, text='Submit', command=start_button)
l_input_path = ttk.Entry(frame_add_form, text='input path')
l_input_cell = ttk.Entry(frame_add_form, text='input cell')

l_input_text = ttk.Entry(frame_add_form, text='input text')
l_tempo_frame_add_path.grid(row=0, column=0)

l_input_path.grid(row=0, column=1)
l_tempo_frame_add_cell.grid(row=1, column=0)

l_input_cell.grid(row=1, column=1)
l_tempo_frame_add_text.grid(row=2, column=0)

l_input_text.grid(row=2, column=1)

l_tempo_frame_add_btn.grid(row=3, column=0, columnspan=2)

window.mainloop()
