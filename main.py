import datetime as dt
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from typing import Optional, Tuple, Union
from Database.database import *
import customtkinter as ctk
from PIL import Image, ImageTk

# SCREENS
from Screens.Registration import registration_screen
from Screens.Overview import start_screen


class BudgetApp(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.font = ctk.CTkFont("Roboto")
        self.geometry("800x600")
        self.iconbitmap("Foto/save_money.ico")
        self.title("BudgetApp")
        self.resizable(True, True)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#333333")
        self.main_frame.grid(column=0, row=0, sticky="nsew", pady=25)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.language_var = ctk.StringVar(value="Hrvatski")
        self.create_login_screen(self.language_var)

    def clear_main_frame(self):
        """
        Destroys every frame inside self.main_frame
        """
        for frame in self.main_frame.winfo_children():
            frame.destroy()

    def create_login_screen(self, language):
        """
        Creates login screen on start of the application
        """
        self.clear_main_frame()
        login_frame = ctk.CTkFrame(self.main_frame)
        login_frame.grid(column=0, row=0, sticky="nsew")
        login_frame.grid_columnconfigure(0, weight=2)
        login_frame.grid_columnconfigure(1, weight=1)
        login_frame.grid_rowconfigure(0, weight=1)
        login_frame.grid_rowconfigure(1, weight=5)
        # Language picker
        # self.language_var = ctk.StringVar(value="Hrvatski")
        self.language_optionmenu = ctk.CTkOptionMenu(
            login_frame,
            variable=self.language_var,
            values=["Hrvatski", "Engleski"],
            command=self.language_change,
        )
        self.language_optionmenu.grid(column=0, row=0, padx=25, sticky="w")

        # Left frame
        left_frame = ctk.CTkFrame(login_frame, corner_radius=10, fg_color="#333333")
        left_frame.grid(column=0, row=1, sticky="nsew")
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure((0, 1, 2), weight=1)

        self.app_name_var = ctk.StringVar(value="Budget App")
        app_name_label = ctk.CTkLabel(
            left_frame,
            textvariable=self.app_name_var,
            fg_color="#2b2b2b",
            corner_radius=5,
        )
        app_name_label.grid(
            column=0, row=0, padx=15, pady=15, ipadx=25, ipady=10, sticky="n"
        )

        logo_image = ctk.CTkImage(
            dark_image=Image.open("Foto/save_money.png"),
            size=(250, 250),
        )
        logo_label = ctk.CTkLabel(left_frame, image=logo_image, text="")
        logo_label.grid(column=0, row=1, pady=25, sticky="n")
        # Quotes
        quotes = [
            "Do not save what is left after spending,\nbut spend what is left after saving.\n-Warren Buffet",
            "Don't go broke trying to look rich",
            "Beware of little expenses;\na small leak will sink a great ship.\n-Benjamin Franklin",
            "Stop buying things you don't need,\nto impress people you don't even like.\n-Suze Orman",
            "A budget is telling your money where to go,\ninstead of wondering where it went.\n-John C. Maxwell",
            "You can be young without money,\nbut you can’t be old without it.\n-Tennessee Williams",
            "You can make money two ways\nmake more or spend less\n-John Hope Bryant",
            "Effective saving can lead to\na successful wealth achievement.\n-Anath Lee Wales",
            "All days are not same. Save for a rainy day.\nWhen you don’t work, savings will work for you.\n-M.K. Soni",
            "If you would be wealthy,\nthink of saving as well as getting.\n-Benjamin Franklin",
            "Never spend your money before you have earned it.\n-Thomas Jefferson",
            "You must gain control over your money\nor the lack of it will forever control you.\n-Dave Ramsey",
            "Saving money is good.\nSaving dreams is not good.\n-Richie Norton",
            "Saving requires us to not get things now\nso that we can get bigger ones later.\n-Jean Chatzky",
            "The secret to financial security is not to have more money,\nbut having more control over the money we presently have.\n-Auliq-Ice",
            "When you have money,\nthink of the time when you had none.\n-Japanese Proverb",
            "To become rich — you must value saving more than spending.\n-George Choy",
            "Balancing your money is the key to having enough.\n-Elizabeth Warren",
        ]
        random_qoute = ctk.StringVar()
        random_qoute.set(quotes[random.randint(0, (len(quotes) - 1))])
        quote_label = ctk.CTkLabel(
            left_frame,
            textvariable=random_qoute,
            anchor="center",
            fg_color="#2b2b2b",
            corner_radius=5,
        )
        quote_label.grid(
            column=0, row=2, padx=15, pady=15, ipadx=25, ipady=10, sticky="n"
        )

        # Right frame
        right_frame = ctk.CTkFrame(login_frame, corner_radius=10, fg_color="#333333")
        right_frame.grid(column=1, row=1, sticky="nsew")
        right_frame.grid_rowconfigure((0, 2), weight=1)
        right_frame.grid_rowconfigure(1, weight=3)
        right_frame.grid_columnconfigure(0, weight=1)

        main_login_frame = ctk.CTkFrame(right_frame, fg_color="#2b2b2b")
        main_login_frame.grid(column=0, row=1, padx=15, ipadx=50, ipady=50)
        main_login_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Login - Title
        self.login_label_var = ctk.StringVar(value="Prijava")
        login_label = ctk.CTkLabel(
            main_login_frame, textvariable=self.login_label_var, font=(self.font, 24)
        )
        login_label.grid(column=1, row=1, columnspan=2, padx=10, pady=10, ipady=25)

        # Username
        self.username_entry_var = ctk.StringVar(value="Korisničko ime")
        self.username_entry = ctk.CTkEntry(
            main_login_frame,
            placeholder_text=self.username_entry_var.get(),
            font=(self.font, 14),
        )
        self.username_entry.grid(column=1, row=2, columnspan=2, padx=5, pady=15)
        self.username_entry.bind("<Return>", lambda e: self.login_check())

        # Password
        # TODO dodati ikonu da se može prikazati lozinka
        self.password_entry_var = ctk.StringVar(value="Lozinka")
        self.password_entry = ctk.CTkEntry(
            main_login_frame,
            placeholder_text=self.password_entry_var.get(),
            font=(self.font, 14),
            show="*",
        )
        self.password_entry.grid(column=1, row=3, columnspan=2, padx=5, pady=15)
        self.password_entry.bind("<Return>", lambda e: self.login_check())

        # Login button
        # TODO napraviti command da se provjeravaju podaci u bazi
        self.login_button_var = ctk.StringVar(value="Prijava")
        login_button = ctk.CTkButton(
            main_login_frame,
            textvariable=self.login_button_var,
            font=(self.font, 16),
            command=self.login_check,
        )
        login_button.grid(column=1, row=4, columnspan=2, padx=10, pady=40, ipadx=10)

        # Registration
        self.registration_label_var = ctk.StringVar(
            value="Nemaš račun?\nRegistriraj se"
        )
        registration_label = ctk.CTkLabel(
            main_login_frame,
            textvariable=self.registration_label_var,
            font=(self.font, 14),
        )
        registration_label.grid(column=1, row=6, columnspan=2, padx=10, pady=10)

        registration_label.bind(
            "<Button-1>", lambda e: self.create_registration_screen()
        )
        self.language_change(language)

    def login_check(self):
        """
        Check for user in database. If user exists then he will be logedin in application.
        If user doesn't exist, the message will appear on screen.
        """
        user = db_check_user_for_login(
            self.username_entry.get(), self.password_entry.get()
        )
        if user:
            self.clear_main_frame()
            start_screen.StartScreen(self, self.main_frame, self.language_var.get())
        else:
            messagebox.showerror(
                title="Nesupješna prijava",
                message="Pogrešno korisničko ime i/ili lozinka",
            )

    def create_registration_screen(self):
        self.clear_main_frame()
        registration_screen.RegistrationScreen(
            self, self.main_frame, self.language_var.get()
        )

    def language_change(self, language):
        if language == "Hrvatski" or language == "Croatian" or language == "Kroatisch":
            self.title("BudgetApp")
            self.app_name_var.set("Budget App")
            self.login_label_var.set("Prijava")
            self.username_entry_var.set("Korisničko ime")
            self.password_entry_var.set("Lozinka")
            self.login_button_var.set("Prijava")
            self.registration_label_var.set("Nemaš račun?\nRegistriraj se")
            self.language_optionmenu.configure(
                values=["Hrvatski", "Engleski", "Njemački"]
            )
            self.language_optionmenu.set("Hrvatski")
        elif language == "Engleski" or language == "English" or language == "Englisch":
            self.title("BudgetApp")
            self.app_name_var.set("Budget App")
            self.login_label_var.set("Login")
            self.username_entry_var.set("Username")
            self.password_entry_var.set("Password")
            self.login_button_var.set("Login")
            self.registration_label_var.set("Don't have an account?\nRegister now")
            self.language_optionmenu.configure(values=["Croatian", "English", "German"])
            self.language_optionmenu.set("English")
        self.username_entry.configure(placeholder_text=self.username_entry_var.get())
        self.password_entry.configure(placeholder_text=self.password_entry_var.get())


if __name__ == "__main__":
    app = BudgetApp()
    app.mainloop()
