import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/sureshneelakandan/Desktop/icu meds")
filename = "ecommerce.csv"

df_read_file = pd.read_csv(filename)
meanSalesReport = df_read_file.groupby("Segment")["Customer ID"].count()

plt.xlabel("Segment")
plt.ylabel("Customer ID")
plt.title("Segment customer Count")
meanSalesReport.plot(kind="bar")
plt.show()
