import datetime

monthDict = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}

year = int(input("Enter a year: "))
month = input("Enter a month: ")
day = int(input("Enter day: "))

date = datetime.datetime(year, monthDict[month], day)
formattedDate = datetime.date.strftime(date, "%d/%m/%Y")
dateNumber = "".join(formattedDate.split("/"))

print(dateNumber == dateNumber[::-1])
