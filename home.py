import streamlit as st
import webbrowser
import json
import pandas as pd
import time


def table_view_choice():
    choice = st.selectbox("Table Display", ("Grid View", "Table View"))
    if choice == "Grid View":
        st.dataframe(df)
    elif choice == "Table View":
        st.table(df)


st.set_page_config(layout="wide")

st.title("Nike DCU Delete Run - PIPA")
st.subheader("[URL Extraction & Page Load Automation]")

option = st.selectbox("Choose the Assignee", ('Anto', 'Arul', 'Arun', 'Karthik'))

if option == "Anto":
    with open('anto.json') as file:
        data = json.load(file)

    df = pd.DataFrame(data["anto"])

    table_url_data = df["table_url"].drop_duplicates()
    table_url = list(table_url_data)

    dependent_dag_url = df["dependent_dag_url"].drop_duplicates()
    dependent_url_data = list(dependent_dag_url)

    table_view_choice()

elif option == "Arul":
    with open('arul.json') as file:
        data = json.load(file)

    df = pd.DataFrame(data["arul"])

    table_url_data = df["table_url"].drop_duplicates()
    table_url = list(table_url_data)

    dependent_dag_url = df["dependent_dag_url"].drop_duplicates()
    dependent_url_data = list(dependent_dag_url)

    table_view_choice()

elif option == "Arun":
    with open('arun.json') as file:
        data = json.load(file)

    df = pd.DataFrame(data["arun"])

    table_url_data = df["table_url"].drop_duplicates()
    table_url = list(table_url_data)

    dependent_dag_url = df["dependent_dag_url"].drop_duplicates()
    dependent_url_data = list(dependent_dag_url)

    table_view_choice()

elif option == "Karthik":
    with open('karthik.json') as file:
        data = json.load(file)

    df = pd.DataFrame(data["karthik"])

    table_url_data = df["table_url"].drop_duplicates()
    table_url = list(table_url_data)

    dependent_dag_url = df["dependent_dag_url"].drop_duplicates()
    dependent_url_data = list(dependent_dag_url)

    table_view_choice()

else:
    pass


def open_table_url():
    for link in table_url:
        if link:
            url = link
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(url)
            time.sleep(1.5)
        else:
            continue


def open_dependent_dag_url():
    for link in dependent_dag_url:
        if link:
            url = link
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(url)
            time.sleep(1.5)
        else:
            continue


c1, c2, c3, c4 = st.columns(4)

c2.button("Open Tables", on_click=open_table_url)
c3.button("Open Dependent DAGs", on_click=open_dependent_dag_url)
