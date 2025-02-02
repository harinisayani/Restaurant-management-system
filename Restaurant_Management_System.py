from tkinter import *
from tkinter.filedialog import asksaveasfilename
root=Tk()
root.geometry("1350x700+0+1")
root.title("Restaurant Management System")
root.config(bg="pink")

def receipt_generate():
    receiptframe.insert(END,"*********************************************************************\n")
    receiptframe.insert(END,"\t\t\tRestaurant\n")
    receiptframe.insert(END,"*********************************************************************\n")
    receiptframe.insert(END,f"\tFood Item :\t\t\t {cof.get()} \n")
    receiptframe.insert(END,f"\tDrinks Item :\t\t\t {cod.get()} \n")
    receiptframe.insert(END,f"\tCakes Item :\t\t\t {coc.get()} \n ")
    receiptframe.insert(END,"********************************************************************\n")
    receiptframe.insert(END,f"\tSub Total :\t\t\t {stotal.get()}  \n")
    receiptframe.insert(END,f"\tService Charges :\t\t\t {service.get()} \n")
    receiptframe.insert(END,"*********************************************************************\n")
    receiptframe.insert(END,f"\tTotal Cost :\t\t\t {tot.get()}  \n")
def saved():
    filepath=asksaveasfilename()
    if not filepath:
        return 
    with open(filepath,'w') as fp:
        txt=receiptframe.get(1.0,END)
        fp.write(txt)
def cal():
    cofentry.delete(0,END)
    codentry.delete(0,END)
    cocentry.delete(0,END)
    subtotalentry.delete(0,END)
    servicechargeentry.delete(0,END)
    totalcostentry.delete(0,END)
    global food_cost,drinks_cost,cakes_cost
    item1=int(roti_text.get())*40
    item2=int(daal_text.get())*30
    item3=int(fish_text.get())*100
    item4=int(sabji_text.get())*50
    item5=int(kebab_text.get())*150
    item6=int(chaval_text.get())*100
    item7=int(mutton_text.get())*200
    item8=int(panner_text.get())*100
    item9=int(chicken_text.get())*150
    item10=int(lassi_text.get())*40
    item11=int(coffee_text.get())*20
    item12=int(faluda_text.get())*40
    item13=int(shikanja_text.get())*40
    item14=int(jaijeera_text.get())*30
    item15=int(roothafza_text.get())*30
    item16=int(masalatea_text.get())*15
    item17=int(badammilk_text.get())*30
    item18=int(colddrinks_text.get())*20
    item19=int(oreo_text.get())*200
    item20=int(apple_text.get())*250
    item21=int(kitkat_text.get())*250
    item22=int(vineela_text.get())*250
    item23=int(banana_text.get())*250
    item24=int(brownie_text.get())*250
    item25=int(pineapple_text.get())*250
    item26=int(chocolate_text.get())*250
    item27=int(blackforest_text.get())*250
    food_cost=item1+item2+item3+item4+item5+item6+item7+item8+item9
    drinks_cost=item10+item11+item12+item13+item14+item15+item16+item17+item18+item19
    cakes_cost=item20+item21+item22+item23+item24+item25+item26+item27
    cofentry.insert(END,food_cost)
    codentry.insert(END,drinks_cost)
    cocentry.insert(END,cakes_cost)
    subtotalentry.insert(END,food_cost+drinks_cost+cakes_cost)
    servicechargeentry.insert(END,6.32)
    totalcostentry.insert(END,food_cost+drinks_cost+cakes_cost+100.32)
def reset_all():
    receiptframe.delete("1.0","end")
    cofentry.delete(0,END)
    codentry.delete(0,END)
    cocentry.delete(0,END)
    subtotalentry.delete(0,END)
    servicechargeentry.delete(0,END)
    totalcostentry.delete(0,END)
    rotitext.delete(0,END)
    roti_text.set('0')
    rotitext.config(state=DISABLED)
    roti_food.set('0')
    
    daaltext.delete(0,END)
    daal_text.set('0')
    daaltext.config(state=DISABLED)
    daal_food.set('0')
    
    fishtext.delete(0,END)
    fish_text.set('0')
    fishtext.config(state=DISABLED)
    fish_food.set('0')
    
    sabjitext.delete(0,END)
    sabji_text.set('0')
    sabjitext.config(state=DISABLED)
    sabji_food.set('0')
    
    kebabtext.delete(0,END)
    kebab_text.set('0')
    kebabtext.config(state=DISABLED)
    kebab_food.set('0')
    
    chavaltext.delete(0,END)
    chaval_text.set('0')
    chavaltext.config(state=DISABLED)
    chaval_food.set('0')
    
    muttontext.delete(0,END)
    mutton_text.set('0')
    muttontext.config(state=DISABLED)
    mutton_food.set('0')
    
    pannertext.delete(0,END)
    panner_text.set('0')
    pannertext.config(state=DISABLED)
    panner_food.set('0')
    
    chickentext.delete(0,END)
    chicken_text.set('0')
    chickentext.config(state=DISABLED)
    chicken_food.set('0')
    
    lassitext.delete(0,END)
    lassi_text.set('0')
    lassitext.config(state=DISABLED)
    lassi_drinks.set('0')
    
    coffeetext.delete(0,END)
    coffee_text.set('0')
    coffeetext.config(state=DISABLED)
    coffee_drinks.set('0')
    
    faludatext.delete(0,END)
    faluda_text.set('0')
    faludatext.config(state=DISABLED)
    faluda_drinks.set('0')
    
    shikanjatext.delete(0,END)
    shikanja_text.set('0')
    shikanjatext.config(state=DISABLED)
    shikanja_drinks.set('0')
    
    jaijeeratext.delete(0,END)
    jaijeera_text.set('0')
    jaijeeratext.config(state=DISABLED)
    jaijeera_drinks.set('0')
    
    roothafzatext.delete(0,END)
    roothafza_text.set('0')
    roothafzatext.config(state=DISABLED)
    roothafza_drinks.set('0')
    
    masalateatext.delete(0,END)
    masalatea_text.set('0')
    masalateatext.config(state=DISABLED)
    masalatea_drinks.set('0')
    
    badammilktext.delete(0,END)
    badammilk_text.set('0')
    badammilktext.config(state=DISABLED)
    badammilk_drinks.set('0')
    
    colddrinkstext.delete(0,END)
    colddrinks_text.set('0')
    colddrinkstext.config(state=DISABLED)
    colddrinks_drinks.set('0')
    
    oreotext.delete(0,END)
    oreo_text.set('0')
    oreotext.config(state=DISABLED)
    oreo_cakes.set('0')
    
    appletext.delete(0,END)
    apple_text.set('0')
    appletext.config(state=DISABLED)
    apple_cakes.set('0')
    
    kitkattext.delete(0,END)
    kitkat_text.set('0')
    kitkattext.config(state=DISABLED)
    kitkat_cakes.set('0')
    
    vineelatext.delete(0,END)
    vineela_text.set('0')
    vineelatext.config(state=DISABLED)
    vineela_cakes.set('0')
    
    bananatext.delete(0,END)
    banana_text.set('0')
    bananatext.config(state=DISABLED)
    banana_cakes.set('0')
    
    brownietext.delete(0,END)
    brownie_text.set('0')
    brownietext.config(state=DISABLED)
    brownie_cakes.set('0')
    
    pineappletext.delete(0,END)
    pineapple_text.set('0')
    pineappletext.config(state=DISABLED)
    pineapple_cakes.set('0')
    
    chocolatetext.delete(0,END)
    chocolate_text.set('0')
    chocolatetext.config(state=DISABLED)
    chocolate_cakes.set('0')
    
    blackforesttext.delete(0,END)
    blackforest_text.set('0')
    blackforesttext.config(state=DISABLED)
    blackforest_cakes.set('0')

    
    
def clicked_roti():
    if roti_food.get():
        rotitext.config(state=NORMAL)
        rotitext.delete(0,END)
        rotitext.focus()
        
    else:
        rotitext.delete(0,END)
        rotitext.config(state=DISABLED)
        
def clicked_daal():
    if daal_food.get():
        daaltext.config(state=NORMAL)
        daaltext.delete(0,END)
        daaltext.focus()
    else:
        daaltext.delete(0,END)
        daaltext.config(state=DISABLED)
def clicked_fish():
    if fish_food.get():
        fishtext.config(state=NORMAL)
        fishtext.delete(0,END)
        fishtext.focus()
    else:
        fishtext.delete(0,END)
        fishtext.config(state=DISABLED)
def clicked_sabji():
    if sabji_food.get():
        sabjitext.config(state=NORMAL)
        sabjitext.delete(0,END)
        sabjitext.focus()
    else:
        sabjitext.delete(0,END)
        sabjitext.config(state=DISABLED)
def clicked_kebab():
    if kebab_food.get():
        kebabtext.config(state=NORMAL)
        kebabtext.delete(0,END)
        kebabtext.focus()    
    else:
        kebabtext.delete(0,END)
        kebabtext.config(state=DISABLED)
def clicked_chaval():
    if chaval_food.get():
        chavaltext.config(state=NORMAL)
        chavaltext.delete(0,END)
        chavaltext.focus()
    else:
        chavaltext.delete(0,END)
        chavaltext.config(state=DISABLED)
def clicked_mutton():
    if mutton_food.get():
        muttontext.config(state=NORMAL)
        muttontext.delete(0,END)
        muttontext.focus()
    else:
        muttontext.delete(0,END)
        muttontext.config(state=DISABLED)
def clicked_panner():
    if panner_food.get():
        pannertext.config(state=NORMAL)
        pannertext.delete(0,END)
        pannertext.focus()
    else:
        pannertext.delete(0,END)
        pannertext.config(state=DISABLED)
def clicked_chicken():
    if chicken_food.get():
        chickentext.config(state=NORMAL)
        chickentext.delete(0,END)
        chickentext.focus()
    else:
        chickentext.delete(0,END)
        chickentext.config(state=DISABLED)
def clicked_lassi():
    if lassi_drinks.get():
        lassitext.config(state=NORMAL)
        lassitext.delete(0,END)
        lassitext.focus()
    else:
        lassitext.delete(0,END)
        lassitext.config(state=DISABLED)  
def clicked_coffee():
    if coffee_drinks.get():
        coffeetext.config(state=NORMAL)
        coffeetext.delete(0,END)
        coffeetext.focus()
    else:
        coffeetext.delete(0,END)
        coffeetext.config(state=DISABLED)  
def clicked_faluda():
    if faluda_drinks.get():
        faludatext.config(state=NORMAL)
        faludatext.delete(0,END)
        faludatext.focus()
    else:
        faludatext.delete(0,END)
        faludatext.config(state=DISABLED)  
def clicked_shikanja():
    if shikanja_drinks.get():
        shikanjatext.config(state=NORMAL)
        shikanjatext.delete(0,END)
        shikanjatext.focus()
    else:
        shikanjatext.delete(0,END)
        shikanjatext.config(state=DISABLED)  
def clicked_jaijeera():
    if jaijeera_drinks.get():
        jaijeeratext.config(state=NORMAL)
        jaijeeratext.delete(0,END)
        jaijeeratext.focus()
    else:
        jaijeeratext.delete(0,END)
        jaijeeratext.config(state=DISABLED)  
def clicked_roothafza():
    if roothafza_drinks.get():
        roothafzatext.config(state=NORMAL)
        roothafzatext.delete(0,END)
        roothafzatext.focus()
    else:
        roothafzatext.delete(0,END)
        roothafzatext.config(state=DISABLED)  
def clicked_masalatea():
    if masalatea_drinks.get():
        masalateatext.config(state=NORMAL)
        masalateatext.delete(0,END)
        masalateatext.focus()
    else:
        masalateatext.delete(0,END)
        masalateatext.config(state=DISABLED)  
def clicked_badammilk():
    if badammilk_drinks.get():
        badammilktext.config(state=NORMAL)
        badammilktext.delete(0,END)
        badammilktext.focus()
    else:
        badammilktext.delete(0,END)
        badammilktext.config(state=DISABLED)      
def clicked_colddrinks():
    if colddrinks_drinks.get():
        colddrinkstext.config(state=NORMAL)
        colddrinkstext.delete(0,END)
        colddrinkstext.focus()
    else:
        colddrinkstext.delete(0,END)
        colddrinkstext.config(state=DISABLED)  
def clicked_oreo():
    if oreo_cakes.get():
        oreotext.config(state=NORMAL)
        oreotext.delete(0,END)
        oreotext.focus()
    else:
        oreotext.delete(0,END)
        oreotext.config(state=DISABLED)  
def clicked_apple():
    if apple_cakes.get():
        appletext.config(state=NORMAL)
        appletext.delete(0,END)
        appletext.focus()
    else:
        appletext.delete(0,END)
        appletext.config(state=DISABLED)  
def clicked_kitkat():
    if kitkat_cakes.get():
        kitkattext.config(state=NORMAL)
        kitkattext.delete(0,END)
        kitkattext.focus()
    else:
        kitkattext.delete(0,END)
        kitkattext.config(state=DISABLED)  
def clicked_vineela():
    if vineela_cakes.get():
        vineelatext.config(state=NORMAL)
        vineelatext.delete(0,END)
        vineelatext.focus()
    else:
        vineelatext.delete(0,END)
        vineelatext.config(state=DISABLED)  
def clicked_banana():
    if banana_cakes.get():
        bananatext.config(state=NORMAL)
        bananatext.delete(0,END)
        bananatext.focus()
    else:
        bananatext.delete(0,END)
        bananatext.config(state=DISABLED)  
def clicked_brownie():
    if brownie_cakes.get():
        brownietext.config(state=NORMAL)
        brownietext.delete(0,END)
        brownietext.focus()
    else:
        brownietext.delete(0,END)
        brownietext.config(state=DISABLED)  
def clicked_pineapple():
    if pineapple_cakes.get():
        pineappletext.config(state=NORMAL)
        pineappletext.delete(0,END)
        pineappletext.focus()
    else:
        pineappletext.delete(0,END)
        pineappletext.config(state=DISABLED)  
def clicked_chocolate():
    if chocolate_cakes.get():
        chocolatetext.config(state=NORMAL)
        chocolatetext.delete(0,END)
        chocolatetext.focus()
    else:
        chocolatetext.delete(0,END)
        chocolatetext.config(state=DISABLED)  
def clicked_blackforest():
    if blackforest_cakes.get():
        blackforesttext.config(state=NORMAL)
        blackforesttext.delete(0,END)
        blackforesttext.focus()    
    else:
        blackforesttext.delete(0,END)
        blackforesttext.config(state=DISABLED)  
#mainframe
mainframe=Frame(root,bd=4,relief=RIDGE)
mainframe.pack(side=TOP)

#mainlabel
mainlabel=Label(mainframe,text="Restaurant Management System",font=('ariel',35),fg="blue",width=52)
mainlabel.grid(row=0,column=0)

#itemsframe
itemsframe=Frame(root,bd=4,relief=RIDGE)
itemsframe.pack(side=LEFT)

#costframe
costframe=Frame(itemsframe,bd=2,relief=RIDGE,bg="pink")
costframe.pack(side=BOTTOM)

#foodlabelframe
foodframe=LabelFrame(itemsframe,text="Food",bd=4,relief=RIDGE,font=('ariel',18,'bold'))
foodframe.pack(side=LEFT)

#drinksframe
drinksframe=LabelFrame(itemsframe,bd=4,text="Drinks",relief=RIDGE,font=('ariel',18,'bold'))
drinksframe.pack(side=LEFT)

#cakesframe
cakesframe=LabelFrame(itemsframe,bd=4,text="Cakes",relief=RIDGE,font=('ariel',18,'bold'))
cakesframe.pack(side=LEFT)




        
#foodcheckboxes
roti_food=IntVar()
daal_food=IntVar()
fish_food=IntVar()
sabji_food=IntVar()
kebab_food=IntVar()
chaval_food=IntVar()
mutton_food=IntVar()
panner_food=IntVar()
chicken_food=IntVar()



lassi_drinks=IntVar()
coffee_drinks=IntVar()
faluda_drinks=IntVar()
shikanja_drinks=IntVar()
jaijeera_drinks=IntVar()
roothafza_drinks=IntVar()
masalatea_drinks=IntVar()
badammilk_drinks=IntVar()
colddrinks_drinks=IntVar()



        
oreo_cakes=IntVar()
apple_cakes=IntVar()
kitkat_cakes=IntVar()
vineela_cakes=IntVar()
banana_cakes=IntVar()
brownie_cakes=IntVar()
pineapple_cakes=IntVar()
chocolate_cakes=IntVar()
blackforest_cakes=IntVar()


roti_text=StringVar()
daal_text=StringVar()
fish_text=StringVar()
sabji_text=StringVar()
kebab_text=StringVar()
chaval_text=StringVar()
mutton_text=StringVar()
panner_text=StringVar()
chicken_text=StringVar()



lassi_text=StringVar()
coffee_text=StringVar()
faluda_text=StringVar()
shikanja_text=StringVar()
jaijeera_text=StringVar()
roothafza_text=StringVar()
masalatea_text=StringVar()
badammilk_text=StringVar()
colddrinks_text=StringVar()


oreo_text=StringVar()
apple_text=StringVar()
kitkat_text=StringVar()
vineela_text=StringVar()
banana_text=StringVar()
brownie_text=StringVar()
pineapple_text=StringVar()
chocolate_text=StringVar()
blackforest_text=StringVar()



roti=Checkbutton(foodframe,text="Roti",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=roti_food,command=clicked_roti)
roti.grid(row=0,column=0,sticky=W)
daal=Checkbutton(foodframe,text="Daal",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=daal_food,command=clicked_daal)
daal.grid(row=1,column=0,sticky=W)
fish=Checkbutton(foodframe,text="Fish",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=fish_food,command=clicked_fish)
fish.grid(row=2,column=0,sticky=W)
sabji=Checkbutton(foodframe,text="Sabji",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=sabji_food,command=clicked_sabji)
sabji.grid(row=3,column=0,sticky=W)
kebab=Checkbutton(foodframe,text="Kebab",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=kebab_food,command=clicked_kebab)
kebab.grid(row=4,column=0,sticky=W)
chaval=Checkbutton(foodframe,text="Chaval",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=chaval_food,command=clicked_chaval)
chaval.grid(row=5,column=0,sticky=W)
mutton=Checkbutton(foodframe,text="mutton",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=mutton_food,command=clicked_mutton)
mutton.grid(row=6,column=0,sticky=W)
panner=Checkbutton(foodframe,text="panner",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=panner_food,command=clicked_panner)
panner.grid(row=7,column=0,sticky=W)
chicken=Checkbutton(foodframe,text="chicken",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=chicken_food,command=clicked_chicken)
chicken.grid(row=8,column=0,sticky=W)

    
#drinkscheckboxes
lassi=Checkbutton(drinksframe,text="Lassi",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=lassi_drinks,command=clicked_lassi)
lassi.grid(row=0,column=0,sticky=W)
coffee=Checkbutton(drinksframe,text="Coffee",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=coffee_drinks,command=clicked_coffee)
coffee.grid(row=1,column=0,sticky=W)
faluda=Checkbutton(drinksframe,text="Faluda",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=faluda_drinks,command=clicked_faluda)
faluda.grid(row=2,column=0,sticky=W)
shikanja=Checkbutton(drinksframe,text="Shikanja",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=shikanja_drinks,command=clicked_shikanja)
shikanja.grid(row=3,column=0,sticky=W)
jaijeera=Checkbutton(drinksframe,text="Jai-Jeera",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=jaijeera_drinks,command=clicked_jaijeera)
jaijeera.grid(row=4,column=0,sticky=W)
roothafza=Checkbutton(drinksframe,text="Roothafza",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=roothafza_drinks,command=clicked_roothafza)
roothafza.grid(row=5,column=0,sticky=W)
masalatea=Checkbutton(drinksframe,text="Masala Tea",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=masalatea_drinks,command=clicked_masalatea)
masalatea.grid(row=6,column=0,sticky=W)
badammilk=Checkbutton(drinksframe,text="Badam Milk",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=badammilk_drinks,command=clicked_badammilk)
badammilk.grid(row=7,column=0,sticky=W)
colddrinks=Checkbutton(drinksframe,text="Cold Drinks",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=colddrinks_drinks,command=clicked_colddrinks)
colddrinks.grid(row=8,column=0,sticky=W)


#cakesframe
oreo=Checkbutton(cakesframe,text="Oreo",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=oreo_cakes,command=clicked_oreo)
oreo.grid(row=0,column=0,sticky=W)
apple=Checkbutton(cakesframe,text="Apple",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=apple_cakes,command=clicked_apple)
apple.grid(row=1,column=0,sticky=W)
kitkat=Checkbutton(cakesframe,text="Kit Kat",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=kitkat_cakes,command=clicked_kitkat)
kitkat.grid(row=2,column=0,sticky=W)
vineela=Checkbutton(cakesframe,text="Vineela",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=vineela_cakes,command=clicked_vineela)
vineela.grid(row=3,column=0,sticky=W)
banana=Checkbutton(cakesframe,text="Banana",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=banana_cakes,command=clicked_banana)
banana.grid(row=4,column=0,sticky=W)
brownie=Checkbutton(cakesframe,text="Brownie",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=brownie_cakes,command=clicked_brownie)
brownie.grid(row=5,column=0,sticky=W)
pineapple=Checkbutton(cakesframe,text="Pineapple",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=pineapple_cakes,command=clicked_pineapple)
pineapple.grid(row=6,column=0,sticky=W)
chocolate=Checkbutton(cakesframe,text="Chocolate",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=chocolate_cakes,command=clicked_chocolate)
chocolate.grid(row=7,column=0,sticky=W)
blackforest=Checkbutton(cakesframe,text="Blackforest",onvalue=1,offvalue=0,font=('ariel',18,'bold'),variable=blackforest_cakes,command=clicked_blackforest)
blackforest.grid(row=8,column=0,sticky=W)


#foodtextfield

rotitext=Entry(foodframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=roti_text)
rotitext.grid(row=0,column=1)
roti_text.set('0')
daaltext=Entry(foodframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=daal_text)
daaltext.grid(row=1,column=1)
daal_text.set('0')
fishtext=Entry(foodframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=fish_text)
fishtext.grid(row=2,column=1)
fish_text.set('0')
sabjitext=Entry(foodframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=sabji_text)
sabjitext.grid(row=3,column=1)
sabji_text.set('0')
kebabtext=Entry(foodframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=kebab_text)
kebabtext.grid(row=4,column=1)
kebab_text.set('0')
chavaltext=Entry(foodframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=chaval_text)
chavaltext.grid(row=5,column=1)
chaval_text.set('0')
muttontext=Entry(foodframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=mutton_text)
muttontext.grid(row=6,column=1)
mutton_text.set('0')
pannertext=Entry(foodframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=panner_text)
pannertext.grid(row=7,column=1)
panner_text.set('0')
chickentext=Entry(foodframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=chicken_text)
chickentext.grid(row=8,column=1,padx=10)
chicken_text.set('0')


#drinkstextfield
lassitext=Entry(drinksframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=lassi_text)
lassitext.grid(row=0,column=1)
lassi_text.set('0')
coffeetext=Entry(drinksframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=coffee_text)
coffeetext.grid(row=1,column=1)
coffee_text.set('0')
faludatext=Entry(drinksframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=faluda_text)
faludatext.grid(row=2,column=1)
faluda_text.set('0')
shikanjatext=Entry(drinksframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=shikanja_text)
shikanjatext.grid(row=3,column=1)
shikanja_text.set('0')
jaijeeratext=Entry(drinksframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=jaijeera_text)
jaijeeratext.grid(row=4,column=1)
jaijeera_text.set('0')
roothafzatext=Entry(drinksframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=roothafza_text)
roothafzatext.grid(row=5,column=1)
roothafza_text.set('0')
masalateatext=Entry(drinksframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=masalatea_text)
masalateatext.grid(row=6,column=1)
masalatea_text.set('0')
badammilktext=Entry(drinksframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=badammilk_text)
badammilktext.grid(row=7,column=1)
badammilk_text.set('0')
colddrinkstext=Entry(drinksframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=colddrinks_text)
colddrinkstext.grid(row=8,column=1,padx=10)
colddrinks_text.set('0')


#cakestextfield
oreotext=Entry(cakesframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=oreo_text)
oreotext.grid(row=0,column=1)
oreo_text.set('0')
appletext=Entry(cakesframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=apple_text)
appletext.grid(row=1,column=1)
apple_text.set('0')
kitkattext=Entry(cakesframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=kitkat_text)
kitkattext.grid(row=2,column=1)
kitkat_text.set('0')
vineelatext=Entry(cakesframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=vineela_text)
vineelatext.grid(row=3,column=1)
vineela_text.set('0')
bananatext=Entry(cakesframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=banana_text)
bananatext.grid(row=4,column=1)
banana_text.set('0')
brownietext=Entry(cakesframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=brownie_text)
brownietext.grid(row=5,column=1)
brownie_text.set('0')
pineappletext=Entry(cakesframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=pineapple_text)
pineappletext.grid(row=6,column=1)
pineapple_text.set('0')
chocolatetext=Entry(cakesframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=chocolate_text)
chocolatetext.grid(row=7,column=1)
chocolate_text.set('0')
blackforesttext=Entry(cakesframe,font=('ariel',15,'bold'),bd=7,width=9,state=DISABLED,textvariable=blackforest_text)
blackforesttext.grid(row=8,column=1,padx=10)
blackforest_text.set('0')


#costofdrinks
costofdrinks=Label(costframe,text="Cost of Drinks",font=('Ariel',16,'bold'),bg="pink")
costofdrinks.grid(row=0,column=0,sticky=W)
#costofcake
costofcake=Label(costframe,text="Cost of Cake",font=('Ariel',16,'bold'),bg="pink")
costofcake.grid(row=1,column=0)
#costoffood
costoffood=Label(costframe,text="Cost of Food",font=('Ariel',16,'bold'),bg="pink")
costoffood.grid(row=2,column=0)
#costofdrinksentry
cod=StringVar()
codentry=Entry(costframe,font=('Ariel',15,'bold'),bd=7,width=14,textvariable=cod)
codentry.grid(row=0,column=1,padx=60)
#costofcakeentry
coc=StringVar()
cocentry=Entry(costframe,font=('Ariel',15,'bold'),bd=7,width=14,textvariable=coc)
cocentry.grid(row=1,column=1)
#costoffoodentry
cof=StringVar()
cofentry=Entry(costframe,font=('Ariel',15,'bold'),bd=7,width=14,textvariable=cof)
cofentry.grid(row=2,column=1)
#subtotal

subtotal=Label(costframe,text="Sub Total",font=('Ariel',16,'bold'),bg="pink")
subtotal.grid(row=0,column=2)
#servicecharge
servicecharge=Label(costframe,text="Service Charge",font=('Ariel',16,'bold'),bg="pink")
servicecharge.grid(row=1,column=2)
#totalcost
totalcost=Label(costframe,text="Total Cost",font=('Ariel',16,'bold'),bg="pink")
totalcost.grid(row=2,column=2)
#subtotalentry
stotal=StringVar()
subtotalentry=Entry(costframe,font=('Ariel',15,'bold'),bd=7,width=14,textvariable=stotal)
subtotalentry.grid(row=0,column=3,padx=60)
#servicechargeentry
service=StringVar()
servicechargeentry=Entry(costframe,font=('Ariel',15,'bold'),bd=7,width=14,textvariable=service)
servicechargeentry.grid(row=1,column=3)
#totalcostentry
tot=StringVar()
totalcostentry=Entry(costframe,font=('Ariel',15,'bold'),bd=7,width=14,textvariable=tot)
totalcostentry.grid(row=2,column=3)

#calculator
calculatorframe=Frame(root,bd=4,relief=RIDGE)
calculatorframe.pack(side=RIGHT)

#evaluation
result=StringVar()
op=''
def evaluation(a):
    global op
    op=op+a
    result.set(op)
def clear():
    global op
    result.set('')
    op=''
def equals():
    result.set(str(eval(op)))

entrybox=Entry(calculatorframe,textvariable=result,font=('Ariel',15,'bold'),width=38,bd=7,relief=RIDGE)
entrybox.grid(row=0,column=0,columnspan=4,ipady=10)

nine=Button(calculatorframe,text="9",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('9'))
nine.grid(row=1,column=0,ipadx=36,ipady=5)
eight=Button(calculatorframe,text="8",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('8'))
eight.grid(row=1,column=1,ipadx=38,ipady=5)
seven=Button(calculatorframe,text="7",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('7'))
seven.grid(row=1,column=2,ipadx=36,ipady=5)
six=Button(calculatorframe,text="6",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('6'))
six.grid(row=1,column=3,ipadx=36,ipady=5)
five=Button(calculatorframe,text="5",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('5'))
five.grid(row=2,column=0,ipadx=36,ipady=5)
four=Button(calculatorframe,text="4",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('4'))
four.grid(row=2,column=1,ipadx=38,ipady=5)
three=Button(calculatorframe,text="3",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('3'))
three.grid(row=2,column=2,ipadx=36,ipady=5)
two=Button(calculatorframe,text="2",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('2'))
two.grid(row=2,column=3,ipadx=36,ipady=5)
one=Button(calculatorframe,text="1",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('1'))
one.grid(row=3,column=0,ipadx=36,ipady=5)
zero=Button(calculatorframe,text="0",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('0'))
zero.grid(row=3,column=1,ipadx=38,ipady=5)
plus=Button(calculatorframe,text="+",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('+'))
plus.grid(row=3,column=2,ipadx=36,ipady=5)
minus=Button(calculatorframe,text="-",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('-'))
minus.grid(row=3,column=3,ipadx=36,ipady=5)
mul=Button(calculatorframe,text="*",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('*'))
mul.grid(row=4,column=0,ipadx=37,ipady=5)
div=Button(calculatorframe,text="/",bd=3,font=('Ariel',15,'bold'),command=lambda:evaluation('/'))
div.grid(row=4,column=1,ipadx=40,ipady=5)
clear=Button(calculatorframe,text="C",bd=3,font=('Ariel',15,'bold'),command=clear)
clear.grid(row=4,column=2,ipadx=36,ipady=5)
equal=Button(calculatorframe,text="=",bd=3,font=('Ariel',15,'bold'),command=equals)
equal.grid(row=4,column=3,ipadx=36,ipady=5)


#receiptframe

receiptframe=Text(calculatorframe,font=('Ariel',11,'bold'),width=52,bd=7,relief=RIDGE,height=10)
receiptframe.grid(row=5,column=0,columnspan=4)


#buttons
total=Button(calculatorframe,text="Total",bd=3,font=('Ariel',15,'bold'),command=cal)
total.grid(row=6,column=0,ipadx=14,ipady=5)
receipt=Button(calculatorframe,text="Receipt",bd=3,font=('Ariel',15,'bold'),command=receipt_generate)
receipt.grid(row=6,column=1,ipadx=14,ipady=5)
save=Button(calculatorframe,text="Save",bd=3,font=('Ariel',15,'bold'),command=saved)
save.grid(row=6,column=2,ipadx=14,ipady=5)
reset=Button(calculatorframe,text="Reset",bd=3,font=('Ariel',15,'bold'),command=reset_all)
reset.grid(row=6,column=3,ipadx=14,ipady=5)


root.mainloop()
