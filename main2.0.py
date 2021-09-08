import os
import openpyxl


class ChangeCell:

    def __init__(self, path: str, cell_number: str, change_value: str):
        self.path = path
        self.cell_number = cell_number
        self.change_value = change_value
        self.status = True

    def file_names_list(self):
        names_list = os.listdir(self.path)
        return [name for name in names_list if '.xls' in name]

    def new_directory(self):
        if not os.path.exists(self.path + '/change_files'):
            os.mkdir(self.path + '/change_files')
        print('-', end='')
        return f'{self.path}/change_files'

    def change_cell(self):
        name_list = self.file_names_list()
        if not name_list:
            print('Choice folder is empty!')
        for file_name in name_list:
            book = openpyxl.open(self.path + '/' + file_name)
            sheet = book.active
            try:
                sheet[self.cell_number] = self.change_value
                book.save(f'{self.new_directory()}/{file_name}')
            except Exception as e:
                print(e)
                self.status = False
            book.close()
        if self.status:
            print('Change successfully!')
        else:
            print('Error!')


def input_text(info_text: str) -> str:
    _text = input(info_text)
    return _text


def chek_path():
    input_path = input_text('Input path of folder or press enter if program in file: ')
    if input_path == '':
        input_path = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    if not os.path.exists(input_path):
        print('Wrong path, input again')
        chek_path()
    return input_path


def main():
    path = chek_path()
    cell_number = input_text('Input cell number of xl file: ')
    text_for_change = input_text('Input text, which will be changed: ')
    change = ChangeCell(path, cell_number, text_for_change)
    change.change_cell()


if __name__ == '__main__':
    main()
