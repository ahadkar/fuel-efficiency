import pandas as pd


def main():

	print("Reading CSV...")
	df = pd.read_csv("data/cars2017.csv")

	avg_dict = {}

	for index, row in df.iterrows():
		car_name = row["Make"]
		if not car_name in avg_dict.keys():
			avg_dict[car_name] = []


if __name__ == '__main__':
	main()