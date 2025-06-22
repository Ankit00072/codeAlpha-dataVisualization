#Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset
df = pd.read_csv('books_data.csv')

#Clean the price column (convert from string to float)
df['Price (£)'] = df['Price (£)'].astype(float)

#Set visual style
sns.set(style="whitegrid", palette="pastel")

#Star Rating Distribution

plt.figure(figsize=(8, 5))
sns.countplot(x='Rating', data=df, order=['One', 'Two', 'Three', 'Four', 'Five'])
plt.title('📚 Number of Books by Star Rating', fontsize=14)
plt.xlabel('Star Rating', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig('rating_distribution_data.png')
plt.show()

#Price Distribution of Books

plt.figure(figsize=(8, 5))
sns.histplot(df['Price (£)'], bins=15, kde=True, color='skyblue')
plt.title('💰 Distribution of Book Prices', fontsize=14)
plt.xlabel('Price (£)', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig('price_distribution_data.png')
plt.show()

#Book Availability Status

plt.figure(figsize=(8, 5))
sns.countplot(x='Availability', data=df, palette='Set2')
plt.title('📦 Book Availability Status', fontsize=14)
plt.xlabel('Availability', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig('availability_status_data.png')
plt.show()


print("All visualizations created and saved successfully.")
