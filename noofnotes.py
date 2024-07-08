a=int(input("Enter amount in Rs = "))
rs= int(a/2000)
rsq=a%2000
print("Number of 2000 notes =  " ,rs)

rss=int(rsq/500)
rsw=rsq%500
print("Number of 500 notes =  " ,rss)

rsss=int(rsw/200)
rse=rsw%200
print("Number of 200 notes =  " ,rsss)

rssss=int(rse/100)
rsr=rse%100
print("Number of 100 notes =  " ,rssss)

rsssss=int(rsr/50)
print("Number of 50 notes =  " ,rsssss)





