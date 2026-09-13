# ============================================================
# STUDENT PERFORMANCE DATA ANALYSIS
# ============================================================

# ============================================================
# IMPORT LIBRARIES
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# PROJECT PATHS
# ============================================================

# Get the main project folder
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Dataset path
DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "student_data_final (1).xlsx"
)

# Output folder path
OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "outputs"
)

# Create output folder if it does not exist
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# MODULE 1: DATASET LOADING
# ============================================================

print("\n========== MODULE 1: DATASET LOADING ==========")

# Load Excel dataset
df = pd.read_excel(DATASET_PATH)

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Loaded Successfully!")
print("Dataset Shape:", df.shape)


# ============================================================
# MODULE 2: DATA EXPLORATION
# ============================================================

print("\n========== MODULE 2: DATA EXPLORATION ==========")

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns.tolist())

# Data Types
print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())


# ============================================================
# MODULE 3: DATA CLEANING
# ============================================================

print("\n========== MODULE 3: DATA CLEANING ==========")

# Missing values before cleaning
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing Certification values
if df["Certification"].isnull().sum() > 0:
    df["Certification"] = df["Certification"].fillna(
        df["Certification"].mode()[0]
    )

# Check duplicates
print("\nDuplicate Rows Before Cleaning:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("Duplicate Rows After Cleaning:")
print(df.duplicated().sum())

# Check Attendance consistency
invalid_attendance = df[
    (df["Attendance_Percentage"] < 0) |
    (df["Attendance_Percentage"] > 100)
]

print("\nInvalid Attendance Records:")
print(invalid_attendance)

# Check CGPA consistency
invalid_cgpa = df[
    (df["CGPA"] < 0) |
    (df["CGPA"] > 10)
]

print("\nInvalid CGPA Records:")
print(invalid_cgpa)

# Check categorical values
print("\nGender Values:")
print(df["Gender"].unique())

print("\nDepartment Values:")
print(df["Department"].unique())

print("\nPlacement Status Values:")
print(df["Placement_Status"].unique())

# Final missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# ============================================================
# MODULE 4: DATA PREPROCESSING
# ============================================================

print("\n========== MODULE 4: DATA PREPROCESSING ==========")

# Numerical columns
numeric_columns = [
    "Age",
    "Semester",
    "Attendance_Percentage",
    "Internal_Marks",
    "External_Marks",
    "Assignment_Marks",
    "Study_Hours_Per_Day",
    "CGPA",
    "LeetCode",
    "CodeChef",
    "HackerRank",
    "Problems Solved"
]

# Convert numerical columns
for col in numeric_columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

print("\nData Types After Conversion:")
print(df.dtypes)

# Encode categorical columns
df_encoded = pd.get_dummies(
    df,
    columns=[
        "Gender",
        "Department",
        "Placement_Status",
        "Hostel / Bus"
    ],
    dtype=int
)

print("\nEncoded Dataset:")
print(df_encoded.head())

# Academic data
academic_columns = [
    "Attendance_Percentage",
    "Internal_Marks",
    "External_Marks",
    "Assignment_Marks",
    "Study_Hours_Per_Day",
    "CGPA"
]

print("\nAcademic Data:")
print(df[academic_columns].head())

# Coding data
coding_columns = [
    "LeetCode",
    "CodeChef",
    "HackerRank",
    "Problems Solved"
]

print("\nCoding Data:")
print(df[coding_columns].head())


# ============================================================
# MODULE 5: EXPLORATORY DATA ANALYSIS
# ============================================================

print("\n========== MODULE 5: EXPLORATORY DATA ANALYSIS ==========")


# ------------------------------------------------------------
# 5.1 CGPA Distribution
# ------------------------------------------------------------

print("\nCGPA Statistics:")
print(df["CGPA"].describe())

plt.figure(figsize=(8, 5))

plt.hist(
    df["CGPA"],
    bins=10
)

plt.xlabel("CGPA")
plt.ylabel("Number of Students")
plt.title("CGPA Distribution")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "cgpa_distribution.png"
    )
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 5.2 Attendance Distribution
# ------------------------------------------------------------

print("\nAttendance Statistics:")
print(df["Attendance_Percentage"].describe())

plt.figure(figsize=(8, 5))

plt.hist(
    df["Attendance_Percentage"],
    bins=10
)

plt.xlabel("Attendance Percentage")
plt.ylabel("Number of Students")
plt.title("Attendance Distribution")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "attendance_distribution.png"
    )
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 5.3 Study Hours Distribution
# ------------------------------------------------------------

print("\nStudy Hours Statistics:")
print(df["Study_Hours_Per_Day"].describe())

plt.figure(figsize=(8, 5))

plt.hist(
    df["Study_Hours_Per_Day"],
    bins=10
)

plt.xlabel("Study Hours Per Day")
plt.ylabel("Number of Students")
plt.title("Study Hours Distribution")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "study_hours_distribution.png"
    )
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 5.4 Performance Patterns
# ------------------------------------------------------------

performance_columns = [
    "Attendance_Percentage",
    "Internal_Marks",
    "External_Marks",
    "Assignment_Marks",
    "Study_Hours_Per_Day",
    "CGPA"
]

print("\nCorrelation with CGPA:")

print(
    df[performance_columns]
    .corr()["CGPA"]
    .sort_values(ascending=False)
)


# Attendance vs CGPA

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Attendance_Percentage"],
    df["CGPA"]
)

plt.xlabel("Attendance Percentage")
plt.ylabel("CGPA")
plt.title("Attendance vs CGPA")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "attendance_vs_cgpa.png"
    )
)

plt.show()
plt.close()


# Study Hours vs CGPA

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Study_Hours_Per_Day"],
    df["CGPA"]
)

plt.xlabel("Study Hours Per Day")
plt.ylabel("CGPA")
plt.title("Study Hours vs CGPA")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "study_hours_vs_cgpa.png"
    )
)

plt.show()
plt.close()


# ============================================================
# MODULE 6: ACADEMIC PERFORMANCE ANALYSIS
# ============================================================

print("\n========== MODULE 6: ACADEMIC PERFORMANCE ANALYSIS ==========")


# ------------------------------------------------------------
# 6.1 Internal Marks vs CGPA
# ------------------------------------------------------------

internal_cgpa_corr = df[
    "Internal_Marks"
].corr(
    df["CGPA"]
)

print("\nCorrelation between Internal Marks and CGPA:")
print(internal_cgpa_corr)

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Internal_Marks"],
    df["CGPA"]
)

plt.xlabel("Internal Marks")
plt.ylabel("CGPA")
plt.title("Internal Marks vs CGPA")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "internal_marks_vs_cgpa.png"
    )
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 6.2 External Marks vs CGPA
# ------------------------------------------------------------

external_cgpa_corr = df[
    "External_Marks"
].corr(
    df["CGPA"]
)

print("\nCorrelation between External Marks and CGPA:")
print(external_cgpa_corr)

plt.figure(figsize=(8, 5))

plt.scatter(
    df["External_Marks"],
    df["CGPA"]
)

plt.xlabel("External Marks")
plt.ylabel("CGPA")
plt.title("External Marks vs CGPA")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "external_marks_vs_cgpa.png"
    )
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 6.3 Department-wise CGPA
# ------------------------------------------------------------

department_cgpa = df.groupby(
    "Department"
)["CGPA"].mean()

print("\nDepartment-wise Average CGPA:")
print(department_cgpa)

plt.figure(figsize=(8, 5))

plt.bar(
    department_cgpa.index,
    department_cgpa.values
)

plt.xlabel("Department")
plt.ylabel("Average CGPA")
plt.title("Department-wise Average CGPA")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "department_cgpa.png"
    )
)

plt.show()
plt.close()


# ============================================================
# MODULE 7: CODING & PLACEMENT ANALYSIS
# ============================================================

print("\n========== MODULE 7: CODING & PLACEMENT ANALYSIS ==========")


# ------------------------------------------------------------
# 7.1 Coding Problems Solved
# ------------------------------------------------------------

print("\nCoding Problems Solved Statistics:")
print(df["Problems Solved"].describe())

print("\nAverage Problems Solved:")
print(df["Problems Solved"].mean())


# ------------------------------------------------------------
# 7.2 Total Coding Activity
# ------------------------------------------------------------

df["Total_Coding_Activity"] = (
    df["LeetCode"] +
    df["CodeChef"] +
    df["HackerRank"]
)

print("\nTotal Coding Activity:")
print(
    df[
        [
            "Student_ID",
            "Total_Coding_Activity"
        ]
    ].head()
)


# ------------------------------------------------------------
# 7.3 Coding Activity vs Placement
# ------------------------------------------------------------

coding_placement = df.groupby(
    "Placement_Status"
)["Total_Coding_Activity"].mean()

print("\nAverage Coding Activity by Placement Status:")
print(coding_placement)


# ------------------------------------------------------------
# 7.4 Projects vs Placement
# ------------------------------------------------------------

projects_placement = pd.crosstab(
    df["Projects"],
    df["Placement_Status"]
)

print("\nProjects vs Placement:")
print(projects_placement)


# ------------------------------------------------------------
# 7.5 Skills vs Placement
# ------------------------------------------------------------

skills_placement = pd.crosstab(
    df["Skills"],
    df["Placement_Status"]
)

print("\nSkills vs Placement:")
print(skills_placement)


# ------------------------------------------------------------
# 7.6 Placement Distribution
# ------------------------------------------------------------

placement_count = df[
    "Placement_Status"
].value_counts()

print("\nPlacement Status Distribution:")
print(placement_count)


# Coding Activity vs Placement Chart

plt.figure(figsize=(8, 5))

plt.bar(
    coding_placement.index,
    coding_placement.values
)

plt.xlabel("Placement Status")
plt.ylabel("Average Coding Activity")
plt.title("Coding Activity vs Placement")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "coding_activity_vs_placement.png"
    )
)

plt.show()
plt.close()


# ============================================================
# MODULE 8: DATA VISUALISATION
# ============================================================

print("\n========== MODULE 8: DATA VISUALISATION ==========")


# ------------------------------------------------------------
# 8.1 Bar Chart
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    department_cgpa.index,
    department_cgpa.values
)

plt.xlabel("Department")
plt.ylabel("Average CGPA")
plt.title("Department-wise Average CGPA")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "bar_department_cgpa.png"
    )
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 8.2 Pie Chart
# ------------------------------------------------------------

plt.figure(figsize=(7, 7))

plt.pie(
    placement_count.values,
    labels=placement_count.index,
    autopct="%1.1f%%"
)

plt.title("Placement Status Distribution")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "pie_placement_distribution.png"
    )
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 8.3 Line Chart
# ------------------------------------------------------------

semester_cgpa = df.groupby(
    "Semester"
)["CGPA"].mean()

print("\nAverage CGPA by Semester:")
print(semester_cgpa)

plt.figure(figsize=(8, 5))

plt.plot(
    semester_cgpa.index,
    semester_cgpa.values,
    marker="o"
)

plt.xlabel("Semester")
plt.ylabel("Average CGPA")
plt.title("Average CGPA by Semester")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "line_semester_cgpa.png"
    )
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 8.4 Heatmap
# ------------------------------------------------------------

heatmap_columns = [
    "Attendance_Percentage",
    "Internal_Marks",
    "External_Marks",
    "Assignment_Marks",
    "Study_Hours_Per_Day",
    "CGPA",
    "Problems Solved"
]

correlation = df[
    heatmap_columns
].corr()

plt.figure(figsize=(9, 6))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "correlation_heatmap.png"
    )
)

plt.show()
plt.close()


# ============================================================
# MODULE 9: INSIGHT GENERATION
# ============================================================

print("\n========== MODULE 9: INSIGHT GENERATION ==========")


# ------------------------------------------------------------
# 9.1 Factors Related to CGPA
# ------------------------------------------------------------

cgpa_factors = [
    "Attendance_Percentage",
    "Internal_Marks",
    "External_Marks",
    "Assignment_Marks",
    "Study_Hours_Per_Day",
    "Problems Solved",
    "CGPA"
]

cgpa_correlation = df[
    cgpa_factors
].corr()["CGPA"]

print("\nFactors Related to CGPA:")

print(
    cgpa_correlation
    .sort_values(ascending=False)
)


# ------------------------------------------------------------
# 9.2 Placement-related Patterns
# ------------------------------------------------------------

placement_coding = df.groupby(
    "Placement_Status"
)["Total_Coding_Activity"].mean()

print("\nAverage Coding Activity by Placement Status:")

print(placement_coding)


# ------------------------------------------------------------
# 9.3 Projects and Placement
# ------------------------------------------------------------

print("\nProjects and Placement Pattern:")

print(projects_placement)


# ------------------------------------------------------------
# 9.4 Skills and Placement
# ------------------------------------------------------------

print("\nSkills and Placement Pattern:")

print(skills_placement)


# ------------------------------------------------------------
# 9.5 Overall Student Performance
# ------------------------------------------------------------

print("\nOverall Student Performance:")

print(
    df[
        [
            "Attendance_Percentage",
            "Internal_Marks",
            "External_Marks",
            "Assignment_Marks",
            "Study_Hours_Per_Day",
            "CGPA"
        ]
    ].describe()
)


# ------------------------------------------------------------
# 9.6 Department with Highest Average CGPA
# ------------------------------------------------------------

highest_department = department_cgpa.idxmax()

highest_cgpa = department_cgpa.max()

print("\nDepartment with Highest Average CGPA:")
print(highest_department)

print("\nHighest Average CGPA:")
print(highest_cgpa)


# ------------------------------------------------------------
# 9.7 Final Placement Distribution
# ------------------------------------------------------------

print("\nFinal Placement Distribution:")

print(placement_count)


# ============================================================
# PROJECT COMPLETION
# ============================================================

print("\n============================================================")
print("STUDENT PERFORMANCE DATA ANALYSIS COMPLETED SUCCESSFULLY!")
print("============================================================")

print("Total Students:", len(df))
print("Total Columns:", len(df.columns))

print("\nAll graphs have been saved in:")
print(OUTPUT_DIR)

print("============================================================")