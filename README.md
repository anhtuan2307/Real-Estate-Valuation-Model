# Real Estate Valuation Model & Web App (ANN)
*Academic Project - Swinburne University of Technology COS30082 Applied Machine Learning*

##  Project Overview
This project involves developing a sophisticated Artificial Neural Network (ANN) to predict real estate prices in King County (including Seattle) using a dataset of over 21,500 sales records. The system includes a fully functional web interface for real-time property valuation.

##  Key Technical Highlights
- **Advanced Data Preprocessing:**
    - Scaled 19 features using `MinMaxScaler` for optimal neural network convergence.
    - Engineered temporal features by extracting month and year from sale dates.
    - Strategic outlier management: Retained high-value property data to ensure the model could recognize luxury estate patterns.
- **Deep Learning Architecture:**
    - Designed a 3-layer ANN (128-64-32 neurons) using Keras and TensorFlow.
    - Optimized with the **Adam** optimizer and Mean Squared Error (MSE) loss function.
    - Implemented Dropout layers (0.2) to mitigate overfitting during the 400-epoch training process.
- **Web Deployment:** Developed a responsive Flask web application featuring HTML5 input validation and interactive CSS animations (loading spinners, hover effects).

##  Performance Results
- **R-Squared Score:** 0.7929 (The model explains ~80% of the price variance).
- **Model Behavior:** Errors follow a near-normal distribution, showing high reliability for mid-range properties.

##  Tech Stack
- **AI/ML:** Python, Keras, TensorFlow, Scikit-learn, Pandas, NumPy.
- **Backend:** Flask.
- **Frontend:** HTML, CSS.

---
*Developed by: Doan Phuong Anh Tuan*
