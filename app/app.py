import random
import streamlit as st
import pandas as pd
from itertools import cycle

from process_ad_data import get_flat_info
from get_stats_waw import get_price_size_category

st.title("Am I overpaying for that flat? Probably.")
st.warning("Not an investment advice. I am just a project for a programming portfolio. Don't listen to me.")

random_flat_link = "https://www.gumtree.pl/a-mieszkania-i-domy-sprzedam-i-kupie/mokotow/mokotow-4-pok-metro-duzy-balkon-parkiet-miejsce-parkingowe/10010444262631011108653509"

if st.button("""Random flat"""):
    #  st.write('Chosen ad address')
    #  st.write(random_flat_link)
     chosen_flat_link = random_flat_link
else:
    #  st.write('Custom input')
     chosen_flat_link = ""

link_label = """Paste a link of a flat from Gumtree (Warsaw, Poland only so far)"""
chosen_flat_link = st.text_input(label=link_label, value=chosen_flat_link, max_chars=250)


if len(chosen_flat_link) > 0:  
    flat_info = get_flat_info(chosen_flat_link)

    st.subheader(flat_info['title'])
    # st.write(flat_info)
    st.write(f"Rooms: {flat_info['num_rooms']}, bathooms: {flat_info['num_bathrooms']}, flat size: {flat_info['flat_area']}")

    category_price = get_price_size_category(flat_info)
    flats_price_per_m = round(flat_info['price'] / int(flat_info['flat_area']))

    price_diff = round(abs(flats_price_per_m - category_price)/category_price * 100)

    if category_price < flats_price_per_m:
        price_diff_msg = "more expensive"      
    else:
        price_diff_msg = "cheaper"

    st.write(f"Price per square metre for this size of flat that month in {flat_info['location']}: {category_price}. \n The price per square metre for this apartment is {flats_price_per_m}")
    st.info(f"Price of square metre of this flat is {price_diff} % {price_diff_msg} than the average for this size, location and date of posting")
    filteredImages = flat_info['photos_links']

    cols = cycle(st.columns(3)) # st.columns here since it is out of beta at the time I'm writing this
    for idx, filteredImage in enumerate(filteredImages):
        next(cols).image(filteredImage, use_column_width=True)