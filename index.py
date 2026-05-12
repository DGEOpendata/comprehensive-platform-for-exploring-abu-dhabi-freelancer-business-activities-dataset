python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_url = "https://example.com/data/Freelancer-Business-Activities-AD-010.csv"
data = pd.read_csv(data_url)

# Display the first few rows of the dataset
print(data.head())

# Filter dataset based on user input (example: Consultancy Services)
filtered_data = data[data['Category'] == 'Consultancy Services']

# Display filtered data
print(filtered_data)

# Create a bar chart to show the number of services in each category
plt.figure(figsize=(12, 6))
sns.countplot(y='Category', data=data, order=data['Category'].value_counts().index)
plt.title('Number of Freelance Activities by Category')
plt.xlabel('Count')
plt.ylabel('Category')
plt.show()

# Save filtered data to a new CSV file
filtered_data.to_csv('Filtered_Freelancer_Business_Activities.csv', index=False)
