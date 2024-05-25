from tkinter import*
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from pharmacy_bd import PharmacyDB

class PhamacyManagementSystem:
    def __init__(self,display):
            
        self.db = PharmacyDB()
        self.display = display
        self.name_var = tk.StringVar()
        self.manufacturer_var = tk.StringVar()
        self.price_var = tk.DoubleVar()
        self.quantity_var = tk.IntVar()
        self.display=display
        self.display.title("Pharmacy Management System")
        self.display.geometry("1550x800+0+0")
        #veriable
        self.addMed_Name=tk.StringVar()
        self.addCom_Name=tk.StringVar()
        self.addRef_No=tk.StringVar()
        self.addPrice=tk.StringVar()
        self.addGen=tk.StringVar()
        self.addIssue=tk.StringVar()
        self.addExp=tk.StringVar()
        self.addQunt=tk.StringVar()
        self.add_Dosages=tk.StringVar()
        

        lbtitle=Label(self.display,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbtitle.pack(side=TOP,fill=X)
        self.setup_ui()
        
    def setup_ui(self):
        #DataFrame
        DataFrame=Frame(self.display,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("arial",14,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkgreen",font=("arial",14,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)
    #Buttons Frame
        ButtonFrame=Frame(self.display,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)
        #Main Button
        tk.Button(ButtonFrame,text="Add",font=("arial",14,"bold"),fg="white",bg="green",width=10).grid(row=0,column=0)

        #btnUpdateData=Button(ButtonFrame,text="Update",font=("arial",14,"bold"),fg="white",bg="green",width=11)
        #btnUpdateData.grid(row=0,column=1)

        tk.Button(ButtonFrame,text="Delete",font=("arial",14,"bold"),fg="white",bg="red",width=11,command=self.delete_medicine).grid(row=0,column=2)

        """btnResetData=Button(ButtonFrame,text="Reset",font=("arial",14,"bold"),fg="white",bg="green",width=11)
        btnResetData.grid(row=0,column=3)

        btnExitData=Button(ButtonFrame,text="Exit",font=("arial",14,"bold"),fg="white",bg="red",width=11)
        btnExitData.grid(row=0,column=4)"""

#Search By
        lblSearch=Label(ButtonFrame,text="Search By",font=("arial",17,"bold"),padx=2,fg="white",bg="green")
        lblSearch.grid(row=0,column=5,sticky=W)
        
        search_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",14,"bold"),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
        
        textSearch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("arial",14,"bold"))
        textSearch.grid(row=0,column=7)

        btnSearchData=Button(ButtonFrame,text="Search",font=("arial",14,"bold"),fg="white",bg="green",width=13)
        btnSearchData.grid(row=0,column=8)

        btnShowData=Button(ButtonFrame,text="Show All",font=("arial",14,"bold"),fg="white",bg="red",width=13)
        btnShowData.grid(row=0,column=9)

#Label And Entry
        frame=tk.Frame(self.display)
        tk.Label(DataFrameLeft,text="Reference No:",font=("arial",14,"bold"),fg="Blue",padx=2).grid(row=0, column=0)
        tk.Entry(DataFrameLeft,width=50,textvariable=self.addRef_No).grid(row=0,column=1,sticky=W)
#Company
        tk.Label(DataFrameLeft,text="Company Name:",font=("arial",14,"bold"),padx=2,fg="Blue").grid(row=1,column=0)
        tk.Entry(DataFrameLeft,width=50,textvariable=self.addCom_Name).grid(row=1,column=1,sticky=W)
        #Type of Medicine

        tk.Label(DataFrameLeft,text="Dosage Form:",font=("arial",14,"bold"),padx=2,fg="Blue").grid(row=2,column=0)
        tk.Entry(DataFrameLeft,width=50,textvariable=self.add_Dosages).grid(row=2,column=1,sticky=W)

        """type_combo=ttk.Combobox(DataFrameLeft,width=25,font=("arial",14,"bold"),state="readonly")
        type_combo["values"]=("Tablet","Capsul","Suspention","Syrup","Suppository")
        type_combo.grid(row=2,column=1)
        type_combo.current(0)"""
        #Medicine
        tk.Label(DataFrameLeft,text="Medicine Name:",font=("arial",14,"bold"),padx=2,fg="Blue").grid(row=3,column=0)
        tk.Entry(DataFrameLeft,width=50,textvariable=self.addMed_Name).grid(row=3,column=1,sticky=W)
        """mediName_combo=ttk.Combobox(DataFrameLeft,width=25,font=("arial",14,"bold"),state="readonly")
        mediName_combo["values"]=("Sergel","Omidon","Turbocef","Ace","Napa Extra")
        mediName_combo.grid(row=3,column=1)
        mediName_combo.current(0) """
        #Generic Name
        tk.Label(DataFrameLeft,text="Generic Name:",font=("arial",14,"bold"),padx=2,fg="Blue").grid(row=4,column=0)
        tk.Entry(DataFrameLeft,width=50,textvariable=self.addGen).grid(row=4,column=1,sticky=W)
        """textExp=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=26,font=("arial",14,"bold"))
        textExp.grid(row=4,column=1)"""

        #Date
        tk.Label(DataFrameLeft,text="Expiry Date",font=("arial",14,"bold"),padx=2,fg="Blue").grid(row=5,column=0)
        tk.Entry(DataFrameLeft,width=50,textvariable=self.addExp).grid(row=5,column=1,sticky=W)

        """textIssuDate=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=26,font=("arial",14,"bold"))
        textIssuDate.grid(row=5,column=1)"""
        #Exper Date
        tk.Label(DataFrameLeft,text="Total Quantity",font=("arial",14,"bold"),padx=2,fg="Blue").grid(row=6,column=0)
        tk.Entry(DataFrameLeft,width=50,textvariable=self.addQunt).grid(row=6,column=1,sticky=W)

        #textExp=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=26,font=("arial",14,"bold"))
        #textExp.grid(row=6,column=1)
        #price
        tk.Label(DataFrameLeft,text="Price",font=("arial",14,"bold"),padx=2,fg="Blue").grid(row=7,column=0)
        tk.Entry(DataFrameLeft,width=50,textvariable=self.addPrice).grid(row=7,column=1,sticky=W)

        #textPrice=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=26,font=("arial",14,"bold"))
       # textPrice.grid(row=7,column=1)
        #Product Qunatity
        """tk.Label(DataFrameLeft,text="Balance Quantity",font=("arial",14,"bold"),padx=2,fg="Blue")
        tk.Entry(DataFrameLeft,width=50,textvariable=self.addCom_Name).grid(row=8,column=0,sticky=W)

        textPQ=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=26,font=("arial",14,"bold"))
        textPQ.grid(row=8,column=1)

        lblRefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=15,pady=6)"""
#-----------------------------------------------------------------------
        tk.Label(DataFrameRight,text="Refarence No:",font=("arial",14,"bold"),padx=2,fg="Blue").grid(row=0,column=0)
        tk.Entry(DataFrameRight,width=50,textvariable=self.addCom_Name).grid(row=0,column=1,sticky=W)
        """textrefNo=Entry(DataFrameRight,bd=3,textvariable=self.addRef_No,relief=RIDGE,width=26,font=("arial",14,"bold"))
        textrefNo.place(x=155,y=0)"""
        
        tk.Label(DataFrameRight,text="Medicine Name:",font=("arial",14,"bold"),padx=2,fg="Blue").grid(row=1,column=0)
        tk.Entry(DataFrameRight,width=50,textvariable=self.addMed_Name).grid(row=1,column=1,sticky=W)
        """textrefNo=Entry(DataFrameRight,bd=3,textvariable=self.addMed_Name,relief=RIDGE,width=26,font=("arial",14,"bold"))
        textrefNo.place(x=155,y=30)"""
        
        #side Frame
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=120,width=290,height=160)
        
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        
        self.medicine_table=ttk.Treeview(side_frame,columns=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.xview)
        
        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")
        
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)
        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)
        
        #medicine add button
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=350,y=130,width=135,height=180)
        
        btnAddData=Button(down_frame,text="ADD",font=("arial",14,"bold"),fg="white",bg="green",width=10,pady=4,command=self.add_medicine)
        btnAddData.grid(row=0,column=0)
        btnUpdateData=Button(down_frame,text="UPDATE",font=("arial",14,"bold"),fg="white",bg="green",width=10,pady=4)
        btnUpdateData.grid(row=1,column=0)
        btnDeleteData=Button(down_frame,text="DELETE",font=("arial",14,"bold"),fg="white",bg="red",width=10,pady=4,command=self.delete_medicine)
        btnDeleteData.grid(row=2,column=0)
        btnClearData=Button(down_frame,text="CLEAR",font=("arial",14,"bold"),fg="white",bg="red",width=10,pady=4)
        btnClearData.grid(row=3,column=0)
#=================Frame Details
        Framedetails=Frame(self.display,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1530,height=210)
        
        #Main Table & Scrollbar
        table_frame=Frame(Framedetails,bd=15,relief=RIDGE,padx=20)
        table_frame.place(x=0,y=1,width=1500,height=180)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.pharmacy_table=ttk.Treeview(table_frame,columns=("ref","companyname","type","tabletname","lotno","issuedate","expdate","price","productqt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        
        self.pharmacy_table["show"]="headings"
        """
        self.pharmacy_table.heading("ref",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Medicine Name")
        self.pharmacy_table.heading("lotno",text="Generic Name")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Quantity")
        ##self.pharmacy_table.pack(fill=BOTH,expand=1)
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)"""
        self.pharmacy_table = ttk.Treeview(table_frame, columns=('ID','Manufacturer', 'Dosages','Name', 'Generic Name','Exp Date', 'Price', 'Quantity'), show='headings')
        self.pharmacy_table.heading('ID', text='ID')
        self.pharmacy_table.heading('Manufacturer', text='Manufacturer')
        self.pharmacy_table.heading('Dosages', text='Dosages')
        self.pharmacy_table.heading('Name', text='Name')
        self.pharmacy_table.heading('Generic Name', text='Generic Name')
        self.pharmacy_table.heading('Exp Date', text='Exp Date')
        self.pharmacy_table.heading('Price', text='Price')
        self.pharmacy_table.heading('Quantity', text='Quantity')
        self.pharmacy_table.pack(fill=BOTH)
        
        self.pharmacy_table.column('ID',width=100)
        self.pharmacy_table.column('Manufacturer',width=100)
        self.pharmacy_table.column('Dosages',width=100)
        self.pharmacy_table.column('Name',width=100)
        self.pharmacy_table.column('Generic Name',width=100)
        self.pharmacy_table.column('Exp Date',width=100)
        self.pharmacy_table.column('Price',width=100)
        self.pharmacy_table.column('Quantity',width=100)
        
        
        #Add medicine
    def add_medicine(self):
        name = self.addMed_Name.get()
        generic_name = self.addGen.get()
        manufacturer = self.addCom_Name.get()
        price = self.addPrice.get()
        quantity = self.addQunt.get()
        exp=self.addExp.get()
        dosages=self.add_Dosages
        self.db.add_medicine(manufacturer,dosages,name, generic_name,exp, price, quantity)
        messagebox.showinfo('Success', 'Medicine added successfully')
        self.view_medicines()
        
    def view_medicines(self):
        records = self.pharmacy_table.get_children()
        for record in records:
            self.pharmacy_table.delete(record)
        
        medicines = self.db.fetch_medicines()
        for med in medicines:
            self.pharmacy_table.insert('', 'end', values=med)
            
    def delete_medicine(self):
        selected_item = self.pharmacy_table.selection()
        if selected_item:
            item_id = self.pharmacy_table.item(selected_item)['values'][0]
            self.db.delete_medicine(item_id)
            messagebox.showinfo('Success', 'Medicine deleted successfully')
            self.view_medicines()
        else:
            messagebox.showwarning('Error', 'Please select a medicine to delete')

        
if __name__ == "__main__":
    display=tk.Tk()
    app=PhamacyManagementSystem(display)
    display.mainloop()