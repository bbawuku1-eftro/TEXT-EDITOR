# Import necessary packages
from email.mime import text
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setup Root Window
window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minisize=800, weight=1)
window.columnconfigure(1, minisize=800, weight=1)

# Function to open a file
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    # If a file is opened then display the contents of the file
    with open(filepath, "r") as input_file:
        # Read contents of the input file
        contents = input_file.read()
        # Insert contents of the file in the editor box
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Codingal's Text Editor - {filepath}")

# Function to Save a file
def save_file():
    # Save the current file as a new file
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
     )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        # Read the edited content and update in the output file
        text = txt_edit.get(1.0, END)
        output_file.write(text)