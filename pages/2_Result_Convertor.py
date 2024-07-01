

# new ajit code 
import streamlit as st
import pandas as pd
import time
import re
import numpy as np
from itdepartment import getTabledownloadLink, displayPDF, pdfToText, cleanText, studentDetails, cleanMarks, cleanMarks1,getSubjectCodes,getSubjectNames 
from st_aggrid import AgGrid




import streamlit as st
import pandas as pd
import time
import re
import numpy as np
from itdepartment import getTabledownloadLink, displayPDF, pdfToText, cleanText, studentDetails, cleanMarks, cleanMarks1,getSubjectCodes,getSubjectNames 
from st_aggrid import AgGrid





# to exctract first line 
@st.cache_data
def modified_details(text):
    pattern = r'PAGE\s*:-\s*(\d+)\s*SAVITRIBAI\sPHULE\s*PUNE\s*UNIVERSITY\s*,[A-Z]\.[A-Z]\.\(\d{0,9}\s*[A-Z]\)\s[A-Z],\s[A-Z]/[A-Z]\s*\d{0,9}\s*[A-Z]\s:\s*\d{0,9}\s*[A-Z]\s\d{0,9}\s*'
    
    # Check if the pattern is present in the text
    match = re.search(pattern, text)
    
    if match:
        # If the pattern is found, replace it with an empty string
        modified_text = re.sub(pattern, '', text)
        return modified_text
    else:
        # If the pattern is not found, return the original text
        return text

@st.cache_data
def concat_subjects(d: dict):
    #function to concat subject wise marks
    return pd.concat([i for i in d.values()], axis=1)


@st.cache_data
def cleanTextRe(text: str) -> str:
    text = re.sub(r'^[a-zA-Z]{2}', '', text)
    return text

@st.cache_data
def extractPrnNo(text: str):
    # function to extract prn no from text
    pattern = re.findall(
        r'7\d{7}[a-zA-Z]*', text
    )
    d = {'PRN-NO': []}
    for i in pattern:
        temp = i.split()
        d['PRN-NO'].append(temp[0])

    return pd.DataFrame(d)

@st.cache_data
def replaceNan(df: pd.DataFrame) -> pd.DataFrame:
    # function to replace nan values
    df = df.replace('nnn', np.nan)
    df = df.replace('nan', np.nan)
    df = df.replace('nnnn', np.nan)
    df = df.replace('nnnn', np.nan)
    df = df.replace('nan', np.nan)
    df = df.replace('nnnnn', np.nan)
    df = df.replace('nnnnn', np.nan)
    df = df.replace('nnnnnnn', np.nan)
    df = df.replace('nnnnnnn', np.nan)
    # df = df.replace('nnn', np.nan)
    # df = df.replace('nan', np.nan)
    df = df.replace('nnnn', np.nan)
    return df

def App():

    st.markdown("""
        ## :outbox_tray: Result Analyzer :outbox_tray:
    """)

    
    col1, col2 = st.columns(2)

    with col1:
        department = st.selectbox(
            'Select Department',
            ('IT', 'COMPUTER', 'AIDS', 'MECHANICAL', 'E&TC',
                'CIVIL', 'ELECTRICAL', 'INSTRUMENTATION')
        )
        st.success(f'Selected department is {department}')

    with col2:
        sem = st.selectbox(
            'Select Semester',
            ('SE-SEM-1','SE-(SEM1 + SEM2)','TE-SEM-1','TE-(SEM1 + SEM2)','BE-SEM-1','BE-(SEM1 + SEM2)')
        )
        st.success(f'Selected Semester is {sem}')


    if department == 'IT':
        st.write('Selected department is ', department)

        pdf_file = st.file_uploader(label="Upload Pdf File", type="pdf")
        if pdf_file:
            # display document
            with st.expander(label="Show Uploaded File"):
                displayPDF(pdf_file)

            try:
                text = pdfToText(pdf_file)
            except FileNotFoundError:
                st.error('File not found try again!')
                return
            # store text to find subject names
            textForSubjectNames = text

            modified_text  = modified_details(text)
            # print("modified text" , modified_text)

            text = cleanText( modified_text)
            # print("cleaned text",text)

            try:

                seat_no_name = studentDetails(text)
                student_prn_no = extractPrnNo(text)

                student_data = pd.concat(
                    [seat_no_name, student_prn_no], axis=1)
            except:
                st.error(
                    "Error in extracting data from pdf. Please check the pdf file and try again.")
                return

            with st.expander('Show Students Details'):
                # remove columns with all nan values
                student_data = student_data.dropna(axis=1, how='all')
                storeStudentData = student_data.copy()
                
                AgGrid(student_data)
                st.spinner('Processing...')
                # time.sleep(4)
                st.text("")

                st.markdown(getTabledownloadLink(storeStudentData, file_name=f"{str(pdf_file.name).split('.')[0]}.csv",), unsafe_allow_html=True)

            with st.expander('Show Students Marks by Subject Code'):

                # text = cleanTextRe(text)
                subject_codes = st.text_input('Enter subject code to see subject marks(One at at time) eg: `314443`')
                subject_codes_submit = st.button('Submit', key='one_subject_codes_submit')
                if subject_codes_submit:
                    try:
                        subject_codes = subject_codes.split()
                        subject_codes = {i: None for i in subject_codes}
                        # st.markdown('#### Selected subjects')
                        # st.write(subject_codes)
                        st.spinner('Processing...')
                        pattern = r'[A-Z]{3}'
                        text = cleanTextRe(text)
                        text = re.sub(pattern, '', text)
                        try:
                            if(sem == 'SE-(SEM1 + SEM2)' or sem == 'TE-(SEM1 + SEM2)' or sem == 'BE-SEM-1'):
                                marks = cleanMarks1(text, subject_codes)
                            else:
                                marks = cleanMarks(text, subject_codes)
                            # print("151 marks " , marks)
                        except:
                            st.error(
                                'Error in processing pdf. Please check the pdf file and try again')
                            return
                        
                        try:
                            student_marks = concat_subjects(marks)
                            student_marks = pd.concat(
                                [student_data, student_marks], axis=1)
                        except:
                            st.error(
                                'Error in extracting marks. Please check the pdf file and try again.@concat_subjects')
                            return


                        st.success('Done!....')
                        # remove columns with all nan values
                        # student_marks = replaceNan(student_marks)
                        student_marks = student_marks.replace(
                            'nnnnnnn', np.nan)
                        student_marks = student_marks.replace(
                            'nnnnnnn', np.nan)
                        student_marks = student_marks.replace('nnn', np.nan)
                        student_marks = student_marks.replace('nan', np.nan)
                        student_marks = student_marks.replace('nnnn', np.nan)

                        student_marks = student_marks.replace('nnn', np.nan)
                        student_marks = student_marks.dropna(axis=1, how='all')
                        studentMarksStore = student_marks.copy()

                        AgGrid(student_marks)
                        
                        st.spinner('Processing...')
                        # time.sleep(4)
                        st.text("")

                        st.markdown(getTabledownloadLink(studentMarksStore, file_name=f"{str(pdf_file.name).split('.')[0]}.csv",), unsafe_allow_html=True)
                    except:
                        st.error('Please enter valid subject code or cannot convert this marks')
                        
                        return

            with st.expander('Download Student marks in Excel/Csv File'):

                # subject_codes = st.text_input('Enter subject codes separated by space Example: `314444 314443`')

                # pat-code-hardcore-is: BE->TE->SE
                subject_codes = "414441 414442 414443 414444A 414445B 414446 414447 414448 414449A 404456 414450 414451E 414452D 414453 414454 414455 414457B 314445A 314444 314443 314442 314441 314449 314447 314446 314448 314450B 314460 314455 314454C 314453 314452 344452 314451 344451 314459B 244441 214441 214442 214443 214444 214445 214446 214447 214448 214449 214450A 247003 207003 214451 214452 214453 214454 214455 214456 214457 214458 214459D"

                subject_codes_submit = st.button('Submit / getExcell', key='all_subject_codes_submit')

                if subject_codes_submit:
                    try:
                        subject_codes = subject_codes.split()
                        subject_codes = {i: None for i in subject_codes}
                        # st.markdown('### Selected subjects are :')
                        student_data = replaceNan(student_data)
                        # st.write(subject_codes)
                        st.spinner('Processing...')
                        stored_text = text
                        text = cleanTextRe(text)
                        # pattern = r'[A-Z]\w*[A-Z]'
                        pattern = r'[A-Z]{3}'
                        text = re.sub(pattern, '', text)
                        try:
                            if(sem == 'SE-(SEM1 + SEM2)' or sem == 'TE-(SEM1 + SEM2)' or sem == 'BE-SEM-1'):
                                marks = cleanMarks1(text, subject_codes)
                            else:
                                marks = cleanMarks(text, subject_codes)
                        except:
                            st.error(
                                'Error in extracting marks. Please check the pdf file and try again.@cleanMarks')
                            return
                        
                        try:

                            student_marks = concat_subjects(marks)
                            student_marks = pd.concat(
                                [student_data, student_marks], axis=1)
                        except:
                            st.error(
                                'Error in extracting marks. Please check the pdf file and try again.@concat_subjects')
                            return
                        
                        student_marks = replaceNan(student_marks)

                        try:
                            # find sgpa
                            print('trying to extract spga')
                            pattern = re.findall(r'SGPA1?\W*\d*\W*\d*', stored_text)
                            # SGPA1: 8.3
                            d = {'sgpa':[],'score':[]}
                            for i in pattern:
                                try:
                                    temp = i.split()
                                    if len(temp) == 1:
                                        temp.append('00')
                                except Exception as e:
                                    temp = ['SGPA1','00']
                                d['sgpa'].append(temp[0])
                                d['score'].append(temp[1])
                            sgpa = pd.DataFrame(d)
                            student_marks = pd.concat([student_marks,sgpa],axis=1)
                        except:
                            print('error in extracting spga')
                            st.error('Error in extracting sgpa')
                            pass

                        

                        student_marks = student_marks.dropna(axis=1, how='all')

                        st.markdown(getTabledownloadLink(student_marks, file_name=f"{str(pdf_file.name).split('.')[0]}.csv",), unsafe_allow_html=True)
                    except:
                        st.error(
                            'Please enter valid subject codes OR Cannot convert following subject codes to excel file')
                        return

            # # with st.expander('Advance subject wise marks'):
            #     st.warning('Use this feature only if above feature is not working')
            #     st.warning('Keep default values if you are not sure')

            #     result_type = st.selectbox(
            #         'Select result type', ['SEMESTER', 'YEAR'])
            #     st.write('You selected:', result_type)
                
            #     # IF SEMESTER RESULT then 10 SUBJECTS ELSE 20
            #     if result_type == 'SEMESTER':
            #         options = st.multiselect(
            #             'select subject codes',
            #             getSubjectCodes(text,10)
            #         )
            #     else:
            #         options = st.multiselect(
            #             'select subject codes',
            #             getSubjectCodes(text,20)
            #         )

                
            #     st.write('Selected subject codes:', options)

            #     if options:

            #         subject_names = st.multiselect(
            #             'select subject names',
            #             list(set(getSubjectNames(textForSubjectNames)))
            #         )
            #         st.write('Selected subject names:', subject_names)

            #     subject_codes = st.text_input(
            #         'Enter subject code')
                
            #     subject_name = st.text_input(
            #         "Enter subject name"
            #     )
            #     pattern = st.selectbox(
            #                 options=['[A-Z]{3}','[A-Z]\w*[A-Z]'],
            #                 label='Try changing pattern if not working(Select one) optional',

            #         )
            #     subject_codes_submit = st.button(
            #         'Submit', key='one_subject_codes_submit_advance')
            #     if subject_codes_submit:
            #         try:
            #             subject_codes = subject_codes.split()
            #             subject_codes = {i: None for i in subject_codes}
            #             st.markdown('#### Selected subjects')
            #             st.write(subject_codes)
            #             st.spinner('Processing...')
                        


            #             text = cleanTextRe(text)
            #             text = text.replace(subject_name,'')
            #             text = re.sub(pattern, '', text)
            #             try:
            #                 marks = cleanMarks(text, subject_codes)
            #             except:
            #                 st.error(
            #                     'Error in processing pdf. Please check the pdf file and try again')
            #                 return
                        
            #             try:
            #                 student_marks = concat_subjects(marks)
            #                 student_marks = pd.concat(
            #                     [student_data, student_marks], axis=1)
            #             except:
            #                 st.error(
            #                     'Error in extracting marks. Please check the pdf file and try again.@concat_subjects')
            #                 return


            #             st.success('Done!....')
            #             # remove columns with all nan values
            #             student_marks = replaceNan(student_marks)
            #             student_marks = student_marks.dropna(axis=1, how='all')
            #             studentMarksStore = student_marks.copy()

            #             AgGrid(student_marks)
                        
            #             st.spinner('Processing...')
            #             time.sleep(4)
            #             st.text("")

            #             st.markdown(getTabledownloadLink(
            #                 studentMarksStore), unsafe_allow_html=True)
            #         except:
            #             st.error('Please enter valid subject code or cannot convert this marks')
                        
            #             return



    else:
        st.write('selected department is ', department)


if __name__ == "__main__":

    # set page title and icon
    try:
        st.set_page_config(
            page_title='Result Analysis',
            page_icon='📃'
        )

        with st.sidebar:
            st.header('Our Contributors')

            import streamlit as st

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

    except Exception as e:
        pass

    App()