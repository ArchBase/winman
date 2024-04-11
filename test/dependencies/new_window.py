import tkinter as tk
from tkinterhtml import HtmlFrame

def show_webpage(html_file):
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Webpage Display")

    # Set window size
    root.geometry("800x600")

    # Create an HtmlFrame widget
    html_frame = HtmlFrame(root)
    html_frame.pack(fill="both", expand=True)

    # Load HTML content from the file
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Set the HTML content of the HtmlFrame
    html_frame.set_content(html_content)

    # Run the Tkinter event loop
    root.mainloop()

# Call the function and pass the path to your HTML file
show_webpage("C:/Users/aksha/Projects/creative under ends/winman/winman/winman/login/index.html")
print("done")