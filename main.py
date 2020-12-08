from tkinter import *
from tkinter import ttk


class Student :
	def __init__ ( self , root ) :
		self.root = root
		self.root.title ( "Student management system" )
		self.root.geometry ( "1500x900+0+0" )
		
		title = Label ( self.root , text="Student Management System" , bd=10 , relief=GROOVE ,
		                font=("times new roman" , 40 , "bold") ,
		                bg="yellow" ,
		                fg="red" )
		title.pack ( side=TOP , fill=X )
		
		####################-----------Create Message frame------------###################
		Message_Frame = Frame ( self.root , bd=4 , relief=RIDGE , bg="cyan" )
		Message_Frame.place ( x=10 , y=90 , width=550 , height=630 )
		
		m_title = Label ( Message_Frame , text="Manage Students" , bg="cyan" , font=("times new roman" , 30 , "bold") )
		m_title.grid ( row=0 , columnspan=2 , pady=15 )
		
		############-----------Name Field---------------###########
		lbl_roll = Label ( Message_Frame , text="Roll No." , bg="cyan" , fg="black" ,
		                   font=("times new roman" , 20 , "bold") )
		lbl_roll.grid ( row=1 , column=0 , pady=10 , padx=20 , sticky="s" )
		
		################----------Create Entry Box--------------##############
		txt_roll = Entry ( Message_Frame , font=("times new roman" , 15 , "bold") , bd=5 , relief=GROOVE )
		txt_roll.grid ( row=1 , column=1 , pady=10 , padx=20 )
		
		############-----------Name Field name-----------###########
		lbl_name = Label ( Message_Frame , text="Name" , bg="cyan" , fg="black" ,
		                   font=("times new roman" , 20 , "bold") )
		lbl_name.grid ( row=2 , column=0 , pady=10 , padx=20 , sticky="s" )
		
		################---------------Create Entry Box for Name---------------##############
		txt_name = Entry ( Message_Frame , font=("times new roman" , 15 , "bold") , bd=5 , relief=GROOVE )
		txt_name.grid ( row=2 , column=1 , pady=10 , padx=20 )
		
		############----------------Name Field E-mail------------------###########
		lbl_Email = Label ( Message_Frame , text="Email" , bg="cyan" , fg="black" ,
		                    font=("times new roman" , 20 , "bold") )
		lbl_Email.grid ( row=3 , column=0 , pady=10 , padx=20 , sticky="s" )
		################----------------Create Entry Box for e-mail------------------------##############
		txt_Email = Entry ( Message_Frame , font=("times new roman" , 15 , "bold") , bd=5 , relief=GROOVE )
		txt_Email.grid ( row=3 , column=1 , pady=10 , padx=20 )
		
		############--------GENDER-------###################
		lbl_Gender = Label ( Message_Frame , text="Gender" , bg="cyan" , fg="black" ,
		                     font=("times new roman" , 20 , "bold") )
		lbl_Gender.grid ( row=4 , column=0 , pady=10 , padx=20 , sticky="s" )
		
		############---------------Combo box-------------------################
		combo_gender = ttk.Combobox ( Message_Frame , font=("times new roman" , 14 , "bold") , state="readonly" )
		combo_gender [ 'values' ] = ("male" , "female" , "other")
		combo_gender.grid ( row=4 , column=1 , pady=10 , padx=20 , sticky="w" )
		
		############------------Name Field Contact-------------###########
		lbl_Contact = Label ( Message_Frame , text="Contact" , bg="cyan" , fg="black" ,
		                      font=("times new roman" , 20 , "bold") )
		lbl_Contact.grid ( row=5 , column=0 , pady=10 , padx=20 , sticky="s" )
		################---------Create Entry Box for e-mail---------------##############
		txt_Contact = Entry ( Message_Frame , font=("times new roman" , 15 , "bold") , bd=5 , relief=GROOVE )
		txt_Contact.grid ( row=5 , column=1 , pady=10 , padx=20 )
		
		############------------Name Field DOB-------------###########
		lbl_dob = Label ( Message_Frame , text="D.O.B" , bg="cyan" , fg="black" ,
		                  font=("times new roman" , 20 , "bold") )
		lbl_dob.grid ( row=6 , column=0 , pady=10 , padx=20 , sticky="s" )
		################---------Create Entry Box for DOB ---------------##############
		txt_dob = Entry ( Message_Frame , font=("times new roman" , 15 , "bold") , bd=5 , relief=GROOVE )
		txt_dob.grid ( row=6 , column=1 , pady=10 , padx=20 )
		
		############------------Name Field Address.-------------###########
		lbl_Address = Label ( Message_Frame , text="Address" , bg="cyan" , fg="black" ,
		                      font=("times new roman" , 20 , "bold") )
		lbl_Address.grid ( row=7 , column=0 , pady=45 , padx=2 , sticky="s" )
		################---------Create Entry Box for TEXT ---------------##############
		txt_Address = Text ( Message_Frame , width=26 , height=6 )
		txt_Address.grid ( row=7 , column=1 , pady=10 , padx=20 , sticky="s" )
		###############-------------Create Frame for displaying the Buttons-----------###############
		btn_Frame = Frame ( Message_Frame , bd=5 , relief=RIDGE , bg="cyan" )
		btn_Frame.place ( x=15 , y=560 , width=510 )
		
		########-----------Adding Buttom to our Buttom Frame-------#########
		Add_btn = Button ( btn_Frame , text="Add" , width=10 ).grid ( row=10 , column=0 , padx=22 , pady=10 )
		Update_btn = Button ( btn_Frame , text="Update" , width=10 ).grid ( row=10 , column=1 , padx=22 , pady=10 )
		Delete_btn = Button ( btn_Frame , text="Delete" , width=10 ).grid ( row=10 , column=2 , padx=22 , pady=10 )
		Clear_btn = Button ( btn_Frame , text="Clear" , width=10 ).grid ( row=10 , column=3 , padx=22 , pady=10 )
		
		########-------------Create another frame for displaying the deatil.-----------###############
		Detail_Frame = Frame ( self.root , bd=5 , relief=RIDGE , bg="cyan" )
		Detail_Frame.place ( x=600 , y=90 , width=880 , height=630 )
		
		lbl_search = Label ( Detail_Frame , text="Search by:-" , bg="cyan" , fg="black" ,
		                     font=("times new roman" , 20 , "bold") )
		lbl_search.grid ( row=0 , column=0 , padx=10 , pady=10 , sticky="w" )
		
		combo_search = ttk.Combobox ( Detail_Frame , width=10 , font=("times new roman" , 15 , "bold") ,
		                              state="readonly" )
		combo_search [ 'values' ] = ("Roll no." , "Name" , "Contact")
		combo_search.grid ( row=0 , column=1 , pady=10 , padx=20 , sticky="w" )
		
		#########------------------Create Search Box----------------###########
		txt_search = Entry ( Detail_Frame , width=20 , font=("times new roman" , 15 , "bold") , bd=5 , relief=GROOVE )
		txt_search.grid ( row=0 , column=2 , pady=10 , padx=20 )
		
		# Create Search Button
		search_btn = Button ( Detail_Frame , text="Search" , width=10 ).grid ( row=0 , column=3 , padx=20 , pady=20 )
		search_btn = Button ( Detail_Frame , text="Show All" , width=10 ).grid ( row=0 , column=4 , padx=20 , pady=20 )
		
		###################---------Table Frame---------------#########################
		Table_Frame = Frame ( Detail_Frame , bd=4 , relief=RIDGE , bg="cyan" )
		Table_Frame.place ( x=10 , y=70 , width=787 , height=500 )
		
		scroll_x = Scrollbar ( Table_Frame , orient=HORIZONTAL )
		scroll_y = Scrollbar ( Table_Frame , orient=VERTICAL )
		Student_table = ttk.Treeview ( Table_Frame ,
		                               columns=("roll" , "name" , "email" , "gender" , "contact" , "dob" , "address") ,
		                               xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set )
		scroll_x.pack ( side=BOTTOM , fill=X )
		scroll_y.pack ( side=RIGHT , fill=Y )
		scroll_x.config ( command=Student_table.xview )
		scroll_y.config ( command=Student_table.yview )
		Student_table.heading ( "roll" , text="Roll No." )
		Student_table.heading ( "name" , text="Name" )
		Student_table.heading ( "email" , text="Email" )
		Student_table.heading ( "gender" , text="Gender" )
		Student_table.heading ( "contact" , text="Contact" )
		Student_table.heading ( "dob" , text="D.O.B" )
		Student_table.heading ( "address" , text="Address" )
		
		Student_table [ 'show' ] = 'headings'
		
		Student_table.column ( "roll" , width=100 )
		Student_table.column ( "name" , width=100 )
		Student_table.column ( "email" , width=100 )
		Student_table.column ( "gender" , width=100 )
		Student_table.column ( "contact" , width=100 )
		Student_table.column ( "dob" , width=100 )
		Student_table.column ( "address" , width=150 )
		
		Student_table.pack ( fill=BOTH , expand=1 )


root = Tk ( )
# Create the object of the base class
obj = Student ( root )
root.mainloop ( )