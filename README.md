# Ecommerce-Segmentation

# Customer Segmentation and Behavior Analysis

**Introduction**

This project aims to analyze customer behavior and segment customers based on their interaction and purchasing patterns. Understanding customer segments can help businesses tailor marketing strategies, improve customer retention, and optimize product offerings.

**DataSet**

The dataset (ecom customer_data.xlsx) contains information about customers including their gender, orders, and various types of searches they performed on an e-commerce platform.

**Workflow**

The project workflow is structured as follows:

**1. Data Loading and Preprocessing**

Libraries Used: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, and Yellowbrick.
Loading Data: The dataset is loaded from an Excel file into a Pandas DataFrame for further analysis.
Initial Data Exploration: Checking data structure, handling duplicates, and missing values.
Data Visualization: Exploring data distributions and relationships using visualizations like count plots and box plots.

**2. Feature Engineering**

Creating New Features: Derived a new feature ('Total Dearch') by summing up search activities across different categories.

**3. Data Normalization**

Normalization: Applied MinMax scaling to normalize numerical features for clustering.

**4. Clustering**

Determining Optimal K: Used the elbow method and silhouette analysis to determine the optimal number of clusters for segmentation.
K-Means Clustering: Implemented K-Means clustering to segment customers into distinct clusters based on their normalized features.

**5. Results Interpretation**

Cluster Analysis: Analyzed characteristics of each cluster such as total searches and past orders.
Visualization: Visualized cluster results using bar plots and count plots to understand customer distribution and behavior across clusters.

**6. Conclusion**

Insights: Derived insights from customer segmentation which can guide targeted marketing campaigns, improve customer engagement, and enhance business strategies.
Future Steps: Discuss potential future steps such as deploying predictive models for customer behavior or integrating real-time data for dynamic segmentation.

**Usage**

Dependencies: Ensure all necessary Python libraries are installed (pip install -r requirements.txt).
Execution: Run the Python script (customer_segmentation.py) to execute the entire workflow from data preprocessing to clustering and visualization.

**Files**
1. ecom customer_data.xlsx: Original dataset containing customer information.
2. customer_segmentation.py: Python script implementing data analysis, preprocessing, clustering, and visualization.
   
**Authors**

Anushka Sharma: https://github.com/AnushkaAn/

**Acknowledgments**

- Pandas: Used for data manipulation and analysis.
- NumPy: Utilized for numerical operations and array handling.
- Matplotlib: Used for creating static, animated, and interactive visualizations.
- Seaborn: Used for statistical data visualization based on Matplotlib.
- Scikit-Learn: Used for machine learning models, preprocessing, and evaluation.
- Yellowbrick: Utilized for visualizing the elbow method and silhouette analysis for clustering.
- GitHub: Used for version control and collaboration.



