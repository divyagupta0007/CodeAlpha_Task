import os
import shutil
import re
import requests
import tkinter as tk
from tkinter import filedialog, messagebox

# --------- TASK FUNCTIONS ----------

# 1. Move all .jpg files
def move_jpg_files():
    source = filedialog.askdirectory(title="Select Source Folder")
    if not source:
        return
    destination = filedialog.askdirectory(title="Select Destination Folder")
    if not destination:
        return

    count = 0
    for file in os.listdir(source):
        if file.lower().endswith(".jpg"):
            shutil.move(os.path.join(source, file), os.path.join(destination, file))
            count += 1

    messagebox.showinfo("✅ Task Complete", f"Moved {count} JPG files successfully!")

# 2. Extract emails
def extract_emails():
    file_path = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    with open(file_path, "r") as f:
        text = f.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

    if emails:
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if save_path:
            with open(save_path, "w") as f:
                f.write("\n".join(emails))
            messagebox.showinfo("✅ Task Complete", f"Extracted {len(emails)} emails successfully!")
    else:
        messagebox.showwarning("⚠️ No Emails Found", "No email addresses found in the file.")

# 3. Scrape webpage title
def scrape_title():
    url = "https://www.example.com"  # fixed webpage
    try:
        response = requests.get(url)
        if "<title>" in response.text:
            title = response.text.split("<title>")[1].split("</title>")[0]
        else:
            title = "No Title Found"

        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if save_path:
            with open(save_path, "w") as f:
                f.write(f"Title: {title}")
            messagebox.showinfo("✅ Task Complete", f"Saved title: {title}")

    except Exception as e:
        messagebox.showerror("❌ Error", f"Could not fetch title: {e}")

# --------- GUI INTERFACE ----------

root = tk.Tk()
root.title("🎨 Task Automation Tool")
root.geometry("450x550")
root.config(bg="#ffe6e6")  # light pastel pink background

title_label = tk.Label(root, text="⚡ Task Automation Tool ⚡",
                       font=("Arial Rounded MT Bold", 20),
                       bg="#ffe6e6", fg="#4b0082")
title_label.pack(pady=20)

btn_style = {
    "font": ("Arial", 12, "bold"),
    "width": 30,
    "height": 2,
    "relief": "raised",
    "bd": 3
}

btn1 = tk.Button(root, text="📂 Move JPG Files", bg="#ff9999", fg="white", command=move_jpg_files, **btn_style)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="📧 Extract Emails from Text File", bg="#66ccff", fg="white", command=extract_emails, **btn_style)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="🌐 Scrape Webpage Title", bg="#99e699", fg="black", command=scrape_title, **btn_style)
btn3.pack(pady=10)

exit_btn = tk.Button(root, text="❌ Exit", bg="#ffcc66", fg="black", command=root.quit, **btn_style)
exit_btn.pack(pady=15)

root.mainloop()
