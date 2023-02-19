SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]
PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2',
'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC',
1099.99]]

totalOrder = []
def pickItems():
    print("Welcome to my PC shop!\n")

    while True:
        decision = input(
            "Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)\n")
        if decision.isdigit():
            decision = int(decision)
            if decision in [1, 2, 3]:
                if decision == 1:
                    customPC()
                elif decision == 2:
                    preBuilt()
                elif decision == 3:
                    checkOut()
                    break

def customPC():
    total = 0
    print("Great! Let's start building your PC")
    print("First, lets pick a CPU.")
    print("1 : {}, {}".format(CPU[0][1], CPU[0][2]))
    print("2 : {}, {}".format(CPU[1][1], CPU[1][2]))

    while True:
        cpu = input("Choose the number that corresponds with the part you want: ")
        if cpu.isdigit() and int(cpu) in [1, 2]:  # check if input is valid
            cpu = int(cpu)
            print("Next, let's pick a compatible motherboard.")
            if cpu == 1:
                total += CPU[0][2]
                print("2 : {}, {}".format(MOTHERBOARD[1][1], MOTHERBOARD[1][2]))
                while True:
                    mb = input("Choose the number that corresponds with the part you want: ")
                    if mb.isdigit():
                        mb = int(mb)
                        if mb == 2:
                            total += MOTHERBOARD[1][2]
                            break
            elif cpu == 2:
                total += CPU[1][2]
                print("1 : {}, {}".format(MOTHERBOARD[0][1], MOTHERBOARD[0][2]))
                while True:
                    mb = input("Choose the number that corresponds with the part you want: ")
                    if mb.isdigit():
                        mb = int(mb)
                        if mb == 1:
                            total += MOTHERBOARD[0][2]
                            break
            break

    print("Next, let's pick your RAM.")
    print("1 : {}, {}".format(RAM[0][1],RAM[0][2]))
    print("2 : {}, {}".format(RAM[1][1], RAM[1][2]))
    while True:
        ram = input("Choose the number that corresponds with the part you want: ")
        if ram.isdigit():
            ram = int(ram)
            if ram == 1:
                total+= RAM[0][2]
                break
            elif ram == 2:
                total+= RAM[1][2]
                break
    print("Next, let's pick your PSU.")
    print("1 : {}, {}".format(PSU[0][1], PSU[0][2]))
    while True:
        psu = input("Choose the number that corresponds with the part you want: ")
        if psu.isdigit():
            psu = int(psu)
            if psu == 1:
                total += PSU[0][2]
                break
    print("Next, lets pick your case.")
    print("1 : {}, {}".format(CASE[0][1],CASE[0][2]))
    print("2 : {}, {}".format(CASE[1][1],CASE[1][2]))
    while True:
        case = input("Choose the number that corresponds with the part you want: ")
        if case.isdigit():
            case = int(case)
            if case == 1:
                total+=CASE[0][2]
                break
            elif case == 2:
                total+=CASE[1][2]
                break
    print("Next, let's pick an SSD (optional, but you must have at least one SSD or HDD).")
    for option in SSD:
        print("{} : {}, {}".format(option[0], option[1], option[2]))

    while True:
        ssd_choice = input("Choose the number that corresponds with the part you want (or X to not get an SSD): ")
        if ssd_choice.upper() == "X":
            ssd_price = 0
            hdd_required = True
            break
        elif ssd_choice.isdigit() and int(ssd_choice) in range(1, len(SSD) + 1):
            ssd_price = SSD[int(ssd_choice) - 1][2]
            hdd_required = False
            break

    if hdd_required:
        print("Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
        for option in HDD:
            print("{} : {}, {}".format(option[0], option[1], option[2]))
        while True:
            hdd_choice = input("Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD): ")
            if hdd_choice.upper() == "X":
                hdd_price = 0
                continue
            elif hdd_choice.isdigit() and int(hdd_choice) in range(1, len(HDD) + 1):
                hdd_price = HDD[int(hdd_choice) - 1][2]
                break
    else:
        print("Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
        for option in HDD:
            print("{} : {}, {}".format(option[0], option[1], option[2]))
        while True:
            hdd_choice = input("Choose the number that corresponds with the part you want(or X to not get an HDD): ")
            if hdd_choice.upper() == "X":
                hdd_price = 0
                break
            elif hdd_choice.isdigit() and int(hdd_choice) in range(1, len(HDD) + 1):
                hdd_price = HDD[int(hdd_choice) - 1][2]
                break

    total += ssd_price
    total += hdd_price

    print("Finally, lets pick your graphics card (or X to not get a graphics card).")
    print("1 : {}, {}".format(GRAPHICS_CARD[0][1], GRAPHICS_CARD[0][2]))
    while(True):
        gpu = input("Choose the number that corresponds with the part you want: ")
        if gpu.upper() == "X":
            break
        elif gpu.isdigit():
            gpu = int(gpu)
            if gpu == 1:
                total+= GRAPHICS_CARD[0][2]
                break
    totalOrder.append(total)
    print("You have selected all your parts! Your total for this PC is ${}".format(total))

def preBuilt():
    total = 0
    print("Great! Let's pick a pre-built PC!")
    print("Which prebuilt would you like to order?")

    for i in range(len(PREBUILTS)):
        print("{} : {}, {}".format(PREBUILTS[i][0],PREBUILTS[i][1],PREBUILTS[1][2]))
    while True:
        prebuilt = input("Choose the number that corresponds with the part you want: ")
        if prebuilt.isdigit():
            prebuilt = int(prebuilt)
            if prebuilt == 1:
                total += PREBUILTS[0][2]
                break
            elif prebuilt == 2:
                total += PREBUILTS[1][2]
                break
            elif prebuilt == 3:
                total += PREBUILTS[2][2]
                break
    totalOrder.append(total)
    print("Your total price for this pre-built is ${}".format(total))

def checkOut():
    print(totalOrder)
pickItems()