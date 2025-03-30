import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

# Define the main window

root = tk.Tk()
root.title("YOUR AI ASSISTANT")

# adding a background color
root.configure(bg='steelblue')


# Define the function for youtube open 
def search_youtube():
    query= entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# Define the function for google open 
def search_google():
    query= entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)    
    
    
# Define the function for instagram open 
def search_instagram():
    user_name = entry.get().replace('@','') #ensure username is clean of @
    url=f"https://www.instagram.com/{user_name}/"
    webbrowser.open(url)
    
    
# create input field
Label(root, text="Enter your command: ").pack(pady=10)
entry=Entry(root, width=50)
entry.pack(pady=10)
Button(root, text="Search on youtube", command=search_youtube).pack(pady=5)    
Button(root, text="Search on instagram", command=search_instagram).pack(pady=5)    
Button(root, text="Search on google", command=search_google).pack(pady=5)    
    
    
#Run the GUI loop
root.mainloop()