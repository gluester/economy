import toml
from typing import Dict
from tkinter import *
def load(a: str = "game"): return toml.load(f"{a}.toml")


def save(a: Dict[]): with open(f"game.toml", "w") as outfile: toml.dump(a, outfile)

