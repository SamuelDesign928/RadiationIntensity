# Gamma Radiation Intensity Graph

This project involves graphing the intensity of gamma radiation as a function of distance. The data and analysis in this project are based on actual results from a practical experiment conducted for my A-level Physics coursework.

## Overview

The code provided in this repository creates a scatter plot of the experimental data and calculates the line of best fit using linear regression. It then extends the x-axis to allow for extrapolation and visualizes the gamma radiation intensity with respect to distance.

## How It Works

- **Data Input:** The code uses pre-collected data points representing the distance from the gamma source (in cm) and the corresponding intensity (in Bq).
- **Linear Regression:** The line of best fit is calculated using the `scipy.stats.linregress` function, which provides the slope, intercept, and other relevant statistics.
- **Plotting:** The code generates a scatter plot for the data points and overlays the line of best fit, extending the x-axis for better visualization. The plot is labeled with axis titles, a legend, and an annotation showing the gradient (slope).
- **Visualization:** The resulting plot visually represents the relationship between the distance from the gamma source and the measured radiation intensity.

## How to Run

To run the code:

1. Ensure you have Python installed along with the required libraries (`matplotlib`, `numpy`, `scipy`).
2. Clone this repository to your local machine or copy and paste the code.
3. Run the script using a Python interpreter:

    ```bash
    python gamma_radiation_intensity.py
    ```

4. The plot will be displayed, showing the data points, line of best fit, and relevant annotations.

## Practical Experiment

The data used in this code was collected during a practical experiment as part of my A-level Physics coursework. The experiment involved measuring gamma radiation intensity at various distances from a radioactive source. The aim was to understand the inverse square relationship between radiation intensity and distance.



