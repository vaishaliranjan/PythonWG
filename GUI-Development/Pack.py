import tkinter as tk
from tkinter import ttk
root=tk.Tk()
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)
# tk.Label(root, text="Label 1", background="red").pack(side="top", fill="both", expand=True)
# tk.Label(root, text="Label 2", background="Red").pack(side="top",  fill="both",expand=True)
# tk.Label(root, text="Label Left", background="green").pack(side="left", fill="both", expand=True)

tk.Label(main, text="Label 1", background="red").pack(side="top", fill="both", expand=True)
tk.Label(main, text="Label 2", background="Red").pack(side="top",  fill="both",expand=True)
tk.Label(main, text="Label Left", background="green").pack(side="left", fill="both", expand=True)

root.mainloop()