import tabula
import pandas as pd

#yaha invertees mai apne file ka global path daal dena aur agli line me path ke aage se hash hatadena
#path = " "

dfs = tabula.read_pdf(path, pages="all", multiple_tables=True)

if dfs:
    first_table_col = dfs[0].columns
    num_cols = len(first_table_col)

    list_table = []

    for df in dfs:
        if df is None or len(df.columns) != num_cols:
            continue
        df = df[~df.apply(lambda row: row.astype(str).str.strip().tolist() == first_table_col.tolist(), axis=1)]

        df.columns = first_table_col

        df = df.dropna(how='all')

        list_table.append(df)

    if list_table:
        combined_df = pd.concat(list_table, axis=0, ignore_index=True)
        combined_df.to_csv("Final.csv", index=False)
        print("Tables extracted from the pdf.")
    else:
        print("Different tables are there in the pdf")
else:
    print("No tables found in the pdf.")
