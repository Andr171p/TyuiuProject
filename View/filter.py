import pandas as pd


def join_address(address):
    address = address.replace(" ", "").replace(".", "").split(",")
    return "".join(address)


def apply_address(data):
    address_index = 3
    for row in data:
        row[address_index] = join_address(row[address_index])

    return data


def check_doubles(data):
    # data = apply_address(data=data)
    dataframe = pd.DataFrame(data, columns=["Info", "Price", "Area", "Location", "Datetime", "URL"])
    dataframe.drop_duplicates(subset=["Price", "Area", "Location"],
                              inplace=True)
    data_uniq = dataframe.values

    return data_uniq

