from tkinter import *

# WINDOW
window = Tk()
window.geometry("400x400")
window.title("ISA Workshop")


# # LABEL
# label = Label(window, text="Hello, world!",background="light blue", foreground="purple",width=10, height=10)
# label.pack()

# # BUTTON
# exit = Button(window,text="Exit",font="poppins 16 bold", command=window.destroy)
# exit.pack()

# # ENTRY
# entry = Entry(window,  width=10)
# entry.pack()

# # CHECKBUTTON
# var1=IntVar()
# Checkbutton(window ,text="Website",variable=var1).pack()
# var2=IntVar()
# Checkbutton(window ,text="App",variable=var2).pack()
# var3=IntVar()
# Checkbutton(window ,text="3D Printer",variable=var3).pack()
# var4=IntVar()
# Checkbutton(window ,text="Digital Library",variable=var4).pack()
# var5=IntVar()
# Checkbutton(window ,text="IoT Kit",variable=var5).pack()

# # RADIOBUTTON
# var = IntVar()
# Radiobutton(window, text="Instagram", variable=var, value=1).pack()
# Radiobutton(window, text="LinkedIn", variable=var, value=2).pack()
# Radiobutton(window, text="Facebook", variable=var, value=3).pack()

# # MESSAGE BOX 
# import tkinter.messagebox as mbox
# mbox.showerror(title="Error", message="Error box")
# mbox.showinfo(title="Info", message="Info box")
# mbox.showwarning(title="Warning", message="Warning box")
# mbox.askquestion(title="Question", message="Question box")

# # SPIN BOX 
# current_value = StringVar(value=0)
# Spinbox(window, from_=0, to=10, textvariable=current_value, wrap="true").pack()

# # EVENT HANDLER
# def hello(event):
#     print("hello, left") 
# def hi(event):
#     print("hi, middle") 
# def aloha(event):
#     print("aloha, right")  
# def double(event):                           
#     print("Double Click") 
# def motion(event):                           
#     print("On motion")

# widget = Button(None, text='Mouse Clicks')
# widget.pack()
# widget.bind('<Button-1>', hello)

# window.bind('<Button-2>', hi)
# window.bind('<Button-3>', aloha)
# window.bind('<Double-1>', double)
# window.bind('<Motion>', motion)

# exit = Button(window,text="Exit",font="poppins 16 bold", command=window.destroy)
# exit.pack()


# # IMAGES
# from PIL import Image, ImageTk

# image1 = Image.open("geometry managers.jpg")
# image1 = image1.resize((250,200), Image.ANTIALIAS)
# test = ImageTk.PhotoImage(image1)

# label1 = Label(image=test)
# label1.image = test
# label1.place(x = 80, y = 50)

window.mainloop()