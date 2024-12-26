import pandas


def squirrel() -> None:
    squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240620.csv")
    gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
    cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
    black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

    color_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray_count, cinnamon_count, black_count]
    }
    data_color = pandas.DataFrame(color_dict)
    data_color.to_csv("squirrel_count.csv")


if __name__ == '__main__':
    squirrel()
