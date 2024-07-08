qty=int(input("Enter the qty = "))
rate=int(input("Enter the rate = "))
total=qty*rate
print("Total = ", total )

disc=int(input("Enter the Discount percentage = "))
dis=(qty*rate)/disc
print("Discount = ", dis )

gst=int(input("Enter the GST = "))
bt=(qty*rate)-dis
print("Basic Total = ", bt)

tgst=(bt)*gst/100
print("Net Total = ", bt+tgst )