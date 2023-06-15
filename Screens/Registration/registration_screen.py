import tkinter as tk

import customtkinter as ctk
from PIL import Image, ImageTk

from Database.database import *


class Registration:
    def __init__(self, main, parent_frame, language):
        self.main = main
        self.parent_frame = parent_frame
        self.language = language
        self.set_language(language)

    def set_language(self, language):
        if language == "Hrvatski":
            pass
        elif language == "English":
            pass
        elif language == "Deutsch":
            pass
