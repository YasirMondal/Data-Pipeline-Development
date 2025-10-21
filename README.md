🧠 MNIST Digit Classifier: Deep Learning for Handwritten Digits

*COMPANY*: CODTECH IT SOLUTIONS PVT.LTD
*NAME*: Yasir Siraj Mondal
*DOMAIN*: Data Science
*DURATION*: 12 weeks
*MENTOR*: Neela Santhosh Kumar


📘 Description

This Python script implements a Convolutional Neural Network (CNN) to classify handwritten digits from the MNIST dataset. The workflow includes data preprocessing (normalization and one-hot encoding), model building (Conv2D, MaxPooling2D, Flatten, Dense layers), training, evaluation, and visualization. The trained model is saved for reuse, providing a complete end-to-end image classification pipeline.


⚙ Steps Performed

1. Extract – Loads the MNIST dataset directly from Keras datasets.

2. Preprocess – Reshapes images to 28×28×1 and normalizes pixel values to range 0–1. Converts labels to one-hot encoding.

3. Transform / Model Building – Builds a simple CNN using Keras:
Conv2D + MaxPooling2D layers to extract image features
Flatten + Dense layers for classification
Softmax output layer for 10 classes

4. Train – Trains the model on 60,000 training images for 5 epochs with a validation split of 20%.

5. Evaluate & Visualize – Prints test accuracy (~98.5%), plots training/validation accuracy and loss, and shows predictions for sample test images.

6. Save – Saves the trained model as mnist_model.h5 for later use without retraining.



🧰 Requirements

Install the necessary libraries:

pip install tensorflow keras matplotlib numpy

Optional (if using a virtual environment):

python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate


▶ How to Run

1. Open the folder containing classifier.py in VS Code or terminal.

2. Ensure the virtual environment is activated (if used).

3. Run the script:
python classifier.py

4. The script will:
Load and preprocess the MNIST dataset
Train the CNN model (first run)
Evaluate test accuracy
Display training/validation curves and sample predictions
Save the trained model as mnist_model.h5

> Subsequent runs automatically load the saved model to skip retraining.



🧾 Output

mnist_model.h5 → Trained CNN model ready for reuse

Plots → Accuracy & loss curves for training/validation

Sample Predictions → Visualizations of predicted digits


🧱 Tech Stack

Python 3.8+

TensorFlow / Keras

Matplotlib

NumPy
