import tkinter as tk
from tkinter import messagebox
import random
import json
import os

# -----------------------
# Cute pastel theme 🍓🍑
# -----------------------
BG = "#fff0f5"
CARD = "#ffe4ec"
BUTTON = "#ff9bb3"
BUTTON_HOVER = "#ff86a3"
TEXT = "#5b3a42"

FONT_TITLE = ("Comic Sans MS", 20, "bold")
FONT_NORMAL = ("Comic Sans MS", 11)

DATA_FILE = "restaurants.json"


# -----------------------
# Storage
# -----------------------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


# -----------------------
# Cute Button
# -----------------------
class CuteButton(tk.Button):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            bg=BUTTON,
            fg="white",
            relief="flat",
            padx=14,
            pady=6,
            font=FONT_NORMAL,
            cursor="hand2",
            **kwargs
        )
        self.bind("<Enter>", lambda e: self.config(bg=BUTTON_HOVER))
        self.bind("<Leave>", lambda e: self.config(bg=BUTTON))


# -----------------------
# Main App
# -----------------------
class FoodChooser(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("What Should We Eat?")
        self.geometry("520x560")
        self.configure(bg=BG)

        self.data = load_data()

        self.build_ui()
        self.refresh()

    # -----------------------
    # UI
    # -----------------------
    def build_ui(self):
        tk.Label(
            self,
            text="What Should We Eat?",
            bg=BG,
            fg=TEXT,
            font=FONT_TITLE
        ).pack(pady=12)

        # Entry card
        card = tk.Frame(self, bg=CARD, padx=20, pady=20)
        card.pack(padx=20, pady=10, fill="x")

        tk.Label(card, text="Add a restaurant", bg=CARD, fg=TEXT).pack()

        self.entry = tk.Entry(card, font=FONT_NORMAL)
        self.entry.pack(pady=6)

        CuteButton(card, text="Add 🍽️", command=self.add_item).pack()

        # List
        self.listbox = tk.Listbox(
            self,
            font=("Comic Sans MS", 11),
            height=10,
            bg="white",
            fg=TEXT
        )
        self.listbox.pack(fill="both", expand=True, padx=20, pady=10)

        btns = tk.Frame(self, bg=BG)
        btns.pack()

        CuteButton(btns, text="Remove Selected", command=self.remove_item).pack(side="left", padx=5)

        # Result display
        self.result = tk.Label(
            self,
            text="Tap to choose!",
            bg=BG,
            fg=TEXT,
            font=("Comic Sans MS", 16, "bold")
        )
        self.result.pack(pady=12)

        CuteButton(
            self,
            text="Pick For Me 🎲",
            command=self.pick_random,
            font=("Comic Sans MS", 13, "bold"),
            padx=18,
            pady=10
        ).pack(pady=8)

    # -----------------------
    # Logic
    # -----------------------
    def add_item(self):
        name = self.entry.get().strip()
        if not name:
            return

        self.data.append(name)
        save_data(self.data)

        self.entry.delete(0, tk.END)
        self.refresh()

    def remove_item(self):
        sel = self.listbox.curselection()
        if not sel:
            return

        self.data.pop(sel[0])
        save_data(self.data)
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for r in self.data:
            self.listbox.insert(tk.END, r)

    # cute little "shuffle" animation
    def pick_random(self):
        if not self.data:
            messagebox.showinfo("Add food first!", "Add some restaurants 🍜")
            return

        self.animate_pick(0)

    def animate_pick(self, count):
        if count < 12:
            choice = random.choice(self.data)
            self.result.config(text=choice)
            self.after(70, lambda: self.animate_pick(count + 1))
        else:
            final = random.choice(self.data)
            self.result.config(text=f"Let's eat at:\n{final} 💖")


# -----------------------
# Run
# -----------------------
if __name__ == "__main__":
    FoodChooser().mainloop()
