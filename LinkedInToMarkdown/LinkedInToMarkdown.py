import csv

# https://realpython.com/python-csv/

with open('Shares.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            file_name = row['Date'].replace(' ', 'T').replace(':', '-') + '.md'
            file_content = row['ShareCommentary'].replace('"\n', '\n').replace('\n"', '\n')
            file_content += '\n\n' + row['SharedURL'] + '\n\n' + row['ShareLink'] + '\n'
            # save to file
            f = open('output/' + file_name, "a")
            f.write(file_content)
            f.close()
            # if line_count == 1:
            #     print(file_content)
            #     print(file_name)
            line_count += 1
    print(f'Processed {line_count} lines.')
