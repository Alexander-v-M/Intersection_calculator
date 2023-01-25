from configparser import ConfigParser
from customtkinter import CTkOptionMenu

config_data = ConfigParser()
config_data.read('Data.ini')


class ReadWriteData:

    def __init__(self):
        self.parameter_save_name = ''
        self.list_ini_sections = config_data.sections()

    def get_sections(self):
        return self.list_ini_sections

    def update_config(self, frame3, option_var):
        self.list_ini_sections = config_data.sections()
        section_list = CTkOptionMenu(frame3, variable=option_var, values=self.get_sections())
        section_list.grid(row=4, column=1, padx=(5, 10), pady=3, sticky="sw")

    def ini_write(self, ent_save_name, x_points, x_min, x_max, equation_1, equation_2, textbox, frame3, option_var):
        # write parameters to an ini file for later use.
        # if the entry for the save name is empty, save name will be 'Unknown'
        # if name is already used, save name is entry name with '(1)' added
        name_for_save = ent_save_name
        if name_for_save != '':
            self.parameter_save_name = name_for_save

            try:
                config_data.add_section(f'{self.parameter_save_name}')
                config_data.set(f'{self.parameter_save_name}', 'x_points', f'{x_points}')
                config_data.set(f'{self.parameter_save_name}', 'x_min', f'{x_min}')
                config_data.set(f'{self.parameter_save_name}', 'x_max', f'{x_max}')
                config_data.set(f'{self.parameter_save_name}', 'equation_1', f'{equation_1}')
                config_data.set(f'{self.parameter_save_name}', 'equation_2', f'{equation_2}')
                with open('Data.ini', 'w') as configfile:
                    config_data.write(configfile)

                textbox.insert('end', 'Parameters saved\n')

                self.update_config(frame3, option_var)

            except Exception:
                textbox.insert('end', 'Parameters saved failed. Name already in use. Enter a new name.\n')
        else:
            textbox.insert('end', 'Parameters saved failed. Name already in use. Enter a new name.\n')

    @staticmethod
    def ini_get(section_name):

        equation_1 = config_data.get(f'{section_name}', 'equation_1')
        equation_2 = config_data.get(f'{section_name}', 'equation_2')
        x_points = config_data.getint(f'{section_name}', 'x_points')
        x_min = config_data.getint(f'{section_name}', 'x_min')
        x_max = config_data.getint(f'{section_name}', 'x_max')

        return [equation_1, equation_2, x_points, x_min, x_max]

    def ini_del(self, section_name, textbox, frame3, option_var):
        print(1)
        if section_name != 'None':
            config_data.remove_section(section_name)

            with open('Data.ini', 'w') as configfile_data:
                config_data.write(configfile_data)

            self.update_config(frame3, option_var)

            textbox.insert('end', 'Parameters deleted\n')
