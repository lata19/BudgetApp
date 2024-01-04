import tkinter as tk
from typing import Literal, Optional, Tuple, Union
from typing_extensions import Literal

import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter.windows.widgets.font import CTkFont

from Database.database import *


class StartScreen:
    def __init__(self, main, parent_frame, language):
        self.main = main
        self.parent_frame = parent_frame
        self.language = language
        self.create_start_screen()
        # self.language_change(self.language)

    def language_change(self, language):
        pass

    def create_start_screen(self):
        start_screen_frame = ctk.CTkFrame(self.parent_frame)
        start_screen_frame.grid(column=0, row=0, sticky="nsew")
        start_screen_frame.grid_columnconfigure((0, 2), weight=1)
        start_screen_frame.grid_columnconfigure(1, weight=5)
        start_screen_frame.grid_rowconfigure(0, weight=1)

        # Header
        header_frame = ctk.CTkFrame(start_screen_frame)
        header_frame.grid(column=0, row=0, columnspan=3, sticky="nsew")

        # TODO staviti na dno
        # Language picker
        self.language_var = ctk.StringVar(value="Hrvatski")
        self.language_optionmenu = ctk.CTkOptionMenu(
            start_screen_frame,
            variable=self.language_var,
            values=["Hrvatski", "Engleski"],
            command=self.language_change,
        )
        self.language_optionmenu.grid(column=0, row=3, padx=25, sticky="w")

        # Navigation
        navigation_frame = ctk.CTkFrame(start_screen_frame)
        navigation_frame.grid(column=0, row=1, columnspan=3, pady=10)

        self.segmented_button_var = ctk.StringVar()
        self.navigation = ctk.CTkSegmentedButton(
            navigation_frame,
            values=[
                "Pregled",
                "Transakcije",
                "Kartice",
                "Trgovine",
            ],
            command=self.segmented_button_callback,
            variable=self.segmented_button_var,
        )
        self.navigation.grid(column=0, row=0)

        # Informations
        self.information_frame = ctk.CTkFrame(start_screen_frame)
        self.information_frame.grid(column=0, row=2, columnspan=3, sticky="nsew")
        self.information_frame.grid_columnconfigure(0, weight=1)
        self.information_frame.grid_rowconfigure(0, weight=1)

    def clear_information_frame(self):
        for child in self.information_frame.winfo_children():
            child.destroy()

    def segmented_button_callback(self, segmented_button_var):
        self.clear_information_frame()
        if segmented_button_var == "Pregled" or segmented_button_var == "Overview":
            Overview(self.information_frame, self.language_var)
        elif (
            segmented_button_var == "Transakcije"
            or segmented_button_var == "Transactions"
        ):
            pass
        elif segmented_button_var == "Kartice" or segmented_button_var == "Cards":
            pass
        elif segmented_button_var == "Trgovine" or segmented_button_var == "Markets":
            pass


class Overview:
    def __init__(self, main_frame, language):
        self.main_frame = main_frame
        self.language = language
        self.create_overview_screen()

    def create_overview_screen(self):
        overview_frame = ctk.CTkScrollableFrame(self.main_frame)
        overview_frame.grid(column=0, row=0, sticky="nsew")

        # Income frame
        income_frame = ctk.CTkFrame(overview_frame)
        income_frame.grid(column=0, row=0, columnspan=2)
        # TODO dodati line graf sa incomom u zadnjih 6 mjeseci

        # Expenses frame
        expenses_frame = ctk.CTkFrame(overview_frame)
        expenses_frame.grid(column=2, row=0, columnspan=2)
        # TODO dodati line graf sa expensima u zdanjih 6 mjeseci

        # Transactions frame
        transactions_frame = ctk.CTkFrame(overview_frame)
        transactions_frame.grid(column=0, row=1, rowspan=3)

        # Expenses by months
        expenses_by_month_frame = ctk.CTkFrame(overview_frame)
        expenses_by_month_frame.grid(column=1, columnspan=3, row=1, rowspan=2)
        # TODO dodati bar graf za zadnjih 6 mjeseci ukupne potrošnje

        # Expenses by market
        expenses_by_market_frame = ctk.CTkFrame(overview_frame)
        expenses_by_market_frame.grid(column=0, columnspan=2, row=2, rowspan=2)
        # TODO dodati pie graf za potrošnju za trenutni mjesec po trgovinama (možda dodati da se može birati mjesec)

        # Expenses by category
        expenses_by_category_frame = ctk.CTkFrame(overview_frame)
        expenses_by_category_frame.grid(column=2, columnspan=2, row=2, rowspan=2)
        # TODO dodati pie graf za potrošnju za trenutni mjesec po kategorijama (možda dodati da se može birati mjesec)


class Transactions:
    def __init__(self, main_frame, language):
        self.main_frame = main_frame
        self.language = language

    def create_transactions_screen(self):
        pass
