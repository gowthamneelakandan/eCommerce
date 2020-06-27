import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/sureshneelakandan/Desktop/icu meds")
filename = "ecommerce.csv"

df_read_file = pd.read_csv(filename)
df_read_file["Sales"] = df_read_file[" Sales "].str.replace("$","").replace(" ","")
df_read_file = df_read_file.astype({"Sales":"float64"})
df_read_file["Months"] = df_read_file["Months"].str.replace("Jan","01").replace("Feb","02").replace("Mar","03").replace("Apr","04").replace("May","05").replace("Jun","06").replace("Jul","07").replace("Aug","08").replace("Sep","09").replace("Oct","10").replace("Nov","11").replace("Dec","12")
df_read_file = df_read_file.astype({"Months":"int64"})
df_read_file = df_read_file.sort_values("Months", ascending=False)
meanSalesReport = df_read_file.groupby("Months")["Sales"].count()

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")
meanSalesReport.plot(kind="line")
plt.show()
