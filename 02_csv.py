import csv

# file_to_output = open('to_save_file.csv',mode='w',newline='')
file_to_output = open('to_save_file.csv',mode='a',newline='')


csv_writer = csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['a','b', 'c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
csv_writer.writerows(['1'])

file_to_output.close()