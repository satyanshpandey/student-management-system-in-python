from distutils import command
from tkinter import *


class Bill_App :
	def __init__ ( self , root ) :
		self.root = root
		self.root.geometry ( "1480x800+0+0" )
		self.root.title ( "Billing Softwere" )
		bg_color = "#074463"
		title = Label ( self.root , text="Billing Softwere" , bd=12 , relief=GROOVE , bg=bg_color , fg="white" ,
		                font=("times new roman" , 30 , "bold") , pady=2 ).pack ( fill=X )
		
		# Customer detail frame
		F1 = LabelFrame ( self.root , bd=10 , relief=GROOVE , text="Customer Details" ,
		                  font=("times new roman" , 15 , "bold") ,
		                  fg="gold" , bg=bg_color )
		F1.place ( x=0 , y=80 , relwidth=1 )
		
		cname_lbl = Label ( F1 , text="Customer Name" , bg=bg_color , fg="white" ,
		                    font=("times new roman" , 18 , "bold") ).grid (
			row=0 , column=0 , padx=20 , pady=5 )
		cname_txt = Entry ( F1 , width=20 , font="arial 15" , bd=7 , relief=SUNKEN ).grid ( row=0 , column=1 , pady=5 ,
		                                                                                    padx=10 )
		
		cphn_lbl = Label ( F1 , text="Phone No." , bg=bg_color , fg="white" ,
		                   font=("times new roman" , 18 , "bold") ).grid (
			row=0 , column=2 , padx=20 , pady=5 )
		cphn_txt = Entry ( F1 , width=20 , font="arial 15" , bd=7 , relief=SUNKEN ).grid ( row=0 , column=3 , pady=5 ,
		                                                                                   padx=10 )
		
		c_bill_lbl = Label ( F1 , text="Bill Number" , bg=bg_color , fg="white" ,
		                     font=("times new roman" , 18 , "bold") ).grid (
			row=0 , column=4 , padx=20 , pady=5 )
		c_bill_lbl = Entry ( F1 , width=20 , font="arial 15" , bd=7 , relief=SUNKEN ).grid ( row=0 , column=5 , pady=5 ,
		                                                                                     padx=10 )
		# print
		bill_btn = Button ( F1 , text="Search" , width=10 , bd=7 , font="arial 12 bold" ).grid ( row=0 , column=6 ,
		                                                                                         padx=10 , pady=10 )
		
		##########Cosmetics Frame###########################
		F2 = LabelFrame ( self.root , bd=10 , relief=GROOVE , text="Cosmetic" , font=("times new roman" , 15 , "bold") ,
		                  fg="gold" , bg=bg_color )
		F2.place ( x=5 , y=180 , width=330 , height=380 )
		
		bath_lbl = Label ( F2 , text="Bath Soap" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                   fg="lightgreen" ).grid ( row=0 , column=0 , padx=10 , pady=10 )
		bath_txt = Entry ( F2 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=0 , column=1 , padx=10 , pady=10 )
		
		Face_cream_lbl = Label ( F2 , text="Face Cream" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                         fg="lightgreen" ).grid ( row=1 , column=0 , padx=10 , pady=10 )
		Face_cream_txt = Entry ( F2 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=1 , column=1 ,
			padx=10 , pady=10 )
		
		Face_w_lbl = Label ( F2 , text="Face Wash" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                     fg="lightgreen" ).grid (
			row=2 , column=0 , padx=10 , pady=10 )
		Face_w_txt = Entry ( F2 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=2 , column=1 ,
			padx=10 , pady=10 )
		
		Hair_s_lbl = Label ( F2 , text="Hair Soap" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                     fg="lightgreen" ).grid (
			row=3 , column=0 , padx=10 , pady=10 )
		Hair_s_txt = Entry ( F2 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=3 , column=1 ,
			padx=10 , pady=10 )
		
		Hair_g_lbl = Label ( F2 , text="Hair Gell" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                     fg="lightgreen" ).grid (
			row=4 , column=0 , padx=10 , pady=10 )
		Hair_g_txt = Entry ( F2 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=4 , column=1 ,
			padx=10 , pady=10 )
		
		Body_lbl = Label ( F2 , text="Body Loshan" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                   fg="lightgreen" ).grid (
			row=5 , column=0 , padx=10 , pady=10 )
		Body_txt = Entry ( F2 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=5 , column=1 , padx=10 ,
			pady=10 )
		
		#   #########Grocesary Frame###########################
		F3 = LabelFrame ( self.root , bd=10 , relief=GROOVE , text="Grocesary" , font=("times new roman" , 15 ,
		                                                                               "bold") ,
		                  fg="gold" , bg=bg_color )
		F3.place ( x=370 , y=180 , width=330 , height=380 )
		
		g1_lbl = Label ( F3 , text="Rice" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid ( row=0 , column=0 , padx=10 , pady=10 )
		g1_txt = Entry ( F3 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=0 , column=1 , padx=10 , pady=10 )
		
		g2_lbl = Label ( F3 , text="Food oil" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid ( row=1 , column=0 , padx=10 , pady=10 )
		g2_txt = Entry ( F3 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=1 , column=1 ,
			padx=10 , pady=10 )
		
		g3_lbl = Label ( F3 , text="Daal" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid (
			row=2 , column=0 , padx=10 , pady=10 )
		g3_txt = Entry ( F3 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=2 , column=1 ,
			padx=10 , pady=10 )
		
		g4_lbl = Label ( F3 , text="Wheat" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid (
			row=3 , column=0 , padx=10 , pady=10 )
		g4_txt = Entry ( F3 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=3 , column=1 ,
			padx=10 , pady=10 )
		
		g5_lbl = Label ( F3 , text="Sugar" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid (
			row=4 , column=0 , padx=10 , pady=10 )
		g5_txt = Entry ( F3 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=4 , column=1 ,
			padx=10 , pady=10 )
		
		g6_lbl = Label ( F3 , text="Tea" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid (
			row=5 , column=0 , padx=10 , pady=10 )
		g6_txt = Entry ( F3 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=5 , column=1 , padx=10 ,
			pady=10 )
		
		#   #########cold drink frame###########################
		F4 = LabelFrame ( self.root , bd=10 , relief=GROOVE , text="Cold Drinks" , font=("times new roman" , 15 ,
		                                                                                 "bold") ,
		                  fg="gold" , bg=bg_color )
		F4.place ( x=735 , y=180 , width=330 , height=380 )
		
		c1_lbl = Label ( F4 , text="Maza" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid ( row=0 , column=0 , padx=10 , pady=10 )
		c1_txt = Entry ( F4 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=0 , column=1 , padx=10 , pady=10 )
		
		c2_lbl = Label ( F4 , text="Cock" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid ( row=1 , column=0 , padx=10 , pady=10 )
		c2_txt = Entry ( F4 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=1 , column=1 ,
			padx=10 , pady=10 )
		
		c3_lbl = Label ( F4 , text="Frooti" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid (
			row=2 , column=0 , padx=10 , pady=10 )
		c3_txt = Entry ( F4 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=2 , column=1 ,
			padx=10 , pady=10 )
		
		c4_lbl = Label ( F4 , text="Thumbs Up" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid (
			row=3 , column=0 , padx=10 , pady=10 )
		c4_txt = Entry ( F4 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=3 , column=1 ,
			padx=10 , pady=10 )
		
		c5_lbl = Label ( F4 , text="Limca" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid (
			row=4 , column=0 , padx=10 , pady=10 )
		c5_txt = Entry ( F4 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=4 , column=1 ,
			padx=10 , pady=10 )
		
		c6_lbl = Label ( F4 , text="Sprite" , font=("times new roman" , 16 , "bold") , bg=bg_color ,
		                 fg="lightgreen" ).grid (
			row=5 , column=0 , padx=10 , pady=10 )
		c6_txt = Entry ( F4 , width=10 , font=("times new roman" , 16 , "bold") , bd=5 , relief=SUNKEN ).grid (
			row=5 , column=1 , padx=10 ,
			pady=10 )
		
		#######################--------BILL--AREA----------##############################
		F5 = Frame ( self.root , bd=10 , relief=GROOVE )
		F5.place ( x=1090 , y=180 , width=375 , height=380 )
		bill_title = Label ( F5 , text="Bill Area" , font="arial 15 bold" , bd=7 , relief=GROOVE ).pack ( fill=X )
		scrol_y = Scrollbar ( F5 , orient=VERTICAL )
		self.txtarea = Text ( F5 , yscrollcommand=scrol_y.set )
		scrol_y.pack ( side=RIGHT , fill=Y )
		scrol_y.config ( command=self.txtarea.yview )
		self.txtarea.pack ( fill=BOTH , expand=1 )
		
		#########################---BUTTON--FRAME----###################
		F6 = LabelFrame ( self.root , bd=10 , relief=GROOVE , text="Bill Menu" ,
		                  font=("times new roman" , 15 , "bold") , fg="gold" ,
		                  bg=bg_color )
		F6.place ( x=0 , y=560 , relwidth=1 , height=140 )

		m1_lbl = Label ( F6 , text="Total Cosmetic Price" , bg=bg_color , fg="lightgreen" ,
		                 font=("times new roman" , 14 ,
		                       "bold") ).grid ( row=0 ,
		                                        column=0 ,
		                                        padx=20 ,
		                                        pady=1 , sticky="w" )
		m1_txt = Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)


		m2_lbl = Label ( F6 , text="Total Grocesary Price" , bg=bg_color , fg="lightgreen" ,
		                 font=("times new roman" , 14 ,
		                       "bold") ).grid ( row=1 ,
		                                        column=0 ,
		                                        padx=20 ,
		                                        pady=1 , sticky="w" )
		m2_txt = Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)


		m3_lbl = Label ( F6 , text="Total Cold Price" , bg=bg_color , fg="lightgreen" ,
		                 font=("times new roman" , 14 ,
		                       "bold") ).grid ( row=2 ,
		                                        column=0 ,
		                                        padx=20 ,
		                                        pady=1 , sticky="w" )
		m3_txt = Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)









		c1_lbl = Label ( F6 , text="Cosmetic Tax" , bg=bg_color , fg="lightgreen" ,
		                 font=("times new roman" , 14 ,
		                       "bold") ).grid ( row=0 ,
		                                        column=2 ,
		                                        padx=20 ,
		                                        pady=1 , sticky="w" )
		c1_txt = Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)


		c2_lbl = Label ( F6 , text="Grocesary Tax" , bg=bg_color , fg="lightgreen" ,
		                 font=("times new roman" , 14 ,
		                       "bold") ).grid ( row=1 ,
		                                        column=2 ,
		                                        padx=20 ,
		                                        pady=1 , sticky="w" )
		c2_txt = Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)


		c3_lbl = Label ( F6 , text="Cold Drinks Tax" , bg=bg_color , fg="lightgreen" ,
		                 font=("times new roman" , 14 ,
		                       "bold") ).grid ( row=2 ,
		                                        column=2,
		                                        padx=20 ,
		                                        pady=1 , sticky="w" )
		c3_txt = Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)



###########___________Button__________#############################
		btn_F = Frame(F6,bd=7,relief=GROOVE)
		btn_F.place(x=750,width=695,height=105)
	
		total_btn = Button ( btn_F , text="Total" , bg="cadetblue" , fg="white", bd=2 , pady=15 , width=12 ,
		                     font="arial 15 bold").grid (row=0 , column=0 , padx=5 , pady=5 )
		
		GBill_btn = Button ( btn_F , text="Generate Bill" , bg="cadetblue" , fg="white" , bd=2 , pady=15 , width=12 ,
		                     font="arial 15 bold" ).grid ( row=0 , column=1 , padx=5 , pady=5 )
		
		Clear_btn  = Button ( btn_F , text="Clear" , bg="cadetblue" , fg="white" , bd=2 , pady=15 , width=12 ,
		                     font="arial 15 bold" ).grid ( row=0 , column=2 , padx=5 , pady=5 )
	
		Exit_btn = Button ( btn_F , text="Exit" , bg="cadetblue" , fg="white" , bd=2 , pady=15 , width=13 ,
	                     font="arial 15 bold" ).grid ( row=0 , column=3 , padx=5 , pady=5 )


root = Tk ( )
obj = Bill_App ( root )
root.mainloop ( )