import os
import csv
total_months = 0
total_sum=0
average_change, revenue, date = [], [], []
Greatest_increase = 0
Greatest_decrease = 0
csvpath=os.path.join('../Resources/budget_data.csv')
output_results = os.path.join('../Resources/Result.txt')
with open (csvpath,"r") as Budget:
    csv_reader=csv.reader(Budget)
    header=next(csv_reader)
   
    for row in csv_reader:
        total_months=csv_reader.line_num -1
        total_sum = total_sum + int(row[1])
        revenue.append(row[1])
        date.append(row[0])
    for i in range(total_months - 1):
        average_diff = int(revenue[i+1]) - int(revenue[i]) 
        average_change.append(average_diff)        
       
        if Greatest_increase < int(average_change[i]):
            Greatest_increase = int(average_change[i])
            max_date = date[i+1]
        if Greatest_decrease > int(average_change[i]):
            Greatest_decrease = int(average_change[i])
            min_date = date[i+1]
        total_Avgchange=sum(average_change)/(total_months-1)          
    print ('Financial Analysis')
    print('--------------------')
    print('Total months:'+str(total_months) )
    print('Total:'+"$"+str(total_sum))
    print("average change :"+"$"+str(round(total_Avgchange)))
    print("the Greatest increase in profit: "+ max_date + " " + str(Greatest_increase))
    print("the Greatest descrease in profit: " + min_date + " " + str(Greatest_decrease))

    with open(output_results, "w") as out_file:
       out_file.write("Financial Analysis"+'\n')
       out_file.write('--------------------'+'\n')
       out_file.write(f"Total: ${total_sum}"+'\n')
       out_file.write(f"Totalmonths:{total_months}"+'\n')     
       out_file.write(f"average change :{total_Avgchange}"+'\n')
       out_file.write("the Greatest increase in profit: "+ max_date + " " + str(Greatest_increase)+'\n')
       out_file.write("the Greatest descrease in profit: " + min_date + " " + str(Greatest_decrease)+'\n')


