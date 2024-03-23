# Student Future Job Prediction Portal

## Overview
This project aims to predict the future job/scope for students based on various factors such as academic performance, internships, interests, and past work experiences. The prediction is made using the Random Forest algorithm, which is a powerful machine learning technique for classification tasks.

## Features
- Predicts future job/scope for students.
- Utilizes Random Forest algorithm for prediction.
- Takes into account multiple factors including academics, internships, interests, and past work experiences.
- Provides insights into potential career paths for students.

## Installation
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/rugvedp/student_portal_ML
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Prepare your dataset containing relevant information about students' academics, internships, interests, and past work experiences.

2. Ensure that the dataset is in a compatible format (e.g., CSV, Excel).

3. Run the main script to train the Random Forest model and make predictions:

    ```bash
    python forest.py 
    ```

4. Follow the instructions prompted by the script to input the student's information for prediction.

## Dataset Format
- The dataset should be in CSV format.
- It should contain columns representing different features such as academics, projects, interests, and past work experiences.
- The last column should indicate the target variable (future job/scope).

Example dataset format:
```
Student ID,Name,Gender,Age,GPA,Major,Interested Domain,Projects,Future Career,Python,SQL,Java
1,John Smith,Male,21,3.5,Computer Science,Artificial Intelligence,Chatbot Development,Machine Learning Researcher,Strong,Strong,Weak
2,Alice Johnson,Female,20,3.2,Computer Science,Data Science,Data Analytics,Data Scientist,Average,Strong,Weak
3,Robert Davis,Male,22,3.8,Computer Science,Software Development,E-commerce Website,Software Engineer,Strong,Strong,Average
4,Emily Wilson,Female,21,3.7,Computer Science,Web Development,Full-Stack Web App,Web Developer,Weak,Strong,Strong
5,Michael Brown,Male,23,3.4,Computer Science,Cybersecurity,Network Security,Information Security Analyst,Average,Weak,Strong
```

## Contributors
- [Rugved Patil](https://github.com/rugvedp)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- This project was inspired by the need to provide students with insights into their potential career paths.
- We thank the open-source community for their invaluable contributions.
  
## Feedback and Contributions
Feedback, bug reports, and contributions are welcome. Please feel free to [open an issue](https://github.com/rugvedp/student_portal_ML/issues) or submit a pull request.

## Support
For any inquiries or support, please contact [your.email@example.com](mailto:rugvedboi50@gmail.com).

---

**Note:** Replace placeholders such as `rugvedp`, `rugvedboi50@gmail.com`, and update links according to your project's specifics.
