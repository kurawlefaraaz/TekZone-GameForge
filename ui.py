root = tk.Tk()
scrambled_label = tk.Label(root, name= "scrambled_label", text= "Hello World", background= "#ffffff", font= "Txt 24 bold roman")
scrambled_label.place(x= "0", y= "0", relx= "0.5", anchor= "center", rely= "0.25")
correct_word_entry = tk.Entry(root, name= "correct_word_entry", )
correct_word_entry.place(x= "0", y= "0", relwidth= "0.9", relx= "0.5", anchor= "center", rely= "0.4")
root.mainloop()
