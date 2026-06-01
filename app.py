import csv

def calculate_marks(file_name):
    try:
        with open(file_name, mode='r') as file:
            csv_reader = csv.DictReader(file)
            
            print(f"{'Name':<15}{'Total Marks':<15}{'Average Marks':<15}")
            print("-" * 45)
            
            for row in csv_reader:
                name = row['Name']
                # Safely convert marks to integers, defaulting to 0 if empty
                marks = [
                    int(row.get('Maths', 0) or 0),
                    int(row.get('Science', 0) or 0),
                    int(row.get('English', 0) or 0)
                ]
                
                total = sum(marks)
                average = round(total / len(marks), 2)
                
                print(f"{name:<15}{total:<15}{average:<15}")
                
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found in this directory.")

if __name__ == "__main__":
    calculate_marks('data.csv')
