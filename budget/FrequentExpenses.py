from . import Expense
import collections
import matplotlib.pyplot as plt


#Create Variable named Expenses that reads csv
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

#Create List of Spending Categories
spending_categories = []

#Create Loop 
for expense in spending_categories:
    spending_categories.append(expense.category)


#Create variable Spending_Counter
spending_counter = collections.Counter(spending_categories)
print(spending_counter)


#Create Top 5
top5 = spending_counter.most_common(5)


#Combining two lists
categories, count = zip(*top5)

#I guess thisgoing to be the graph 
fig,ax = plt.subplots()

#create the bar chart
ax.bar(categories, count)

#Add Title
ax.set_title('# of Purchases by Category')

#display graph
plt.show()



    
