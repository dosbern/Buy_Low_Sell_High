import tkinter as tk
import random
import locale

locale.setlocale(locale.LC_ALL, 'em_US.UTF-8')

# set up window
window = tk.Tk()
window.title("Buy low, Sell high")
#window.geometry("440x600")

# define player variables
cash_Display = tk.StringVar()
debt_Display = tk.StringVar()
health_Display = tk.StringVar()
account_Display = tk.StringVar()
trunk_Space_Display = tk.StringVar()
trunk_Space_Total_Display = tk.StringVar()
day_Display = tk.StringVar()
location_Display = tk.StringVar()

cash = str(1000)
debt = str(3000)
health = str(100)
account = str(0)
trunk_Space = str(25)
trunk_Space_Total = str(25)
day = str(1)
location = str("Coney Island")

cash_Display.set(cash)
debt_Display.set(debt)
health_Display.set(health)
trunk_Space_Display.set(trunk_Space)
trunk_Space_Total_Display.set(trunk_Space_Total)
day_Display.set(day)
location_Display.set(location)

# define player drug variables
player_Acid_Display = tk.StringVar()
player_Exstacy_Display = tk.StringVar()
player_Speed_Display = tk.StringVar()
player_Weed_Display = tk.StringVar()
player_Shrooms_Display = tk.StringVar()
player_Hash_Display = tk.StringVar()
player_Opium_Display = tk.StringVar()
player_Heroin_Display = tk.StringVar()
player_Mescaline_Display = tk.StringVar()
player_Cocaine_Display = tk.StringVar()

player_Acid = str(0)
player_Exstacy = str(0)
player_Speed = str(0)
player_Weed = str(0)
player_Shrooms = str(0)
player_Hash = str(0)
player_Opium = str(0)
player_Heroin = str(0)
player_Mescaline = str(0)
player_Cocaine = str(0)

player_Acid_Display.set(player_Acid)
player_Exstacy_Display.set(player_Exstacy)
player_Speed_Display.set(player_Speed)
player_Weed_Display.set(player_Weed)
player_Shrooms_Display.set(player_Shrooms)
player_Hash_Display.set(player_Hash)
player_Opium_Display.set(player_Opium)
player_Heroin_Display.set(player_Mescaline)
player_Cocaine_Display.set(player_Cocaine)

# define world variables
acid_Value_Display = tk.StringVar()
exstacy_Value_Display = tk.StringVar()
speed_Value_Display = tk.StringVar()
weed_Value_Display = tk.StringVar()
shrooms_Value_Display = tk.StringVar()
hash_Value_Display = tk.StringVar()
opium_Value_Display = tk.StringVar()
heroin_Value_Display = tk.StringVar()
mescaline_Value_Display = tk.StringVar()
cocaine_Value_Display = tk.StringVar()

acid_Value = str(random.randint(20, 49))
exstacy_Value = str(random.randint(92, 134))
speed_Value = str(random.randint(123, 202))
weed_Value = str(random.randint(204, 421))
shrooms_Value = str(random.randint(470, 662))
hash_Value = str(random.randint(501, 827))
opium_Value = str(random.randint(624, 860))
heroin_Value = str(random.randint(806, 1181))
mescaline_Value = str(random.randint(2024, 2833))
cocaine_Value = str(random.randint(10120, 18133))

acid_Value_Display.set(acid_Value)
exstacy_Value_Display.set(exstacy_Value)
speed_Value_Display.set(speed_Value)
weed_Value_Display.set(weed_Value)
shrooms_Value_Display.set(shrooms_Value)
hash_Value_Display.set(hash_Value)
opium_Value_Display.set(opium_Value)
heroin_Value_Display.set(heroin_Value)
mescaline_Value_Display.set(mescaline_Value)
cocaine_Value_Display.set(cocaine_Value)

# define functions
def player_Variables_To_Int():
    global cash, debt, health, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value, day
    cash = int(cash)
    health = int(health)
    debt = int(debt)
    trunk_Space = int(trunk_Space)
    player_Acid = int(player_Acid)
    player_Exstacy = int(player_Exstacy)
    player_Speed = int(player_Speed)
    player_Weed = int(player_Weed)
    player_Shrooms = int(player_Shrooms)
    player_Hash = int(player_Hash)
    player_Opium = int(player_Opium)
    player_Heroin = int(player_Heroin)
    player_Mescaline = int(player_Mescaline)
    player_Cocaine = int(player_Cocaine)
    acid_Value = int(acid_Value)
    exstacy_Value = int(exstacy_Value)
    speed_Value = int(speed_Value)
    weed_Value = int(weed_Value)
    shrooms_Value = int(shrooms_Value)
    hash_Value = int(hash_Value)
    opium_Value = int(opium_Value)
    heroin_Value = int(heroin_Value)
    mescaline_Value = int(mescaline_Value)
    cocaine_Value = int(cocaine_Value)
    day = int(day)

def player_Variables_To_Str():
    global cash, debt, health, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value, day
    cash = str(cash)
    debt = str(debt)
    health = str(health)
    trunk_Space = str(trunk_Space)
    player_Acid = str(player_Acid)
    player_Exstacy = str(player_Exstacy)
    player_Speed = str(player_Speed)
    player_Weed = str(player_Weed)
    player_Shrooms = str(player_Shrooms)
    player_Hash = str(player_Hash)
    player_Opium = str(player_Opium)
    player_Heroin = str(player_Heroin)
    player_Mescaline = str(player_Mescaline)
    player_Cocaine = str(player_Cocaine)
    acid_Value = str(acid_Value)
    exstacy_Value = str(exstacy_Value)
    speed_Value = str(speed_Value)
    weed_Value = str(weed_Value)
    shrooms_Value = str(shrooms_Value)
    hash_Value = str(hash_Value)
    opium_Value = str(opium_Value)
    heroin_Value = str(heroin_Value)
    mescaline_Value = str(mescaline_Value)
    cocaine_Value = str(cocaine_Value)
    day = str(day)

def update_Player_Labels():
    global cash, debt, debt_Display, health, health_Display, label_Health, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value, day_Display, label_Day_Display, location, location_Display
    cash_Display.set(cash)
    label_Cash.config(text="Your Cash: $" + str(cash) + ".00")
    debt_Display.set(debt)
    label_Debt_Two_Display.config(text="$" + str(debt) + ".00")
    health_Display.set(health)
    label_Health.config(text="Your Health: " + str(health))
    trunk_Space_Display.set(trunk_Space)
    label_Trunk_Space.config(text="Trunk Space: "+ str(trunk_Space) + "/" + str(trunk_Space_Total) + " units")
    player_Acid_Display.set(player_Acid)
    label_Acid_Inventory.config(text="Acid: " + str(player_Acid) + " units")
    player_Exstacy_Display.set(player_Exstacy)
    label_Exstacy_Inventory.config(text="Exstacy: " + str(player_Exstacy) + " units")
    player_Speed_Display.set(player_Speed)
    label_Speed_Inventory.config(text="Speed: " + str(player_Speed) + " units")
    player_Weed_Display.set(player_Weed)
    label_Weed_Inventory.config(text="Weed: " + str(player_Weed) + " units")
    player_Shrooms_Display.set(player_Shrooms)
    label_Shrooms_Inventory.config(text="Shrooms: " + str(player_Shrooms) + " units")
    player_Hash_Display.set(player_Hash)
    label_Hash_Inventory.config(text="Hash: " + str(player_Hash) + " units")
    player_Opium_Display.set(player_Opium)
    label_Opium_Inventory.config(text="Opium: " + str(player_Opium) + " units")
    player_Heroin_Display.set(player_Heroin)
    label_Heroin_Inventory.config(text="Heroin: " + str(player_Heroin) + " units")
    player_Mescaline_Display.set(player_Mescaline)
    label_Mescaline_Inventory.config(text="Mescaline: " + str(player_Mescaline) + " units")
    player_Cocaine_Display.set(player_Cocaine)
    label_Cocaine_Inventory.config(text="Cocaine: " + str(player_Cocaine) + " units")
    day_Display.set(day)
    label_Day_Display.config(text="Day: " + str(day))
    location_Display.set(location)
    label_Location_Display.config(text="Location: " + location)

def update_World_Labels():
    acid_Value_Display.set(acid_Value)
    exstacy_Value_Display.set(exstacy_Value)
    speed_Value_Display.set(speed_Value)
    weed_Value_Display.set(weed_Value)
    shrooms_Value_Display.set(shrooms_Value)
    hash_Value_Display.set(hash_Value)
    opium_Value_Display.set(opium_Value)
    heroin_Value_Display.set(heroin_Value)
    mescaline_Value_Display.set(mescaline_Value)
    cocaine_Value_Display.set(cocaine_Value)
    label_Acid.config(text="Acid: $" + str(acid_Value) + ".00")
    label_Exstacy.config(text="Exstacy: $" + str(exstacy_Value) + ".00")
    label_Speed.config(text="Speed: $" + str(speed_Value) + ".00")
    label_Weed.config(text="Weed: $" + str(weed_Value) + ".00")
    label_Shrooms.config(text="Shrooms: $" + str(shrooms_Value) + ".00")
    label_Hash.config(text="Hash: $" + str(hash_Value) + ".00")
    label_Opium.config(text="Opium: $" + str(opium_Value) + ".00")
    label_Heroin.config(text="Heroin: $" + str(heroin_Value) + ".00")
    label_Mescaline.config(text="Mescaline: $" + str(mescaline_Value) + ".00")
    label_Cocaine.config(text="Cocaine: $" + str(cocaine_Value) + ".00")

def change_Button_State():
    if location == "Coney Island":
        coney_Island_Button['state'] = tk.DISABLED
        the_Ghetto_Button['state'] = tk.NORMAL
        queens_Button['state'] = tk.NORMAL
        the_Bronx_Button['state'] = tk.NORMAL
        central_Park_Button['state'] = tk.NORMAL
        Brooklyn_Button['state'] = tk.NORMAL
    if location == "The Ghetto":
        coney_Island_Button['state'] = tk.NORMAL
        the_Ghetto_Button['state'] = tk.DISABLED
        queens_Button['state'] = tk.NORMAL
        the_Bronx_Button['state'] = tk.NORMAL
        central_Park_Button['state'] = tk.NORMAL
        Brooklyn_Button['state'] = tk.NORMAL
    if location == "Queens":
        coney_Island_Button['state'] = tk.NORMAL
        the_Ghetto_Button['state'] = tk.NORMAL
        queens_Button['state'] = tk.DISABLED
        the_Bronx_Button['state'] = tk.NORMAL
        central_Park_Button['state'] = tk.NORMAL
        Brooklyn_Button['state'] = tk.NORMAL
    if location == "The Bronx":
        coney_Island_Button['state'] = tk.NORMAL
        the_Ghetto_Button['state'] = tk.NORMAL
        queens_Button['state'] = tk.NORMAL
        the_Bronx_Button['state'] = tk.DISABLED
        central_Park_Button['state'] = tk.NORMAL
        Brooklyn_Button['state'] = tk.NORMAL
    if location == "Central Park":
        coney_Island_Button['state'] = tk.NORMAL
        the_Ghetto_Button['state'] = tk.NORMAL
        queens_Button['state'] = tk.NORMAL
        the_Bronx_Button['state'] = tk.NORMAL
        central_Park_Button['state'] = tk.DISABLED
        Brooklyn_Button['state'] = tk.NORMAL
    if location == "Brooklyn":
        coney_Island_Button['state'] = tk.NORMAL
        the_Ghetto_Button['state'] = tk.NORMAL
        queens_Button['state'] = tk.NORMAL
        the_Bronx_Button['state'] = tk.NORMAL
        central_Park_Button['state'] = tk.NORMAL
        Brooklyn_Button['state'] = tk.DISABLED

def buy_Acid():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = acid_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= trunk_Space and quantity * acid_Value <= cash:
        player_Acid = player_Acid + quantity
        trunk_Space = trunk_Space - quantity
        cost = quantity * acid_Value
        cash = cash - cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(buy_Acid_Status))

def buy_Exstacy():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = exstacy_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= trunk_Space and quantity * exstacy_Value <= cash:
        player_Exstacy = player_Exstacy + quantity
        trunk_Space = trunk_Space - quantity
        cost = quantity * exstacy_Value
        cash = cash - cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(buy_Exstacy_Status))

def buy_Speed():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = speed_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= trunk_Space and quantity * speed_Value <= cash:
        player_Speed = player_Speed + quantity
        trunk_Space = trunk_Space - quantity
        cost = quantity * speed_Value
        cash = cash - cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(buy_Speed_Status))

def buy_Weed():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = weed_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= trunk_Space and quantity * weed_Value <= cash:
        player_Weed = player_Weed + quantity
        trunk_Space = trunk_Space - quantity
        cost = quantity * weed_Value
        cash = cash - cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(buy_Weed_Status))

def buy_Shrooms():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = shrooms_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= trunk_Space and quantity * shrooms_Value <= cash:
        player_Shrooms = player_Shrooms + quantity
        trunk_Space = trunk_Space - quantity
        cost = quantity * shrooms_Value
        cash = cash - cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(buy_Shrooms_Status))

def buy_Hash():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = hash_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= trunk_Space and quantity * hash_Value <= cash:
        player_Hash = player_Hash + quantity
        trunk_Space = trunk_Space - quantity
        cost = quantity * hash_Value
        cash = cash - cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(buy_Hash_Status))

def buy_Opium():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = opium_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= trunk_Space and quantity * opium_Value <= cash:
        player_Opium = player_Opium + quantity
        trunk_Space = trunk_Space - quantity
        cost = quantity * opium_Value
        cash = cash - cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(buy_Opium_Status))

def buy_Heroin():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = heroin_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= trunk_Space and quantity * heroin_Value <= cash:
        player_Heroin = player_Heroin + quantity
        trunk_Space = trunk_Space - quantity
        cost = quantity * heroin_Value
        cash = cash - cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(buy_Heroin_Status))

def buy_Mescaline():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = mescaline_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= trunk_Space and quantity * mescaline_Value <= cash:
        player_Mescaline = player_Mescaline + quantity
        trunk_Space = trunk_Space - quantity
        cost = quantity * mescaline_Value
        cash = cash - cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(buy_Mescaline_Status))

def buy_Cocaine():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = cocaine_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= trunk_Space and quantity * cocaine_Value <= cash:
        player_Cocaine = player_Cocaine + quantity
        trunk_Space = trunk_Space - quantity
        cost = quantity * cocaine_Value
        cash = cash - cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(buy_Cocaine_Status))

def sell_Acid():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = acid_Sell_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= player_Acid:
        player_Acid = player_Acid - quantity
        trunk_Space = trunk_Space + quantity
        cost = quantity * acid_Value
        cash = cash + cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(sell_Acid_Status))

def sell_Exstacy():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = exstacy_Sell_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= player_Exstacy:
        player_Exstacy = player_Exstacy - quantity
        trunk_Space = trunk_Space + quantity
        cost = quantity * exstacy_Value
        cash = cash + cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(sell_Exstacy_Status))

def sell_Speed():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = speed_Sell_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= player_Speed:
        player_Speed = player_Speed - quantity
        trunk_Space = trunk_Space + quantity
        cost = quantity * speed_Value
        cash = cash + cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(sell_Speed_Status))

def sell_Weed():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = weed_Sell_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= player_Weed:
        player_Weed = player_Weed - quantity
        trunk_Space = trunk_Space + quantity
        cost = quantity * weed_Value
        cash = cash + cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(sell_Weed_Status))

def sell_Shrooms():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = shrooms_Sell_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= player_Shrooms:
        player_Shrooms = player_Shrooms - quantity
        trunk_Space = trunk_Space + quantity
        cost = quantity * shrooms_Value
        cash = cash + cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(sell_Shrooms_Status))

def sell_Hash():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = hash_Sell_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= player_Hash:
        player_Hash = player_Hash - quantity
        trunk_Space = trunk_Space + quantity
        cost = quantity * hash_Value
        cash = cash + cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(sell_Hash_Status))

def sell_Opium():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = opium_Sell_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= player_Opium:
        player_Opium = player_Opium - quantity
        trunk_Space = trunk_Space + quantity
        cost = quantity * opium_Value
        cash = cash + cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(sell_Opium_Status))

def sell_Heroin():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = heroin_Sell_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= player_Heroin:
        player_Heroin = player_Heroin - quantity
        trunk_Space = trunk_Space + quantity
        cost = quantity * heroin_Value
        cash = cash + cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(sell_Heroin_Status))

def sell_Mescaline():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = mescaline_Sell_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= player_Mescaline:
        player_Mescaline = player_Mescaline - quantity
        trunk_Space = trunk_Space + quantity
        cost = quantity * mescaline_Value
        cash = cash + cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(sell_Mescaline_Status))

def sell_Cocaine():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value
    quantity = cocaine_Sell_Entry.get()
    quantity = int(quantity)
    player_Variables_To_Int()
    if quantity > 0 and quantity <= player_Cocaine:
        player_Cocaine = player_Cocaine - quantity
        trunk_Space = trunk_Space + quantity
        cost = quantity * cocaine_Value
        cash = cash + cost
        player_Variables_To_Str()
        update_Player_Labels()
        statusbar.config(text=random.choice(sell_Cocaine_Status))

def travel_Coney_Island():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value, day, day_Display, location
    player_Variables_To_Int()
    if cash >= 10:
        cash = cash - 10
        val1 = random.randint(20, 49)
        acid_Value = val1
        val1 = random.randint(92, 134)
        exstacy_Value = val1
        val1 = random.randint(123, 202)
        speed_Value = val1
        val1 = random.randint(204, 377)
        weed_Value = val1
        val1 = random.randint(470, 662)
        shrooms_Value = val1
        val1 = random.randint(501, 827)
        hash_Value = val1
        val1 = random.randint(624, 860)
        opium_Value = val1
        val1 = random.randint(806, 1181)
        heroin_Value = val1
        val1 = random.randint(2024, 2833)
        mescaline_Value = val1
        val1 = random.randint(10120, 18133)
        cocaine_Value = val1
        day = day + 1
        location = str("Coney Island")
        interest()
        change_Button_State()
        statusbar.config(text=random.choice(travel_Status))
    player_Variables_To_Str()
    update_Player_Labels()
    update_World_Labels()

def travel_The_Ghetto():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value, day, day_Display, location
    player_Variables_To_Int()
    if cash >= 10:
        cash = cash - 10
        val1 = random.randint(20, 49)
        acid_Value = val1
        val1 = random.randint(92, 134)
        exstacy_Value = val1
        val1 = random.randint(123, 202)
        speed_Value = val1
        val1 = random.randint(204, 377)
        weed_Value = val1
        val1 = random.randint(470, 662)
        shrooms_Value = val1
        val1 = random.randint(501, 827)
        hash_Value = val1
        val1 = random.randint(624, 860)
        opium_Value = val1
        val1 = random.randint(806, 1181)
        heroin_Value = val1
        val1 = random.randint(2024, 2833)
        mescaline_Value = val1
        val1 = random.randint(10120, 18133)
        cocaine_Value = val1
        day = day + 1
        location = str("The Ghetto")
        interest()
        change_Button_State()
        statusbar.config(text=random.choice(travel_Status))
    player_Variables_To_Str()
    update_Player_Labels()
    update_World_Labels()

def travel_Queens():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value, day, day_Display, location
    player_Variables_To_Int()
    if cash >= 10:
        cash = cash - 10
        val1 = random.randint(20, 49)
        acid_Value = val1
        val1 = random.randint(92, 134)
        exstacy_Value = val1
        val1 = random.randint(123, 202)
        speed_Value = val1
        val1 = random.randint(204, 377)
        weed_Value = val1
        val1 = random.randint(470, 662)
        shrooms_Value = val1
        val1 = random.randint(501, 827)
        hash_Value = val1
        val1 = random.randint(624, 860)
        opium_Value = val1
        val1 = random.randint(806, 1181)
        heroin_Value = val1
        val1 = random.randint(2024, 2833)
        mescaline_Value = val1
        val1 = random.randint(10120, 18133)
        cocaine_Value = val1
        day = day + 1
        location = str("Queens")
        interest()
        change_Button_State()
        statusbar.config(text=random.choice(travel_Status))
    player_Variables_To_Str()
    update_Player_Labels()
    update_World_Labels()

def travel_The_Bronx():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value, day, day_Display, location
    player_Variables_To_Int()
    if cash >= 10:
        cash = cash - 10
        val1 = random.randint(20, 49)
        acid_Value = val1
        val1 = random.randint(92, 134)
        exstacy_Value = val1
        val1 = random.randint(123, 202)
        speed_Value = val1
        val1 = random.randint(204, 377)
        weed_Value = val1
        val1 = random.randint(470, 662)
        shrooms_Value = val1
        val1 = random.randint(501, 827)
        hash_Value = val1
        val1 = random.randint(624, 860)
        opium_Value = val1
        val1 = random.randint(806, 1181)
        heroin_Value = val1
        val1 = random.randint(2024, 2833)
        mescaline_Value = val1
        val1 = random.randint(10120, 18133)
        cocaine_Value = val1
        day = day + 1
        location = str("The Bronx")
        interest()
        change_Button_State()
        statusbar.config(text=random.choice(travel_Status))
    player_Variables_To_Str()
    update_Player_Labels()
    update_World_Labels()

def travel_Central_Park():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value, day, day_Display, location
    player_Variables_To_Int()
    if cash >= 10:
        cash = cash - 10
        val1 = random.randint(20, 49)
        acid_Value = val1
        val1 = random.randint(92, 134)
        exstacy_Value = val1
        val1 = random.randint(123, 202)
        speed_Value = val1
        val1 = random.randint(204, 377)
        weed_Value = val1
        val1 = random.randint(470, 662)
        shrooms_Value = val1
        val1 = random.randint(501, 827)
        hash_Value = val1
        val1 = random.randint(624, 860)
        opium_Value = val1
        val1 = random.randint(806, 1181)
        heroin_Value = val1
        val1 = random.randint(2024, 2833)
        mescaline_Value = val1
        val1 = random.randint(10120, 18133)
        cocaine_Value = val1
        day = day + 1
        location = str("Central Park")
        interest()
        change_Button_State()
        statusbar.config(text=random.choice(travel_Status))
    player_Variables_To_Str()
    update_Player_Labels()
    update_World_Labels()

def travel_Brooklyn():
    global cash, trunk_Space, player_Acid, player_Exstacy, player_Speed, player_Weed, player_Shrooms, player_Hash, player_Opium, player_Heroin, player_Mescaline, player_Cocaine, acid_Value, exstacy_Value, speed_Value, weed_Value, shrooms_Value, hash_Value, opium_Value, heroin_Value, mescaline_Value, cocaine_Value, day, day_Display, location
    player_Variables_To_Int()
    if cash >= 10:
        cash = cash - 10
        val1 = random.randint(20, 49)
        acid_Value = val1
        val1 = random.randint(92, 134)
        exstacy_Value = val1
        val1 = random.randint(123, 202)
        speed_Value = val1
        val1 = random.randint(204, 377)
        weed_Value = val1
        val1 = random.randint(470, 662)
        shrooms_Value = val1
        val1 = random.randint(501, 827)
        hash_Value = val1
        val1 = random.randint(624, 860)
        opium_Value = val1
        val1 = random.randint(806, 1181)
        heroin_Value = val1
        val1 = random.randint(2024, 2833)
        mescaline_Value = val1
        val1 = random.randint(10120, 18133)
        cocaine_Value = val1
        day = day + 1
        location = str("Brooklyn")
        interest()
        change_Button_State()
        statusbar.config(text=random.choice(travel_Status))
    player_Variables_To_Str()
    update_Player_Labels()
    update_World_Labels()

def deposit_Cash():
    global cash, account, account_Display
    cash = int(cash)
    account = int(account)
    amount = bank_Entry.get()
    amount = int(amount)
    if amount > 0 and amount <= cash:
        account = account + amount
        cash = cash - amount
        statusbar.config(text=random.choice(bank_Deposit_Approved_Status))
    cash = str(cash)
    account = str(account)
    cash_Display.set(cash)
    label_Cash.config(text="Your Cash: $" + str(cash) + ".00")
    account_Display.set(account)
    label_Account_Two_Display.config(text="$" + str(account) + ".00")

def withdraw_Cash():
    global cash, account, account_Display
    cash = int(cash)
    account = int(account)
    amount = bank_Entry.get()
    amount = int(amount)
    if amount > 0 and amount <= account:
        account = account - amount
        cash = cash + amount
        statusbar.config(text=random.choice(bank_Withdraw_Approved_Status))
    if amount > 0 and amount > account:
        statusbar.config(text=random.choice(bank_Withdraw_Denied_Insufficient_Status))
    cash = str(cash)
    account = str(account)
    cash_Display.set(cash)
    label_Cash.config(text="Your Cash: $" + str(cash) + ".00")
    account_Display.set(account)
    label_Account_Two_Display.config(text="$" + str(account) + ".00")

def rob_Bank():
    global cash, account, label_Account_Two_Display, health
    success_Chance = random.randint(1, 10)
    cash = int(cash)
    account = int(account)
    health = int(health)
    if success_Chance == 5:
        cash = cash + 743856
        account = 0
        cash = str(cash)
        account = str(account)
        cash_Display.set(cash)
        label_Cash.config(text="Your Cash: $" + str(cash) + ".00")
        account_Display.set(account)
        label_Account_Two_Display.config(text="$" + str(account) + ".00")
        statusbar.config(text="You did it! You made it out with $743,856!")
    else:
        health = health - 65
        statusbar.config(text=random.choice(rob_Bank_Fail_Status))
        label_Health.config(text="Your health: " + str(health))
    cash = str(cash)
    account = str(account)
    health = str(health)

def interest():
    global debt, debt_Display, account, label_Account_Two_Display
    debt = debt + (debt * 0.02)
    debt = round(debt)
    debt = str(debt)
    debt_Display.set(debt)
    label_Debt_Two_Display.config(text="$" + str(debt) + ".00")
    account = int(account)
    account = account + (account * 0.005)
    account = round(account)
    account = str(account)
    account_Display.set(account)
    label_Account_Two_Display.config(text="$" + str(account) + ".00")

def borrow_Cash():
    global debt, debt_Display, cash
    debt = int(debt)
    cash = int(cash)
    amount = loan_Entry.get()
    amount = int(amount)
    if amount > 0 and debt > 0:
        statusbar.config(text=random.choice(debt_Borrow_Denied_Outstanding_Status))
    if amount > 0 and debt == 0 and amount <= 10000:
        cash = cash + amount
        debt = debt + amount
        statusbar.config(text=random.choice(debt_Borrow_Approved_Status))
    if amount > 0 and debt == 0 and amount > 10000:
        statusbar.config(text=random.choice(debt_Borrow_Denied_High_Status))
    cash = str(cash)
    debt = str(debt)
    cash_Display.set(cash)
    label_Cash.config(text="Your Cash: $" + str(cash) + ".00")
    debt_Display.set(debt)
    label_Debt_Two_Display.config(text="$" + str(debt) + ".00")

def make_Payment():
    global debt, debt_Display, cash
    debt = int(debt)
    cash = int(cash)
    amount = loan_Entry.get()
    amount = int(amount)
    if amount > 0 and cash >= amount:
        if amount <= debt:
            cash = cash - amount
            debt = debt - amount
            statusbar.config(text=random.choice(debt_Payment_Status))
    cash = str(cash)
    debt = str(debt)
    cash_Display.set(cash)
    label_Cash.config(text="Your Cash: $" + str(cash) + ".00")
    debt_Display.set(debt)
    label_Debt_Two_Display.config(text="$" + str(debt) + ".00")

def rob_Bank_Warning_On(event):
    rob_Bank_Button["bg"] = "red"

def rob_Bank_Warning_Off(event):
    rob_Bank_Button["bg"] = "SystemButtonFace"

# set up frame layout
#title_Display = tk.Label(master=window, text="This is a Title", font=("TkDefaultFont", 16))

frame_Info = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_Info.grid(row=0, column=0, padx=5, pady=5)
frame_Bank = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_Bank.grid(row=0, column=1, padx=5, pady=5)
frame_Loan = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_Loan.grid(row=0, column=2, padx=5, pady=5)
frame_Travel = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_Travel.grid(row=0, column=3, padx=5, pady=5)
frame_Item = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_Item.grid(row=1, column=0, padx=5, pady=5)
frame_Inventory = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_Inventory.grid(row=1, column=1, padx=5, pady=5)
frame_Buy = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_Buy.grid(row=1, column=2, padx=5, pady=5)
frame_Sell = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_Sell.grid(row=1, column=3, padx=5, pady=5)

# frame_Info
label_Info_Title = tk.Label(master=frame_Info, text="Your Information:", font=("TkDefaultFont", 12))
label_Info_Title.grid(row=0)
label_Cash = tk.Label(master=frame_Info, text="Your Cash: $" + str(cash) + ".00")
label_Cash.grid(row=1)
label_Health = tk.Label(master=frame_Info, text="Your health: " + str(health))
label_Health.grid(row=2)
label_Trunk_Space = tk.Label(master=frame_Info, text="Trunk Space: "+ str(trunk_Space) + "/" + str(trunk_Space_Total) + " units")
label_Trunk_Space.grid(row=3)
label_Day_Display = tk.Label(master=frame_Info, text="Day: " + str(day))
label_Day_Display.grid(row=4)
label_Location_Display = tk.Label(master=frame_Info, text="Location: " + location)
label_Location_Display.grid(row=5)

# frame_Bank
label_Bank_Title = tk.Label(master=frame_Bank, text="The Bank:", font=("TkDefaultFont", 12))
label_Bank_Title.grid(row=0, columnspan=2)
bank_Entry = tk.Entry(master=frame_Bank, width=12)
bank_Entry.grid(row=1, columnspan=2)
bank_Entry.insert(0, str(0))
deposit_Button = tk.Button(master=frame_Bank, text="Deposit", command=deposit_Cash)
deposit_Button.grid(row=2, column=0)
withdraw_Button = tk.Button(master=frame_Bank, text="Withdraw", command=withdraw_Cash)
withdraw_Button.grid(row=3, column=0)
label_Account_Display = tk.Label(master=frame_Bank, text="Account Balance:")
label_Account_Display.grid(row=4, column=0)
label_Account_Two_Display = tk.Label(master=frame_Bank, text="$" + str(account) + ".00")
label_Account_Two_Display.grid(row=5, column=0)
rob_Bank_Button = tk.Button(master=frame_Bank, text="Rob the Joint!", command=rob_Bank)
rob_Bank_Button.grid(row=6, column=0)
rob_Bank_Button.bind("<Enter>", rob_Bank_Warning_On)
rob_Bank_Button.bind("<Leave>", rob_Bank_Warning_Off)



# frame_Loan
label_Loan_Title = tk.Label(master=frame_Loan, text="Loan Shark:", font=("TkDefaultFont", 12))
label_Loan_Title.grid(row=0, columnspan=2)
loan_Entry = tk.Entry(master=frame_Loan, width=12)
loan_Entry.grid(row=1, columnspan=2)
loan_Entry.insert(0, str(0))
make_Payment_Button = tk.Button(master=frame_Loan, text="Make Payment", command=make_Payment)
make_Payment_Button.grid(row=2, column=0)
borrow_Cash_Button = tk.Button(master=frame_Loan, text="Borrow Cash", command=borrow_Cash)
borrow_Cash_Button.grid(row=3, column=0)
label_Debt_Display = tk.Label(master=frame_Loan, text="You owe:")
label_Debt_Display.grid(row=4)
label_Debt_Two_Display = tk.Label(master=frame_Loan, text="$" + str(debt) + ".00")
label_Debt_Two_Display.grid(row=5)

# frame_Travel
label_Travel_Title = tk.Label(master=frame_Travel, text="Travel to:", font=("TkDefaultFont", 12))
label_Travel_Title.grid(row=0, column=0, columnspan=2)
coney_Island_Button = tk.Button(master=frame_Travel, text="Coney Island", command=travel_Coney_Island, state=tk.DISABLED)
coney_Island_Button.grid(row=1, column=0, padx=4, pady=4)
the_Ghetto_Button = tk.Button(master=frame_Travel, text="The Ghetto", command=travel_The_Ghetto, state=tk.NORMAL)
the_Ghetto_Button.grid(row=2, column=0, padx=4, pady=4)
queens_Button = tk.Button(master=frame_Travel, text="Queens", command=travel_Queens, state=tk.NORMAL)
queens_Button.grid(row=3, column=0, padx=4, pady=4)
the_Bronx_Button = tk.Button(master=frame_Travel, text="The Bronx", command=travel_The_Bronx, state=tk.NORMAL)
the_Bronx_Button.grid(row=4, column=0, padx=4, pady=4)
central_Park_Button = tk.Button(master=frame_Travel, text="Central Park", command=travel_Central_Park, state=tk.NORMAL)
central_Park_Button.grid(row=5, column=0, padx=4, pady=4)
Brooklyn_Button = tk.Button(master=frame_Travel, text="Brooklyn", command=travel_Brooklyn, state=tk.NORMAL)
Brooklyn_Button.grid(row=6, column=0, padx=4, pady=4)

# frame_Item
label_Item_Title = tk.Label(master=frame_Item, text="Current Prices:", font=("TkDefaultFont", 12))
label_Item_Title.grid(row=0)
label_Acid = tk.Label(master=frame_Item, text="Acid: $" + str(acid_Value) + ".00")
label_Acid.grid(row=1, padx=2.5, pady=2.5)
label_Exstacy = tk.Label(master=frame_Item, text="Exstacy: $" + str(exstacy_Value) + ".00")
label_Exstacy.grid(row=2, padx=2.25, pady=2.25)
label_Speed = tk.Label(master=frame_Item, text="Speed: $" + str(speed_Value) + ".00")
label_Speed.grid(row=3, padx=2.25, pady=2.25)
label_Weed = tk.Label(master=frame_Item, text="Weed: $" + str(weed_Value) + ".00")
label_Weed.grid(row=4, padx=2.25, pady=2.25)
label_Shrooms = tk.Label(master=frame_Item, text="Shrooms: $" + str(shrooms_Value) + ".00")
label_Shrooms.grid(row=5, padx=2.25, pady=2.25)
label_Hash = tk.Label(master=frame_Item, text="Hash: $" + str(hash_Value) + ".00")
label_Hash.grid(row=6, padx=2.25, pady=2.25)
label_Opium = tk.Label(master=frame_Item, text="Opium: $" + str(opium_Value) + ".00")
label_Opium.grid(row=7, padx=2.25, pady=2.25)
label_Heroin = tk.Label(master=frame_Item, text="Heroin: $" + str(heroin_Value) + ".00")
label_Heroin.grid(row=8, padx=2.25, pady=2.25)
label_Mescaline = tk.Label(master=frame_Item, text="Mescaline: $" + str(mescaline_Value) + ".00")
label_Mescaline.grid(row=9, padx=2.25, pady=2.25)
label_Cocaine = tk.Label(master=frame_Item, text="Cocaine: $" + str(cocaine_Value) + ".00")
label_Cocaine.grid(row=10, padx=2.25, pady=2.25)

# frame_Inventory
label_Inventory = tk.Label(master=frame_Inventory, text="Your Trunk Contents:", font=("TkDefaultFont", 12))
label_Inventory.grid(row=0)
label_Acid_Inventory = tk.Label(master=frame_Inventory, text="Acid: " + str(player_Acid) + " units")
label_Acid_Inventory.grid(row=1, padx=2, pady=2)
label_Exstacy_Inventory = tk.Label(master=frame_Inventory, text="Exstacy: " + str(player_Exstacy) + " units")
label_Exstacy_Inventory.grid(row=2, padx=2, pady=2)
label_Speed_Inventory = tk.Label(master=frame_Inventory, text="Speed: " + str(player_Speed) + " units")
label_Speed_Inventory.grid(row=3, padx=2, pady=2)
label_Weed_Inventory = tk.Label(master=frame_Inventory, text="Weed: " + str(player_Weed) + " units")
label_Weed_Inventory.grid(row=4, padx=2, pady=2)
label_Shrooms_Inventory = tk.Label(master=frame_Inventory, text="Shrooms: " + str(player_Shrooms) + " units")
label_Shrooms_Inventory.grid(row=5, padx=2, pady=2)
label_Hash_Inventory = tk.Label(master=frame_Inventory, text="Hash: " + str(player_Hash) + " units")
label_Hash_Inventory.grid(row=6, padx=2, pady=2)
label_Opium_Inventory = tk.Label(master=frame_Inventory, text="Opium: " + str(player_Opium) + " units")
label_Opium_Inventory.grid(row=7, padx=2, pady=2)
label_Heroin_Inventory = tk.Label(master=frame_Inventory, text="Heroin: " + str(player_Heroin) + " units")
label_Heroin_Inventory.grid(row=8, padx=2, pady=2)
label_Mescaline_Inventory = tk.Label(master=frame_Inventory, text="Mescaline: " + str(player_Mescaline) + " units")
label_Mescaline_Inventory.grid(row=9, padx=2, pady=2)
label_Cocaine_Inventory = tk.Label(master=frame_Inventory, text="Cocaine: " + str(player_Cocaine) + " units")
label_Cocaine_Inventory.grid(row=10, padx=2, pady=2)

# frame_Buy
label_Buy_Title = tk.Label(master=frame_Buy, text="Buy Some Drugs:", font=("TkDefaultFont", 12))
label_Buy_Title.grid(row=0, column=0, columnspan=2)

acid_Entry = tk.Entry(master=frame_Buy, width=6)
acid_Entry.grid(row=1, column=0)
acid_Entry.insert(0, str(1))
acid_Button = tk.Button(master=frame_Buy, text="Buy Acid", command=buy_Acid)
acid_Button.grid(row=1, column=1)

exstacy_Entry = tk.Entry(master=frame_Buy, width=6)
exstacy_Entry.grid(row=2, column=0)
exstacy_Entry.insert(0, str(1))
exstacy_Button = tk.Button(master=frame_Buy, text="Buy Exstacy", command=buy_Exstacy)
exstacy_Button.grid(row=2, column=1)

speed_Entry = tk.Entry(master=frame_Buy, width=6)
speed_Entry.grid(row=3, column=0)
speed_Entry.insert(0, str(1))
speed_Button = tk.Button(master=frame_Buy, text="Buy Speed", command=buy_Speed)
speed_Button.grid(row=3, column=1)

weed_Entry = tk.Entry(master=frame_Buy, width=6)
weed_Entry.grid(row=4, column=0)
weed_Entry.insert(0, str(1))
weed_Button = tk.Button(master=frame_Buy, text="Buy Weed", command=buy_Weed)
weed_Button.grid(row=4, column=1)

shrooms_Entry = tk.Entry(master=frame_Buy, width=6)
shrooms_Entry.grid(row=5, column=0)
shrooms_Entry.insert(0, str(1))
shrooms_Button = tk.Button(master=frame_Buy, text="Buy Shrooms", command=buy_Shrooms)
shrooms_Button.grid(row=5, column=1)

hash_Entry = tk.Entry(master=frame_Buy, width=6)
hash_Entry.grid(row=6, column=0)
hash_Entry.insert(0, str(1))
hash_Button = tk.Button(master=frame_Buy, text="Buy Hash", command=buy_Hash)
hash_Button.grid(row=6, column=1)

opium_Entry = tk.Entry(master=frame_Buy, width=6)
opium_Entry.grid(row=7, column=0)
opium_Entry.insert(0, str(1))
opium_Button = tk.Button(master=frame_Buy, text="Buy Opium", command=buy_Opium)
opium_Button.grid(row=7, column=1)

heroin_Entry = tk.Entry(master=frame_Buy, width=6)
heroin_Entry.grid(row=8, column=0)
heroin_Entry.insert(0, str(1))
heroin_Button = tk.Button(master=frame_Buy, text="Buy Heroin", command=buy_Heroin)
heroin_Button.grid(row=8, column=1)

mescaline_Entry = tk.Entry(master=frame_Buy, width=6)
mescaline_Entry.grid(row=9, column=0)
mescaline_Entry.insert(0, str(1))
mescaline_Button = tk.Button(master=frame_Buy, text="Buy Mescaline", command=buy_Mescaline)
mescaline_Button.grid(row=9, column=1)

cocaine_Entry = tk.Entry(master=frame_Buy, width=6)
cocaine_Entry.grid(row=10, column=0)
cocaine_Entry.insert(0, str(1))
cocaine_Button = tk.Button(master=frame_Buy, text="Buy Cocaine", command=buy_Cocaine)
cocaine_Button.grid(row=10, column=1)

# frame_Sell
label_Sell_Title = tk.Label(master=frame_Sell, text="Sell Your Drugs:", font=("TkDefaultFont", 12))
label_Sell_Title.grid(row=0, column=0, columnspan=2)

acid_Sell_Entry = tk.Entry(master=frame_Sell, width=6)
acid_Sell_Entry.grid(row=1, column=0)
acid_Sell_Entry.insert(0, str(1))
acid_Sell_Button = tk.Button(master=frame_Sell, text="Sell Acid", command=sell_Acid)
acid_Sell_Button.grid(row=1, column=1)

exstacy_Sell_Entry = tk.Entry(master=frame_Sell, width=6)
exstacy_Sell_Entry.grid(row=2, column=0)
exstacy_Sell_Entry.insert(0, str(1))
exstacy_Sell_Button = tk.Button(master=frame_Sell, text="Sell Exstacy", command=sell_Exstacy)
exstacy_Sell_Button.grid(row=2, column=1)

speed_Sell_Entry = tk.Entry(master=frame_Sell, width=6)
speed_Sell_Entry.grid(row=3, column=0)
speed_Sell_Entry.insert(0, str(1))
speed_Sell_Button = tk.Button(master=frame_Sell, text="Sell Speed", command=sell_Speed)
speed_Sell_Button.grid(row=3, column=1)

weed_Sell_Entry = tk.Entry(master=frame_Sell, width=6)
weed_Sell_Entry.grid(row=4, column=0)
weed_Sell_Entry.insert(0, str(1))
weed_Sell_Button = tk.Button(master=frame_Sell, text="Sell Weed", command=sell_Weed)
weed_Sell_Button.grid(row=4, column=1)

shrooms_Sell_Entry = tk.Entry(master=frame_Sell, width=6)
shrooms_Sell_Entry.grid(row=5, column=0)
shrooms_Sell_Entry.insert(0, str(1))
shrooms_Sell_Button = tk.Button(master=frame_Sell, text="Sell Shrooms", command=sell_Shrooms)
shrooms_Sell_Button.grid(row=5, column=1)

hash_Sell_Entry = tk.Entry(master=frame_Sell, width=6)
hash_Sell_Entry.grid(row=6, column=0)
hash_Sell_Entry.insert(0, str(1))
hash_Sell_Button = tk.Button(master=frame_Sell, text="Sell Hash", command=sell_Hash)
hash_Sell_Button.grid(row=6, column=1)

opium_Sell_Entry = tk.Entry(master=frame_Sell, width=6)
opium_Sell_Entry.grid(row=7, column=0)
opium_Sell_Entry.insert(0, str(1))
opium_Sell_Button = tk.Button(master=frame_Sell, text="Sell Opium", command=sell_Opium)
opium_Sell_Button.grid(row=7, column=1)

heroin_Sell_Entry = tk.Entry(master=frame_Sell, width=6)
heroin_Sell_Entry.grid(row=8, column=0)
heroin_Sell_Entry.insert(0, str(1))
heroin_Sell_Button = tk.Button(master=frame_Sell, text="Sell Heroin", command=sell_Heroin)
heroin_Sell_Button.grid(row=8, column=1)

mescaline_Sell_Entry = tk.Entry(master=frame_Sell, width=6)
mescaline_Sell_Entry.grid(row=9, column=0)
mescaline_Sell_Entry.insert(0, str(1))
mescaline_Sell_Button = tk.Button(master=frame_Sell, text="Sell Mescaline", command=sell_Mescaline)
mescaline_Sell_Button.grid(row=9, column=1)

cocaine_Sell_Entry = tk.Entry(master=frame_Sell, width=6)
cocaine_Sell_Entry.grid(row=10, column=0)
cocaine_Sell_Entry.insert(0, str(1))
cocaine_Sell_Button = tk.Button(master=frame_Sell, text="Sell Cocaine", command=sell_Cocaine)
cocaine_Sell_Button.grid(row=10, column=1)

# status bar
statusbar = tk.Label(master=window, text="  Status Bar", bd=1, relief=tk.SUNKEN, anchor="w")
statusbar.grid(row=11, column=0, columnspan=4, sticky="WE", ipady=3)

travel_Status = ["  You spent 10 dollars on gas!",
                 "  It cost you 10 bucks to travel!",
                 "  You burned 10 dollars worth of fuel!"]

debt_Payment_Status = ["  Thank you for your payment!",
                  "  Paying your debts is a good idea!",
                  "  Your money went to a good home!"]

debt_Borrow_Approved_Status = ["  You borrowed some cash from the loan shark!",
                          "  The loan shark lent you some money!"]

debt_Borrow_Denied_High_Status = ["  Woah, no one is letting you borrow that much cash!",
                             "  That's a little excessive, don't you think?"]

debt_Borrow_Denied_Outstanding_Status = ["  You must pay off your debt before borrowing more money!",
                                    "  Try paying back what you owe, first!"]

bank_Deposit_Approved_Status = ["  You deposited some cash!"]

bank_Deposit_Denied_Insufficient_Status = ["  You don't have enough cash to deposit that much!",
                                           "  Insufficient funds!"]

bank_Withdraw_Approved_Status = ["  You withdrew some cash!"]

bank_Withdraw_Denied_Insufficient_Status = ["  There's not enough money in your account to withdraw that much!"]

rob_Bank_Fail_Status = ["  Oh no! You failed!",
                        "  That was a bad idea!"]

buy_Acid_Status = ["  You bought some Acid!"]
buy_Exstacy_Status = ["  You bought some Exstacy!"]
buy_Speed_Status = ["  You bought some Speed!"]
buy_Weed_Status = ["  You bought some Weed!"]
buy_Shrooms_Status = ["  You bought some Shrooms!"]
buy_Hash_Status = ["  You bought some Hash!"]
buy_Opium_Status = ["  You bought some Opium!"]
buy_Heroin_Status = ["  You bought some Heroin!"]
buy_Mescaline_Status = ["  You bought some Mescaline!"]
buy_Cocaine_Status = ["  You bought some Cocaine!"]

sell_Acid_Status = ["  You sold some Acid!"]
sell_Exstacy_Status = ["  You sold some Exstacy!"]
sell_Speed_Status = ["  You sold some Speed!"]
sell_Weed_Status = ["  You sold some Weed!"]
sell_Shrooms_Status = ["  You sold some Shrooms!"]
sell_Hash_Status = ["  You sold some Hash!"]
sell_Opium_Status = ["  You sold some Opium!"]
sell_Heroin_Status = ["  You sold some Heroin!"]
sell_Mescaline_Status = ["  You sold some Mescaline!"]
sell_Cocaine_Status = ["  You sold some Cocaine!"]

#    statusbar.set()
#    statusbar.config(text="  You spent 10 dollars on gas!")

# '{:,}'.format()

window.mainloop()