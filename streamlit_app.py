import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('Cringe')

streamlit.header('Header')
streamlit.text('Body Line 1')
streamlit.text('Body Line 2')

streamlit.dataframe(my_fruit_list)
