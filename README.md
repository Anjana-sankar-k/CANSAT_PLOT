# Cansat Project (IRES-SEDS CUSAT)

This is a simulation-based project aimed at visualizing data from CanSat missions. The project uses Streamlit to present the simulation in an interactive and user-friendly way. While the current version uses simulated data, it is designed to be updated with real-time data for future use.

## Live Demo

You can view the project live here: [CanSat SEDS Live Demo](https://cansatseds.streamlit.app/)

## Features

- **Data Simulation**: The project currently simulates data relevant to CanSat missions.
- **Interactive Visualization**: Real-time data will eventually replace the simulation, and users will be able to interact with it via an intuitive interface.
- **Modular Components**: The code is structured to allow easy updates and integration with real-time data sources.

## Setup Instructions

To run the project locally:
```bash
git clone <repo-url>
cd CANSAT_PLOT
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
## Future Work
- Real-time Data Integration: Replace simulated data with real-time data from CanSat missions.
- Additional Features: Expand on the interactive features, including more detailed graphs and analysis tools.

## Contributions
Feel free to fork the repository and submit pull requests with improvements or suggestions!

## License
This project is licensed under the MIT License.
