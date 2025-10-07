import streamlit as st
import streamlit.components.v1 as components

# Display custom HTML content
htmlf = '''<iframe width="392" height="620" style="border: 0px;" src="https://studio.code.org/projects/applab/3w-53qDYJIXBqt3PX30J9RaZ79aE7aecDq1Mk-4szJg/embed"></iframe>'''

components.html(
    htmlf,
    height=650,  # Adjust height if needed
    width=600
)
