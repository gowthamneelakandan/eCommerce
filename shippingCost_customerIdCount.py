import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/sureshneelakandan/Desktop/icu meds")
filename = "ecommerce.csv"

df_read_file = pd.read_csv(filename)
df_read_file["Shipping Cost"] = df_read_file[" Shipping Cost "].str.replace("$","").replace(" ","")
df_read_file = df_read_file.astype({"Shipping Cost":"float64"})
meanSalesReport = df_read_file.groupby("Shipping Cost")["Customer ID"].count()

plt.xlabel("Shipping Cost")
plt.ylabel("Count")
plt.title("Shipping Cost Count")
meanSalesReport.plot(kind="line")
plt.show()
