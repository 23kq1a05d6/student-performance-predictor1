🎓 Student Performance Predictor

📁 Folder Structure

Student_Performance_Predictor/
│
├── app.py                # Main Streamlit app
├── student_data.csv      # Dataset file
├── requirements.txt      # Library dependencies
└── README.md             # Project documentation

📂 Project Files Description

📄 app.py

This is the main Python file that runs the Streamlit application.
It loads the dataset, trains the ML model, accepts user input, and shows predicted marks and pass/fail output.

📊 student_data.csv

This dataset contains sample student records used to train the ML model.
It includes Attendance, CGPA, study hours, assignment marks, internal marks, quiz marks, final % and pass/fail result.

📋 requirements.txt

Contains the list of Python libraries needed for this project such as Streamlit, Pandas, NumPy, and Scikit-learn.

📝 README.md

Documentation file that explains the project, setup steps, technologies used, and file details.

📘 What the project does

This project predicts a student’s semester percentage and whether they will Pass or Fail based on their academic details.
The user enters information like:

Attendance percentage

Previous CGPA

Study hours per week

Assignment completion rate

Mid exam marks

Quiz/test scores


The app then uses Machine Learning to analyze these details and gives a prediction about the student’s result and expected percentage.


---

⚙ How to install or run it

1. Save the project files (including app.py and student_data.csv) in one folder.


2. Open VS Code or Command Prompt in that folder.


3. Make sure you have Python installed.


4. Install the required libraries by typing:

pip install streamlit pandas scikit-learn numpy

5. Run the app using the command:

streamlit run app.py

6. A web page will open where you can enter student details and get predictions.

---

💻 What technologies it uses

Python – main programming language

Streamlit – web UI framework

Pandas & NumPy – data handling

Scikit-learn (Random Forest) – machine learning model



---

👩‍💻 Who created it

This project was created by .......... as a beginner-friendly Machine Learning + Streamlit project to predict student performance in a simple and interactive way.


---

🤝 How to contribute or report issues

If you want to improve the project:

Add more features or better UI

Add more student records to dataset

Try different ML algorithms

Report bugs or suggestions

---
✅ Conclusion

This project demonstrates how Machine Learning can predict student performance using academic details.
It is a simple, beginner-friendly application built with Python + Streamlit.

With more data and enhancements, it can evolve into a complete student performance analysis system.

Keep learning, experimenting, and improving! 🚀
