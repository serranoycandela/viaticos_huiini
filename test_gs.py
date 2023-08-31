import pandas as pd
sheet_id = "1a3-O0OvzDQect8EszxeeDrKbrLxNaw2Lti7t37Usfq8"
r = "https://docs.google.com/spreadsheets/export?id={}&exportFormat=csv".format(sheet_id)
df = pd.read_csv(r)
print(df.head())
