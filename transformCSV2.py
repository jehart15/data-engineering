#store csv data in a dictionary, where the file's columns are the keys, and the
#values are a list containing all the rows under that column

import csv

file = 'diabetes_data.csv'

def dict_from_data(file):
    '''This function takes the contents of a CSV file
       and returns a dictionary where the keys are the
       file's columns, and the values are a list containing
       each piece of data under the columns. Works best if
       the first line of the CSV lists the column names.
       Argument = name of a comma-delimited CSV file in cwd (str)'''

    data_store = []
    data_dict = {}
    
    #store csv contents as a list of ordered dicts for each row
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_store.append(row)

    #keys of the ordered dicts will also be the data_dict's keys
    keys = data_store[0].keys()

    #data_dict now has above keys with values that are empty lists
    for key in keys:
        data_dict[key] = []

    #first loop iterates through each ordered dic to cover all rows
    for row in data_store:
        #second loop references the key in the row to the key in the
        #final dictionary, appending that value to it
        for key in row:
            (data_dict[key]).append(row[key])

    return data_dict
        
def main():
    print(dict_from_data(file))

if __name__ == '__main__':
    main()
