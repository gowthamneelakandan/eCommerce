import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/sureshneelakandan/Desktop/icu meds")
filename = "ecommerce.csv"

df_read_file = pd.read_csv(filename)
meanSalesReport = df_read_file.groupby("Discount")["Customer ID"].count()

plt.xlabel("Discount")
plt.ylabel("Customer ID")
plt.title("People expecting Discount")
meanSalesReport.plot(kind="bar")
plt.show()
