import tkinter as tk

#312f47
#3f3e52
#1c1a2e

root = tk.Tk()
root.geometry("900x750")
root.resizable(False, False) 

frame0 = tk.Frame(root, bg="black", width=900, height=650)
frame0.pack(fill=tk.X)

# Sección 1
frame1 = tk.Frame(frame0, bg="#312f47", width=650,height=680)
frame1.pack(fill=tk.X, side="right")

# Sección 2
frame2 = tk.Frame(frame0, bg="#3f3e52",width=250, height=680)
frame2.pack(fill=tk.X, side="left")

# Sección 3
frame3 = tk.Frame(root, bg="#1c1a2e", height=70)
frame3.pack(fill=tk.X)

root.mainloop()