# Wine Quality Predictor

This is a simple web application that predicts the quality of wine based on various input parameters. The application is built using Flask, a Python web framework, and a pre-trained machine learning model.

## Features

- Predict wine quality based on input parameters.
- Provides user-friendly input form with validation.
- Displays the predicted wine quality on the web page.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Required Python packages can be installed using `pip` by running `pip install -r requirements.txt`.
- Pre-trained machine learning model (`wine.model`) is included in the project.

### Installation

1. Clone the repository:
   ```bash
   pip install flask
   pip install pandas
   pip install scikit learn
   python app.py

The application will be accessible at http://localhost:5000 in your web browser.

### Usage
Visit http://localhost:5000 in your web browser.

Fill in the input fields with wine parameters such as acidity, volatile acidity, citric acid, and more.

Click the "Predict" button.

The predicted wine quality, on a scale of 0 to 10, will be displayed on the web page.

### Contributing
Contributions are welcome. If you find a bug or have an idea for an improvement, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
This project was created by [Vedant Kadam].
Machine learning model trained on wine data is based on [Random Forest Regressor].
