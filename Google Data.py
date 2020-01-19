import csv
from datetime import datetime

path="/home/renzan/Desktop/Python/czv/Google Stock Market Data - google_stock_data.csv.csv"
file=open(path, newline= '')
reader=csv.reader(file)

header=next(reader)

data=[]
for row in reader:
    date=datetime.strptime(row[0], '%m/%d/%Y')      # strptime means string-parse-time where the first argument is the string and the second argument is the format
    open_price=float(row[1])
    high=float(row[2])
    low=float(row[3])
    close=float(row[4])
    volume=int(row[5])
    adj_close=float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])    #here, data is a list of lists where each list represents a day in trading.
                                                                            #suppose we have list number 499 out of 500 lists, which means this is the 449th day
    print(data[0])

    #Compute and store daily stock returns

    returns_path="/home/renzan/Desktop/Python/czv/GOOG.csv"
    file2=open(returns_path, 'w')
    writer2=csv.writer(file2)
    writer2.writerow(["Date", "Return"])

    print(writer2)

    for i in range(len(data)-1):
        todays_row=data[i]
        todays_date=todays_row[0]
        todays_price=todays_row[1]
        yesterdays_row=data[i+1]
        yesterdays_price=yesterdays_row[-1]

        daily_return=(todays_price-yesterdays_price)/yesterdays_price
        formatted_date=todays_date.strftime('%m/%d/%Y')       #the strftime means string format time 
        writer2.writerow([formatted_date, daily_return])
        
        




