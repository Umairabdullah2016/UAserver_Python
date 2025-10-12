import streamlit
def start_uaserver():
    st.title("UAserver Mobile Emulator")


    htmlf = '''<iframe width="392" height="620" style="border: 0px;" 
    src="https://studio.code.org/projects/applab/3w-53qDYJIXBqt3PX30J9RaZ79aE7aecDq1Mk-4szJg/embed"></iframe>'''
    path = site.getusersitepackages()
    stp = path,"/python5/main.py"
    cmd = f"streamlit run {stp} --server.port 9000"
    components.html(htmlf, height=650, width=600)
    result = subprocess.run(
        ["powershell", cmd , "Get-Process"],
        capture_output=True,
        text=True
        )
    webbrowser.open("tinyurl.com/localhostprovider")
    
