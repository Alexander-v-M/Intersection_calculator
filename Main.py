import customtkinter
from tkinter import messagebox
import GUI


def main():
    root = customtkinter.CTk()

    def when_quit():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.quit()

    gui = GUI.GUI(root)
    root.protocol("WM_DELETE_WINDOW", when_quit)
    gui.root.mainloop()


if __name__ == "__main__":
    main()
