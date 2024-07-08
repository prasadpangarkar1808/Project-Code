days=int(input("Enter number of Days = "))
year=int(days/365)
remday=days%365
print("Year of Days = " , year)

month=int(remday/30)
remmonth=remday%30
print("Month of Days = " , month)

week=int(remmonth/7)
reweek=remmonth%7
print("Week of Days = " , week)

day=int(reweek/1)
print("Remaining Days = " , day)