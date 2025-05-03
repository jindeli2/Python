date = "8/28/2022"
time = "2:36 pm,"
bitcoinprice = float("19980.40")
print("As of",date ,"at",time,"bitcoin is currently trading at ${:,.2f}".format(bitcoinprice), "per bitcoin.")
bitcoin_amount = float (input("Enter the bitcoin amount:"))
bitcoin_dollars = bitcoin_amount * bitcoinprice
print("That is worth", bitcoin_dollars, "us dollars.")