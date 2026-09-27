import streamlit as st
import tensorflow as tf
import numpy as np

from PIL import Image


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌱",
    layout="centered"
)


# -----------------------------------
# LOAD MODEL
# -----------------------------------

MODEL_PATH = r"C:\Users\admin\Downloads\PlantVillage\resnet50_model.keras"

model = tf.keras.models.load_model(
    MODEL_PATH
)


# -----------------------------------
# CLASS NAMES
# -----------------------------------

class_names = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___healthy"
]


# -----------------------------------
# RECOMMENDATIONS
# -----------------------------------

recommendations = {

    "Tomato___Early_blight": {
        "treatment":
        "Remove severely affected leaves and follow appropriate fungicide label directions.",
        "prevention":
        "Maintain good spacing and avoid prolonged leaf wetness."
    },

    "Tomato___Late_blight": {
        "treatment":
        "Remove affected plant material and follow locally recommended late-blight management.",
        "prevention":
        "Monitor plants regularly and minimize prolonged moisture on foliage."
    },

    "Tomato___healthy": {
        "treatment":
        "No disease treatment is indicated by this classification.",
        "prevention":
        "Continue regular monitoring and good crop management."
    },

    "Potato___Early_blight": {
        "treatment":
        "Remove heavily affected foliage and follow recommended disease-management practices.",
        "prevention":
        "Maintain good plant spacing and reduce prolonged leaf wetness."
    },

    "Potato___Late_blight": {
        "treatment":
        "Remove affected material and follow locally recommended disease-management practices.",
        "prevention":
        "Monitor the crop frequently and minimize prolonged moisture."
    },

    "Potato___healthy": {
        "treatment":
        "No disease treatment is indicated by this classification.",
        "prevention":
        "Continue regular crop monitoring."
    }
}


# -----------------------------------
# TITLE
# -----------------------------------

st.title("🌱 Plant Disease Detection")
st.write(
    "Upload a plant leaf image to detect possible disease."
)


# -----------------------------------
# UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)


# -----------------------------------
# PREDICTION
# -----------------------------------

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.image(
        image,
        caption="Uploaded Leaf",
        use_container_width=True
    )

    # Resize
    img = image.resize(
        (224, 224)
    )

    # Convert
    img_array = np.array(img)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    # MobileNetV2 preprocessing
    img_array = (
        img_array / 127.5
    ) - 1

    # Prediction
    predictions = model.predict(
        img_array
    )

    predicted_index = np.argmax(
        predictions[0]
    )

    disease = class_names[
        predicted_index
    ]

    confidence = (
        predictions[0][predicted_index]
        * 100
    )


    # -----------------------------------
    # RESULT
    # -----------------------------------

    st.subheader("🔍 Prediction")

    st.success(
        f"Disease: {disease}"
    )

    st.info(
        f"Confidence: {confidence:.2f}%"
    )


    # -----------------------------------
    # RECOMMENDATION
    # -----------------------------------

    if disease in recommendations:

        st.subheader("💊 Treatment")

        st.write(
            recommendations[disease]["treatment"]
        )

        st.subheader("🛡️ Prevention")

        st.write(
            recommendations[disease]["prevention"]
        )

    else:

        st.warning(
            "Recommendation is not available for this class."
        )