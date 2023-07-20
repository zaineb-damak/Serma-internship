def dataframe(file_path):
    #creating dataframe
    df = pd.read_excel(file_path, header=56)
    #saving the changes in a new excel file
    df.to_excel('modified.xlsx', index = False)
    
    #printing name of columns
    print(df.columns)
    #printing a specific column
    print(df['Action Field 3'])
    
    # iterating through the rows
    # for index, row in df.iterrows():
    #     print(row)

    #converting the data of the column into numerical type in order to apply the operations
    df['Action Field 3'] = pd.to_numeric(df['Action Field 3'], errors='coerce')

    #printing the rows corresponding to a specific value of a column(filtering)
    print(df.loc[(df['Action Field 3'] < 10) & (df['Action Field 3'] >0) ])
    
    #printing the rows corresponding to a specific text of a column
    df['Action Field 1 ( Tag Name/Request Name/ Picture Name)'] = df['Action Field 1 ( Tag Name/Request Name/ Picture Name)'].astype(str)
    print(df.loc[(df['Action Field 1 ( Tag Name/Request Name/ Picture Name)'].str.contains('Phone'))])
    

#dataframe('./resources/test_case3.xlsx')