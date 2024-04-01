# Stress Detector

Stress Detector is a simple Streamlit application that predicts whether the input text indicates stress or not. It utilizes a pre-trained text classification model to make predictions.

## About Project

This project aims to provide a user-friendly interface for users to input text and quickly determine if the text suggests stress. The model behind the application has been fine-tuned on a dataset to classify text into "Stressed" or "Not Stressed" categories.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using ```bashpip install -r requirements.txt```.
3. Run the Streamlit application using ```bashstreamlit run main.py```.
4. Input text into the provided textbox.
5. Click the "Predict" button to see the prediction.

## Model

The model used in this project  which is a pre-trained text classification model fine-tuned for the task of stress detection.

## Dependencies

- Streamlit
- Transformers
- Torch

You can install these dependencies using the following command:
```bash
pip install -r requirements.txt
```

## Author

This project was created by [Adarsh Ajay]. Feel free to reach out with any questions or feedback.

## License

This project is licensed under the [MIT License](LICENSE).
