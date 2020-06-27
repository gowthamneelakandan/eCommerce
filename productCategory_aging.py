import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/sureshneelakandan/Desktop/icu meds")
filename = "ecommerce.csv"

df_read_file = pd.read_csv(filename)
meanSalesReport = df_read_file.groupby("Product Category")["Aging"].mean()

plt.xlabel("Product Category")
plt.ylabel("Aging")
plt.title("Average time for delivery")
meanSalesReport.plot(kind="bar")
plt.show()
