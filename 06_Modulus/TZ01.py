startyear = int(input("Start?"))
endyear = int(input("End?"))
for year in range(startyear, endyear + 1):
    print(year,end = ": ")
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Common year")
