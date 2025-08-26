import tkinter as tk
from tkinter import messagebox
import random

# --- Word List (100 easy English vocab) ---
words = [
    "apple","banana","orange","grape","mango","lemon","pear","peach","plum","melon",
    "dog","cat","fish","bird","horse","tiger","lion","zebra","monkey","sheep",
    "car","bus","train","truck","plane","ship","bike","jeep","van","boat",
    "chair","table","bed","sofa","lamp","door","wall","floor","roof","window",
    "book","pen","pencil","paper","bag","board","chalk","eraser","scale","sharpener",
    "sun","moon","star","sky","rain","cloud","wind","snow","storm","light",
    "happy","sad","big","small","fast","slow","hot","cold","kind","good",
    "run","walk","eat","drink","sleep","read","write","jump","play","sing",
    "red","blue","green","yellow","pink","black","white","brown","purple","gray",
    "king","queen","man","woman","boy","girl","child","baby","friend","family"
]

coins = 0  # Global coin counter

# --- Functions ---
def start_game():
    start_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    new_round()

def new_round():
    global word, guessed, attempts
    word = random.choice(words)
    guessed = []
    attempts = 6
    update_display()

def update_display():
    display_word = " ".join([letter if letter in guessed else "_" for letter in word])
    word_label.config(text=display_word)

    coins_label.config(text=f"Coins: {coins} 🪙")
    attempts_label.config(text=f"Attempts left: {attempts}")

def guess_letter(letter):
    global attempts, coins
    if letter in guessed:
        return
    
    guessed.append(letter)
    if letter not in word:
        attempts -= 1
        if attempts == 1:  # Hint trigger at 5th wrong attempt
            hint_label.config(text=f"Hint: Word starts with '{word[0]}'")
    else:
        if all(l in guessed for l in word):
            messagebox.showinfo("Congratulations!", f"You guessed the word: {word}\nYou earned 40 coins!")
            coins_add(40)
            new_round()
            return

    if attempts <= 0:
        messagebox.showinfo("Game Over", f"Out of attempts! The word was: {word}")
        new_round()
    else:
        update_display()

def coins_add(amount):
    global coins
    coins += amount
    update_display()

def take_hint():
    global coins, guessed
    if coins < 80:
        messagebox.showwarning("Not Enough Coins", "You need at least 80 coins to buy a hint!")
        return
    
    # Deduct coins and reveal a random unguessed letter
    coins_spend(80)
    hidden_letters = [l for l in word if l not in guessed]
    if hidden_letters:
        reveal = random.choice(hidden_letters)
        guessed.append(reveal)
        messagebox.showinfo("Hint", f"The letter '{reveal}' is in the word!")
        update_display()

def coins_spend(amount):
    global coins
    coins -= amount
    update_display()

# --- UI Setup ---
root = tk.Tk()
root.title("HangmaN VocaB")
root.geometry("1920x1080")


# --- Start Screen ---
start_frame = tk.Frame(root, bg="white")
start_frame.pack(fill="both", expand=True)

# Pastel background with blurred alphabets
for i in range(100):
    x, y = random.randint(10, 1920), random.randint(30, 1080)
    letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    color = random.choice(["#ffd6e0", "#d6f5ff", "#e6ffd6", "#fff0b3", "#e0d6ff"])
    tk.Label(start_frame, text=letter, font=("Arial", random.randint(20,40), "bold"),
             fg=color, bg="white").place(x=x, y=y)

start_btn = tk.Button(start_frame, text="Start Game", font=("Arial", 16, "bold"), bg="#6a5acd", fg="white", command=start_game)
start_btn.place(relx=0.5, rely=0.5, anchor="center")

# --- Game Screen ---
game_frame = tk.Frame(root, bg="#f4f4f4")

word_label = tk.Label(game_frame, text="", font=("Arial", 28), bg="#f4f4f4")
word_label.pack(pady=20)

coins_label = tk.Label(game_frame, text="Coins: 0 🪙", font=("Arial", 14), bg="#f4f4f4", fg="gold")
coins_label.pack()

attempts_label = tk.Label(game_frame, text="Attempts left: 6", font=("Arial", 14), bg="#f4f4f4")
attempts_label.pack()

hint_label = tk.Label(game_frame, text="", font=("Arial", 12), fg="blue", bg="#f4f4f4")
hint_label.pack(pady=5)

# Alphabet buttons
buttons_frame = tk.Frame(game_frame, bg="black")
buttons_frame.pack(pady=20)

for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    btn = tk.Button(buttons_frame, text=letter, width=4, height=2,
                    command=lambda l=letter.lower(): guess_letter(l))
    btn.grid(row=i // 9, column=i % 9, padx=3, pady=3)

# Hint button
hint_btn = tk.Button(game_frame, text="Take Hint (80 🪙)", font=("Arial", 12), bg="orange", command=take_hint)
hint_btn.pack(pady=15)

# First screen with Start button
def start_screen():
   

    title = tk.Label(start_frame, text="🎮Welcome to Hangman!🎮", font=("Edwardian Script IT", 48), bg="#e0a5c6")
    title.pack(pady=160)

    


start_screen()
root.mainloop()
