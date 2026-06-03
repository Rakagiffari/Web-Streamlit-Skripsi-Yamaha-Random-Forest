import os

# =========================================
# LOAD SIDEBAR CSS
# =========================================
css_path = os.path.join(

    os.path.dirname(__file__),

    "..",

    "styles",

    "global.css"
)

with open(css_path) as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True
    )
