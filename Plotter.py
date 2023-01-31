import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import darkdetect


class Plotter:
    """
    A few plot functions for the main window widget
    """

    def __init__(self):
        self.figure = None

    def app_dark(self, root):
        # delete existing plot
        self._clear(root)

        # match the frame color to the theme
        root.configure(fg_color="#3b3b3b")

        # plot style
        plt.style.use("dark_background")

        # Initialise plot figure
        self.figure = plt.figure(figsize=(7, 5), dpi=100)
        self.figure.add_subplot(111)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        # Place plot into frame2
        chart = FigureCanvasTkAgg(self.figure, root)
        chart.get_tk_widget().pack(side='top', fill='both', expand=1)  # (side='top')

        # Settings for the navigation toolbar
        toolbar = NavigationToolbar2Tk(chart, root, pack_toolbar=False)
        toolbar.config(background="#3b3b3b")
        # toolbar.message_label.config(background="#3b3b3b", fg='black')
        toolbar.winfo_children()[9].config(background="#3b3b3b")
        toolbar.winfo_children()[10].config(background="#3b3b3b")

        for button in toolbar.winfo_children():
            button.config(background="#3b3b3b")

        toolbar.pack(side='left')

    def app_light(self, root):
        # delete existing plot
        self._clear(root)

        # match the frame color to the theme
        root.configure(fg_color="#f0ecec")

        # plot style
        plt.style.use('bmh')

        # Initialise plot figure
        self.figure = plt.figure(figsize=(7, 5), dpi=100)
        self.figure.add_subplot(111)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        # Place plot into frame2
        chart = FigureCanvasTkAgg(self.figure, root)
        chart.get_tk_widget().pack(side='top', fill='both', expand=1)  # (side='top')

        # Settings for the navigation toolbar
        toolbar = NavigationToolbar2Tk(chart, root, pack_toolbar=False)
        toolbar.config(background="#f0ecec")
        # toolbar.message_label.config(background="#f0ecec", fg='black')
        toolbar.winfo_children()[9].config(background="#f0ecec")
        toolbar.winfo_children()[10].config(background="#f0ecec")

        for button in toolbar.winfo_children():
            button.config(background="#f0ecec")

        toolbar.pack(side='left')

    def draw_plot(self, root, appearance):

        if appearance == "System":

            try:
                if darkdetect.theme() == "Dark":
                    self.app_dark(root)  # Dark
                else:
                    self.app_light(root)  # Light
            except NameError:
                self.app_light(root)  # Light

        elif appearance == "Dark":
            self.app_dark(root)

        elif appearance == "Light":
            self.app_light(root)

    def _clear(self, frame):

        # close the figure
        plt.close(self.figure)

        # delete all the children from the frame
        for widget in frame.winfo_children():
            widget.destroy()

        # reset matplotlib
        mpl.rcParams.update(mpl.rcParamsDefault)

    @staticmethod
    def plot_lines(get_y, x_list):
        # plot the lines from the TwoLines class into the plot
        # check if y list is empty (no equations has been entered)
        sol_1, sol_2 = get_y
        for i in [[sol_1, '#5a30ff'], [sol_2, '#ff4d17']]:
            if len(i[0]) != 0:
                plt.plot(x_list, i[0], color=i[1])
            else:
                plt.plot([], i[0])

    @staticmethod
    def plot_intersection(get_intersect, textbox):
        # If an intersect is present and the option is turned on, display intersect coordinates in plot.
        cor = get_intersect
        if cor != 'No intersect':
            for i in cor:
                plt.plot(i[0], i[1], marker="o", markersize=3)
                round_1, round_2 = round(i[0], 2), round(i[1], 2)
                plt.annotate(f'({round_1}; {round_2})', (i[0], i[1]))
