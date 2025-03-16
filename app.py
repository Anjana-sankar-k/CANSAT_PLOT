import streamlit as st
import serial
import time
import matplotlib.pyplot as plt

# Set up serial communication (Update 'COMx' or '/dev/ttyUSBx' based on your system)
SERIAL_PORT = "COMx"  # Change to your port (e.g., '/dev/ttyUSB0' for Linux/Mac)
BAUD_RATE = 115200

# Initialize serial connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Wait for connection to establish
except Exception as e:
    st.error(f"Could not connect to serial port: {e}")
    ser = None

# Streamlit UI
st.title("CanSat Real-Time Data Visualization")
st.write("Live temperature and humidity readings from CanSat.")

# Create figure for plotting
fig, ax = plt.subplots()
temp_data, humidity_data = [], []
timestamps = []

# Function to update the graph
def update_graph():
    ax.clear()
    ax.plot(timestamps, temp_data, label="Temperature (°C)", color="red", marker="o")
    ax.plot(timestamps, humidity_data, label="Humidity (%)", color="blue", marker="o")
    
    ax.set_xlabel("Time")
    ax.set_ylabel("Values")
    ax.legend()
    ax.set_title("Temperature & Humidity Over Time")
    st.pyplot(fig)

# Read and display data in real-time
if ser:
    while True:
        try:
            line = ser.readline().decode().strip()
            if line:
                try:
                    temp, humidity = map(float, line.split(","))
                    temp_data.append(temp)
                    humidity_data.append(humidity)
                    timestamps.append(time.strftime("%H:%M:%S"))

                    if len(temp_data) > 20:  # Keep the last 20 readings
                        temp_data.pop(0)
                        humidity_data.pop(0)
                        timestamps.pop(0)

                    update_graph()
                except ValueError:
                    st.warning("Received malformed data.")
        except Exception as e:
            st.error(f"Error reading serial data: {e}")
            break
else:
    st.error("Serial connection not established.")

