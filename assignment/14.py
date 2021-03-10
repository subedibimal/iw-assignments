import csv


def csv_read(filename: str) -> bool:
    items = []
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        indexes = next(csv_reader)
        for i in csv_reader:
            dict_ = dict()
            for k,v in enumerate(indexes):
                dict_[v] = i[k]
            items.append(dict_)
    return items 