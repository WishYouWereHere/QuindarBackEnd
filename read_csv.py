import csv
from pathlib import Path

def read_csv():
    '''
    This function reads a csv file, converts the CSV file into a list(dict) and prints out
    object. 
    Func Args:
    None

    Return:
    List[Dict{}]
    '''
    file_path = Path(__file__).parent/"test_data"/"example_station_data.csv"

    rows = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            # Remove random characters
            header = [h.replace('ï»¿', '') for h in header]
            
            # Convert remaining rows to dictionaries
            for row in reader:
                row_dict = {header[i]: row[i] for i in range(len(header))}
                rows.append(row_dict)

        return rows
    except Exception as e:
        print(f"File cannot be correctly parsed : {e}")

def read_csv_locally():
    '''
    This function reads a csv file, converts the CSV file into a list(dict) and prints out
    object. 
    Func Args:
    None

    Return:
    None
    '''
    file_path = Path(__file__).parent/"test_data"/"example_station_data.csv"

    rows = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            # Remove random characters
            header = [h.replace('ï»¿', '') for h in header]
            
            # Convert remaining rows to dictionaries
            for row in reader:
                row_dict = {header[i]: row[i] for i in range(len(header))}
                rows.append(row_dict)
                #print(row_dict)  # Optional: print each dict

        print(rows)
    except Exception as e:
        print(f"File cannot be correctly parsed : {e}")
        

if __name__ == "__main__":
    read_csv_locally()