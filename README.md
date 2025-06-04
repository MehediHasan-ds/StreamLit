# BMI Calculator Streamlit App

## Overview
This is a **BMI Calculator** built using Streamlit, which allows users to calculate their **Body Mass Index (BMI)** by entering their weight and height. The app provides different functionalities such as data visualization, interactive maps, and session tracking using Streamlit's state management. It also demonstrates advanced features like **forms**, **sessions**, **callbacks**, **layouts**, **widgets**, **cache**, **fragments**, **pages**, and **multipages**.

### Features:
- **BMI Calculator**: Users can input their weight and height (in cm, meters, or feet) to calculate their BMI and receive an interpretation.
- **Data & Chart**: Displays a random dataset and visualizes it using an area chart.
- **Interactive Map**: Shows a map with random geographical coordinates.
- **Counter**: Tracks a counter value using **session state** with a button to increment the count.
- **Navigation**: The app uses **multipage navigation** via the sidebar to switch between different sections (Home, BMI Calculator, Data & Chart, Map, Counter).

## Technologies Used:
- **Streamlit**: For building interactive web apps with Python.
- **Pandas**: For data manipulation and handling DataFrame structures.
- **Numpy**: For generating random data and performing numerical calculations.
- **Matplotlib**: (Used implicitly by Streamlit for charting).
- **Session State**: For maintaining the state across app reruns.

## Features Demonstrated:
This app demonstrates the following features of Streamlit:
- **Forms**: For handling user input and preventing submission without filling the required fields.
- **Sessions**: For maintaining persistent data (e.g., the counter value).
- **Callbacks**: Used in the counter section to update the session state when the button is clicked.
- **Layouts**: Organized with a **sidebar** and **main area** for displaying different sections.
- **Widgets**: Various Streamlit widgets (`st.number_input()`, `st.radio()`, `st.button()`, etc.) to collect user inputs.
- **Cache**: Used for caching expensive computations to improve performance.
- **Fragments**: A reusable function (`display_bmi_interpretation()`) to handle BMI interpretation and avoid code duplication.
- **Pages**: The app contains multiple pages that change content based on the sidebar selection.
- **Multipages**: The sidebar navigation provides easy switching between different sections of the app.

## Installation

1. **Clone the repository**:
   ```bash
    git remote add origin https://github.com/MehediHasan-ds/StreamLit.git
````

2. **Install the required dependencies**:

   ```bash
   pip install streamlit pandas numpy
   ```

3. **Run the app**:
   In your terminal, navigate to the project folder and run:

   ```bash
   streamlit run bmi_calculator.py
   ```

4. The app will launch in your web browser at [http://localhost:8501](http://localhost:8501).

## App Features Walkthrough

### **1. BMI Calculator**

* Enter your **weight** and **height** in one of the following formats: **centimeters (cms)**, **meters**, or **feet**.
* The **BMI** is calculated, and an interpretation (e.g., "Underweight", "Healthy", "Overweight") is shown based on the BMI value.

### **2. Data & Chart**

* Displays a randomly generated dataset with 3 columns.
* Shows an **area chart** of two columns (A & B) from the DataFrame.

### **3. Interactive Map**

* Displays a map with **random geographical data** (latitude and longitude).

### **4. Counter**

* Tracks a counter value stored in **session state**. The counter can be incremented using a button. The value persists across sessions.

### **5. Sidebar Navigation**

* The sidebar allows users to easily navigate between the following pages:

  * **Home**: Introduction to the app.
  * **BMI Calculator**: BMI input and calculation.
  * **Data & Chart**: View random data and visualizations.
  * **Map**: See random geographic coordinates plotted on a map.
  * **Counter**: Track the count with a button and session state.

## Advanced Features:

### **Session State**:

* The app uses **Streamlit's session state** to persist values (such as the counter) across app reruns.
* This ensures that the count value is not reset every time the app is refreshed.

### **Caching**:

* **`st.cache_data`** is used to cache the result of an expensive computation (e.g., random data generation) to speed up the app.

### **Forms**:

* The app uses **forms** to ensure that users provide all required information (weight, height) before submitting.

### **Callbacks**:

* **Callbacks** are used to handle button presses, like incrementing the counter value in the "Counter" section.

### **Multipage Layout**:

* The app is divided into **multiple pages**, each containing different sections of functionality (BMI Calculator, Data & Chart, Map, Counter).

### **Fragments**:

* **Reusable functions** (fragments) like `display_bmi_interpretation()` for handling BMI interpretation ensure code reuse and maintainability.

## Example Screenshots:

1. **BMI Calculator** Page:

   * Users input their weight and height and receive their BMI index and interpretation.

2. **Data & Chart** Page:

   * Displays a randomly generated table and area chart of columns "A" and "B".

3. **Map** Page:

   * Displays an interactive map with random geographical coordinates.

4. **Counter** Page:

   * A counter that can be incremented using a button. The count persists across app reruns.

