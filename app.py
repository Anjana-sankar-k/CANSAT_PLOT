import streamlit as st
import time
import matplotlib.pyplot as plt
# import serial  # Uncomment for real data
import random  # Used only for simulation

# Page config
st.set_page_config(page_title="CanSat Live", layout="wide")

# Pastel background and soft UI
st.markdown(
    """
    <style>
        body {
            background-color: #002147;
            color: white;
        }
        .stApp {
            background-color: #002147;
        }
        .block-container {
            padding: 2rem;
        }
        .css-18e3th9, .css-1d391kg {
            background-color: #002147;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Cansat Real-Time Data Viewer")

# Serial settings (replace COM3 if needed)
SERIAL_PORT = "COM3"
BAUD_RATE = 115200

# Initialize session state
if "reading" not in st.session_state:
    st.session_state.reading = False
if "temp_data" not in st.session_state:
    st.session_state.temp_data = []
    st.session_state.humidity_data = []
    st.session_state.timestamps = []

# Start/Stop Buttons
col1, col2 = st.columns(2)
if col1.button("Start Reading"):
    st.session_state.reading = True
if col2.button("Stop Reading"):
    st.session_state.reading = False

# For simulation (comment this out and uncomment serial for real data)
ser = "SIMULATED"

# # Uncomment for actual serial use:
# try:
#     ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
# except Exception as e:
#     st.error(f"Could not connect to serial port: {e}")
#     ser = None

# Reading and plotting
if st.session_state.reading and ser:
    try:
        # Simulated values
        temp = round(random.uniform(24, 35), 2)
        humidity = round(random.uniform(40, 80), 2)
        
        # For real data:
        # line = ser.readline().decode().strip()
        # if line:
        #     temp, humidity = map(float, line.split(","))

        st.session_state.temp_data.append(temp)
        st.session_state.humidity_data.append(humidity)
        st.session_state.timestamps.append(time.strftime("%H:%M:%S"))

        if len(st.session_state.temp_data) > 20:
            st.session_state.temp_data.pop(0)
            st.session_state.humidity_data.pop(0)
            st.session_state.timestamps.pop(0)

    except Exception as e:
        st.error(f"Error reading data: {e}")

# Plot with smaller size and pastel colors
if st.session_state.temp_data:
    fig, ax = plt.subplots(figsize=(6, 3.5))  # Smaller size

    ax.plot(
        st.session_state.timestamps,
        st.session_state.temp_data,
        label="Temperature (°C)",
        color="#fda4af",  # pastel pink
        marker="o"
    )
    ax.plot(
        st.session_state.timestamps,
        st.session_state.humidity_data,
        label="Humidity (%)",
        color="#93c5fd",  # pastel blue
        marker="o"
    )
    ax.set_xlabel("Time", color="white")  # Set label color to white
    ax.set_ylabel("Value", color="white")  # Set label color to white
    ax.set_title("Cansat Temperature & Humidity", color="white")  # Set title color to white
    ax.legend(facecolor='#002147', edgecolor='white', labelcolor='white')  # Make legend text white and background dark
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis='x', rotation=45, colors='white')  # Change tick label color to white
    ax.tick_params(axis='y', colors='white')  # Change y-axis tick label color to white
    fig.patch.set_facecolor('#002147')  # Very soft blue background
    st.pyplot(fig)

# Refresh loop
if st.session_state.reading:
    time.sleep(1)
    st.rerun()
