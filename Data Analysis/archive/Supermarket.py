import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = r'C:\Users\arman\OneDrive\Desktop\Coding\supermarket_sales - Sheet1.csv'
data = pd.read_csv(file_path)

# Data Cleaning and Preparation
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month

# Display the first few rows and info of the data
print(data.head())
print(data.info())

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values:\n", missing_values)

# Exploratory Data Analysis (EDA)
# Total and average sales by department (Product line)
total_sales_by_dept = data.groupby('Product line')['Total'].sum().reset_index()
average_sales_by_dept = data.groupby('Product line')['Total'].mean().reset_index()

# Define a color palette for distinct colors
colors = sns.color_palette("hsv", len(total_sales_by_dept))

# Plot total sales by department
plt.figure(figsize=(12, 6))
sns.barplot(x='Product line', y='Total', data=total_sales_by_dept, palette=colors)
plt.title('Total Sales by Department')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Plot average sales by department
plt.figure(figsize=(12, 6))
sns.barplot(x='Product line', y='Total', data=average_sales_by_dept, palette=colors)
plt.title('Average Sales by Department')
plt.xlabel('Product Line')
plt.ylabel('Average Sales')
plt.xticks(rotation=45)
plt.show()

# Analyze Seasonal Trends
# Total sales by month (only 3 months in the dataset)
total_sales_by_month = data.groupby('Month')['Total'].sum().reset_index()

# Plot total sales by month
plt.figure(figsize=(12, 6))
sns.lineplot(x='Month', y='Total', data=total_sales_by_month, marker='o')
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 4))
plt.show()

# Developing Insights for Optimizing Sales Strategies
# Total sales by city and payment method
total_sales_by_city_payment = data.groupby(['City', 'Payment'])['Total'].sum().unstack()

# Plot total sales by city and payment method
total_sales_by_city_payment.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Total Sales by City and Payment Method')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.show()

# Insights and Recommendations
def generate_insights(data):
    insights = []

    # Insight 1: Top-performing departments
    top_dept = total_sales_by_dept.sort_values(by='Total', ascending=False)
    insights.append(f"Top-performing departments are: {', '.join(top_dept['Product line'].head(3))}")

    # Insight 2: Seasonal trends
    peak_month = total_sales_by_month.sort_values(by='Total', ascending=False).iloc[0]['Month']
    insights.append(f"The peak sales month is {peak_month}. Consider running promotions during this month.")

    # Insight 3: Preferred payment methods
    preferred_payment = total_sales_by_city_payment.idxmax(axis=1)
    for city in preferred_payment.index:
        insights.append(f"In {city}, the preferred payment method is {preferred_payment[city]}.")
    
    # Insight 4: Customer types and sales
    sales_by_customer_type = data.groupby('Customer type')['Total'].sum().reset_index()
    top_customer_type = sales_by_customer_type.sort_values(by='Total', ascending=False).iloc[0]['Customer type']
    insights.append(f"Majority of the sales are from {top_customer_type} customers. Focus marketing efforts on this segment.")

    return insights

# Generate and display insights
insights = generate_insights(data)
for i, insight in enumerate(insights, 1):
    print(f"Insight {i}: {insight}")

# Display the summary statistics
print(data.describe())

# Sales Strategy Development
# Identify the highest performing department
highest_performing_dept = total_sales_by_dept.sort_values(by='Total', ascending=False).iloc[0]['Product line']
total_sales_highest_dept = total_sales_by_dept.sort_values(by='Total', ascending=False).iloc[0]['Total']

# Sales Strategy Plan
strategy = f"""
Sales Strategy for {highest_performing_dept} Department
-------------------------------------------------------
**Objective:** Increase sales for the highest-performing department, '{highest_performing_dept}'.

**Current Performance:** 
- Total Sales: ${total_sales_highest_dept:.2f}

**Plan of Execution:**
1. **Promotion Campaign:**
   - **Discount Offers:** Provide a 10% discount on all products in the '{highest_performing_dept}' category.
   - **Bundle Deals:** Offer bundle deals where customers get a complimentary product from another department with every purchase over a certain amount.
   - **Loyalty Points:** Double the loyalty points for members purchasing items from the '{highest_performing_dept}' category during the promotion period.

2. **Marketing Strategies:**
   - **Email Marketing:** Send out targeted emails to customers highlighting the discount offers and bundle deals.
   - **Social Media Campaigns:** Use social media platforms to promote the campaign, highlighting the benefits and deals.
   - **In-store Promotions:** Use in-store posters and flyers to inform customers about the ongoing promotion.

3. **Duration:** 
   - The promotion will run for one month, during the peak sales month identified (e.g., March).

**Rationale:**
- The '{highest_performing_dept}' department has shown significant sales performance, indicating strong customer interest and demand.
- Providing targeted promotions and marketing efforts can further capitalize on this interest, driving more sales and enhancing customer loyalty.
- Offering bundle deals and double loyalty points can incentivize higher spending and attract more repeat customers.

**Expected Outcome:**
- Increase in overall sales for the '{highest_performing_dept}' department.
- Higher customer engagement and satisfaction due to attractive deals and offers.
- Enhanced customer loyalty through the rewards and promotions.
"""

# Display the sales strategy
print(strategy)

# Plot sales strategy details (as a mock page display)
fig, ax = plt.subplots(figsize=(12, 8))
ax.text(0.5, 0.5, strategy, horizontalalignment='center', verticalalignment='center', wrap=True, fontsize=12)
ax.axis('off')
plt.title('Sales Strategy for Highest Performing Department')
plt.show()
