import customtkinter
from GUI_Base import Base


class GUI(Base):
    def __init__(self, root):
        super().__init__(root)

        customtkinter.set_appearance_mode(self.appearance)  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme(self.theme)  # Themes: "blue" (standard), "green", "dark-blue"

        # Initialise The window with frames and widgets
        self.frame_one()
        self.frame_two()
        self.frame_tree()
        self.frame_four()

        # configure matplotlib plot in frame2
        self.PT.draw_plot(self.frame2, self.appearance)

    def frame_one(self):
        # frame for the plot entry
        self.frame1 = customtkinter.CTkFrame(self.root, corner_radius=0)
        self.frame1.pack(fill="both", expand=True, side="left")

        header_frame1 = customtkinter.CTkLabel(self.frame1, text="Parameters for the plot",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        header_frame1.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 10))

        header_ent_eq1 = customtkinter.CTkLabel(self.frame1, text="Equation one: ")
        header_ent_eq1.grid(row=1, column=0, padx=10, pady=3, sticky="sw")

        self.ent_eq1 = customtkinter.CTkEntry(self.frame1, placeholder_text="None")
        self.ent_eq1.grid(row=1, column=1, padx=10, pady=3, sticky="sw")

        header_ent_eq2 = customtkinter.CTkLabel(self.frame1, text="Equation two: ")
        header_ent_eq2.grid(row=2, column=0, padx=10, pady=3, sticky="sw")

        self.ent_eq2 = customtkinter.CTkEntry(self.frame1, placeholder_text="None")
        self.ent_eq2.grid(row=2, column=1, padx=10, pady=3, sticky="sw")

        header_ent_mix = customtkinter.CTkLabel(self.frame1, text="Minimum x : ")
        header_ent_mix.grid(row=3, column=0, padx=10, pady=3, sticky="sw")

        self.ent_min_x = customtkinter.CTkEntry(self.frame1, placeholder_text="-10")
        self.ent_min_x.grid(row=3, column=1, padx=10, pady=3, sticky="sw")

        header_ent_mix = customtkinter.CTkLabel(self.frame1, text="Maximum x : ")
        header_ent_mix.grid(row=4, column=0, padx=10, pady=3, sticky="sw")

        self.ent_max_x = customtkinter.CTkEntry(self.frame1, placeholder_text="10")
        self.ent_max_x.grid(row=4, column=1, padx=10, pady=3, sticky="sw")

        header_ent_xp = customtkinter.CTkLabel(self.frame1, text="Number of x values: ")
        header_ent_xp.grid(row=5, column=0, padx=10, pady=3, sticky="sw")

        self.ent_xp = customtkinter.CTkEntry(self.frame1, placeholder_text="200")
        self.ent_xp.grid(row=5, column=1, padx=10, pady=3, sticky="sw")

        button_plot = customtkinter.CTkButton(self.frame1, text="Plot", command=lambda: self.plot_everything())
        button_plot.grid(row=6, column=0, columnspan=2, padx=10, pady=3, sticky="news")

        switch_intersection = customtkinter.CTkSwitch(self.frame1, text="Intersection",
                                                      command=lambda: self.update_intersection())
        switch_intersection.grid(row=7, column=0, padx=10, pady=30, sticky="news")

    def frame_two(self):
        # frame for the plot
        self.frame2 = customtkinter.CTkFrame(self.root, corner_radius=0, fg_color="#3b3b3b")
        self.frame2.pack(pady=20, padx=20, fill="both", expand=True, side="left")

    def frame_tree(self):
        # frame for the Ini
        self.frame3 = customtkinter.CTkFrame(self.root)
        self.frame3.pack(pady=10, padx=(0, 20), fill="both", expand=True)

        label_save_plot = customtkinter.CTkLabel(self.frame3, text="Save plot",
                                                 font=customtkinter.CTkFont(size=15, weight="bold"))
        label_save_plot.grid(row=0, column=0, columnspan=2, padx=10, sticky="sw")

        label_save_name = customtkinter.CTkLabel(self.frame3, text="Save name: ")
        label_save_name.grid(row=1, column=0, padx=10, pady=3, sticky="sw")

        self.ent_save_name = customtkinter.CTkEntry(self.frame3, placeholder_text="None")
        self.ent_save_name.grid(row=1, column=1, padx=10, pady=3, sticky="sw")

        save_button = customtkinter.CTkButton(self.frame3, text="Save",
                                              command=lambda: self.RWD.ini_write(self.ent_save_name.get(), self.x_points,
                                                                                 self.x_min, self.x_max, self.equation_1,
                                                                                 self.equation_2, self.textbox,
                                                                                 self.frame3, self.option_var))
        save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=3, sticky="news")

        label_access_data = customtkinter.CTkLabel(self.frame3, text="Access saved data",
                                                   font=customtkinter.CTkFont(size=15, weight="bold"))
        label_access_data.grid(row=3, column=0, columnspan=2, padx=10, sticky="sw")

        label_saved_data = customtkinter.CTkLabel(self.frame3, text="Saved data: ")
        label_saved_data.grid(row=4, column=0, padx=(10, 5), pady=3, sticky="sw")

        self.option_var.set(self.RWD.get_sections()[0])
        self.option_var.trace("w", self.update_section_name)
        section_list = customtkinter.CTkOptionMenu(self.frame3, variable=self.option_var, values=self.RWD.get_sections())
        section_list.grid(row=4, column=1, padx=(5, 10), pady=3, sticky="sw")

        plot_button = customtkinter.CTkButton(self.frame3, text="Load", command=self.update_ini_parameters)
        plot_button.grid(row=5, column=0, padx=(10, 5), pady=3, sticky="news")

        delete_button = customtkinter.CTkButton(self.frame3, text="Delete", command=lambda: self.RWD.ini_del(
            self.section_name,
            self.textbox,
            self.frame3,
            self.option_var))
        delete_button.grid(row=5, column=1, padx=(5, 10), pady=3, sticky="news")

        plot_ini_button = customtkinter.CTkButton(self.frame3, text="Plot loaded data",
                                                  command=lambda: self.plot_everything(update_values=False))
        plot_ini_button.grid(row=6, column=0, columnspan=2, padx=10, pady=3, sticky="news")

    def frame_four(self):
        # frame for the log and settings
        self.frame4 = customtkinter.CTkFrame(self.root)
        self.frame4.pack(pady=20, padx=(0, 20), fill="both", expand=True)

        # create tabview
        tabview = customtkinter.CTkTabview(self.frame4)
        tabview.pack(pady=5, padx=5, fill="both", expand=True)
        tabview.add("Log")
        tabview.add("Settings")
        tabview.tab("Log").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        tabview.tab("Settings").grid_columnconfigure(0, weight=1)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(tabview.tab("Log"))
        self.textbox.insert('end', 'Welcome to the calculator.\n')
        self.textbox.pack(fill="both", expand=True)

        # settings stuff
        scaling_label = customtkinter.CTkLabel(tabview.tab("Settings"), text="UI Scaling:")
        scaling_label.grid(row=0, column=0, pady=(10, 0))
        scaling_option_menu = customtkinter.CTkOptionMenu(tabview.tab("Settings"),
                                                          values=["80%", "90%", "100%", "110%", "120%"],
                                                          command=self.change_scaling_event)
        scaling_option_menu.set("100%")
        scaling_option_menu.grid(row=1, column=0)

        appearance_label = customtkinter.CTkLabel(tabview.tab("Settings"), text="Appearance mode:")
        appearance_label.grid(row=2, column=0, pady=(10, 0))
        appearance_option_menu = customtkinter.CTkOptionMenu(tabview.tab("Settings"),
                                                             values=["System", "Light", "Dark"],
                                                             command=self.change_appearance_mode_event)
        appearance_option_menu.set("System")
        appearance_option_menu.grid(row=3, column=0)

        theme_label = customtkinter.CTkLabel(tabview.tab("Settings"), text="Theme:")
        theme_label.grid(row=4, column=0, pady=(10, 0))
        theme_option_menu = customtkinter.CTkOptionMenu(tabview.tab("Settings"),
                                                        values=["blue", "green", "dark-blue"],
                                                        command=self.change_color_theme_event)
        theme_option_menu.set(self.theme)
        theme_option_menu.grid(row=5, column=0)

    def plot_everything(self, update_values=True):
        # update entry values if true
        if update_values:
            self.update_values()

        # set the plot en plot the lines
        self.PT.draw_plot(self.frame2, self.appearance)
        self.PT.plot_lines(self.TL.get_y(), self.TL.x_list)
        # plot to intersect if true
        if self.intersection:
            intersect = self.TL.get_intersection()
            if intersect != "Calculation not possible":

                self.PT.plot_intersection(intersect, self.textbox)
                # show in log
                self.textbox.insert('end', f'Coordinates intersection:\n{intersect}\n')
            elif intersect == "Calculation not possible":
                self.textbox.insert('end', text="Calculation not possible")

    @classmethod
    def change_scaling_event(cls, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        # change the self parameter
        self.appearance = new_appearance_mode

        # save in ini for later use
        self.RWS.edit_style('appearance', new_appearance_mode)

        #apply the change
        customtkinter.set_appearance_mode(self.appearance)

        self.PT.draw_plot(self.frame2, self.appearance)

    def change_color_theme_event(self, new_theme: str):
        # change the self parameter
        self.theme = new_theme

        # save in ini for later use
        self.RWS.edit_style('theme', new_theme)

        # apply the change
        customtkinter.set_default_color_theme(new_theme)

        # delete and restructure the GUI with the new theme
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()

        self.frame_one()
        self.frame_two()
        self.frame_tree()
        self.frame_four()

        self.PT.draw_plot(self.frame2, self.appearance)
