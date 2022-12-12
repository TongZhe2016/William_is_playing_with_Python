money = 8000
year = 1
while money >= 0 and year <= 10:
    money = money +2000*year
    for month in range(1,13):
        money = money - 1000
        print("Year"+str(year)+"Month"+str(month),end = ":")
        if money <= 0:
            print("No money lift, must go home.")
            print("")
            print("")
            print("")
            break
        print("I have enough to stay away from home.")
        print(money)
    year = year + 1
