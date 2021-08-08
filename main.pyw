from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database_module as db_module
import class_customers as customer_class

#========================================================================
#Uncomment one of the 3 sets of variable declarations to change the theme

#########
#THEME 1#
#########
# label_color = "DarkOrange3"        #Title labels (name, surname, email...)
# global_background_color = "tan2"   #Background
# global_customers_color = "sienna3" #Data cells

#########
#THEME 2#
#########
label_color = "cyan3"
global_background_color = "DarkBlue"
global_customers_color = "cyan2"

#########
#THEME 3#
#########
# label_color = "green2"
# global_background_color = "SeaGreen2"
# global_customers_color = "green3"
#=======================================================================



root = Tk()
root.title("Enterprise Database")
#root.iconbitmap("C:\\users\\...") #Specify a .ico file to set as the window icon (use \\ instead of \)
root.config(bg=global_background_color, bd=25, relief="sunken") 

#Window Size
WindWidth = root.winfo_screenwidth()
WindHeight = root.winfo_screenheight()

#Make the Screen Schrollable
# Create A Main Frame
main_frame = Frame(root,bg=global_background_color,bd = 0)
main_frame.grid(row = 0, column = 1, ipadx = WindWidth/5, ipady = WindHeight/5)
# Create A Canvas
my_canvas = Canvas(main_frame,bg=global_background_color,bd = 0)
my_canvas.grid(row = 0, column = 0,ipadx = WindWidth/3, ipady=WindHeight/3.5)
# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.grid(row = 0, column = 10, ipady = 200)
# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas,bg=global_background_color,bd = 0)
# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

#Adding customers window
def add_customer():
    top = Toplevel()
    frame = Frame(top)
    frame.grid(row = 0,column = 0)
    frame.config(bg=global_background_color,bd=25,relief="sunken") 
    #Widgets 
    name_Entry = Entry(frame, width=30)
    name_Entry.grid(row = 0, column= 1, padx = 20,pady = 4)

    surname_Entry = Entry(frame, width=30)
    surname_Entry.grid(row = 1, column= 1, padx = 20,pady = 4)

    dni_Entry = Entry(frame, width=30)
    dni_Entry.grid(row = 2, column= 1, padx = 20,pady = 4)

    email_Entry = Entry(frame, width=30)
    email_Entry.grid(row = 3, column= 1, padx = 20,pady = 4)

    phone_Entry = Entry(frame, width=30)
    phone_Entry.grid(row = 4, column= 1, padx = 20,pady = 4)

    #Labels
    name_Label = Label(frame, text="Name").grid(row = 0, column= 0)
    surname_Label = Label(frame, text="Surname").grid(row = 1, column= 0)
    dni_Label = Label(frame, text="DNI").grid(row = 2, column= 0)
    email_Label = Label(frame, text="Email").grid(row = 3, column= 0)
    phone_Label = Label(frame, text="Phone Number").grid(row = 4, column= 0)

    def save_customer():
        db_module. add_customer(name_Entry.get(),surname_Entry.get(),dni_Entry.get(),email_Entry.get(),phone_Entry.get())
        name_Entry.delete(0,END)
        surname_Entry.delete(0,END)
        dni_Entry.delete(0,END)
        email_Entry.delete(0,END)
        phone_Entry.delete(0,END)
    #Save Button
    submit = Button(frame, text= "Save Customer", command=save_customer).grid(row=5, column=1,pady=10, padx=10, ipadx=100)

def delete_customer():
    top2 = Toplevel()
    frame2 = Frame(top2)
    frame2.config(bg=global_background_color,bd=25,relief="sunken") 
    frame2.grid(row = 0,column = 0)   

    id_Entry = Entry(frame2, width=30)
    id_Entry.grid(row = 0, column= 1, padx = 20)

    id_Label = Label(frame2, text="Type the customer to delete: ")
    id_Label.grid(row = 0, column= 0)
    
    def delete_customer_database():
        db_module.delete_by_ID(id_Entry.get())
        id_Entry.delete(0,END)
    #Delete Customers
    submit = Button(frame2, text= "Delete Customer", command=delete_customer_database).grid(row=2, column=0,pady=10, padx=10, ipadx=100)

def search_name():
    global search_entry
    top3 = Toplevel()
    frame3 = Frame(top3)
    frame3.grid(row = 0,column = 0)
    frame3.config(bg=global_background_color,bd=25,relief="sunken") 
     
    search_entry = Entry(frame3)
    search_entry.grid(row = 0, column = 1)

    search_label = Label(frame3, text="Enter customer to select")
    search_label.grid(row= 0, column = 0)

    def find_element():
        global search_entry
        list_of_results = db_module.find_by_name(search_entry.get())
        row_value = 1
        for item in list_of_results:
            label = Label(frame3, text = item).grid(row = row_value,column = 3,pady= 5)
            row_value+= 1

    search_button = Button(frame3, text="Search", command = find_element).grid(row = 0, column = 3)

def search_DNI():
    global entry2
    top4 = Toplevel()
    frame4 = Frame(top4)
    frame4.grid(row = 0,column = 0)
    frame4.config(bg=global_background_color,bd=25,relief="sunken")

    entry2 = Entry(frame4)
    entry2.grid(row = 0, column = 1)

    search_label2 = Label(frame4, text="Enter customer to select")
    search_label2.grid(row= 0, column = 0)
    
    def search_DNI_database():
        global entry2
        list_of_results = db_module.find_by_DNI(entry2.get())
        row_value = 1
        for item in list_of_results:
            label = Label(frame4, text = item).grid(row = row_value,column = 3,pady= 5)
            row_value+= 1

    button_search_DNI = Button(frame4, text="Search", command = search_DNI_database).grid(row = 0, column = 3)

def edit_customer():
    global name_Entry, surname_Entry, dni_Entry, email_Entry, phone_Entry, enter_ID
    top5 = Toplevel()
    frame5 = Frame(top5)
    frame5.grid(row = 0,column = 0)
    frame5.config(bg=global_background_color,bd=25,relief="sunken")     
    
    enter_ID= Entry(frame5, width=20)
    enter_ID.grid(row = 0, column =1,pady = 10)

    name_Entry = Entry(frame5, width=30)
    name_Entry.grid(row = 1, column= 1, padx = 20)

    surname_Entry = Entry(frame5, width=30)
    surname_Entry.grid(row = 2, column= 1, padx = 20)

    dni_Entry = Entry(frame5, width=30)
    dni_Entry.grid(row = 3, column= 1, padx = 20)

    email_Entry = Entry(frame5, width=30)
    email_Entry.grid(row = 4, column= 1, padx = 20)

    phone_Entry = Entry(frame5, width=30)
    phone_Entry.grid(row = 5, column= 1, padx = 20)


    def setValuesOnEntrys():
        global name_Entry, surname_Entry, dni_Entry, email_Entry, phone_Entry
        name_Entry.delete(0,END)
        surname_Entry.delete(0,END)
        dni_Entry.delete(0,END)
        email_Entry.delete(0,END)
        phone_Entry.delete(0,END)
        try:
            db_list.clear()
        except:
            pass
        db_list = db_module.find_by_ID(enter_ID.get())
        
        if db_list != []:
            name_Entry.insert(END, db_list[1])
            surname_Entry.insert(END, db_list[2])
            dni_Entry.insert(END, db_list[3])
            email_Entry.insert(END, db_list[4])
            phone_Entry.insert(END, db_list[5])
        else:
            messagebox.showwarning(message="Customer not found", title="ERROR")

    def save_edit():
        global name_Entry, surname_Entry, dni_Entry, email_Entry, phone_Entry,enter_ID
        try:
            db_module.delete_by_ID(enter_ID.get())
            #print(name_Entry.get(),surname_Entry.get(),dni_Entry.get(),email_Entry.get(),phone_Entry.get())
            db_module. add_customer(name_Entry.get(),surname_Entry.get(),dni_Entry.get(),email_Entry.get(),phone_Entry.get())
        except:
            messagebox.showwarning(message="Enter the selecter customer in the search entry", title="ERROR")
        finally:
            name_Entry.delete(0,END)
            surname_Entry.delete(0,END)
            dni_Entry.delete(0,END)
            email_Entry.delete(0,END)
            phone_Entry.delete(0,END)


    #Labels
    
    enter_ID_button = Button(frame5, text = "Search",command = setValuesOnEntrys).grid(row = 0,column = 0,pady = 10)
    name_Label = Label(frame5, text="Name").grid(row = 1, column= 0)
    surname_Label = Label(frame5, text="Surname").grid(row = 2, column= 0)
    dni_Label = Label(frame5, text="DNI").grid(row = 3, column= 0)
    email_Label = Label(frame5, text="Email").grid(row = 4, column= 0)
    phone_Label = Label(frame5, text="Phone number").grid(row =5, column= 0)
    save_button = Button(frame5, text = "Save",command = save_edit).grid(row = 6, column = 1)

def sort_name():
    global row_position, column_position, sort
    sort = "name"
    row_position = 2
    column_position = 1
    db_dump_setup()
    customers_table()

def sort_num():
    global row_position,column_position,sort
    row_position = 2
    column_position = 1
    sort="number"
    db_dump_setup()
    customers_table()

def exit_funct():
    root.quit()

#Dropdown Menus
my_menu = Menu(root)
root.config(menu = my_menu)

#Sort Menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="Sort by:", menu=file_menu)
file_menu.add_command(label = "Name", command = sort_name)
file_menu.add_separator()
file_menu.add_command(label= "Customer ID", command =sort_num)

#Customers Menu
add_menu = Menu(my_menu)
my_menu.add_cascade(label="Customers", menu = add_menu)
add_menu.add_command(label="Add Customer", command=add_customer)
add_menu.add_separator()
add_menu.add_command(label="Delete Customer", command=delete_customer)
add_menu.add_separator()
add_menu.add_command(label="Edit Customer", command=edit_customer)
add_menu.add_separator()

#Search Menu
find_menu = Menu(my_menu)
my_menu.add_cascade(label = "Search by:", menu = find_menu)
find_menu.add_command(label="Name", command=search_name)
find_menu.add_separator()
find_menu.add_command(label="DNI", command=search_DNI)

#Dropdown Menu exit
exit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Exit",menu = exit_menu)
exit_menu.add_command(label="Exit",command = exit_funct)

#Title Labels
num_label = Label(second_frame, text = "Customer ID",bg = label_color,bd = 5, relief="sunken",font=("FreeSans"))
num_label.grid(row = 1, column=1, ipadx = (WindWidth/5)*0.25)

name_label = Label(second_frame, text = "Name",bg = label_color,bd = 5, relief="sunken",font=("FreeSans"))
name_label.grid(row = 1, column=2, ipadx = (WindWidth/5)*0.25)

surname_label = Label(second_frame, text = "Surname",bg = label_color,bd = 5, relief="sunken",font=("FreeSans"))
surname_label.grid(row = 1, column=3, ipadx = (WindWidth/5)*0.25)

dni_label = Label(second_frame, text = "DNI",bg = label_color,bd = 5, relief="sunken",font=("FreeSans"))
dni_label.grid(row = 1, column=4, ipadx =(WindWidth/5)*0.25)

correo_label = Label(second_frame, text = "Email",bg = label_color,bd = 5, relief="sunken",font=("FreeSans"))
correo_label.grid(row = 1, column=5, ipadx = (WindWidth/5)*0.25)

phone_label = Label(second_frame, text = "Phone Number",bg = label_color,bd = 5, relief="sunken",font=("FreeSans"))
phone_label.grid(row = 1, column=6, ipadx = (WindWidth/5)*0.25)

sort="number"
row_position = 2
column_position = 1
def db_dump_setup():
    global db_dump,sort
    try:
        if sort == "number":
            db_dump =db_module.sort_by_ID()
        elif sort=="name":
            db_dump =db_module.sort_by_name()
    except:
        db_dump =db_module.show_clients()
        print(f"Error while sorting by {sort}")

def customers_table():
    global row_position,column_position
    for item in db_dump:
        #Customer ID
        customer_label = Label(second_frame, text=item[0],width =15,height = 2,bg = global_customers_color,font=("FreeSans"))
        customer_label.grid(row = row_position, column = column_position,padx = 5, pady= 5)
        #Name
        customer_label = Label(second_frame, text=item[1],width =15,height = 2,bg = global_customers_color,font=("FreeSans"))
        customer_label.grid(row = row_position, column = column_position+1,padx = 5, pady= 5)
        #Surname
        customer_label = Label(second_frame, text=item[2],width = 15,height = 2,bg = global_customers_color,font=("FreeSans"))
        customer_label.grid(row = row_position, column = column_position+2,padx = 5, pady= 5)
        #DNI
        customer_label = Label(second_frame, text=item[3],width =15,height = 2,bg = global_customers_color,font=("FreeSans"))
        customer_label.grid(row = row_position, column = column_position+3,padx = 5, pady= 5)
        #Email
        customer_label = Label(second_frame, text=item[4],width =15,height = 2,bg = global_customers_color,font=("FreeSans"))
        customer_label.grid(row = row_position, column = column_position+4,padx = 5, pady= 5)
        #Phone Number
        customer_label = Label(second_frame, text=item[5],width =15,height = 2,bg = global_customers_color,font=("FreeSans"))
        customer_label.grid(row = row_position, column = column_position+5,padx = 5, pady= 5)
        row_position += 1

#Start the db 
db_dump_setup()
customers_table()



root.mainloop()