import streamlit as st
import pandas as pd
import numpy as np

# Page configuration for multi-pages layout
st.set_page_config(page_title="BMI Calculator", layout="wide")

# Sidebar navigation setup
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page", ["Home", "BMI Calculator", "Data & Chart", "Map", "Counter"])

# **Session State**
if "count" not in st.session_state:
    st.session_state.count = 0

# **Fragments**: Reusable function for BMI Interpretation
def display_bmi_interpretation(bmi):
    """Returns a BMI interpretation."""
    if bmi < 16:
        return "You are Extremely Underweight", "error"
    elif 16 <= bmi < 18.5:
        return "You are Underweight", "warning"
    elif 18.5 <= bmi < 25:
        return "You are Healthy", "success"
    elif 25 <= bmi < 30:
        return "You are Overweight", "warning"
    elif bmi >= 30:
        return "You are Extremely Overweight", "error"

# **Pages**
if page == "Home":
    st.title('Welcome to the BMI Calculator')
    st.write("""
    This BMI Calculator allows you to calculate your Body Mass Index (BMI) by entering your weight and height.
    You can choose your preferred height unit (Centimeters, Meters, or Feet).
    The application also provides a real-time data table, chart, and an interactive map for you to explore.
    """)

elif page == "BMI Calculator":
    st.title("BMI Calculator")

    # **Forms**: Collecting input for BMI calculation
    with st.form(key='bmi_form'):
        weight = st.number_input("Enter your weight (in kgs)", min_value=0.0, format="%.2f")
        height_unit = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))
        
        # Height input based on selected unit
        if height_unit == 'cms':
            height = st.number_input('Enter your height in centimeters', min_value=0.0)
        elif height_unit == 'meters':
            height = st.number_input('Enter your height in meters', min_value=0.0)
        else:
            height = st.number_input('Enter your height in feet', min_value=0.0)

        submit_button = st.form_submit_button(label='Calculate BMI')

        # **BMI Calculation**
        if submit_button:
            if height_unit == 'cms':
                bmi = weight / ((height / 100) ** 2)
            elif height_unit == 'meters':
                bmi = weight / (height ** 2)
            else:
                bmi = weight / (((height / 3.28)) ** 2)

            st.write(f"Your BMI is **{bmi:.2f}**.")

            # **Fragments**: Using a function to display BMI interpretation
            interpretation, alert_type = display_bmi_interpretation(bmi)
            getattr(st, alert_type)(interpretation)

elif page == "Data & Chart":
    st.title("Data & Chart")

    # **DataFrame**: Creating a random DataFrame
    demo_data = pd.DataFrame(np.random.rand(30, 3), columns=['A', 'B', 'C'])
    st.subheader("Random Data Table")
    st.table(demo_data)

    # **Area Chart**: Visualizing data
    st.subheader("Area Chart for Columns A & B")
    st.area_chart(demo_data[['A', 'B']])

elif page == "Map":
    st.title("Interactive Map")

    # **Map**: Showing random geographical data
    map_data = pd.DataFrame(np.random.randn(100, 2) / [50, 50] + [23.8, 90.4], columns=['lat', 'lon'])
    st.map(map_data)

elif page == "Counter":
    st.title("Session Counter")

    # **Sessions**: Counting with session state
    def increment_counter():
        st.session_state.count += 1
        st.rerun()

    st.write(f"Current count: {st.session_state.count}")

    # **Callbacks**: Button callback for incrementing the counter
    if st.button("Increment Counter"):
        increment_counter()

# **Sidebar Content**
st.sidebar.header("Additional Info")
st.sidebar.write("""
- **BMI Calculator**: Calculate your BMI by providing weight and height.
- **Data & Chart**: View random data and visualizations.
- **Interactive Map**: See random geographic coordinates plotted on a map.
- **Counter**: Track the count with a button and session state.
""")

# Adding an image to the sidebar
st.sidebar.subheader("BMI Calculator Image")
image_url = "https://via.placeholder.com/500x300.png?text=BMI+Calculator"
st.sidebar.image(image_url, caption="BMI Calculator", use_column_width=True)

# **Cache**: Simulating a heavy computation
@st.cache_data
def get_heavy_computation():
    """Simulate an expensive computation"""
    result = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
    return result

# Display the result of a heavy computation (cached data)
st.sidebar.subheader("Heavy Computation (cached data)")
heavy_result = get_heavy_computation()
st.sidebar.write(heavy_result)

# **Multipages**: Simplified multi-page navigation using sidebar
st.sidebar.subheader("Multipage Navigation")
st.sidebar.write("""
This app demonstrates multiple pages. Choose from **Home**, **BMI Calculator**, **Data & Chart**, **Map**, or **Counter**.
""")

