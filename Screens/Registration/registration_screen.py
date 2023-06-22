import tkinter as tk

import customtkinter as ctk
from PIL import Image, ImageTk

from Database.database import *


class Registration:
    def __init__(self, main, parent_frame, language):
        self.main = main
        self.parent_frame = parent_frame
        self.language = language
        self.create_registration_screen()
        self.language_change(self.language)

    def language_change(self, language):
        if language == "Hrvatski":
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
        elif language == "Deutsch":
            self.first_name_var.set("Vorname:")
            self.last_name_var.set("Nachname:")
            self.username_var.set("Benutzername:")
            self.password_var.set("Passwort:")
            self.email_var.set("E-Mail-Addresse:")
            self.email_notifications_var.set(
                "Möchten Sie Benachrichtigungen per E-Mail erhalten?"
            )
            self.admin_var.set("Administrator/in:")
            self.active_var.set("Aktiv:")
            self.register_button_var.set("Registrieren")

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
            values=["Hrvatski", "English", "Deutsch"],
            command=self.language_change,
        )
        language_optionmenu.grid(column=0, row=0, padx=25, pady=25, sticky="w")

        # First name
        self.first_name_var = ctk.StringVar(value="Ime:")
        first_name_label = ctk.CTkLabel(
            registration_frame, textvariable=self.first_name_var
        )
        first_name_label.grid(column=1, row=1, padx=10, pady=10, sticky="w")
        first_name_entry = ctk.CTkEntry(registration_frame)
        first_name_entry.grid(column=1, row=2, columnspan=2, padx=10, pady=5)
        # Last name
        self.last_name_var = ctk.StringVar(value="Prezime:")
        last_name_label = ctk.CTkLabel(
            registration_frame, textvariable=self.last_name_var
        )
        last_name_label.grid(column=1, row=3, padx=10, pady=10, sticky="w")
        last_name_entry = ctk.CTkEntry(registration_frame)
        last_name_entry.grid(column=1, row=4, columnspan=2, padx=10, pady=5)
        # Username
        self.username_var = ctk.StringVar(value="Korisničko ime:")
        username_label = ctk.CTkLabel(
            registration_frame, textvariable=self.username_var
        )
        username_label.grid(column=1, row=5, padx=10, pady=10, sticky="w")
        username_entry = ctk.CTkEntry(registration_frame)
        username_entry.grid(column=1, row=6, columnspan=2, padx=10, pady=5)
        # Password
        self.password_var = ctk.StringVar(value="Lozinka:")
        password_label = ctk.CTkLabel(
            registration_frame, textvariable=self.password_var
        )
        password_label.grid(column=1, row=7, padx=10, pady=10, sticky="w")
        password_entry = ctk.CTkEntry(registration_frame)
        password_entry.grid(column=1, row=8, columnspan=2, padx=10, pady=5)
        # E-mail
        self.email_var = ctk.StringVar(value="Adresa elektroničke pošte:")
        email_label = ctk.CTkLabel(registration_frame, textvariable=self.email_var)
        email_label.grid(column=4, row=1, padx=25, pady=10, sticky="w")
        email_entry = ctk.CTkEntry(registration_frame)
        email_entry.grid(column=4, row=2, columnspan=2, padx=25, pady=5)
        # E-mail notifications
        self.email_notifications_var = ctk.StringVar(
            value="Želiš li primati obavijesti putem elektroničke pošte?"
        )
        email_notifications_label = ctk.CTkLabel(
            registration_frame, textvariable=self.email_notifications_var
        )
        email_notifications_label.grid(column=4, row=3, padx=25, pady=10, sticky="w")
        email_notifications_entry = ctk.CTkSwitch(registration_frame, text="")
        email_notifications_entry.grid(column=4, row=4, columnspan=2, padx=25, pady=5)
        # Admin
        self.admin_var = ctk.StringVar(value="Administrator:")
        admin_label = ctk.CTkLabel(registration_frame, textvariable=self.admin_var)
        admin_label.grid(column=4, row=5, padx=25, pady=10, sticky="w")
        admin_entry = ctk.CTkSwitch(registration_frame, text="")
        admin_entry.grid(column=4, row=6, columnspan=2, padx=25, pady=5)
        # Activity
        self.active_var = ctk.StringVar(value="Aktivan:")
        active_label = ctk.CTkLabel(registration_frame, textvariable=self.active_var)
        active_label.grid(column=4, row=7, padx=25, pady=10, sticky="w")
        active_entry = ctk.CTkSwitch(registration_frame, text="")
        active_entry.grid(column=4, row=8, columnspan=2, padx=25, pady=5)

        # Buttons
        self.register_button_var = ctk.StringVar(value="Registriraj se")
        registration_button = ctk.CTkButton(
            registration_frame, textvariable=self.register_button_var
        )
        registration_button.grid(column=4, row=9, padx=5, pady=25, ipadx=10)
