import streamlit as st
from PIL import Image
import torch
from torchvision import models, transforms

# Load your model
@st.cache_resource
def load_model():
    # Initialize the ResNet model with the correct number of output classes
    model = models.resnet152(num_classes=2)  # Ensure num_classes matches your training setup
    
    # Load the state_dict and handle the mismatch by setting strict=False
    model.load_state_dict(torch.load("model/resnet152_ai_vs_real_img_model.pth", map_location=torch.device('cpu')), strict=False)
    
    # Set the model to evaluation mode
    model.eval()
    return model

model = load_model()

# Define transformations (adjust as needed for your model)
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Match model's expected input size
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Adjust to your model's training normalization
])

# Define class names
class_names = ["Real", "Fake"]

# Streamlit app UI
st.title("Real or Fake Art Classifier")
st.write("Upload an image to determine if it's 'Real' or 'Fake' art.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process and classify the image
    if st.button("Classify"):
        # Apply transformations
        input_tensor = transform(image).unsqueeze(0)

        # Perform inference
        with torch.no_grad():
            output = model(input_tensor)
            _, predicted_class = torch.max(output, 1)
            predicted_label = class_names[predicted_class.item()]

        # Display the result
        st.write(f"Prediction: **{predicted_label}**")

