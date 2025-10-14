import streamlit as st
import streamlit.components.v1 as components
import subprocess
import site
import webbrowser

def emulator():
    st.title("UAserver Mobile Emulator")


    htmlf = '''<iframe width="392" height="620" style="border: 0px;" 
    src="https://studio.code.org/projects/applab/3w-53qDYJIXBqt3PX30J9RaZ79aE7aecDq1Mk-4szJg/embed"></iframe>'''
    path = site.getusersitepackages()
    stp = f"{path}/python5/main.py"
    cmd = f"python -m streamlit run {stp} --server.port 9000"
    components.html(htmlf, height=650, width=600)
    cmd = ["streamlit", "run", stp, "--server.port", "9000"]
    webbrowser.open("tinyurl.com/localhostprovider")
    print(f"\n\n\n Please Enter this in Your Shell: {cmd}")
