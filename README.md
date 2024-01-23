# Game Lobby Wait Time Estimator

Welcome to the Wait Time Estimator project, developed as part of the ConUHacks VIII hackathon challenge hosted by Behaviour Interactive.

## Project Overview

This web application is designed to estimate wait times for a game lobby. It leverages a supervised regression model created using Flask and Python for the backend, and JavaScript, HTML, and CSS for the frontend.

For more information about ConUHacks VIII, visit [ConUHacks](https://conuhacks.io/).

## Getting Started

To get started with the Game Lobby Wait Time Estimator, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/NawarTurk/Wait_Time_Estimator.git

2. **Navigate to the Project Directory**: Change your current directory to the root of the project.

3. **Run the Flask Application**: You'll need to run the Flask application at the root of the project directory. Use the following command ( This will start the web application locally.
):
   ```bash
   flask run

4. **Upload and Train Historical Data**
To use the wait time estimation model, you should upload and train it using historical data. A mock historical data file, 'Mock Historical Data.csv,' is provided in the repository. Ensure that your data file follows the same format as the mock file.

5. **Add Additional Feature Values**<br>
If you have additional possible values for different features, you can incorporate them by extending the encode_dataframe(df) function in the train_model.py file.


## Key Insights and Areas for Enhancement
Experiment with different algorithms (Decision Trees, Random Forests, Neural Networks) to improve prediction accuracy.
Consider enhancing the frontend and visualization for a better user experience.
Thank you for exploring our project, and we hope it proves valuable in estimating game lobby wait times. Feel free to contribute and enhance this project further!
  

