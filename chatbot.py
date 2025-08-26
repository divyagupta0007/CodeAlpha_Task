import tkinter as tk
from tkinter import scrolledtext, font

def get_chatbot_response(user_input):
    """Return a response based on user input using predefined patterns."""
    user_input = user_input.lower().strip()
    
    # Dictionary of patterns and responses
    responses = {
        "hi|hello|hey": "Hello! Welcome to the CodeAlpha Chatbot. How can I help you today?",
        "what is codealpha|about codealpha|who is codealpha": 
            "CodeAlpha is a platform that offers internship programs in various fields like Python programming, web development, and more. It provides hands-on tasks to help beginners learn and build projects!",
        "internship|internships": 
            "CodeAlpha offers a one-month internship program in Python programming and other domains. Interns work on tasks like building chatbots, web apps, and other projects to gain practical experience.",
        "tasks|projects|what do interns do": 
            "Interns at CodeAlpha work on tasks like creating rule-based chatbots, web applications, or data analysis projects. For example, this chatbot is a sample task from their Python internship program!",
        "how to apply|apply for internship": 
            "To apply for a CodeAlpha internship, visit their official website or check their LinkedIn page for application details. You may need to submit a resume and complete a registration process.",
        "python|programming": 
            "CodeAlpha's Python internship focuses on building projects like chatbots, using basic programming concepts such as conditionals, loops, and functions. It's great for beginners!",
        "bye|goodbye|exit": 
            "Goodbye! Thanks for chatting about CodeAlpha. Come back if you have more questions! 😊",
        "help|what can you do": 
            "I can answer questions about CodeAlpha, its internship program, tasks, and how to apply. Try asking 'What is CodeAlpha?' or 'How to apply for internship?'"
    }
    
    # Default response for unmatched inputs
    default_response = "Hmm... I'm not sure how to respond to that. Try asking about CodeAlpha's internships or tasks! Type 'help' for more options."
    
    # Check for matching patterns
    for pattern, response in responses.items():
        if any(keyword in user_input for keyword in pattern.split("|")):
            return response
    
    return default_response

class CodeAlphaChatbotGUI:
    def __init__(self):
        # Initialize the main window
        self.window = tk.Tk()
        self.window.title("CodeAlpha Chatbot")
        self.window.geometry("600x600")
        self.window.configure(bg="#f0f0f0")
        
        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.chat_font = font.Font(family="Arial", size=10)
        self.input_font = font.Font(family="Arial", size=10)
        
        # Header
        header = tk.Label(self.window, text="🤖 CodeAlpha Chatbot", font=self.title_font,
                         bg="#4CAF50", fg="white", pady=10)
        header.pack(fill=tk.X)
        
        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(
            self.window, wrap=tk.WORD, width=60, height=30,
            state=tk.DISABLED, font=self.chat_font,
            bg="white", fg="#333333", relief=tk.FLAT
        )
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Configure tags for user and bot messages
        self.chat_display.tag_config("user", foreground="#007BFF", justify="right")
        self.chat_display.tag_config("bot", foreground="#333333", justify="left")
        
        # Input frame
        input_frame = tk.Frame(self.window, bg="#f0f0f0")
        input_frame.pack(padx=10, pady=10, fill=tk.X)
        
        self.user_input = tk.Entry(
            input_frame, width=50, font=self.input_font,
            bg="white", fg="#333333", relief=tk.FLAT
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.user_input.bind("<Return>", self.send_message)
        self.user_input.focus_set()
        
        send_button = tk.Button(
            input_frame, text="Send", command=self.send_message,
            bg="#4CAF50", fg="white", font=self.input_font,
            relief=tk.FLAT, activebackground="#45a049"
        )
        send_button.pack(side=tk.RIGHT)
        
        # Initial message
        self.display_message("bot", "Welcome to the CodeAlpha Chatbot! Ask about CodeAlpha, internships, or tasks. Type 'bye' to exit.")
    
    def display_message(self, sender, message):
        """Display a message in the chat window."""
        self.chat_display.config(state=tk.NORMAL)
        tag = "user" if sender == "user" else "bot"
        prefix = "You: " if sender == "user" else "Bot: "
        self.chat_display.insert(tk.END, f"{prefix}{message}\n", tag)
        self.chat_display.insert(tk.END, "\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def send_message(self, event=None):
        """Handle sending a user message."""
        user_text = self.user_input.get().strip()
        if user_text:
            self.display_message("user", user_text)
            self.user_input.delete(0, tk.END)
            
            # Check for exit condition
            if user_text.lower() in ["bye", "goodbye", "exit"]:
                self.display_message("bot", get_chatbot_response("bye"))
                self.window.after(1000, self.window.quit)  # Close window after 1 second
                return
            
            # Get and display bot response
            response = get_chatbot_response(user_text)
            self.display_message("bot", response)
    
    def run(self):
        """Start the Tkinter main loop."""
        self.window.mainloop()

if __name__ == "__main__":
    chatbot = CodeAlphaChatbotGUI()
    chatbot.run()