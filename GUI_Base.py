from tkinter import StringVar

import TwoLines
import Plotter
import ReadWriteData
import ReadWriteSettings


class Base:
    def __init__(self, root):
        # settings for the GUI root
        # self.width = 1165
        # self.height = 550
        self.root = root
        self.root.title("Intersection Calculator")
        # self.root.geometry(f'{self.width}x{self.height}')
        # self.root.resizable(False, False)
        # self.root.minsize(self.width, self.height)

        # starting parameters for the plot
        self.x_points = 200
        self.x_min = -10
        self.x_max = 10
        self.equation_1 = ''
        self.equation_2 = ''

        # Initialise the classes
        self.TL = TwoLines.TwoLines(self.equation_1, self.equation_2, self.x_points, self.x_min, self.x_max)
        self.PT = Plotter.Plotter()
        self.RWD = ReadWriteData.ReadWriteData()
        self.RWS = ReadWriteSettings.ReadWriteSettings()

        # additional plot settings
        self.intersection = False

        # set frames and widget to self
        self.frame1 = None
        self.ent_eq1 = None
        self.ent_eq2 = None
        self.ent_min_x = None
        self.ent_max_x = None
        self.ent_xp = None
        self.frame2 = None
        self.frame3 = None
        self.frame4 = None
        self.textbox = None

        self.theme = self.RWS.get_style('theme')
        self.appearance = self.RWS.get_style('appearance')

        # ini parameters
        self.ent_save_name = ''
        self.section_name = 'None'
        self.option_var = StringVar()

    def update_values(self):
        # update self.parameters by replacing the existing value by the entry value.
        self.equation_1 = str(self.ent_eq1.get())
        self.equation_2 = str(self.ent_eq2.get())

        try:
            self.x_points = int(self.ent_xp.get())
        except ValueError:
            pass

        try:
            self.x_min = int(self.ent_min_x.get())
        except ValueError:
            pass

        try:
            self.x_max = int(self.ent_max_x.get())
        except ValueError:
            pass

        self.TL = TwoLines.TwoLines(self.equation_1, self.equation_2, self.x_points, self.x_min, self.x_max)

    def update_intersection(self):
        # update self.parameters by replacing the existing value by the entry value.
        if self.intersection:
            self.intersection = False
            self.textbox.insert('end', 'Intersection disabled\n')

        elif not self.intersection:
            self.intersection = True
            self.textbox.insert('end', 'Intersection enabled\n')

    def update_ini_parameters(self):

        list_parameters = self.RWD.ini_get(self.section_name)

        self.equation_1 = list_parameters[0]
        self.equation_2 = list_parameters[1]
        self.x_points = list_parameters[2]
        self.x_min = list_parameters[3]
        self.x_max = list_parameters[4]

        self.update_calc_class()

        self.textbox.insert('end', 'Parameters loaded\n')

    def update_calc_class(self):
        # update the calculation class
        self.TL = TwoLines.TwoLines(self.equation_1, self.equation_2, self.x_points, self.x_min, self.x_max)

    def update_section_name(self, *args):
        self.section_name = self.option_var.get()
