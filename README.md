# video link ;- https://drive.google.com/file/d/16aZrY-51IiwEqBjswj3rb3F5B4pDjJj6/view?usp=sharing
# Student Performance Data Analysis

## 📌 Project Overview

Student Performance Data Analysis is a Python-based data analysis project that analyzes students' academic performance, attendance, study habits, coding activity, projects, skills, and placement status.

The main goal of this project is to identify patterns and factors related to student performance and placement outcomes using data analysis and visualization techniques.

---

## 🎯 Objectives

- Analyze students' academic performance.
- Study the relationship between attendance and CGPA.
- Analyze the relationship between internal marks, external marks, and CGPA.
- Compare average CGPA across different departments.
- Analyze CGPA across different semesters.
- Study coding activity and placement status.
- Analyze projects and skills with respect to placement.
- Generate meaningful insights using data visualization.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- OpenPyXL
- Jupyter / VS Code

---

## 📂 Project Structure

```text
Student-Performance-Data-Analysis/
│
├── dataset/
│   └── student_data_final (1).xlsx
│
├── outputs/
│   ├── attendance_distribution.png
│   ├── attendance_vs_cgpa.png
│   ├── cgpa_distribution.png
│   ├── correlation_heatmap.png
│   ├── department_cgpa.png
│   ├── external_marks_vs_cgpa.png
│   ├── internal_marks_vs_cgpa.png
│   ├── line_semester_cgpa.png
│   ├── pie_placement_distribution.png
│   ├── study_hours_distribution.png
│   └── study_hours_vs_cgpa.png
│
└── src/
    └── student_performance_analysis.py
📊 Dataset

The dataset contains information about 500 students and includes attributes such as:

Student ID
Name
Gender
Age
Department
Semester
Attendance Percentage
Internal Marks
External Marks
Assignment Marks
Study Hours per Day
CGPA
Placement Status
LeetCode
CodeChef
HackerRank
Projects
Skills
Problems Solved
Certification

The dataset was obtained from Kaggle.

🔍 Analysis Performed
1. Data Loading
Loaded the dataset using Pandas.
Removed completely empty columns.
Displayed the dataset and basic information.
2. Data Exploration
Checked dataset shape.
Examined column names and data types.
Identified missing values.
Generated statistical summaries.
3. Data Cleaning
Handled missing certification values.
Checked and removed duplicate records.
Validated attendance and CGPA values.
4. Data Preprocessing
Converted numerical columns into appropriate data types.
Encoded categorical variables for analysis.
5. Exploratory Data Analysis

Analyzed:

CGPA distribution
Attendance
Study hours
Academic performance
6. Academic Performance Analysis

Studied:

Internal Marks vs CGPA
External Marks vs CGPA
Department-wise Average CGPA
Semester-wise Average CGPA
7. Coding and Placement Analysis

Analyzed:

Coding activity
Problems solved
Projects and placement
Skills and placement
Overall placement distribution
8. Data Visualization

The project generates visualizations including:

Bar charts
Pie charts
Line graphs
Histograms
Scatter plots
Correlation heatmaps
📈 Key Findings
The average CGPA of students is approximately 7.30.
External marks show a strong positive relationship with CGPA.
Internal marks show a moderate positive relationship with CGPA.
CSE has the highest average CGPA among the departments in this dataset.
The dataset contains 100 placed students and 400 not-placed students.
Coding activity alone does not show a strong difference between placed and not-placed students in this dataset.
Study hours show a very weak relationship with CGPA in this dataset.
▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/Tripurakilaparthi/Student-Performance-Data-Analysis-.git
2. Open the project folder
cd Student-Performance-Data-Analysis-
3. Install required libraries
pip install pandas numpy matplotlib seaborn openpyxl
4. Run the Python program
python src/student_performance_analysis.py

The generated graphs will be saved in the outputs folder.

👩‍💻 Team Members
P. Surya Varshitha
k. Tripura
M. Bhagya Satya Sri
M. Veeresh
📌 Conclusion

This project demonstrates how Python-based data analysis can be used to understand student academic performance, coding activity, and placement patterns. The visualizations and statistical analysis help identify important relationships within the dataset.
📚 Dataset Source

Dataset obtained from Kaggle.
