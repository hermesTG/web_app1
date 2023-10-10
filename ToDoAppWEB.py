import streamlit as st
import functions

def add_todo():
    todo=st.session_state['new_todo']
    todos.append(todo)
    functions.write_to_file(todos)



todos=functions.get_todos()

st.title('My To Do App')
st.subheader('This is my ToDo App')

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_to_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label='Enter a new ToDo:',placeholder='placeholder',key='new_todo',on_change=add_todo)

