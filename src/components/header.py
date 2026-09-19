import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px">
            <img src="{logo_url}" style="height:100px;" />
            <div style="
                text-align:center;
                color:#E0E3FF;
                font-size:50px;
                font-weight:bold;
                font-family:'Climate Crisis', sans-serif;
                line-height:1.2;
                margin-top:10px;
            ">
                SNAP<br/>CLASS
            </div>
        </div>
        """, unsafe_allow_html=True)