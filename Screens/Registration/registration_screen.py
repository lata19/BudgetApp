import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image, ImageTk

from Database.database import *
import main


class RegistrationScreen:
    def __init__(self, main, parent_frame, language):
        self.main = main
        self.parent_frame = parent_frame
        self.language = language
        self.create_registration_screen()
        self.language_change(self.language)

    def language_change(self, language):
        if language == "Hrvatski":
            self.back_button_var.set("Natrag")
            self.first_name_var.set("Ime:")
            self.last_name_var.set("Prezime:")
            self.username_var.set("Korisničko ime:")
            self.password_var.set("Lozinka:")
            self.email_var.set("Adresa elektroničke pošte:")
            self.email_notifications_var.set(
                "Želiš li primati obavijesti putem elektroničke pošte?"
            )
            self.admin_var.set("Administrator:")
            self.active_var.set("Aktivan:")
            self.register_button_var.set("Registriraj se")
        elif language == "English":
            self.back_button_var.set("Back")
            self.first_name_var.set("First name:")
            self.last_name_var.set("Last name:")
            self.username_var.set("Username:")
            self.password_var.set("Password")
            self.email_var.set("E-Mail address")
            self.email_notifications_var.set(
                "Would you like to receive notifications by email?"
            )
            self.admin_var.set("Administrator:")
            self.active_var.set("Active")
            self.register_button_var.set("Register")

    def create_registration_screen(self):
        registration_frame = ctk.CTkFrame(self.parent_frame)
        registration_frame.grid(column=0, row=0, sticky="nsew")
        registration_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        # registration_frame.grid_rowconfigure(0, weight=1)

        # Language picker
        self.language_var = ctk.StringVar(value=self.language)
        language_optionmenu = ctk.CTkOptionMenu(
            registration_frame,
            variable=self.language_var,
            values=["Hrvatski", "English"],
            command=self.language_change,
        )
        language_optionmenu.grid(column=0, row=0, padx=25, pady=25, sticky="w")

        # Back button
        self.back_button_var = ctk.StringVar(value="Natrag")
        back_button = ctk.CTkButton(
            registration_frame,
            textvariable=self.back_button_var,
            command=self.back_to_login_screen,
        )
        back_button.grid(column=0, row=1, padx=25, pady=25, sticky="w")

        # First name
        self.first_name_var = ctk.StringVar(value="Ime:")
        first_name_label = ctk.CTkLabel(
            registration_frame, textvariable=self.first_name_var
        )
        first_name_label.grid(column=1, row=1, padx=10, pady=10, sticky="w")
        self.first_name_entry = ctk.CTkEntry(registration_frame)
        self.first_name_entry.grid(column=1, row=2, columnspan=2, padx=10, pady=5)
        # Last name
        self.last_name_var = ctk.StringVar(value="Prezime:")
        last_name_label = ctk.CTkLabel(
            registration_frame, textvariable=self.last_name_var
        )
        last_name_label.grid(column=1, row=3, padx=10, pady=10, sticky="w")
        self.last_name_entry = ctk.CTkEntry(registration_frame)
        self.last_name_entry.grid(column=1, row=4, columnspan=2, padx=10, pady=5)
        # Username
        self.username_var = ctk.StringVar(value="Korisničko ime:")
        username_label = ctk.CTkLabel(
            registration_frame, textvariable=self.username_var
        )
        username_label.grid(column=1, row=5, padx=10, pady=10, sticky="w")
        self.username_entry = ctk.CTkEntry(registration_frame)
        self.username_entry.grid(column=1, row=6, columnspan=2, padx=10, pady=5)
        # Password
        self.password_var = ctk.StringVar(value="Lozinka:")
        password_label = ctk.CTkLabel(
            registration_frame, textvariable=self.password_var
        )
        password_label.grid(column=1, row=7, padx=10, pady=10, sticky="w")
        self.password_entry = ctk.CTkEntry(registration_frame, show="*")
        self.password_entry.grid(column=1, row=8, columnspan=2, padx=10, pady=5)
        # E-mail
        self.email_var = ctk.StringVar(value="Adresa elektroničke pošte:")
        email_label = ctk.CTkLabel(registration_frame, textvariable=self.email_var)
        email_label.grid(column=4, row=1, padx=25, pady=10, sticky="w")
        self.email_entry = ctk.CTkEntry(registration_frame)
        self.email_entry.grid(column=4, row=2, columnspan=2, padx=25, pady=5)
        # E-mail notifications
        self.email_notifications_var = ctk.StringVar(
            value="Želiš li primati obavijesti putem elektroničke pošte?"
        )
        email_notifications_label = ctk.CTkLabel(
            registration_frame, textvariable=self.email_notifications_var
        )
        email_notifications_label.grid(column=4, row=3, padx=25, pady=10, sticky="w")
        self.email_notifications_switch = ctk.CTkSwitch(registration_frame, text="")
        self.email_notifications_switch.grid(
            column=4, row=4, columnspan=2, padx=25, pady=5
        )
        # Admin
        self.admin_var = ctk.StringVar(value="Administrator:")
        admin_label = ctk.CTkLabel(registration_frame, textvariable=self.admin_var)
        admin_label.grid(column=4, row=5, padx=25, pady=10, sticky="w")
        self.admin_switch = ctk.CTkSwitch(registration_frame, text="")
        self.admin_switch.grid(column=4, row=6, columnspan=2, padx=25, pady=5)
        # Activity
        self.active_var = ctk.StringVar(value="Aktivan:")
        active_label = ctk.CTkLabel(registration_frame, textvariable=self.active_var)
        active_label.grid(column=4, row=7, padx=25, pady=10, sticky="w")
        self.active_switch = ctk.CTkSwitch(registration_frame, text="")
        self.active_switch.grid(column=4, row=8, columnspan=2, padx=25, pady=5)

        # Buttons
        self.register_button_var = ctk.StringVar(value="Registriraj se")
        registration_button = ctk.CTkButton(
            registration_frame,
            textvariable=self.register_button_var,
            command=self.add_new_user,
        )
        registration_button.grid(column=4, row=9, padx=5, pady=25, ipadx=10)

    def back_to_login_screen(self):
        self.main.clear_main_frame()
        self.main.create_login_screen(self.language_var.get())

    def add_new_user(self):
        user = db_add_user(
            self.first_name_entry.get(),
            self.last_name_entry.get(),
            self.username_entry.get(),
            self.password_entry.get(),
            self.email_entry.get(),
            self.email_notifications_switch.get(),
            self.admin_switch.get(),
            self.active_switch.get(),
        )
        if user == None:
            if (
                self.language_var.get() == "Hrvatski"
                or self.language_var.get() == "Croatian"
            ):
                messagebox.showinfo(
                    title="Uspješno!",
                    message="Korisnik je uspješno dodan u bazu podataka.",
                )
            if (
                self.language_var.get() == "Engleski"
                or self.language_var.get() == "English"
            ):
                messagebox.showinfo(
                    title="Successfully!",
                    message="The user has been successfully added to the database.",
                )
        else:
            if (
                self.language_var.get() == "Hrvatski"
                or self.language_var.get() == "Croatian"
            ):
                messagebox.showerror(
                    title="Postojeći korisnik!",
                    message="Korisnik već postoji u bazi podataka.",
                )
            if (
                self.language_var.get() == "Engleski"
                or self.language_var.get() == "English"
            ):
                messagebox.showerror(
                    title="Existing user!",
                    message="The user already exists in the database.",
                )
