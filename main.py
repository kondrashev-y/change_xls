import os
import openpyxl

path = 'files'
cell_number = 'A24'
change_value = 'Хуякт'

file_path_list = os.listdir(path)
if not os.path.exists('change_files'):
    os.mkdir('change_files')
print(file_path_list)

for file_name in file_path_list:
    book = openpyxl.open(path + '/' + file_name)

    sheet = book.active
    # print(sheet[cell_number].value)
    sheet[cell_number] = change_value
    book.save(f'change_files/{file_name}')
    book.close()
    # print(sheet[cell_number].value)