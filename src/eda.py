import pandas
import matplotlib.pyplot as plt
import sklearn
import random


def main():
    path = 'data/flats_29August2021.csv'

    df = pandas.read_csv(path, sep='\t')
    print(df.head())

    columns = ['price_id', 'flat_id', 'price', 'date', 'ad_id', \
    'title', 'date_posted', 'date_scraped', 'location', 'seller', \
     'property_type', 'num_rooms', 'num_bathrooms', 'flat_area',  \
     'text', 'description', 'photos_links', 'page_address']

     


if __name__ == "__main__":
    main()