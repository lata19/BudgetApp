import tkinter as tk
from tkinter import ttk
from typing import Optional, Tuple, Union
import customtkinter as ctk
import datetime as dt
from PIL import ImageTk, Image

# SCREENS


class BudgetApp(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.font = ctk.CTkFont("Roboto")
        self.geometry("800x600")
        self.iconbitmap("../Foto/save_money.ico")
        self.title("BudgetApp")
        self.resizable(True, True)
        # sizegrip = ttk.Sizegrip(self)
        # sizegrip.pack(side="right", anchor="se")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#161925")
        self.main_frame.grid(column=0, row=0, sticky="nswe", padx=25, pady=25)
        self.create_login_screen()

    def create_login_screen(self):
        """
        Creates login screen on start of the application
        """
        # Left frame
        left_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        left_frame.pack(side="left", fill="both", expand=True)
        # logo_label = ctk.CTkLabel(left_frame, text="Budget App")
        # logo_label.grid(column=0, row=0, padx=15, pady=15)
        left_frame_image = ctk.CTkImage(
            dark_image=Image.open("../Foto/euro_grow.png"),
            size=(192, 288),
        )
        photo_label = ctk.CTkLabel(left_frame, image=left_frame_image, text="")
        photo_label.grid(column=0, row=0, padx=15, pady=15, sticky="nsew")

        photo_label.update()
        left_frame_image.configure(
            size=(left_frame.winfo_width(), left_frame.winfo_height())
        )

        # Right frame
        right_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        right_frame.pack(side="right", fill="both", expand=False)
        right_frame.grid_rowconfigure((0, 2), weight=1)
        right_frame.grid_rowconfigure(1, weight=3)
        right_frame.grid_columnconfigure(0, weight=1)

        main_login_frame = ctk.CTkFrame(right_frame)
        main_login_frame.grid(column=0, row=1, padx=15)
        main_login_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        login_label = ctk.CTkLabel(
            main_login_frame, text="Prijava", font=(self.font, 18)
        )
        login_label.grid(column=1, row=1, columnspan=2, padx=10, pady=10)

        self.username_label_var = ctk.StringVar()
        self.username_label_var.set("Korisnicko ime")
        username_label = ctk.CTkLabel(
            main_login_frame, textvariable=self.username_label_var
        )
        username_label.grid(column=1, row=3, padx=10, pady=15)

        self.username_entry_var = ctk.StringVar()
        username_entry = ctk.CTkEntry(
            main_login_frame, textvariable=self.username_entry_var
        )
        username_entry.grid(column=2, row=3, padx=5, pady=15)

        self.password_label_var = ctk.StringVar()
        self.password_label_var.set("Lozinka")
        password_label = ctk.CTkLabel(
            main_login_frame, textvariable=self.password_label_var
        )
        password_label.grid(column=1, row=4, padx=10, pady=15)

        self.password_entry_var = ctk.StringVar()
        password_entry = ctk.CTkEntry(
            main_login_frame, textvariable=self.password_entry_var
        )
        password_entry.grid(column=2, row=4, padx=5, pady=15)

        self.login_button_var = ctk.StringVar()
        self.login_button_var.set("Prijava")
        login_button = ctk.CTkButton(
            main_login_frame, textvariable=self.login_button_var
        )
        login_button.grid(column=1, row=5, columnspan=2, padx=10, pady=50, ipadx=10)


if __name__ == "__main__":
    app = BudgetApp()
    app.mainloop()
