import csv
with open('cleaned_data.csv', mode = 'a', newline='') as cleaned_data:
    sales_writer = csv.writer(cleaned_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    sales_writer.writerow(['product','sales','date','region'])
def read_file(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0         
        for row in csv_reader:
            if line_count == 0:
                print(f'column names are {",".join(row)}')
                line_count += 1
            #write file into new file
            if row[0] == 'pink morsel':              
                with open('cleaned_data.csv', mode = 'a', newline='') as cleaned_data:
                    sales_writer = csv.writer(cleaned_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    sales_writer.writerow([row[0], float(row[2]) * float(row[1].replace("$", "")), row[3], row[4]])
            line_count += 1        
    print(f'Processed {line_count} lines.')

read_file('daily_sales_data_0.csv')
read_file('daily_sales_data_1.csv')
read_file('daily_sales_data_2.csv')

