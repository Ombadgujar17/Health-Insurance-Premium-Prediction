# Health Insurance Premium Prediction

This project predicts health insurance premiums based on user input using a trained machine learning model. It provides a interface: a Streamlit web app(see `app.py`).

## Features
- Predicts insurance premium based on:
  - Age
  - Sex
  - BMI
  - Number of Children
  - Smoking status
- User-friendly web interface (Streamlit)
- Flask app for alternative deployment

## Project Structure
```
├── app.py                        # Streamlit app
├── model.pkl                     # Trained ML model

```

## Getting Started

### Prerequisites
- Python 3.7+
- Install required packages:
  ```bash
  pip install streamlit scikit-learn
  ```

### Running the Streamlit App
```bash
streamlit run app.py
```

## Usage
1. Open the app in your browser (Streamlit).
2. Enter your details (age, sex, BMI, children, smoker).
3. Click **Predict Premium** to see your predicted insurance premium.

## Model
- The model is trained using the data and code in the provided Jupyter notebook.
- The trained model is saved as `model.pkl`.

## License
This project is for educational purposes.
