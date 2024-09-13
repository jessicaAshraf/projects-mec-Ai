import csv
import os
from tkinter import*
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
class Book:
     __title=""
     __author=""
     __genre=""
     __publicationYear=0
     def __init__(self,title,author,genre,publicationYear):
         self.__title=title
         self.__author=author
         self.__genre=genre
         self.__publicationYear=publicationYear

class Library:
      
      def __init__(self):
       self.__ListOfBooks=[]


      def addBook (self,title,author,genre,publicationYear):
          self.title=title
          self.author=author
          self.genre=genre
          self.publicationYear=publicationYear
         
          self.book= Book(self.title,self.author,self.genre,self.publicationYear)
          dict={
                         "Title": self.title,
                        "Author": self.author,
                        "Genre": self.genre,
                        "Publication Year": self.publicationYear
            }
          path='E:\project personal library python\library.csv'
          try:
        
            file_exists = os.path.exists(path)
            with open(path, mode='a', newline='') as csvfile:
               fieldnames = ["Title", "Author", "Genre", "Publication Year"]
               writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
               if not file_exists:
                 writer.writeheader()
               writer.writerow(dict)
               messagebox.showinfo("SUCCESS", f"Book '{self.title}' added successfully!")
          except Exception as e:
             print("Error:", e)
             messagebox.showerror("ERROR", f"Failed to add the book. Error: {str(e)}")
              
              
                  
                  
              
      def removeBook(self,title):
         self.title=title
         try:
             with open('library.csv', mode='r') as csvfile:
               csv_reader = csv.DictReader(csvfile)
               for row in csv_reader:
                  if(row["Title"]!=self.title):
                      self.__ListOfBooks.append(row)
               with open('library.csv',mode='w') as csvfile:
                      fieldnames=["Title","Author","Genre","Publication Year"]
                      writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
                      writer.writerows(self.__ListOfBooks)
                      messagebox.showinfo("SUCCESS", f"Book '{self.title}' successfully removed!")
                  
         except Exception as e:
            print("Error:", e)
            messagebox.showerror("ERROR", f"Failed to remove the book. Error: {str(e)}")






        

    
    
        
      def searchBook(self,comboValue,searchValue,viewFrame):
        self.__list=[]
               #scrollbar
        self.scroll_y=Scrollbar(viewFrame,orient=VERTICAL)
        #structure of treeview
        self.my_tree=ttk.Treeview(viewFrame,columns=('Book Title','Author','Genre','Publication Year'),yscrollcommand=self.scroll_y.set)
        self.my_tree['show']='headings'
        
        self.my_tree.heading('Book Title',text="Book Title")
        self.my_tree.heading('Author',text="Author")
        self.my_tree.heading('Genre',text="Genre")
        self.my_tree.heading('Publication Year',text="Publication Year")
        
        self.my_tree.column('Book Title',width=120,anchor=W)
        self.my_tree.column('Author',width=120,anchor= W)
        self.my_tree.column('Genre',width=120,anchor=CENTER)
        self.my_tree.column('Publication Year',width=80,anchor=CENTER)
        
        self.scroll_y.pack(side=LEFT,fill=Y)
        self.scroll_y.config(command=self.my_tree.yview)
       
        try:
        
             with open('library.csv', mode='r') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                for row in csv_reader:
                   self.__ListOfBooks.append(row)

        except FileNotFoundError:
              messagebox.showerror("File Error", "Explanation: The file 'library.csv' is not found!")  
        except Exception as e:
              messagebox.showerror("File Error", f"Explanation: Unable to load the 'library.csv' file. Error: {str(e)}")
        count=0 
        try:
            for book in self.__ListOfBooks:
              if (comboValue == "Title" and book["Title"] == searchValue) or (comboValue == "Author" and book["Author"] == searchValue):
                 self.__list.append(book)
                 count+=1
        except Exception as e:
             messagebox.showerror("Search Error", f"An error occurred during the search: {str(e)}")
          
        if (count==0):
            if comboValue == "Title":
                messagebox.showerror("Input Error", f"The book titled '{searchValue}' was not found!")
            elif comboValue == "Author":
                messagebox.showerror("Input Error", f"No books by author '{searchValue}' were found!")
        else:
            self.Count=0
            for record in self.__list:
              self.my_tree.insert(parent='',index='end',iid=self.Count,values=(record['Title'],record['Author'],record['Genre'],record['Publication Year']))
              self.Count+=1
        self.my_tree.place(x=18,y=1,width=980,height=739)

              
                 
         
            
              
                
              
      def displayBooks(self,viewFrame):
            #scrollbar
        self.scroll_y=Scrollbar(viewFrame,orient=VERTICAL)
        #structure of treeview
        self.my_tree=ttk.Treeview(viewFrame,columns=('Book Title','Author','Genre','Publication Year'),yscrollcommand=self.scroll_y.set)
        self.my_tree['show']='headings'
        
        self.my_tree.heading('Book Title',text="Book Title")
        self.my_tree.heading('Author',text="Author")
        self.my_tree.heading('Genre',text="Genre")
        self.my_tree.heading('Publication Year',text="Publication Year")
        
        self.my_tree.column('Book Title',width=120,anchor=W)
        self.my_tree.column('Author',width=120,anchor= W)
        self.my_tree.column('Genre',width=120,anchor=CENTER)
        self.my_tree.column('Publication Year',width=80,anchor=CENTER)
        
        self.scroll_y.pack(side=LEFT,fill=Y)
        self.scroll_y.config(command=self.my_tree.yview)
        
        try:
        
             with open('library.csv', mode='r') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                for row in csv_reader:
                   self.__ListOfBooks.append(row)

        except FileNotFoundError:
              messagebox.showerror("File Error", "Explanation: The file 'library.csv' is not found!")  
        except Exception as e:
              messagebox.showerror("File Error", f"Explanation: Unable to load the 'library.csv' file. Error: {str(e)}")
        self.count=0
        for record in self.__ListOfBooks:
              self.my_tree.insert(parent='',index='end',iid=self.count,values=(record['Title'],record['Author'],record['Genre'],record['Publication Year']))
              self.count+=1
        self.my_tree.place(x=18,y=1,width=980,height=739)
           
class Windmain:
    def __init__(self,pro):
        self.pro=pro
        self.pro.geometry('1250x780+150+0')
        self.pro.resizable(False,False)
        self.pro.title('Personal Library')
        self.pro.config(background='silver')
        self.title=Label(self.pro,text="Personal Library Management System",bg='#607274',font=("Courier New",25,'bold'),fg='white')
        self.title.pack(fill=X)
        
       
        # frame with labels and entries
        ManageFrame=Frame(self.pro,bg='white')
        ManageFrame.place(x=1000,y=43,width=250,height=400)
        lbl_title=Label(ManageFrame,text="Book Title",bg="white",font=("Consolas",14,'bold'))
        lbl_title.pack()
        self.Entry_title=Entry(ManageFrame,font=( 9), width=15,justify=CENTER)
        self.Entry_title.pack()
        lbl_author=Label(ManageFrame,text="Author",bg="white",font=("Consolas",14,'bold'))
        lbl_author.pack()
        self.Entry_author=Entry(ManageFrame,font=( 9), width=15,justify=CENTER)
        self.Entry_author.pack()
        lbl_genre=Label(ManageFrame,text="Genre",bg="white",font=("Consolas",14,'bold'))
        lbl_genre.pack()
        self.Entry_genre=Entry(ManageFrame,font=( 9), width=15,justify=CENTER)
        self.Entry_genre.pack()
        lbl_publicationYear=Label(ManageFrame,text="Publication Year",bg="white",font=("Consolas",14,'bold'))
        lbl_publicationYear.pack()
        self.Entry_publicationYear=Entry(ManageFrame,font=( 9), width=15,justify=CENTER)
        self.Entry_publicationYear.pack()
        lbl_removeTi=Label(ManageFrame,text="Remove Book (Title)",bg="white",font=("Consolas",14,'bold'),fg="red")
        lbl_removeTi.pack()
        self.Entry_removeTi=Entry(ManageFrame,font=( 12), width=15,justify=CENTER)
        self.Entry_removeTi.pack()
       
        #buttons
        btn_frame=Frame(self.pro,bg="white")
        btn_frame.place(x=1000,y=446,width=250,height=340)
        btn_title=Label(btn_frame,text="Control Panel",bg="#607274",font=("Consolas",14,'bold'),fg='white')
        btn_title.pack(fill=X)
        btAdd=Button(btn_frame,text="Add Book",bg="#1abc9c",font=("Consolas",14,'bold'),command=self.add)
        btAdd.place(x=50,y=44,width=150,height=30)
        btremove=Button(btn_frame,text="Remove Book",bg="#1abc9c",font=("Consolas",14,'bold'),command=self.remove)
        btremove.place(x=50,y=94,width=150,height=30)
        btshow=Button(btn_frame,text="Display Library",bg="#1abc9c",font=("Consolas",14,'bold'),command=self.viewBooks)
        btshow.place(x=42,y=144,width=170,height=30)
        
        

       #search manage
        search_frame=Frame(self.pro,bg="white")
        search_frame.place(x=1,y=43,width=998,height=50)
        lbl_search=Label(search_frame,text="Search For a Book",bg="white")
        lbl_search.place(x=10,y=12)
        self.combo_search=ttk.Combobox(search_frame,justify="left")
        self.combo_search['value']=("Title","Author")
        self.combo_search.place(x=115,y=12)
        self.search_Entry=Entry(search_frame,justify="left",bd='2',font=(5))
        self.search_Entry.place(x=270,y=10)
        searc_button=Button(search_frame,text="Search",bg="#7fa6bc",font=("Consolas",14,'bold'),command=self.search)
        searc_button.place(x=650,y=10,width=170,height=30)

        #view books
        self.view_Frame=Frame(self.pro)
        self.view_Frame.place(x=1,y=95,width=998,height=740)
     
    def add(self):
        #get data
        self.title=self.Entry_title.get()
        self.author=self.Entry_author.get()
        self.genre=self.Entry_genre.get()
        self.publicationYear=self.Entry_publicationYear.get()
        self.library=Library()
        if self.title and self.author and self.genre and self.publicationYear:
            try:
                publicationYear = int(self.publicationYear)  
            except ValueError:
                messagebox.showerror("Input Error", "Publication Year must be a number!")
            self.library.addBook(self.title,self.author, self.genre,publicationYear)
        else:
            messagebox.showerror("Input Error", "All fields must be filled in!")
        
    def remove(self):
        self.bookremove=self.Entry_removeTi.get()
        if(self.bookremove):
            self.library=Library()
            self.library.removeBook(self.bookremove)
        else:
            messagebox.showerror("Input Error", "field remove book is required!")
    def search(self):
       comboValue= self.combo_search.get()
       entryValue=self.search_Entry.get()
       if(comboValue and entryValue):
           self.library=Library()
           self.library.searchBook(comboValue,entryValue,self.view_Frame)

       else:
           raise Exception( messagebox.showerror("Input Error", "All fields must be filled in!"))
    def viewBooks(self):
         self.library=Library()
         self.library.displayBooks(self.view_Frame)

pro=Tk()
win1=Windmain(pro)
pro.mainloop()