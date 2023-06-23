import tkinter as tk

import customtkinter as ctk
from PIL import Image, ImageTk

from Database.database import *


class Overview:
    def __init__(self, main, parent_frame, language):
        self.main = main
        self.parent_frame = parent_frame
        self.language = language
        # self.create_overview_screen()
        # self.language_change(self.language)

    def language_change(self, language):
        pass

    def create_overview_screen():
        pass
