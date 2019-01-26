"""------------------------------------ Project Made By Vijay Sehgal-----------------------------------------------"""

from tkinter import *

import random

import time

from tkinter import messagebox

root = Tk()

root.geometry("1200x700+0+0")       # Geometric measurement of the system created

root.title("Restaurant Management System")      # Title is set

root.configure(background='gray')


Tops = Frame(root, width=1250, height=90, bd=12, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=750, height=750, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=950, bd=9, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width=900, height=330, bd=6, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width=850, height=520, bd=6, relief="raise")
f2a.pack(fill=BOTH, side=BOTTOM)

ft2 = Frame(f2, width=440, height=450, bd=12, relief="raise")
ft2.pack(side=TOP)

fb2 = Frame(f2, width=440, height=750, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)

f1ab = Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

# ============================ Configuration set background black ==================================================

Tops.configure(background='white')
f1.configure(background='white')
f2.configure(background='white')

# =========================================== Label Set on Top to Restaurant MS =================================

lblInfo = Label(Tops, font=('arial', 64, 'bold'), text="Restaurant Management System", bd=9)
lblInfo.grid(row=0, column=0)

# ============================================== Methods Declaration ================================================


# ======================================================== Cost of Items ====================================

def CostofItems():

    Item1 = float(E_Fries.get())
    Item2 = float(E_Lunch.get())
    Item3 = float(E_Burger.get())
    Item4 = float(E_Pizza.get())
    Item5 = float(E_CheeseBurger.get())
    Item6 = float(E_MacNuggets.get())
    Item7 = float(E_MacPuff.get())
    Item8 = float(E_ChickenWings.get())

    Item9 = float(E_Coffee_Cake.get())
    Item10 = float(E_Red_Velvet_Cake.get())
    Item11 = float(E_Black_Forest.get())
    Item12 = float(E_Boston_Cream_Cake.get())
    Item13 = float(E_Latta.get())
    Item14 = float(E_Coke.get())
    Item15 = float(E_Pepsi.get())
    Item16 = float(E_Cappuccino.get())

    PriceofFood =(Item1 * 70) + (Item2 * 90) + (Item3 * 50) + (Item4 *100) + (Item5 * 50) + (Item6 * 80) +\
                   (Item7 * 50) + (Item8 * 120)

    PriceofCakesandDrinks =(Item9 * 100) + (Item10 * 110) + (Item11 * 100) + (Item12 *110) + (Item13 * 70) + \
                  (Item14 * 70) + (Item15 * 80) + (Item16 * 100)

    FoodPrice = "Rs "+ str('%.2f' % PriceofFood)
    DrinksandCakesPrice = "Rs "+ str("%.2f" % PriceofCakesandDrinks)
    CostofFood.set(FoodPrice)
    CostofCakesandDrinks.set(DrinksandCakesPrice)
    SC = "Rs "+ str("%.2f" % 0.15)
    print(SC)
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs "+ str(round(PriceofFood + PriceofCakesandDrinks + 0.15))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs "+ str(round((PriceofFood + PriceofCakesandDrinks + 0.15)*0.05))
    PaidTax.set(Tax)
    TT = ((PriceofFood + PriceofCakesandDrinks + 0.15)*0.05)
    TC = "Rs "+ str(round((PriceofFood + PriceofCakesandDrinks + 0.15) + TT))
    print((TC))
    TotalCost.set(TC)

# ================================================ Exit the Main frame ===============================================


def qExit():

    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

# ================================================== Reset the Entries Module =========================================


def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofCakesandDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Fries.set("0")
    E_Lunch.set("0")
    E_Burger.set("0")
    E_Pizza.set("0")
    E_CheeseBurger.set("0")
    E_MacNuggets.set("0")
    E_MacPuff.set("0")
    E_ChickenWings.set("0")

    E_Coffee_Cake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Black_Forest.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Latta.set("0")
    E_Coke.set("0")
    E_Pepsi.set("0")
    E_Cappuccino.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")

    txtLatta.configure(state=DISABLED)
    txtLunch.configure(state=DISABLED)
    txtBurger.configure(state=DISABLED)
    txtPizza.configure(state=DISABLED)
    txtCheeseBurger.configure(state=DISABLED)
    txtMacNuggets.configure(state=DISABLED)
    txtMacPuff.configure(state=DISABLED)
    txtChickenWings.configure(state=DISABLED)
    txtCoffee_Cake.configure(state=DISABLED)
    txtRed_Valet_Cake.configure(state=DISABLED)
    txtBlack_Forest_Cake.configure(state=DISABLED)
    txtBoston_Cream_Cake.configure(state=DISABLED)
    txtLatta.configure(state=DISABLED)
    txtCoke.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)

# ====================================================== Added Receipt Functionality Module ======================

def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(1000, 500890)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t' + "Cost of Items \n\n")
    txtReceipt.insert(END, 'Fries:\t\t\t\t\t' + E_Fries.get() + "\n")
    txtReceipt.insert(END, 'Lunch Meal: \t\t\t\t\t' + E_Lunch.get() + "\n")
    txtReceipt.insert(END, 'Burger: \t\t\t\t\t' + E_Burger.get() + "\n")
    txtReceipt.insert(END, 'Pizza: \t\t\t\t\t' + E_Pizza.get() + "\n")
    txtReceipt.insert(END, 'Cheese Burger: \t\t\t\t\t' + E_CheeseBurger.get() + "\n")
    txtReceipt.insert(END, 'Mac Nuggets: \t\t\t\t\t' + E_MacNuggets.get() + "\n")
    txtReceipt.insert(END, 'Mac Puff: \t\t\t\t\t' + E_MacPuff.get() + "\n")
    txtReceipt.insert(END, 'Chicken Wings: \t\t\t\t\t' + E_ChickenWings.get() + "\n")
    txtReceipt.insert(END, 'Coffee Cake: \t\t\t\t\t' + E_Coffee_Cake.get() + "\n")
    txtReceipt.insert(END, 'Red Valet Cake: \t\t\t\t\t' + E_Red_Velvet_Cake.get() + "\n")
    txtReceipt.insert(END, 'Black Forest Cake: \t\t\t\t\t' + E_Black_Forest.get() + "\n")
    txtReceipt.insert(END, 'Boston Cream Cake: \t\t\t\t\t' + E_Boston_Cream_Cake.get() + "\n")
    txtReceipt.insert(END, 'Latte: \t\t\t\t\t' + E_Latta.get() + "\n")
    txtReceipt.insert(END, 'Coke: \t\t\t\t\t' + E_Coke.get() + "\n")
    txtReceipt.insert(END, 'Pepsi: \t\t\t\t\t' + E_Pepsi.get() + "\n")
    txtReceipt.insert(END, 'Cappuccino: \t\t\t\t\t' + E_Cappuccino.get() + "\n")
    txtReceipt.insert(END, 'Cost of Food: \t\t\t\t\t' + CostofFood.get() + "\t\t\tTax Paid:\t\t\t\t\t" + PaidTax.get() + "\n")
    txtReceipt.insert(END, 'Cost of Cakes and Drinks: \t\t\t\t\t' + CostofCakesandDrinks.get() + "\t\t\tSub Total:\t\t\t\t\t" +
                      SubTotal.get() + "\n")
    txtReceipt.insert(END, 'Service Charge: \t\t\t\t\t' + ServiceCharge.get() + "\t\t\tTotal Cost:\t\t\t\t\t" + TotalCost.get() + "\n")


# ============================================ CheckButton check performed module ====================================


def chkbutton_value():
    if var1.get() == 1:
        txtFries.configure(state=NORMAL)
    elif var1.get() == 0:
        txtFries.configure(state=DISABLED)
        E_Fries.set("0")
    if var2.get() == 1:
        txtLunch.configure(state=NORMAL)
    elif var2.get() == 0:
        txtLunch.configure(state=DISABLED)
        E_Lunch.set("0")
    if var3.get() == 1:
        txtBurger.configure(state=NORMAL)
    elif var3.get() == 0:
        txtBurger.configure(state=DISABLED)
        E_Burger.set("0")
    if var4.get() == 1:
        txtPizza.configure(state=NORMAL)
    elif var4.get() == 0:
        txtPizza.configure(state=DISABLED)
        E_Pizza.set("0")
    if var5.get() == 1:
        txtCheeseBurger.configure(state=NORMAL)
    elif var5.get() == 0:
        txtCheeseBurger.configure(state=DISABLED)
        E_CheeseBurger.set("0")
    if var6.get() == 1:
        txtMacNuggets.configure(state=NORMAL)
    elif var6.get() == 0:
        txtMacNuggets.configure(state=DISABLED)
        E_MacNuggets.set("0")
    if var7.get() == 1:
        txtMacPuff.configure(state=NORMAL)
    elif var7.get() == 0:
        txtMacPuff.configure(state=DISABLED)
        E_MacPuff.set("0")
    if var8.get() == 1:
        txtChickenWings.configure(state=NORMAL)
    elif var8.get() == 0:
        txtChickenWings.configure(state=DISABLED)
        E_ChickenWings.set("0")
    if var9.get() == 1:
        txtCoffee_Cake.configure(state=NORMAL)
    elif var9.get() == 0:
        txtCoffee_Cake.configure(state=DISABLED)
        E_Coffee_Cake.set("0")
    if var10.get() == 1:
        txtRed_Valet_Cake.configure(state=NORMAL)
    elif var10.get() == 0:
        txtRed_Valet_Cake.configure(state=DISABLED)
        E_Red_Velvet_Cake.set("0")
    if var11.get() == 1:
        txtBlack_Forest_Cake.configure(state=NORMAL)
    elif var11.get() == 0:
        txtBlack_Forest_Cake.configure(state=DISABLED)
        E_Black_Forest.set("0")
    if var12.get() == 1:
        txtBoston_Cream_Cake.configure(state=NORMAL)
    elif var12.get() == 0:
        txtBoston_Cream_Cake.configure(state=DISABLED)
        E_Boston_Cream_Cake.set("0")
    if var13.get() == 1:
        txtLatta.configure(state=NORMAL)
    elif var13.get() == 0:
        txtLatta.configure(state=DISABLED)
        E_Latta.set("0")
    if var14.get() == 1:
        txtCoke.configure(state=NORMAL)
    elif var14.get() == 0:
        txtCoke.configure(state=DISABLED)
        E_Coke.set("0")
    if var15.get() == 1:
        txtPepsi.configure(state=NORMAL)
    elif var15.get() == 0:
        txtPepsi.configure(state=DISABLED)
        E_Pepsi.set("0")
    if var16.get() == 1:
        txtCappuccino.configure(state=NORMAL)
    elif var16.get() == 0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")

# =======================================================================================================


# ======================================================= Variables ===============================================


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakesandDrinks = StringVar()
CostofFood = StringVar()
ServiceCharge = StringVar()

E_Fries = StringVar()
E_Lunch = StringVar()
E_Burger = StringVar()
E_Pizza = StringVar()
E_CheeseBurger = StringVar()
E_MacNuggets = StringVar()
E_MacPuff = StringVar()
E_ChickenWings = StringVar()

E_Coffee_Cake = StringVar()
E_Red_Velvet_Cake = StringVar()
E_Black_Forest = StringVar()
E_Boston_Cream_Cake = StringVar()
E_Latta = StringVar()
E_Coke = StringVar()
E_Pepsi = StringVar()
E_Cappuccino = StringVar()


E_Fries.set("0")
E_Lunch.set("0")
E_Burger.set("0")
E_Pizza.set("0")
E_CheeseBurger.set("0")
E_MacNuggets.set("0")
E_MacPuff.set("0")
E_ChickenWings.set("0")


E_Coffee_Cake.set("0")
E_Red_Velvet_Cake.set("0")
E_Black_Forest.set("0")
E_Boston_Cream_Cake.set("0")
E_Latta.set("0")
E_Coke.set("0")
E_Pepsi.set("0")
E_Cappuccino.set("0")

# ===================================================== Date Declared =============================================

DateofOrder.set(time.strftime("%d/%m/%y"))

# ====================================== Food Check buttons =======================================================

Fries = Checkbutton(f1aa, font=('arial',18, 'bold'), text="Fries Meal \t", variable=var1, onvalue=1,
                    offvalue=0, command=chkbutton_value).grid(row=0, sticky=W)

Lunch = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="Lunch Meal \t", variable=var2, onvalue=1,
                       offvalue=0, command=chkbutton_value).grid(row=1, sticky=W)

Burger = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="Burger Meal \t", variable=var3, onvalue=1,
                         offvalue=0, command=chkbutton_value).grid(row=2, sticky=W)

Pizza = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="Pizza Meal \t", variable=var4, onvalue=1,
                          offvalue=0, command=chkbutton_value).grid(row=3, sticky=W)

CheeseBurger = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="Cheese Burger  \t", variable=var5, onvalue=1,
                         offvalue=0, command=chkbutton_value).grid(row=4, sticky=W)

MacNuggets = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="Mac Nuggets \t", variable=var6, onvalue=1,
                             offvalue=0, command=chkbutton_value).grid(row=5, sticky=W)

MacPuff = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="Mac Puff \t", variable=var7, onvalue=1,
                              offvalue=0, command=chkbutton_value).grid(row=6, sticky=W)

ChickenWings = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="Chicken Wings \t", variable=var8, onvalue=1,
                              offvalue=0, command=chkbutton_value).grid(row=7, sticky=W)

# ====================================== Drinks & Cake Check Buttons ================================================

CoffeeCake = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="Coffee Cake \t", variable=var9, onvalue=1,
                         offvalue=0, command=chkbutton_value).grid(row=0, sticky=W)

Red_Velvet_Cake = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="Red Velvet Cake \t", variable=var10, onvalue=1,
                              offvalue=0, command=chkbutton_value).grid(row=1, sticky=W)

Black_Forest_Cake = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="Black Forest Cake \t", variable=var11,
                                onvalue=1, offvalue=0, command=chkbutton_value).grid(row=2, sticky=W)

Boston_Cream_Cake = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="Boston Cream Cake \t", variable=var12, onvalue=1,
                                offvalue=0, command=chkbutton_value).grid(row=3, sticky=W)

Latta = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="Latte \t", variable=var13,
                                   onvalue=1, offvalue=0, command=chkbutton_value).grid(row=4, sticky=W)

Coke = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="Coke \t", variable=var14,
                                     onvalue=1, offvalue=0, command=chkbutton_value).grid(row=5, sticky=W)

Pepsi = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="Pepsi \t", variable=var15, onvalue=1,
                                offvalue=0, command=chkbutton_value).grid(row=6, sticky=W)

Cappuccino = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="Cappuccino \t", variable=var16,
                              onvalue=1, offvalue=0, command=chkbutton_value).grid(row=7, sticky=W)

# ====================================== Entry Widget for Food ===================================================

txtFries = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Fries, state=DISABLED)
txtFries.grid(row=0, column=1)
txtLunch = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Lunch,
                    state=DISABLED)
txtLunch.grid(row=1, column=1)
txtBurger = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Burger,
                      state=DISABLED)
txtBurger.grid(row=2, column=1)
txtPizza = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Pizza,
                       state=DISABLED)
txtPizza.grid(row=3, column=1)
txtCheeseBurger = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_CheeseBurger,
                      state=DISABLED)
txtCheeseBurger.grid(row=4, column=1)
txtMacNuggets = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_MacNuggets
                          , state=DISABLED)
txtMacNuggets.grid(row=5, column=1)
txtMacPuff = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                           textvariable=E_MacPuff, state=DISABLED)
txtMacPuff.grid(row=6, column=1)
txtChickenWings = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                           textvariable=E_ChickenWings, state=DISABLED)
txtChickenWings.grid(row=7, column=1)

# ====================================== Entry Widget for Cakes ===================================================

txtCoffee_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                       textvariable=E_Coffee_Cake, state=DISABLED)
txtCoffee_Cake.grid(row=0, column=1)
txtRed_Valet_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                          textvariable=E_Red_Velvet_Cake, state=DISABLED)
txtRed_Valet_Cake.grid(row=1, column=1)
txtBlack_Forest_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                             textvariable=E_Black_Forest, state=DISABLED)
txtBlack_Forest_Cake.grid(row=2, column=1)
txtBoston_Cream_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                             textvariable=E_Boston_Cream_Cake, state=DISABLED)
txtBoston_Cream_Cake.grid(row=3, column=1)
txtLatta = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                textvariable=E_Latta, state=DISABLED)
txtLatta.grid(row=4, column=1)
txtCoke = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                 textvariable=E_Coke, state=DISABLED)
txtCoke.grid(row=5, column=1)
txtPepsi = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                             textvariable=E_Pepsi, state=DISABLED)
txtPepsi.grid(row=6, column=1)
txtCappuccino = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                           textvariable=E_Cappuccino, state=DISABLED)
txtCappuccino.grid(row=7, column=1)

# ========================================== Receipt Information ====================================================

lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, width=59, height=22, bg="white", bd=8, font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0, sticky=W+E)

# =================================== Cost Items Information(f2aa) ==================================================

lblCostofFood = Label(f2aa, font=('arial', 16, 'bold'), text="Cost of Food", bd=8)
lblCostofFood.grid(row=2, column=0, sticky=W)
txtCostofFood = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=CostofFood)
txtCostofFood.grid(row=2, column=1)

lblCostofCakesandDrinks = Label(f2aa, font=('arial', 16, 'bold'), text="Drink & Cake", bd=8)
lblCostofCakesandDrinks.grid(row=3, column=0, sticky=W)
txtCostofCakesandDrinks = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=CostofCakesandDrinks)
txtCostofCakesandDrinks.grid(row=3, column=1, sticky=W)

lblServiceCharge = Label(f2aa, font=('arial', 16, 'bold'), text="Service Charge", bd=8)
lblServiceCharge.grid(row=4, column=0, sticky=W)
txtServiceCharge = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=ServiceCharge)
txtServiceCharge.grid(row=4, column=1, sticky=W)

# ======================================Payment Information(f2ab)===================================================

lblPaidTax = Label(f2ab, font=('arial', 16, 'bold'), text="Tax", bd=8)
lblPaidTax.grid(row=2, column=0, sticky=W)
txtPaidTax = Entry(f2ab, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=PaidTax)
txtPaidTax.grid(row=2, column=1, sticky=W)

lblSubTotal = Label(f2ab, font=('arial', 16, 'bold'), text="Sub Total", bd=8)
lblSubTotal.grid(row=3, column=0, sticky=W)
txtSubTotal = Entry(f2ab, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1, sticky=W)

lblTotalCost = Label(f2ab, font=('arial', 16, 'bold'), text="Total", bd=8)
lblTotalCost.grid(row=4, column=0, sticky=W)
txtTotalCost = Entry(f2ab, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=TotalCost)
txtTotalCost.grid(row=4, column=1, sticky=W)


# ======================================Button===================================================

btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                  text="Total", command=CostofItems).grid(row=0, column=0, sticky=W+E+N+S)
btnReceipt = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                    text="Receipt", command=Receipt).grid(row=0, column=1, sticky=W+E+N+S)
btnReset = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                  text="Reset", command=Reset).grid(row=0, column=2, sticky=W+E+N+S)
btnExit = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                 text="Exit", command=qExit).grid(row=0, column=3, sticky=W+E+N+S)




root.mainloop()
