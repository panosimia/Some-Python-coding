def date(day, month, year, reverse):
    if reverse:
        return str(month)+ '-' +str(day) +'-'+str(year)
    else:
        return str(day)+'-'+str(month)+'-'+str(year)



x=input("Give tha day: ")
y=input("Give the month: ")
z=input("Give the year: ")
a=input("Reverse? ")

print("The date is:", date(x,y,z,a))


      
