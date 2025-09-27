# SDkA-Synthetic-Data-Integrated-k-Anonymity-
This repository provides implementation of SDkA model.


Main Modules of the proposed SDkA 
<br>
There are two key modules in the proposed DCLD model.
<br>
1- Data Pre-processing
<br>
In this module, the data to be anonymized is pre-processed to make it anonymization-ready. This work innovates the existing work and amalgamates synthetic data with real data to address the distribution imbalance problem. When the class imbalance problem is addressed then the constraints regarding SA values and distributions are effectively met whereas most of the existing methods do not fix this problem, leading to two crucial design problems (i.e., expose privacy or leave many records un-processed).**
<br>
2- Level-0/1 Anonymization
<br>
In this module, minimal necessary anonymization is applied to curate high-quality data. Specifically, the population-level information is abstracted and minimal necessary generalization is applied. It is worth noting that privacy is not risked due to minimal generalization as there exists higher uncertainty in the SA column due to synthetic data addition.
<br>
.....
Next, we provide the details of the implementation that can help the re-implementation of the proposed SDkA model.

**Dataset used in Experimentation**

Four real-world publicly available datasets have been used to evaluate the effectiveness of the proposed DCLD.

1-Adult dataset

This is a reasonable-sized dataset encompassing US individuals' diverse information (demographics). The database and privacy community have widely used this dataset for experimentation purposes. Its original form is available at http://archive.ics.uci.edu/dataset/2/adult. 

2- Diabetes 130-US Hospitals dataset

This is also the largest dataset encompassing the diverse medical information of individuals fetched from the clinical care at 130 US hospitals and integrated delivery networks. The database and privacy community have also used this dataset for experimentation purposes. This dataset in its original form is available at [https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008].

**Implementation process**


At the outset, it is imperative to install all required libraries. Depending upon the programming language, the necessary libraries should be included in the development environment.
Below we show a sample to install basic data processing libraries and installation procedures in Python.
<code>pip install name of library </code> i.e., <code>pip install numpy, pip install pandas, pip install scikit-learn, pip install scipy</code>.

Below, we provide the code information that can help understand the implementation and reproduce the results.

| File Name | Description of implementation | Output files/information
| ------------- | ------------- | ------------- |
| Arrange_Attributes.py  | Remove direct identifiers and arrange the remaining attributes  | Data with QIDs and SA only (The last column is SA)  |
| Imbalance_Ratio_Computing_Records Analysis.py  | Analyze the imbalance w.r.t. SA & find the # of records needed for balance  |Imbalance ratio information, and size of synthetic required for data balancing  |
| Interface_Program_SD_Generation.py  | Generating synthetic data[^1] to balance the distribution of rare SA value  | Synthetic data with identical structure to real data  |
| KLDCriteria_Aware_Clustering.py  | Clustering data as per k while ensuring sufficient diversity  | Clustered data where the size of each cluster is at least k and every cluster is diverse w.r.t. SA values  |
| Generalization-Values_Replacements.py  |Generalized data with lower level generalization | Generalized data where the functional relationship between real and anonymized data is very high |
| Skewness_Analysis.py, Homogeniety_Analysis.py, etc.   |Privacy tests to ensure better performance that standard k-anonymity | Probablistic disclosure of SA values or problematic clusters |
| Utility_Analysis.py  |Utility tests to ensure better performance that standard k-anonymity | Accuracy of the classifiers in anonymized/real dataset |

[^1]: The open-source implementation was used with slight modifications (https://github.com/sdv-dev/CTGAN). 
[^2]: The information/details about the generalization heirarchies (https://www.sciencedirect.com/science/article/pii/S2667305323000923). 


**Citing DCLD**

If you use the SDka implementation, please cite the following work:

[1] A. Majeed and S. O. Hwang, "SDkA: Synthetic Data Integrated k-Anonymity
Model for Data Sharing with Improved Utility," (To be updated soon)



