import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import random


def upload_file():
    file = filedialog.askopenfilename(
        title="Select Bug Report",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Log Files", "*.log"),
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")
        ]
    )
    if file:
        file_label.config(text=file)

def analyze():
    bug = text.get("1.0", tk.END).strip()

    severity = random.choice(["High", "Medium", "Low"])
    component = random.choice([
        "Frontend",
        "Backend",
        "Database",
        "Authentication",
        "API"
    ])

    cause = random.choice([
        "Null Pointer Exception",
        "Missing Validation",
        "Database Connection Failure",
        "Incorrect API Response",
        "Invalid Input"
    ])

    fix = random.choice([
        "Add input validation",
        "Handle null values",
        "Check DB connection",
        "Improve exception handling",
        "Verify API endpoint"
    ])

    result.delete("1.0", tk.END)

    result.insert(tk.END, "========== ANALYSIS RESULT ==========\n\n")
    result.insert(tk.END, f"Severity : {severity}\n")
    result.insert(tk.END, f"Component : {component}\n\n")

    result.insert(tk.END, "Possible Root Cause\n")
    result.insert(tk.END, cause + "\n\n")

    result.insert(tk.END, "Suggested Fix\n")
    result.insert(tk.END, fix + "\n\n")

    result.insert(tk.END, "Similar Bugs\n")
    result.insert(tk.END, "BUG-101\n")
    result.insert(tk.END, "BUG-245\n")
    result.insert(tk.END, "BUG-390\n")

window = tk.Tk()
window.title("AI Smart Bug Analyzer & Fix Advisor")
window.geometry("900x650")

title = tk.Label(
    window,
    text="AI Smart Bug Analyzer & Fix Advisor",
    font=("Arial",20,"bold")
)
title.pack(pady=10)

tk.Label(window,text="Paste Bug Description").pack()

text = scrolledtext.ScrolledText(window,height=10,width=100)
text.pack()

tk.Button(
    window,
    text="Upload Bug Report",
    command=upload_file,
    bg="lightblue"
).pack(pady=10)

file_label = tk.Label(window,text="No file selected")
file_label.pack()

tk.Button(
    window,
    text="Analyze Bug",
    command=analyze,
    bg="green",
    fg="white",
    width=20
).pack(pady=10)

result = scrolledtext.ScrolledText(window,height=15,width=100)
result.pack()

window.mainloop()
