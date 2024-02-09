import pandas as pd;
import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt;

df=pd.read_excel('D:/Semester 2/2203-big data visualisation -ishant gupta/Flight_prices.xlsx')

print(df.head()) 
print(df.tail())

#To print rows and columns
rows, columns = df.shape
print("the no of rows :",rows)
print("the no of cols :",columns)

#Q2. What is the distribution of flight prices in the dataset? Create a histogram to visualize the distribution.

df['Price'].plot.hist(bins=10, edgecolor='black', color='skyblue')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Histogram of Price')
plt.show()

#Q3 the max min and range of price

# Calculate maximum price
max_price = df['Price'].max()
# Calculate minimum price
min_price = df['Price'].min()

# Calculate range of prices
price_range = max_price - min_price

print(f"Maximum Price: ${max_price:.2f}")
print(f"Minimum Price: ${min_price:.2f}")
print(f"Range of Prices: ${price_range:.2f}")


#Q4 How does the price of flights vary by airline? Create a boxplot to compare the prices of different airlines.

plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Airline'], y=df['Price'])
plt.xlabel('Airline')
plt.ylabel('Price ($)')
plt.title('Flight Prices by Airline')
plt.xticks(rotation=45)
plt.show()

#Q5 check for outliers in the datset.

#we can check ouliers using a boxplot 
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, y='Price')
plt.title('Boxplot of Flight Arrival Time')
plt.ylabel('Arrival time')
plt.show()


