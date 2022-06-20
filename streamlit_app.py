import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('Cringe')

streamlit.header('Header')
streamlit.text('Body Line 1')
streamlit.text('Body Line 2')

streamlit.multiselect("Pick some fruits", list(my_fruit_list.index), ['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)
