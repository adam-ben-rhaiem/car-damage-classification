# 🚗 Car Damage Classification

Classifying the **severity of car damage** is crucial for insurance claims, safety evaluations, and automated vehicle assessments.  
In this project, we **compare four different deep learning models** to classify car damage into three categories:

- 🟢 **Minor**
- 🟡 **Moderate**
- 🔴 **Severe**

---

## 📊 Dataset

**Source:** [Kaggle - Car Damage Severity Dataset](https://www.kaggle.com/datasets/prajwalbhamere/car-damage-severity-dataset)

The dataset is well-balanced with samples across three classes and is used to evaluate performance across all four models.

### 📈 Dataset Distribution

![Dataset Distribution](https://github.com/user-attachments/assets/6afc2256-917f-4768-874f-9f2dbeff7f84)

---

## 🧪 Model Comparisons

We applied and evaluated the following models:

---

### 🔧 1. CNN Model (Built from Scratch)

#### 📉 Training vs Validation Loss

![CNN Loss](https://github.com/user-attachments/assets/2b6d7712-befe-4bf7-ba26-c5f0b3d61810)

#### 📈 Training vs Validation Accuracy

![CNN Accuracy](https://github.com/user-attachments/assets/2314ec67-db8a-4b72-937f-e5c730da28f8)

#### 🧩 Confusion Matrix

![CNN Confusion Matrix](https://github.com/user-attachments/assets/9057e83e-6ce8-4ad6-b2ca-d7e379e8fcb2)

#### 🧾 Classification Report

![CNN Classification](https://github.com/user-attachments/assets/8926698c-e0da-4fe8-ab19-1d48e4e2e1f6)

---

### 📱 2. MobileNetV2 (Transfer Learning)

#### 🏗️ Model Architecture

![MobileNetV2 Architecture](https://github.com/user-attachments/assets/6b1a697e-d692-4e9e-bef9-c94bb1e6b43f)

#### 📉 Loss Curve

![MobileNetV2 Loss](https://github.com/user-attachments/assets/275b018f-1633-493c-b673-d4868bd7eaae)

#### 📈 Accuracy Curve

![MobileNetV2 Accuracy](https://github.com/user-attachments/assets/e901b3f7-8b9b-4236-9c1d-43a9b0f64755)

#### 🧩 Confusion Matrix

![MobileNetV2 Confusion Matrix](https://github.com/user-attachments/assets/170a9352-895e-4cdc-888b-c9bb60e22c88)

#### 🧾 Classification Report

![MobileNetV2 Classification](https://github.com/user-attachments/assets/15db7b74-17f1-4fc0-9beb-6cb75dbb1de1)

---

### 🏛️ 3. VGG16 (Transfer Learning)

#### 🏗️ Model Architecture

![VGG16 Architecture](https://github.com/user-attachments/assets/7edabebf-de67-426e-908e-a37163ced2ff)

#### 📉 Loss Curve

![VGG16 Loss](https://github.com/user-attachments/assets/55565212-2f31-4a96-922c-a4e686d4a051)

#### 📈 Accuracy Curve

![VGG16 Accuracy](https://github.com/user-attachments/assets/86f5fea6-c640-45d1-9c0a-f44d31a727b9)

#### 🧩 Confusion Matrix

![VGG16 Confusion Matrix](https://github.com/user-attachments/assets/8825b58b-d319-40d7-9599-b3ae3aae06bc)

#### 🧾 Classification Report

![VGG16 Classification](https://github.com/user-attachments/assets/e6772ba2-dde4-4600-b6c5-0fa11dcc66f3)

---

## 🧠 Conclusion

This project provides a comprehensive comparison between custom CNN and popular pretrained architectures (MobileNetV2, VGG16).  
It reveals:

- 📉 Training loss trends
- 📈 Accuracy performance
- 🧩 Confusion matrices
- 📝 Detailed classification reports

Each model has strengths, and the choice depends on the deployment constraints and accuracy requirements.

---

## 🚀 Future Work

- ✅ Add more advanced architectures (e.g., EfficientNet, ResNet)  
- 🧪 Integrate cross-validation  
- 💡 Deploy as a web app for user upload and real-time predictions  

---

## 🛠️ Tech Stack

- Python 🐍  
- TensorFlow / Keras  
- OpenCV   
- Scikit-learn  
- Matplotlib / Seaborn  
- NumPy / Pandas  


## 🛠️ Getting Started

### 📦 Prerequisites
Make sure you have the following installed:

- Python 
- Git
- Jupyter Notebook or JupyterLab
- A modern GPU (recommended for training)
- pip or conda for package management

### 🧰 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/car-damage-classification.git
cd car-damage-classification

---
