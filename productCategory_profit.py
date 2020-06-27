import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/sureshneelakandan/Desktop/icu meds")
filename = "ecommerce.csv"

df_read_file = pd.read_csv(filename)
df_read_file["Profit"] = df_read_file[" Profit "].str.replace("$","").replace(" ","")
df_read_file = df_read_file.astype({"Profit":"float64"})
meanSalesReport = df_read_file.groupby("Product Category")["Profit"].count()

plt.xlabel("Product Category")
plt.ylabel("Profit")
plt.title("Product Category Profit")
meanSalesReport.plot(kind="bar")
plt.show()
