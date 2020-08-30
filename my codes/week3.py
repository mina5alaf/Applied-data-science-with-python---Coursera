import pandas as import pd

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())

#pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
#pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
"""staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
"""
#print(pd.merge(products, invoices, left_index=True, right_on='Product ID'))
#print(df.drop(df[df['Quantity'] == 0].index).rename(columns={'Weight': 'Weight (oz.)'}))

# def totalweight(df, w, q):
#        return sum(df[w] * df[q])
#
# print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))


"""s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])

s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)
"""
#print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))
