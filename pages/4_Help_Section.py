import streamlit as st
import smtplib


st.set_page_config(
    page_title='Result Analysis',
    page_icon='📃'
)

# Details how to use the app

def app():
    st.code("""
    Que 1: How to use this app?
    Ans: This app is very easy to use. Just upload the file and click on the button to convert it to the desired format.""")

    st.code("""Que 2: What are features of this app?
    Ans: This app has the following features:
    1. Convert PDF to Excel/CSV
    2.Result Analysis
    3.Result Analysis Visualization
    4.Subject Wise Result Analysis
    5.Topper Details
    6.Download CSV/Excel files 
     """)

    st.code("""Que 2: How to convert PDF to Excel?
    Ans: To convert PDF to Excel, follow the steps below:
    1. Click On the Result Convertor button on the sidebar
    2. Upload the PDF file
    3. Click On  Download student Marks in Excel/csv file Accordian
    4. Click On Submit Button to download students marks.""")

    st.code("""Que 3: How to contact the developer?
    Ans: You can contact the developer at:
    1. Email: ajitss2003@gmail.com
    2. Email: kishorasabe2020@gmail.com.com""")

    st.code("""Que 4: How to contribute to this project?
    Ans: You can contribute to this project by:
    1. Forking the project
    2. Making changes to the code
    3. Creating a pull request""")

    st.code("""Que 5: How to report a bug?
    Ans: You can report a bug by:
    1. Creating an issue on GitHub
    2. Mentioning the bug in the issue""")

    st.code("""Que 6: How to suggest a feature?
    Ans: You can suggest a feature by:
    1. Creating an issue on GitHub
    2. Mentioning the feature in the issue""")

    st.code("""Que 7: How to get the latest updates?
    Ans: You can get the latest updates by:
    1. Forking the project
    2. Pulling the latest changes from the main branch""")

    st.code("""Que 8: Why should I use this app?
    Ans: You should use this app because:
    1. It is free
    2. It is easy to use
    3. It is fast
    4. It is secure
    5. It is open source""")

    st.code("""Que 9: How to visualize the data?
 Ans: To visualize Data File contains columns name similar to this:
1. seat_no: Seat number of the student
2. name: Name of the student
3. PRN-NO: Permanent Registration Number of the student
4. subject: code of the subject  
5. OE: Marks obtained in the Objective Examination
6. TH: Marks obtained in the Theory Examination
7. OE_TH: Total marks obtained in Objective and Theory Examinations
8. TOT: Total marks obtained in the subject
9. CRD: Credits earned for the subject
10. GRD: Grade obtained in the subject
11. PTS1: Points earned (Part 1)
12. PTS2: Points earned (Part 2)
13. TW: Term Work marks
14. OR: Oral marks
15. PR: Practical marks
16. sgpa: Semester Grade Point Average(eg SGPA1 or SGPA)
17. score: Total sgpa achieved (eg 9.0)



""")


    # form to get feedback from the user
    
OWN_EMAIL = 'smartdeveloper18@gmail.com'
OWN_PASSWORD = 'hmurflgozwclflwu'  # Replace with your app password


def send_email(fname, email, phone, message):
    email_message = f"Subject: New Feedback\n\nFull Name: {fname}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.set_debuglevel(1)  # Enable debugging
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


st.title('Feedback')

with st.form('feedback_form'):
    name = st.text_input('Name')
    email = st.text_input('Email')
    phone = st.text_input('Phone')
    feedback = st.text_area('Feedback')
    submit = st.form_submit_button('Submit')

if submit:
    try:
        send_email(name, email, phone, feedback)
        st.success('Email sent successfully')
        st.balloons()
    except Exception as e:
        st.error(f"An error occurred: {e}")






with st.sidebar:
    st.header('Our Contributors')


    st.markdown(
        """
        <style>
            /* Add CSS styles here */
            .avatar-container {
                display: inline-block;
                margin-right: 20px; /* Adjust the margin to your desired spacing */
            }
        </style>

        <div class="avatar-container">
            <a href="https://github.com/SaTyle/merit-matrix/graphs/contributors">
                <img src="https://contrib.rocks/image?max=50&repo=SaTyle/merit-matrix" />
            </a>
        </div>


        """,
        unsafe_allow_html=True
    )

app()