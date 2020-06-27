import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/sureshneelakandan/Desktop/icu meds")
filename = "ecommerce.csv"

df_read_file = pd.read_csv(filename)
meanSalesReport = df_read_file.groupby(["Region", "Product Category"])["Product Category"].count()

plt.xlabel("Region")
plt.ylabel("Product Category")
plt.title("Region category Count")
meanSalesReport.plot(kind="bar")
plt.show()
