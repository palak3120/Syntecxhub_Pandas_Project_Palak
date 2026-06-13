import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

print("===== First 5 Rows =====")
print(df.head())

print("\n===== Last 5 Rows =====")
print(df.tail())

print("\n===== Data Types =====")
print(df.dtypes)

print("\n===== Summary Statistics =====")
print("Mean Salary:", df["Salary"].mean())
print("Median Salary:", df["Salary"].median())
print("Minimum Salary:", df["Salary"].min())
print("Maximum Salary:", df["Salary"].max())
print("Count:", df["Salary"].count())

# Filter IT Department Employees
it_employees = df[df["Department"] == "IT"]

print("\n===== IT Employees =====")
print(it_employees)

# Save filtered data
it_employees.to_csv("filtered_data.csv", index=False)

print("\nFiltered data saved successfully!")