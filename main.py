import streamlit as st
import json

def TMPchat():
    '''临时聊天区'''
    st.write('# 临时聊天区')
    col3, col4 = st.columns([1, 1])
    with col4:
        messages_list = load_messages()
        name = st.text_input('昵称')
        new_message = st.text_input('内容')
        col1, col2 = st.columns([1, 3])
        with col1:
            if_leave_message = st.button('发送')
        with col2:
            if if_leave_message:
                message = [str(int(messages_list[-1][0])+1), name, new_message]
                messages_list.append(message)
                with open('leave_messages.json', 'w', encoding='utf-8') as f:
                    json.dump(messages_list, f)
                st.write('发送成功')
    with col3:
        messages_list = load_messages()
        for i in messages_list:
            display_message(i)

def load_messages():
    with open('leave_messages.json', 'r', encoding='utf-8') as f:
        messages_list = json.load(f)
    return messages_list

def display_message(i):
    if i[1] == 'Liu':
        with st.chat_message('🌞'):
            st.write('站长 : ' + i[2])
    else:
        with st.chat_message('🍥'):
            st.text(i[1] + ' : ' + i[2])


def main():
    TMPchat()

main()
