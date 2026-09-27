# 🌱 Plant Disease Prediction and Recommendation System

An AI-based **Plant Disease Prediction and Recommendation System** that uses deep learning and a Streamlit web application to identify possible plant diseases from leaf images.

The project trains and compares three image-classification approaches:

- **Custom CNN**
- **MobileNetV2**
- **ResNet50**

The selected model can predict the disease class from an uploaded leaf image and display a confidence score along with available treatment and prevention recommendations.

---

##  Dataset:

    https://www.kaggle.com/datasets/emmarex/plantdisease?utm_source=chatgpt.com

---
## 📌 Project Overview

Plant diseases can significantly affect crop production and quality. Early identification can help farmers and growers take appropriate action.

This project provides an image-based approach where a user uploads a plant leaf image and the system:

1. Loads the uploaded image.
2. Resizes it to **224 × 224** pixels.
3. Preprocesses the image for the trained deep-learning model.
4. Predicts the disease class.
5. Calculates the prediction confidence.
6. Displays treatment information when available.
7. Displays prevention information when available.

The Streamlit application is implemented in `app.py`.

---

## ✨ Features

- 🌿 Plant leaf image upload
- 🤖 Deep-learning-based disease classification
- 🧠 Comparison of CNN, MobileNetV2, and ResNet50
- 📊 Model accuracy comparison
- 🔍 Prediction confidence score
- 💊 Treatment recommendation
- 🛡️ Prevention recommendation
- 🖥️ Interactive Streamlit web interface
- 💾 Saved Keras models for deployment

---

## 🏷️ Disease Classes

The Streamlit application currently defines these classes:

1. Pepper bell Bacterial spot
2. Pepper bell healthy
3. Potato Early blight
4. Potato Late blight
5. Potato healthy
6. Tomato Early blight
7. Tomato Late blight
8. Tomato healthy

The exact class list is obtained from the training dataset in the notebook.

---

# 🔐 Limitations

- Model predictions depend heavily on image quality and training data.
- The system may perform differently on real-world images than on dataset images.
- A confidence score does not guarantee that a prediction is correct.
- The current recommendation system covers only selected classes.
- The notebook uses a validation split; a separate independent test set would strengthen evaluation.
- The current application contains a local Windows model path that should be changed before sharing or deployment.
- Agricultural treatment decisions should be verified with appropriate local expertise and product labels.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| TensorFlow / Keras | Deep learning |
| CNN | Image classification |
| MobileNetV2 | Transfer learning |
| ResNet50 | Transfer learning |
| NumPy | Numerical processing |
| Pandas | Data analysis |
| Matplotlib | Visualization |
| Seaborn | Visualization |
| Scikit-learn | Evaluation metrics |
| Pillow | Image processing |
| Streamlit | Web application |
| Git / GitHub | Version control and project sharing |

---

# ⭐ Project Highlights

- Deep-learning-based plant disease classification
- Custom CNN implementation
- Transfer learning with MobileNetV2
- Transfer learning with ResNet50
- Data augmentation
- Validation-based model comparison
- Streamlit deployment interface
- Confidence-based prediction
- Treatment and prevention recommendations
- Clear path toward mobile, edge, cloud, explainable-AI, and multilingual extensions

---

## 📬 Future Development

The project can be expanded from a basic image-classification application into a broader **AI-assisted crop-health platform** by combining image diagnosis with severity estimation, environmental data, explainable AI, multilingual support, mobile/edge deployment, and expert-validated recommendations.
