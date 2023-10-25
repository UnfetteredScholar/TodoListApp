import streamlit as st
from db_driver.functions import get_current_items, change_item_status, insert_item, delete_item




cols = st.columns([2,5])

with cols[0]:
    st.image('images/list.jpeg', width=150)

with cols[1]:
    st.header("Todo List")



col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 2, 2))

st.subheader("Add Task")
task_desc = st.text_input("Task Description")
if st.button("Add Task"):
    insert_item(task_desc)
    

todo_table = get_current_items()

col1.write("Task ID")
col2.write("Description")
col3.write("Status")
col4.write("Change Status")
col5.write("Delete Item")

for i in todo_table.index:
    col1.write(todo_table['Id'][i])
    col1.text("")
    col2.write(todo_table['Description'][i])
    col2.text("")
    col3.write(todo_table['Status'][i])
    col3.text("")
    button_place = col4.empty()
    
    if todo_table['Status'][i] == 'Pending':
        button_place.button("Complete", key = str(i), on_click=change_item_status, args=[str(todo_table['Id'][i]), 'Complete'])
    elif todo_table['Status'][i] == 'Complete':
        button_place.button("Pending", key = str(i), on_click=change_item_status, args=[str(todo_table['Id'][i]), 'Pending'])
    
    col5.button("Delete", key= f'del{i}', on_click=delete_item, args=[str(todo_table['Id'][i])])
    
        

