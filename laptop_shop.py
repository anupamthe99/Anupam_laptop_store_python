
print("\t\t\t Welcome to the Anupam Store\n\n")
products = input("Do you wanna see the products :")

if products == "yes" or products == "YES":
    print("1)Dell(Rs 80000) \n2)Asus(Rs90000)\n3)Mac(Rs 200000)")
    option = int(input("Select the option :"))
    quantity = int(input("Select the quatity :"))
    if option == 1:
        price_amt = 80000*quantity
    elif option == 2:
        price_amt = 90000*quantity
    else:
        price_amt = 200000*quantity
    # fro price without vat store garana lai 
    vat_lagna_price=price_amt
    print(f"\nYour total amount of purchased is{price_amt}\n")
    print("Delivery option \n1)Home delivery (Rs1000) \n2)Pickup (Free)")
    deleivery_option = int(input("Enter your option :"))
    if option == 1:
        price_amt = price_amt+1000
        print(f"Now your total purchased with delivery charge is {price_amt}")
    else:
        pass
    print("\nWhat type of packing style you want?:")
    print("1)Wrapper(RS 200) \n2)Bag(Rs 300) \n3)Gift(Rs500) \n4)none")
    option_packing = int(input("Select your option :"))
    if option_packing == 1:
        price_amt = price_amt+200
    elif option_packing == 2:
         price_amt = price_amt+300
    elif option_packing == 3:
         price_amt = price_amt+500
    else:
        pass
    print(f"Your total price till now is {price_amt}")
    print("Your location")
    print("1)Kathmandu(13% vat) \n2)Lalitpur \n3)Bhaktapur")
    option_location=int(input("Enter your option :"))
    if option_location==1:
        vat_lagna_price=(vat_lagna_price*13)/100
        print(f"Your total purchased is {price_amt+vat_lagna_price}")
    elif option_location==2:
        print(f"Your total price is {price_amt}")
    else:
        print(f"Your total price is {price_amt}")
        print("Thanks for buying")
else:
    print("Have a great day .")