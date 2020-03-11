import xlsxwriter
import pandas as pd

readDataframe = pd.read_excel(r'fruits.xlsx')
newDataframe = pd.DataFrame(
    {'Name': ['orange'], 'Price': [88], 'Amount': [15]}
)

frames = [readDataframe, newDataframe]
result = pd.concat(frames)

writer = pd.ExcelWriter('fruits.xlsx', engine='xlsxwriter')

result.to_excel(writer, index=False)
writer.save()

print(readDataframe)
