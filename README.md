# Traffic-Flow-Data-Analyzer
![Histogram-demo](/Images/Histogram.png)

As part of our Software Development coursework, I built a command-line application in Python to analyze traffic data collected from two key junctions.
## 🚦 Traffic Flow Data Analyzer — Python-Based Analytical Tool

📅 **December 2024**  
🏫 **University of Westminster**

As part of my Software Development coursework, I developed a **command-line Python application** to analyze traffic flow data collected from two key junctions:

- **Elm Avenue / Rabbit Road**
- **Hanley Highway / Westway**

The application works with real-world structured **CSV datasets** containing vehicle movement, type, speed, direction, and weather information recorded over **24-hour periods**.

---

### 🔍 Project Objectives

- ✅ **Task A** – Accept and validate a user-specified date to locate and load the relevant traffic CSV file.
- ✅ **Task B** – Process the file to extract key traffic insights including vehicle counts, speed violations, and direction changes.
- ✅ **Task C** – Automatically log analysis results into a clear and readable text report.
- ✅ **Task D** – Generate basic data visualizations (like histograms) using `graphics.py` for improved data interpretation.

---

### ✨ Key Features

#### 📅 Date Input Validation
- Validates a date input and maps it to appropriate filenames (e.g., `traffic_data21062024.csv`).

#### 📊 Traffic Pattern Analysis
- Vehicle type distribution
- Travel directions
- Speed behavior and violations
- Specific vehicle movement queries (e.g., number of buses heading north)

#### 📝 Report Generation
- Outputs clean, structured analysis reports to a local `.txt` file.

#### 📈 Basic Data Visualization
- Visualizes selected data insights (like vehicle counts by type) using simple `graphics.py` plots.

---

### 🧰 Tools & Technologies

- **Python** (Procedural Programming)
- `csv` module (for file operations)
- `graphics.py` (for visualizations)
- File I/O (for report generation)

---

## 📖 What I Learned

This project enhanced my skills in:

- Real-world data parsing
- User input validation
- Logical conditions for data analysis
- File handling for report generation
- Basic data visualization using Python

---

## 📌 Future Improvements

- Add more advanced visualizations using **matplotlib**
- Implement **object-oriented programming** for scalability
- Integrate **real-time data streaming support**

---

## 📑 License

This project is for **academic use** as part of the **University of Westminster Software Development coursework**.

Additionally, the source code is made available under the [MIT License](LICENSE). You are free to use, modify, and distribute this project with proper attribution.
