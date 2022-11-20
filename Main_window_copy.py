from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.scrolledtext import *
from tkinter import ttk  # ttk contains 18 widgets
from bs4 import BeautifulSoup
from urllib.request import urlopen
import spacy_summarization as text_summarizer

counter = [0,0]
my_dir=''
plain_text=''
filepath  = "D:\python(full)\Project\Documents\Summary.txt"
files = [ #('All Files','.*'),
        ('Text File', '*.txt'),
        ('Document File', '*.docx'),
        ('PDF File', '*.pdf')]
main_counter=[0,0,0]
def About_us_clicked():
    os.startfile(r'About Us.txt')
def Help_clicked():
    os.startfile(r'Help.txt')
def btn_clicked():
    print("Menu Button Clicked")



## ----------------------------------------------------DOCUMENT TEXT FILE INTERFACE---------------------------------------------------- ##
def doc_sum_open(window):
    doc_window = Toplevel(window)
    window.withdraw()
    doc_window.geometry("1024x600+100+20")
    doc_window.title("Document Text Summarizer")
    doc_window.iconbitmap(r"Doc Text Summarizer GUI\textsummary.ico")
    doc_window.configure(bg = "#141012")

    # Canvas Layout
    doc_canvas = Canvas(
    doc_window,
    bg = "#141012",
    height = 600,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    doc_canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = r"Doc Text Summarizer GUI\doc_bg_u.png")
    background = doc_canvas.create_image(
    # 650.5, 129.0,
    515,300,
    image=background_img)

    # Summary Display Text Box
    textBox0_img = PhotoImage(file = r"Doc Text Summarizer GUI\img_textBox0_u.png")
    textBox0_bg = doc_canvas.create_image(
    715, 315.0,
    image = textBox0_img)

    textBox0 = scrolledtext.ScrolledText(
    master=doc_canvas,
    bd = 0,
    bg = "#d9d9d9",
    wrap = WORD,
    highlightthickness = 0)

    textBox0.place(
    x = 465, y = 180,
    width = 500,
    height = 270)

    # Entry Text Box
    entry0_img = PhotoImage(file = r"Doc Text Summarizer GUI\img_textBox1_u.png")
    entry0_bg = doc_canvas.create_image(
    650, 112.5,
    image = entry0_img)

    entry0 = Entry(
    master=doc_canvas,
    font=("Helvetica 12"),
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

    entry0.insert(0,r"D:\python(full)\Project\Documents")

    entry0.place(
    x = 465, y = 88,
    width = 380,
    height = 50)


    ## ---- FUNCTIONS ----
    # Function that let user select the file(.txt) he/she want to summarize from local system
    def document_sel_btn_clicked(entry0):
        global counter
        if counter[0]<1:
            global my_dir
            counter[0]+=1
            my_dir = filedialog.askopenfilename(filetypes=files,defaultextension=files,
            initialdir=r"Documents")
            if(my_dir):
                entry0.delete(0,END)
                entry0.insert(0,my_dir)
        counter=[0,0]

    # Clear input textbox and display textbox widget
    def document_reset_btn_clicked(textBox0,entry0):
        global my_dir,counter
        counter=[0,0]
        my_dir=""
        if os.path.isfile(filepath):
            os.remove(filepath)
            entry0.delete(0,END)
            textBox0.delete("1.0","end")
            messagebox.showinfo("Message","Successfully Reset!")
        elif len(entry0.get()) != 0:
            entry0.delete(0,END)
            textBox0.delete("1.0","end")
            messagebox.showinfo("Message","Successfully Reset!")
        else:
            messagebox.showerror("Error","Already Reset!")

    # Function that read file content and then call summary function to generate summary
    def document_summary_btn_clicked(textBox0):
        if not os.path.isfile(my_dir):
            messagebox.showinfo("Message","No such file found!")
        else:
            print("Directory is " + my_dir)
            file_obj=open(my_dir,mode='r',encoding="utf-8")
            plain_text=file_obj.read()
            file_obj.close()
            summary_text = text_summarizer.text_summarizer(plain_text,4)
            textBox0.insert(END,"                                     Summary\n\n",)
            textBox0.insert(END,summary_text)            
            f=open(filepath,'w')
            f.write(summary_text)
            f.close()

    # Function that Save the generated summary in a specified .txt file
    def document_save_btn_clicked():
        if not os.path.isfile(filepath) and not os.path.isfile(my_dir):
            messagebox.showinfo("Message","No such file found!")
        else:
            if os.path.isfile(filepath):
                save_file_dir = filepath
                file_obj=open(save_file_dir,'r')
                summary_text=file_obj.read()
                file_obj.close()
            elif os.path.isfile(my_dir):
                save_file_dir = my_dir
                file_obj=open(save_file_dir,'r')
                plain_text=file_obj.read()
                file_obj.close()
                summary_text = text_summarizer.text_summarizer(plain_text,7)
            print("Directory is " + save_file_dir)
            global counter
            if counter[1]<1:
                counter[1]+1
                save_dir=filedialog.asksaveasfilename(filetypes = files, defaultextension = '.txt')
                with open(save_dir,'w') as sv:
                    sv.write(summary_text)
            counter=[0,0]

    # Function that takes you back to home page
    def document_home_btn_clicked():
        bol_ans=messagebox.askokcancel("Message","Go to Home Page ?")
        if bol_ans == True:
            doc_window.destroy()
            window.deiconify()
        print("Button Clicked")


    ## ---- BUTTONS ----
    # HOME BUTTON
    document_home_img = PhotoImage(file = r"Doc Text Summarizer GUI\DocHome_Button.png")
    document_home_button = Button(
    master=doc_canvas,
    image = document_home_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : document_home_btn_clicked(),
    bd=0,
    activebackground="#59192b",
    background="#59192b",
    relief = "flat")

    document_home_button.place(
    x = 180, y = 500,
    width = 61,
    height = 61)

    # RESET BUTTON
    document_reset_img  = PhotoImage(file = r"Doc Text Summarizer GUI\Reset_Button.png")
    document_reset_button = Button(
    master=doc_canvas,
    image = document_reset_img ,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : document_reset_btn_clicked(textBox0=textBox0,entry0=entry0),
    bd=0,
    activebackground="#1e1e1e",
    background="#1e1e1e",
    relief = "flat")

    document_reset_button.place(
    x = 840, y = 500,
    width = 119,
    height = 48)

    # SUMMARY BUTTON
    document_summary_img = PhotoImage(file = r"Doc Text Summarizer GUI\Summary_Button.png")
    document_summary_button = Button(
    master=doc_canvas,    
    image = document_summary_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : document_summary_btn_clicked(textBox0=textBox0),
    bd=0,
    activebackground="#1e1e1e",
    background="#1e1e1e",
    relief = "flat")

    document_summary_button.place(
    x = 470, y = 500,
    width = 119,
    height = 48)

    # SAVE BUTTON
    document_save_img= PhotoImage(file = r"Doc Text Summarizer GUI\Save_Button.png")
    document_save_button = Button(
    master=doc_canvas,
    image = document_save_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = document_save_btn_clicked,
    bd=0,
    activebackground="#1e1e1e",
    relief = "flat")

    document_save_button.place(
    x = 655, y = 500,
    width = 119,
    height = 48)

    # SELECT BUTTON
    document_select_img = PhotoImage(file = r"Doc Text Summarizer GUI\Select_Button.png")
    document_select_button = Button(
    master=doc_canvas,
    image = document_select_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : document_sel_btn_clicked(entry0=entry0),
    bd=0,
    activebackground="#1e1e1e",
    relief = "flat")

    document_select_button.place(
    x = 860, y = 90,
    width = 119,
    height = 48)

    doc_window.resizable(False, False)
    
    # FUNCTION TO CLOSE WINDOW ABRUPTLY 
    def doSomething():
        window.deiconify()
        doc_window.destroy()
    doc_window.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
    doc_window.mainloop()

    

## ------------------------------------------------------URL INTERFACE------------------------------------------------------------- ##

def url_sum_open(window):
    url_window = Toplevel(window)
    window.withdraw()
    url_window.title("URL GUI")
    url_window.geometry("1024x600+100+20")

    # Frame Layout
    textBox = Frame(url_window)
    textBox.pack(side=TOP, fill=X)

    # FUNCTIONS
    # Function that Read text entered and then call summary function to generate summary
    def get_url_summary():
        if (len(str(urll_entry.get()))!=1):
            raw_text = str(urll_entry.get())
            page = urlopen(raw_text)
            # print(len(final_text))
            # if len(final_text)==0:
            #     messagebox.showerror("Error", "Unable to generate summary due to forbidden site!")
            soup = BeautifulSoup(page,features="html.parser")
            fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
            final_text = text_summarizer.text_summarizer(fetched_text,5)
            # else:
            result = '\nSummary:{}'.format(final_text)
            url_display_textbox.insert(END,result)	          
        else:
            messagebox.showerror("Error", "Input textbox is empty!")

    # Function that Clear input textbox and display textbox widget
    def url_clear_text():
        if len(urll_entry.get()) != 1:
            urll_entry.delete(0,END)
            url_display_textbox.delete('1.0', END)
            messagebox.showinfo("Message", "Successfully Reset!")
        else:
            messagebox.showerror("Error", "Already Reset!")

    # Function that Save the generated summary in a specified .txt file
    def url_save_summary():
        raw_text = str(urll_entry.get())
        if (len(raw_text)) != 1:
            final_text = text_summarizer.text_summarizer(raw_text,5)
            file_name = filedialog.asksaveasfilename(
                filetypes=files, defaultextension='.txt')
            with open(file_name, 'w', encoding='utf-8') as sv:
                sv.write(final_text)
            messagebox.showinfo("Message", "Summary is saved successfully!")
            result = '\nName of File: {} \nSummary:{}'.format(
                file_name, final_text) 
            url_display_textbox.delete('1.0', END)
            url_display_textbox.insert(END, result)
        else:
            messagebox.showerror("Error", "Input textbox is empty!")

    url_l1=Label(textBox,text="Enter URL To Summarize",background='grey', foreground='white')
    url_l1.grid(row=1,column=0,pady=(15, 0), padx=(18, 0))

    raww_entry=StringVar()
    urll_entry=Entry(textBox,textvariable=raww_entry,width=50)
    urll_entry.grid(row=1,column=1)

    # BUTTONS
    buttonn1 = Button(textBox, text="Reset", command=url_clear_text,
                    width=12, bg='#cd201f', fg='#fff')
    buttonn1.grid(row=4, column=0, padx=5, pady=5)

    buttonn2 = Button(textBox, text="Summarize", command=get_url_summary,
                    width=12, bg='#03A9F4', fg='#fff')
    buttonn2.grid(row=4, column=1, padx=10)

    buttonn3 = Button(textBox, text="Save", command=url_save_summary,
                    width=12, bg='#25D366', fg='#fff')
    buttonn3.grid(row=4, column=2, padx=13)

    # Resultant Summary display text Area
    url_l2 = Label(textBox, text="                                                                                    Resultant Summary                                                                                     ", background='grey', foreground='white')
    url_l2.grid(row=6, column=0, columnspan=3, pady=(20, 0), padx=(17, 0))
    url_display_textbox = ScrolledText(textBox)
    url_display_textbox.grid(row=7, column=0, columnspan=3, padx=(35, 0), pady=(0, 10))

    url_window.resizable(False, False)

    def doSomething():
        window.deiconify()
        url_window.destroy()
    url_window.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
    url_window.mainloop()



## ------------------------------------------------------TEXT BOX INTERFACE------------------------------------------------------------- ##

def text_sum_open(window):
    text_window = Toplevel(window)
    window.withdraw()
    text_window.geometry("1024x600+100+20")
    text_window.title("Text Summarizer")
    window.iconbitmap(r"Simple Text Summarizer GUI\textsummary.ico")

    # Canvas Layout
    texbox_canvas = Canvas(
        text_window,
        height = 600,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    texbox_canvas.place(x = 0, y = 0)

    textbox_background_img = PhotoImage(file = r'Simple Text Summarizer GUI\final_bg_u.png')
    textbox_background = texbox_canvas.create_image(
        0, 0,
        image=textbox_background_img,
        anchor = "nw")

    ## ---- FUNCTIONS ----
    # Function that Read text entered and then call summary function to generate summary 
    def get_summary():
        raw_text = str(input_textBox.get('1.0',END)) # get whatever text entered in input box
        if (len(raw_text)) != 1:
            final_text = text_summarizer.text_summarizer(raw_text,4) 
            result = '\nSummary:{}'.format(final_text) # final resultant text to display on GUI
            display_textBox.insert(END,result) # display_textBox is result display screen 
        else:
            messagebox.showerror("Error","Input textbox is empty!")

    # Function that Clear input textbox and display textbox widget
    def clear_text():
        if len(input_textBox.get('1.0',END)) != 1:
            input_textBox.delete('1.0',END)
            display_textBox.delete('1.0',END)
            messagebox.showinfo("Message","Successfully Reset!")
        else:   
            messagebox.showerror("Error","Already Reset!")

    # Function that Save the generated summary in a specified .txt file
    def save_summary():
        raw_text = str(input_textBox.get('1.0',END)) # get whatever text entered in input box
        if (len(raw_text)) != 1:
            final_text = text_summarizer.text_summarizer(raw_text,4)
            file_name=filedialog.asksaveasfilename(filetypes = files, defaultextension = '.txt')
            with open(file_name,'w',encoding='utf-8') as sv:
                sv.write(final_text)
            messagebox.showinfo("Message","Summary is saved successfully!")
            result = '\nName of File: {} \nSummary:{}'.format(file_name,final_text) # final resultant text to display on GUI
            display_textBox.delete('1.0',END)
            display_textBox.insert(END,result) # display_textBox is display screen of home tab
        else:
            messagebox.showerror("Error","Input textbox is empty!")

    # Funcion that takes you back to home page
    def textbox_home_button_clicked():
        bol_ans=messagebox.askokcancel("Message","Go to Home Page ?")
        if bol_ans == True:
            text_window.destroy()
            window.deiconify()
        print("Button Clicked")

    # Title label
    title_lbl = Label(texbox_canvas,text="Sumr!zer",font=("Helvetica",24,"bold"),bg="#1e1e1e",fg="white")
    title_lbl.place(x=0,y=0,width=1024,height=50)

    # Input Text Box
    input_textBox = ScrolledText(
        texbox_canvas,
        bd = 0,
        bg = "old lace",
        wrap = WORD,
        highlightthickness = 0)

    input_textBox.place(
        x = 110, y = 115,
        width = 360,
        height = 360)

    l1=Label(texbox_canvas,text="Original text",background='#87213b',foreground='white')
    l1.place(x=110, y=80,width=100,height=35)

    # Output Text Box
    display_textBox = ScrolledText(
        texbox_canvas,
        bd = 0,
        bg = "linen",
        wrap = WORD,
        highlightthickness = 0)

    display_textBox.place(
        x = 550, y = 115,
        width = 360,
        height = 360)

    l2=Label(texbox_canvas,text="Summarized text",background='#87213b',foreground='white')
    l2.place(x=550, y=80,width=100,height=35)

    ## ---- BUTTONS ----
    # HOME BUTTON
    textbox_home_img = PhotoImage(file = r'Simple Text Summarizer GUI\Home_Button.png')
    textbox_home_button = Button(
        texbox_canvas,
        image = textbox_home_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = textbox_home_button_clicked,
        bd=0,
        activebackground="#59192b",
        relief = "flat")

    textbox_home_button.place(
        x = 0, y = 0,
        width = 43,
        height = 40)

    # RESET BUTTON
    textbox_reset_img = PhotoImage(file = r'Simple Text Summarizer GUI\Reset_Button.png')
    textbox_reset_buuton = Button(
        texbox_canvas,
        image = textbox_reset_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = clear_text,
        bd=0,
        activebackground="#1e1e1e",
        relief = "flat")

    textbox_reset_buuton.place(
        x = 250, y = 500,
        width = 119,
        height = 40)

    # SUMMARY BUTTON
    textbox_summary_img = PhotoImage(file = r'Simple Text Summarizer GUI\Summary_Button.png')
    textbox_summary_button = Button(
        texbox_canvas,
        image = textbox_summary_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = get_summary,
        bd=0,
        activebackground="#1e1e1e",
        relief = "flat")

    textbox_summary_button.place(
        x = 450, y = 500,
        width = 119,
        height = 40)

    # SAVE BUTTON
    textbox_save_img = PhotoImage(file = r'Simple Text Summarizer GUI\Save_Button.png')
    textbox_save_button = Button(
        texbox_canvas,
        image = textbox_save_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = save_summary,
        bd=0,
        activebackground="#1e1e1e",
        relief = "flat")

    textbox_save_button.place(
        x = 650, y = 500,
        width = 119,
        height = 40)

    text_window.resizable(False, False)

    # FUNCTION TO CLOSE WINDOW ABRUPTLY 
    def doSomething():
        window.deiconify()
        text_window.destroy()

    text_window.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
    text_window.mainloop()



## ---------------------------------------------------------HOME PAGE----------------------------------------------------------------- ##  
    
# Define a function to close the window
def close(window):
   window.destroy()

def main_window():
    window = Tk()
    window.overrideredirect(True)
    window.geometry("1230x600+10+20")
    window.configure(bg = "#0f0f11")

    canvas = Canvas(
    window,
    bg = "#0f0f11",
    height = 600,
    width = 1230,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    )
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = r"Final Main GUI\HomePage.png")
    background = canvas.create_image(
    # 765,50,
    615,299,
    image=background_img)

    # DOCUMENT FILE TEXT INTERFACE
    docImg = PhotoImage(file = r"Final Main GUI\docImg_u.png")
    b0 = Button(
    image = docImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : doc_sum_open(window=window),
    activebackground="#87213b",
    background="#87213b",
    relief = "flat")

    b0.place(
    x = 810, y = 85,
    width = 160,
    height = 150)

    # TEXTBOX INTERFACE BUTTON
    textImg = PhotoImage(file = r"Final Main GUI\textImg_u1.png")
    b2 = Button(
    image = textImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : text_sum_open(window=window),
    activebackground="#87213b",
    background="#87213b",
    relief = "flat")

    b2.place(
    x = 540, y = 240,
    width = 150,
    height = 142)

    # URL INTERFACE
    UrlImg = PhotoImage(file = r"Final Main GUI\UrlImg_u1.png")
    b3 = Button(
    image = UrlImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : url_sum_open(window=window),
    bd=0,
    activebackground="#87213b",
    relief = "flat")

    b3.place(
    x = 1060, y = 260,
    width = 150,
    height = 140)

    # MENU TAB
    menuImg = PhotoImage(file = r"Final Main GUI\menuImg.png")
    b4 = Button(
    image = menuImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    bd=0,
    activebackground="#0B0E10",
    background="#0B0E10",
    relief = "flat")

    b4.place(
    x = 85, y = 41,
    width = 75,
    height = 35)

    # ABOUT TAB
    aboutImg = PhotoImage(file = r"Final Main GUI\aboutImg_u.png")
    b5 = Button(
    image = aboutImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = About_us_clicked,
    bd=0,
    activebackground="#87213b",
    background="#87213b",
    relief = "flat")

    b5.place(
    x = 415, y = 42,
    width = 82,
    height = 23)

    # HOME TAB
    helpImg = PhotoImage(file = r"Final Main GUI\helpImg_u.png")
    b6 = Button(
    image = helpImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = Help_clicked,
    bd=0,
    activebackground="#87213b",
    background="#87213b",
    relief = "flat")

    b6.place(
    x = 570, y = 42,
    width = 69,
    height = 23)

    # CLOSE TAB
    closeImg = PhotoImage(file = r"Final Main GUI\closeImg.png")
    b7 = Button(
    image = closeImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : close(window=window),
    bd=0,
    activebackground="#87213b",
    background="#87213b",
    relief = "flat")

    b7.place(
    x = 1165, y = 40,
    width = 35,
    height = 33)

    window.resizable(False, False)
    window.mainloop()

if __name__== '__main__':
    main_window()
