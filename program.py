import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox
import os

body = tk.Tk()
body.geometry("700x400")
body.title("Rohit Text Editor")

body_part = tk.Menu()

# menu option creation
file_btn = tk.Menu(body_part, tearoff=False)
edit_btn = tk.Menu(body_part, tearoff=False)
view_btn = tk.Menu(body_part, tearoff=False)

# cascade
body_part.add_cascade(label="File", menu=file_btn)
body_part.add_cascade(label="Edit", menu=edit_btn)
body_part.add_cascade(label="View", menu=view_btn)

tool_bar_label = ttk.Label(body)
tool_bar_label.pack(side=tk.TOP, fill=tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label, width=28,
                        textvariable=font_family, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial CE"))
font_box.grid(row=0, column=0, padx=5, pady=5)

# size box
size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label, width=10,
                         textvariable=size_variable, state="readonly")
font_size["values"] = tuple(range(0, 100, 2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

# putting image for bold button

bold_icon = tk.PhotoImage(file="icon2/bold_icon.png")
boldbtn = ttk.Button(tool_bar_label, image=bold_icon)
boldbtn.grid(row=0, column=2, padx=5)

# putting image for italic button

italic_icon = tk.PhotoImage(file="icon2/italic_icon.png")
italicbtn = ttk.Button(tool_bar_label, image=italic_icon)
italicbtn.grid(row=0, column=3, padx=5)

# putting image for underline button

underline_icon = tk.PhotoImage(file="icon2/underline_icon.png")
underlinebtn = ttk.Button(tool_bar_label, image=underline_icon)
underlinebtn.grid(row=0, column=4, padx=5)

# putting image for align left
align_left_icon = tk.PhotoImage(file="icon2/left_icon.png")
alignleft_btn = ttk.Button(tool_bar_label, image=align_left_icon)
alignleft_btn.grid(row=0, column=5, padx=5)

# putting image for align mid
align_center_icon = tk.PhotoImage(file="icon2/center_icon.png")
aligncenter_btn = ttk.Button(tool_bar_label, image=align_center_icon)
aligncenter_btn.grid(row=0, column=6, padx=5)

# putting image for align right
align_right_icon = tk.PhotoImage(file="icon2/right_icon.png")
alignright_btn = ttk.Button(tool_bar_label, image=align_right_icon)
alignright_btn.grid(row=0, column=7, padx=5)
# putting image for font color button

font_color_icon = tk.PhotoImage(file="icon2/font_color_icon.png")
fontcolor_btn = ttk.Button(tool_bar_label, image=font_color_icon)
fontcolor_btn.grid(row=0, column=8, padx=5)

# putting image for text Editor

Editor = tk.Text(body)
Editor.config(wrap="word", relief=tk.FLAT)

scroll_bar = tk.Scrollbar(body)
Editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
Editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=Editor.yview)
Editor.config(yscrollcommand=scroll_bar.set)

# defining function for font family and function

font_now = "Arial"
font_size_now = 16


def change_font(body):
    global font_now
    font_now = font_family.get()
    Editor.configure(font=(font_now, font_size_now))


def change_size(body):
    global font_size_now
    font_size_now = size_variable.get()
    Editor.configure(font=(font_now, font_size_now))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)

# creation of bold function


def bold_fun():
    textget = tk.font.Font(font=Editor["font"])
    if textget.actual()["weight"] == 'normal':
        Editor.configure(font=(font_now, font_size_now, "bold"))
    if textget.actual()["weight"] == 'bold':
        Editor.configure(font=(font_now, font_size_now, "normal"))


boldbtn.configure(command=bold_fun)

# creation of italic function


def italic_fun():
    textget = tk.font.Font(font=Editor["font"])
    if textget.actual()["slant"] == 'roman':
        Editor.configure(font=(font_now, font_size_now, "italic"))
    if textget.actual()["slant"] == 'italic':
        Editor.configure(font=(font_now, font_size_now, "roman"))


italicbtn.configure(command=italic_fun)

# creation of underline function


def underline_fun():
    textget = tk.font.Font(font=Editor["font"])
    if textget.actual()["underline"] == 0:
        Editor.configure(font=(font_now, font_size_now, "underline"))
    if textget.actual()["underline"] == 1:
        Editor.configure(font=(font_now, font_size_now, "normal"))


underlinebtn.configure(command=underline_fun)

# creation of Color function


def Color_choose():
    color_var = tk.colorchooser.askcolor()
    Editor.configure(fg=color_var[1])


fontcolor_btn.configure(command=Color_choose)

# creation of  all align function


def align_left():
    textget_all = Editor.get(1.0, "end")
    Editor.tag_config("left", justify=tk.LEFT)
    Editor.delete(1.0, tk.END)
    Editor.insert(tk.INSERT, textget_all, "left")


alignleft_btn.configure(command=align_left)


def align_center():
    textget_all = Editor.get(1.0, "end")
    Editor.tag_config("center", justify=tk.CENTER)
    Editor.delete(1.0, tk.END)
    Editor.insert(tk.INSERT, textget_all, "center")


aligncenter_btn.configure(command=align_center)


def align_right():
    textget_all = Editor.get(1.0, "end")
    Editor.tag_config("right", justify=tk.RIGHT)
    Editor.delete(1.0, tk.END)
    Editor.insert(tk.INSERT, textget_all, "right")


alignright_btn.configure(command=align_right)

# creation of status bar word and character count

status_bars = ttk.Label(body, text="Status Bar")
status_bars.pack(side=tk.BOTTOM)

text_change = False


def change_word(event=None):
    global text_change
    if Editor.edit_modified():
        text_change = True
        word = len(Editor.get(1.0, "end-1c").split())
        character = len(Editor.get(1.0, "end-1c").replace(" ", ""))
        status_bars.config(text=f"character :{character} word :{word}")
    Editor.edit_modified(False)


Editor.bind("<<Modified>>", change_word)

#####################file part########################

# new function file creation

text_url = " "


def newfile(event=None):
    global text_url
    text_url = ""
    Editor.delete(1.0, tk.END)


file_btn.add_command(label="New", accelerator="Ctrl+N",
                     compound=tk.LEFT, command=newfile)

# open function file creating


def openfile(event=None):
    global text_url
    text_url = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title="select file", filetypes=(("All files", "*.*"), ("Text File", ".txt")))
    try:
        with open(text_url, "r") as for_read:
            Editor.delete(1.0, tk.END)
            Editor.insert(1.0, for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    body.title(os.path.basename(text_url))


file_btn.add_command(label="Open", compound=tk.LEFT,
                     accelerator="Ctrl+O", command=openfile)

# save function file creating


def save_file(event=None):
    global text_url
    try:
        if text_url:
            content = str(Editor.get(1.0, tk.END))
            with open(text_url, "w", encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(
                ("All files", "*.*"), ("Text File", ".txt")))
            content2 = Editor.get(1.0, tk.END)
            text_url.write(content2)
            text_url.close()
    except:
        return


file_btn.add_command(label="Save", compound=tk.LEFT, accelerator="Ctrl+S", command=save_file)

# Save As function file creation


def Save_as_file(event=None):
    global text_url
    try:
        content = Editor.get(1.0, tk.END)
        text_url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(
            ("All files", "*.*"), ("Text File", ".txt")))
        text_url.write(content)
        text_url.close()
    except:
        return


file_btn.add_command(label="Save as", compound=tk.LEFT,
                     accelerator="Ctrl+Alt+N", command=Save_as_file)

# exit function creation


def exit_fun(event=None):
    global text_url, text_change
    try:
        if text_change:
            msgbox = messagebox.askyesnocancel(
                "WARNING", "-:Do you want to save this file:-")
            if msgbox is True:
                if text_url:
                    content = Editor.get(1.0, tk.END)
                    with open(text_url, "w", encoding="utf-8") as for_read:
                        for_read.write(content)
                        body.destroy()
                else:
                    content2 = Editor.get(1.0, tk.END)
                    text_url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(
                        ("All files", "*.*"), ("Text File", ".txt")))
                    text_url.write(content)
                    text_url.close()
                    body.destroy()
            elif msgbox is False:
                body.destroy()
        else:
            body.destroy()
    except:
        return


file_btn.add_command(label="Exit", compound=tk.LEFT,
                     accelerator="Ctrl+x", command=exit_fun)

# edit_btn part creation with short cut keys

edit_btn.add_command(label="Cut", compound=tk.LEFT, accelerator="Ctrl+x",
                     command=lambda: Editor.event_generate("<Control x>"))
edit_btn.add_command(label="Copy", compound=tk.LEFT, accelerator="Ctrl+c",
                     command=lambda: Editor.event_generate("<Control c>"))
edit_btn.add_command(label="Paste", compound=tk.LEFT, accelerator="Ctrl+v",
                     command=lambda: Editor.event_generate("<Control v>"))
edit_btn.add_command(label="Delete", compound=tk.LEFT,
                     accelerator="Del", command=lambda: Editor.delete(1.0, tk.END))


def find_fun(event=None):

    def find():
        word = find_inputs.get()
        Editor.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = Editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                Editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                Editor.tag_config('match', foreground="red", background="blue")

    def replace():
        word = find_inputs.get()
        replace_text_input = replace_input.get()
        content = Editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text_input)
        Editor.delete(1.0, tk.END)
        Editor.insert(1.0, new_content)

    find_popups = tk.Toplevel()
    find_popups.geometry("400x250")
    find_popups.title("Find And Replace Word")
    find_popups.resizable(0, 0)

    # fram for find
    find_frames = ttk.LabelFrame(find_popups, text="Find and Replace Word")
    find_frames.pack(pady=20)

    # label
    text_find = ttk.Label(find_frames, text="Find Word")
    text_replace = ttk.Label(find_frames, text="Replace Word")

    # entry_box
    find_inputs = ttk.Entry(find_frames, width=30)
    replace_input = ttk.Entry(find_frames, width=30)

    # button
    find_button = ttk.Button(find_frames, command=find, text="Click to Find")
    replace_button = ttk.Button(
        find_frames, command=replace, text="Click to Replace")

    # text label grid
    text_find.grid(row=0, column=0, padx=5, pady=5)
    text_replace.grid(row=1, column=0, padx=5, pady=5)

    # entry grid
    find_inputs.grid(row=0, column=1, padx=5, pady=5)
    replace_input.grid(row=1, column=1, padx=5, pady=5)

    # button grid
    find_button.grid(row=0, column=2, padx=8, pady=5)
    replace_button.grid(row=1, column=2, padx=8, pady=5)


edit_btn.add_command(label="Find", compound=tk.LEFT,
                     accelerator="Ctrl+f", command=find_fun)

#####################view_btn part#########################

# tool bar creation


showtoolbar = tk.BooleanVar()
showtoolbar.set(True)
show_status_bar = tk.BooleanVar()
show_status_bar.set(True)

# function creation to hide tool bar


def hide_toolbar():
    global showtoolbar
    if showtoolbar:
        tool_bar_label.pack_forget()
        showtoolbar = False
    else:
        Editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side=tk.TOP, fill=tk.X)
        Editor.pack(fill=tk.BOTH, expand=True)
        status_bars.pack(side=tk.BOTTOM)
        showtoolbar = True

# function creation to hide status bar


def hide_status_bar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False
    else:
        status_bars.pack(side=tk.BOTTOM)
        show_status_bar = True


view_btn.add_checkbutton(label="Tool Bar", offvalue=0, onvalue=1,
                         variable=showtoolbar, compound=tk.LEFT, command=hide_toolbar)

view_btn.add_checkbutton(label="Status Bar", offvalue=0, variable=show_status_bar,
                         onvalue=1, compound=tk.LEFT, command=hide_status_bar)

body.config(menu=body_part)

body.mainloop()
