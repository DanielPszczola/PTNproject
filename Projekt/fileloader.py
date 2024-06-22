import pandas as pd
from tkinter import filedialog

def load_file():
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filename:
        data = pd.read_csv(filename)
        return data
