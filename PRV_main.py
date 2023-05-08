import tkinter as tk

#312f47
#3f3e52
#1c1a2e

root = tk.Tk()
root.geometry("1000x700")
root.resizable(False, False) 

frame0 = tk.Frame(root, bg="black", width=1000, height=700)
frame0.pack(fill=tk.X)

# Sección 1
frame1 = tk.Frame(frame0, bg="#312f47", width=300,height=700)
frame1.pack(fill=tk.X, side="right")

# Sección 2
frame2 = tk.Frame(frame0, bg="#3f3e52",width=700, height=700)
frame2.pack(fill=tk.X, side="left")


root.mainloop()