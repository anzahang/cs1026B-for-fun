#declaring counter variables for selection of meals and beverages
pizzaCounter = 0
pastaCounter = 0
falafelCounter = 0
steakCounter = 0
beverageCounter = 0

# prompt user for number of invitees
numInvitees = int(input("Please enter the number of invitees:"))

# iterate in range of number of invitees
for i in range(numInvitees):
    #the current iteration/invitee out of total invitees
    print("Please enter the order details for invitee Number {}/{}".format(i+1,numInvitees))
    # prompting for selection
    keto = input("Do you want a keto friendly meal?")
    vegan = input("Do you want a vegan meal?")
    gluten = input("Do you want a Gluten-free meal?")
    print("--------------------")
    # conditions for each meal and beverage selection
    if(keto == "y" and vegan == "y" and gluten != "y"):
        pizzaCounter += 1
    elif(keto != "y" and vegan =="y" and gluten != "y"):
        pastaCounter += 1
    elif(keto == "y" and vegan == "y" and gluten == "y"):
        falafelCounter += 1
    elif(keto == "y" and vegan !="y" and gluten == "y"):
        steakCounter += 1
    else:
        # if none of the previous conditions are met, then invitee can only have a beverage
        beverageCounter += 1

# calculating the totals per meal selection
totalCostPizza = pizzaCounter*44.50
totalCostPasta = pastaCounter*48.99
totalCostFalafel = falafelCounter*52.99
totalCostSteak = steakCounter*49.60
totalCostBeverage = beverageCounter*5.99

# calculating order total
totalCost = totalCostPizza + totalCostPasta + totalCostFalafel + totalCostSteak + totalCostBeverage

# calculating total after tax
totalCostTax = totalCost * 1.13

# prompting for tip percentage
tip = int(input("How much do you want to tip your server (% percent)? "))
print()
# converting tip input into processable float value
percentage = float(tip*0.01)
# calculating total after tip is included
tipAmount = totalCostTax * (1+percentage)

#outputs/receipts
print("You have {:.0f} invitees with the following orders:".format(numInvitees))
print("{} invitees ordered Pizza. The cost is: ${:.2f}".format(pizzaCounter,totalCostPizza))
print("{} invitees ordered Pasta. The cost is: ${:.2f}".format(pastaCounter,totalCostPasta))
print("{} invitees ordered Falafel. The cost is: ${:.2f}".format(falafelCounter,totalCostFalafel))
print("{} invitees ordered Steak. The cost is: ${:.2f}".format(steakCounter,totalCostSteak))
print("{} invitees ordered only beverage. The cost is: ${:.2f}\n".format(beverageCounter,totalCostBeverage))

print("The total cost before tax is ${:.2f}".format(totalCost))
print("The total cost after tax is ${:.2f}".format(totalCostTax))
print("The total cost after {}% tip is ${:.0f}".format(tip,tipAmount))