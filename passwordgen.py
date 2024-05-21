import string
import random
import tkinter as tk
from tkinter import messagebox 

def passgen(lenth):
    s_all = string.ascii_letters
    s_up = string.ascii_uppercase
    s_low = string.ascii_lowercase
    s_num = string.digits
    
    s_punc = string.punctuation

    
   
    passs = []
    # lenth = input("Enter password length \n:")
    lenth = int(lenth)
    passs.extend(random.choice(s_all))
    passs.extend(random.choice(s_up))
    passs.extend(random.choice(s_all))
    passs.extend(random.choice(s_all))
    passs.extend(random.choice(s_low))
    passs.extend(random.choice(s_punc))
    passs.extend(random.choice(s_all))
    passs.extend(random.choice(s_num))
    
    if lenth < 8:
        random.shuffle(passs)
        password = "".join(passs[0:lenth])
    else:
        rem_len = (lenth - 8)
        # print(rem_len)
        newl = []
        newl.extend(list(s_all))
        newl.extend(list(s_punc))
        newl.extend(list(s_num))
        for _ in range(rem_len):
            passs.extend(random.choice(newl))
        password = "".join(passs)
    return password
    

def main():
    def generate_password():
        length = length_var.get()
        password = passgen(length)


        result_label.config(text=f"Your password is: {password}")
    def copy_to_clip():
        length = length_var.get()
        password = passgen(length)
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

        
    root =  tk.Tk()
    root.geometry("500x300")
    root.title("Password Generator")
    root.resizable(False,False)
    length_var = tk.IntVar()
    main_frame = tk.Frame(root, bg="BLUE",height=300, width=500, bd = 10)
    main_frame.place(x = 0, y = 0)
    inside_frame = tk.Frame(main_frame, bg = "BLUE", height=200, width = 400)
    inside_frame.place(x= 50, y = 50)
    label = tk.Label(inside_frame, text="Enter Your Password Length ", font=("poppins", 10, "bold", ), bg="Blue", fg="WHITE")
    label.grid(row=0, column=0, padx = 10, pady = 20)
    entry = tk.Entry(inside_frame, textvariable=length_var, font=("poppins", 10, "bold"),bd = 1, relief="groove")
    entry.grid(row=0, column = 1,padx = 10, pady = 20)

    button = tk.Button(inside_frame, text="Get Password", font=("poppins", 10, "bold") ,bg = "GREEN", fg = "WHITE", command=generate_password)
    button.grid(row= 1, column = 1, padx=10, pady =10)
    button2 = tk.Button(inside_frame, text="Copy", font=("poppins", 10, "bold") ,bg = "GREEN", fg = "WHITE", command=copy_to_clip)
    button2.grid(row= 3, column = 1, padx=10, pady =10)
    result_label = tk.Label(inside_frame, text="", font=("Poppins", 10, "bold"), bg="BLUE", fg="WHITE")
    result_label.grid(row = 3, column = 0)


    




    root.mainloop()


    # passgen()
    

if __name__ == "__main__":
    main()

    
            
        

     


    
       
     

        
            


        
    
    

    

