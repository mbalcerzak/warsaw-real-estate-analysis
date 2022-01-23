import random
import streamlit as st
import pandas as pd
from itertools import cycle

from process_ad_data import get_flat_info

st.title("Am I overpaying for that flat? Probably.")
st.warning("Not an investment advice. I am just a project for a programming portfolio. Don't listen to me.")

random_flat_link = "https://www.gumtree.pl/a-mieszkania-i-domy-sprzedam-i-kupie/mokotow/mokotow-4-pok-metro-duzy-balkon-parkiet-miejsce-parkingowe/10010444262631011108653509"

if st.button("""Random flat"""):
     st.write('Chosen ad address')
     st.write(random_flat_link)
     chosen_flat_link = random_flat_link
else:
     st.write('Custom input')
     chosen_flat_link = ""

link_label = """Paste a link of a flat from Gumtree (Warsaw, Poland only so far)"""
chosen_flat_link = st.text_input(label=link_label, value=chosen_flat_link, max_chars=250)


if len(chosen_flat_link) > 0:  
    flat_info = get_flat_info(chosen_flat_link)
    st.write(flat_info)

    # st.image(flat_info['photos_links'], use_column_width=True)

    filteredImages = flat_info['photos_links']


cols = cycle(st.columns(3)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(filteredImages):
    next(cols).image(filteredImage, use_column_width=True)