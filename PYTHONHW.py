import csv
import os
# /Users/lauren.mckinzie/CU-NYC-DATA-PT-10-2019-U-C/Homework/03-Python/Instructions/PyBank/Resources
print(os.getcwd())
file_ = os.path.join("..", "..", "..", "..",
             "CU-NYC-DATA-PT-10-2019-U-C", "Homework", "03-Python", "Instructions", "PyBank", "Resources",
             "budget_data.csv")

with open(file_) as  budget_data:
    reader = csv.DictReader(budget_data)

     for row in reader:


         total_months = (total_months + 1)
         total_revenue = total_revenue + int(row["Revenue"])
            print(total_months)
            print(total_months)


         # Keep track of changes
         revenue_change = int(row["Revenue"]) - prev_revenue
         print(revenue_change)

          #Reset the value of prev_revenue to the row I completed my analysis
          prev_revenue = int(row["Revenue"])
          print(prev_revenue)

         # Determine the greatest increase
         if (revenue_change > greatest_increase[1]):
             greatest_increase[1] = revenue_change
             greatest_increase[0] = row["Date"]

         if (revenue_change < greatest_decrease[1]):
             greatest_decrease[1] = revenue_change
             greatest_decrease[0] = row["Date"]

#         # Add to the revenue_changes list
         revenue_changes.append(int(row["Revenue"]))
#
#     # Set the Revenue average
     revenue_avg = sum(revenue_changes) / len(revenue_changes)
#
#     # Show Output
     print()
     print()
     print()
     print("Financial Analysis")
     print("-------------------------")
     print("Total Months: " + str(total_months))
     print("Total Revenue: " + "$" + str(total_revenue))
     print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes), 2)))
     print("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
     print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")



