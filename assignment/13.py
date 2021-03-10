import csv


def csv_write(filename: str, texts_to_write: list[tuple[str,str,int]]) -> bool:
    with open(filename, "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['name', 'address', 'age'])
        csv_writer.writerows(texts_to_write)  
    return True 