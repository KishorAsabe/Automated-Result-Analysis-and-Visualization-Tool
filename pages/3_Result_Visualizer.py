




import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import csv
import os
import base64


def replace_subject_codes_with_names(subject_code):
    # Dictionary mapping subject codes to names

    subject_mapping = {
        214441: 'DISCRETE MATHEMATICS',
        244441: 'DISCRETE MATHEMATICS LAB',
        214442: 'LOGIC DESIGN & COMP. ORG.',
        214443: 'DATA STRUCTURES & ALGO.',
        214444: 'OBJECT ORIENTED PROGRAMMING',
        214445: 'BASIC OF COMPUTER NETWORK',
        214446: 'LOGIC DESIGN COMP. ORG. LAB',
        214447: 'DATA STRUCTURES & ALGO. LAB',
        214448: 'OBJECT ORIENTED PROG. LAB',
        214449: 'SOFT SKILL LAB',
        '214450A': 'ETHICS AND VALUES IN IT',
        207003: 'ENGINEERING MATHEMATICS-III',
        214451: 'PROCESSOR ARCHITECTURE',
        214452: 'DATABASE MANAGEMENT SYSTEM',
        214453: 'COMPUTER GRAPHICS',
        214454: 'SOFTWARE ENGINEERING',
        214455: 'PROG. SKILL DEVELOPMENT LAB',
        214456: 'DATABASE MGMT. SYSTEM LAB',
        214457: 'COMPUTER GRAPHICS LAB',
        214458: 'PROJECT BASED LEARNING',
        '214459D': 'INTELLECTUAL PROPERTY RIGHTS',
        '314445A': 'DESIGN AND ANALYSIS OF ALG.',
        314444: 'HUMAN COMPUTER INTERACTION',
        314443: 'MACHINE LEARNING',
        314442: 'OPERATING SYSTEMS',
        314441: 'THEORY OF COMPUTATION',
        314449: 'SEMINAR',
        314447: 'HUMAN COMP. INTERACTION-LAB.',
        314446: 'OPERATING SYSTEMS LAB (TW+PR)',
        314448: 'LABORATORY PRACTICE-I',
        '314450B': 'STARTUP ECOSYSTEMS',
        314460: 'LABORATORY PRACTICE-II',
        314455: 'INTERNSHIP',
        '314454C': 'CLOUD COMPUTING',
        314453: 'WEB APPLICATION DEV.',
        314452: 'DS & BDA LAB.',
        344452: 'DS & BDA',

        314451: 'COMP. NET. & SEC.LAB',  # th
        344451: 'COMP. NET. & SEC ',
        '314459B': 'LEAD. & PERSONALITY DEV.',

        # SE
        247003: 'ENGINEERING MATHEMATICS-III lab',

    }

    # Return the corresponding name if found in the dictionary, otherwise return the code itself
    return subject_mapping.get(subject_code, subject_code)


# Dictionary mapping subject codes to their names
subject_mapping_for_subjects_replaced = {
    '214441': 'DISCRETE MATHEMATICS -(T)',
    '214442': 'LOGIC DESIGN & COMP. ORG. -(T)',
    '214443': 'DATA STRUCTURES & ALGO. -(T)',
    '214444': 'OBJECT ORIENTED PROGRAMMING -(T)',
    '214445': 'BASIC OF COMPUTER NETWORK -(T)',
    '214449': 'SOFT SKILL LAB ',
    '214450A': 'ETHICS AND VALUES IN IT',
    '244441': 'DISCRETE MATHEMATICS LAB -(T)',
    '214446': 'LOGIC DESIGN COMP. ORG. LAB -(L)',
    '214447': 'DATA STRUCTURES & ALGO. LAB -(L)',
    '214448': 'OBJECT ORIENTED PROG. LAB -(L)',
    '207003': 'ENGINEERING MATHEMATICS-III -(T)',
    '214451': 'PROCESSOR ARCHITECTURE -(T)',
    '214452': 'DATABASE MANAGEMENT SYSTEM -(T)',
    '214453': 'COMPUTER GRAPHICS -(T)',
    '214454': 'SOFTWARE ENGINEERING -(T)',
    '214458': 'PROJECT BASED LEARNING',
    '214459D': 'INTELLECTUAL PROPERTY RIGHTS',
    '247003': 'ENGINEERING MATHEMATICS-III lab -(T)',
    '214455': 'PROG. SKILL DEVELOPMENT LAB -(L)',
    '214456': 'DATABASE MGMT. SYSTEM LAB -(L)',
    '214457': 'COMPUTER GRAPHICS LAB -(L)',
    '314445A': 'DESIGN AND ANALYSIS OF ALG. -(T)',
    '314444': 'HUMAN COMPUTER INTERACTION -(T)',
    '314443': 'MACHINE LEARNING -(T)',
    '314442': 'OPERATING SYSTEMS -(T)',
    '314441': 'THEORY OF COMPUTATION -(T)',
    '314449': 'SEMINAR -(T)',
    '314447': 'HUMAN COMP. INTERACTION-LAB. -(O)',
    '314446': 'OPERATING SYSTEMS LAB (TW+PR) -(L)',
    '314448': 'LABORATORY PRACTICE-I -(L)',
    '314450B': 'STARTUP ECOSYSTEMS -(T)',
    '314460': 'LABORATORY PRACTICE-II -(L)',
    '314455': 'INTERNSHIP -(T)',
    '314454C': 'CLOUD COMPUTING -(T)',
    '314453': 'WEB APPLICATION DEV. -(T)',
    '314452': 'DS & BDA LAB. -(L) ',
    '344452': 'DS & BDA -(T)',
    '314451': 'COMP. NET. & SEC.LAB -(O)',
    '344451': 'COMP. NET. & SEC -(T)',
    '314459B': 'LEAD. & PERSONALITY DEV. -(T)',
    '414441': 'INFO. & STORAGE RETRIEVAL -(T)',
    '414442': 'SOFTWARE PROJECT MANAGEMENT -(T)',
    '414443': 'DEEP LEARNING -(T)',
    '414444A': 'MOBILE COMPUTING -(T)',
    '414445B': 'INTRODUCTION TO DEVOPS -(T)',
    '414449A': 'COPYRIGHTS AND PATENTS -(T)',
    '414446': 'LAB PRACTICE III -(O)',
    '414447': 'LAB PRACTICE IV -(L)',
    '414448': 'PROJECT STAGE-I -(T)',
    '404456': 'PROJECT STAGE II -(O)',
    '414450': 'DISTRIBUTED SYSTEMS -(T)',
    '4141E45': 'GAME ENGINEERING -(T)',
    '414452D': 'BLOCKCHAIN TECHNOLOGY -(T)',
    '414453': 'STARTUP & ENTREPRENEURSHIP -(T)',
    '414454': 'LAB PRACTICE V -(L)',
    '414455': 'LAB PRACTICE VI -(O)',
    '414457B': 'CYBER LAWS & USE OF S.M. -(T)',
}

# Function to replace subject codes with their names


def replace_subject_codes(subject_code):
    return subject_mapping_for_subjects_replaced.get(subject_code, subject_code)

# Function to remove commas from the 'score' column


def remove_commas_from_score(score):
    return score.replace(',', '')

# Function to process the CSV file


def process_csv(file_name):
    try:
        # Read the CSV file and replace subject codes with names
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

            for row in data:
                for i in range(len(row)):
                    row[i] = replace_subject_codes(row[i])

        # Write the updated data back to the CSV file
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        # Read the CSV file and remove commas from the 'score' column
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

            # Find the index of the 'score' column
            header = data[0]
            score_index = header.index('score')

            # Remove commas from the 'score' column
            for row in data[1:]:
                row[score_index] = remove_commas_from_score(row[score_index])

        # Write the updated data back to the CSV file
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        # st.success("Subject codes replaced and commas removed from the 'score' column successfully.")
        return data
    except Exception as e:
        # st.error(f"Error processing CSV file: {e}")
        return None


def main():
    # Set the title of the web app
    st.title('Result Visualizer')

    # Allow the user to upload a CSV or Excel file
    uploadedFile = st.file_uploader(
        label="Upload CSV or Excel File", type=["csv", "xlsx"])

    # Display a warning message for the user
    st.warning('To view the visualization, please upload the file in the format provided in the sample file. See the help Section')

    if uploadedFile is not None:
        # Read the uploaded file into a DataFrame
        storedDf = None
        if uploadedFile.type == 'text/csv':
            storedDf = pd.read_csv(uploadedFile)
        else:
            storedDf = pd.read_excel(uploadedFile)

        subject_columns = [
            col for col in storedDf.columns if 'subject' in col.lower()]
        # print(subject_columns)
        for col in subject_columns:
            #   storedDf[col] = storedDf[col].apply(replace_subject_codes_with_names)
            # print(f"Processing column: {col}")
            storedDf[col] = storedDf[col].apply(
                lambda x: replace_subject_codes_with_names(x))

        df = storedDf

        # Download updated CSV/Excel file with code -> subject name mapping
        # with st.expander('Download updated CSV/Excel'):
        #     if uploadedFile is not None:
        #         try:
        #             # Save the uploaded file
        #             upload_dir = "uploads"
        #             if not os.path.exists(upload_dir):
        #                 os.makedirs(upload_dir)
        #             file_path = os.path.join(upload_dir, uploadedFile.name)
        #             with open(file_path, "wb") as f:
        #                 f.write(uploadedFile.getvalue())

        #             processed_data = process_csv(file_path)

        #             if processed_data is not None:
        #                 # Display a success message
        #                 st.write("CSV file processed successfully.")

        #                 # Download link for processed CSV file
        #                 # Convert processed data to CSV format
        #                 csv_file = '\n'.join([','.join(row)
        #                                      for row in processed_data])
        #                 # Convert CSV data to base64
        #                 b64 = base64.b64encode(csv_file.encode()).decode()
        #             download_button = st.button("Download Processed Data")
        #             if download_button:
        #             # Hide the button
        #               hide_button_style = """
        #             <style>
        #             #hide-button { display: none; }
        #             </style>
        #             """
        #             st.markdown(hide_button_style, unsafe_allow_html=True)

        #             # Trigger file download using JavaScript
        #             download_js = f"""
        #             <script>
        #             var csvData = 'data:file/csv;base64,{b64}';
        #             var blob = new Blob(["\ufeff", atob('{b64}')], {{type: 'text/csv'}});
        #             var url = window.URL.createObjectURL(blob);
        #             var a = document.createElement('a');
        #             a.href = csvData;
        #             a.download = '{uploadedFile.name}';
        #             document.body.appendChild(a);
        #             a.click();
        #             document.body.removeChild(a);
        #             </script>
        #             """
        #             st.markdown(download_js, unsafe_allow_html=True)
        #                 # href = f'<a href="data:file/csv;base64,{b64}" download="{uploadedFile.name}">Download processed data</a>'
        #                 # st.markdown(href, unsafe_allow_html=True)
        #         except Exception as e:
        #             print(f"Error processing CSV file:----{e}")
        #         finally:
        #             # Delete the uploaded file after processing
        #             if os.path.exists(file_path):
        #                 os.remove(file_path)



        # Display details and table of the uploaded data in an expander
        with st.expander('Show Details'):
            st.write("Data in Uploaded file")
            AgGrid(storedDf)
   
                # Download updated CSV/Excel file with code -> subject name mapping
                
                
        with st.expander('Download updated CSV/Excel'):
            if uploadedFile is not None:
                try:
                    # Save the uploaded file
                    upload_dir = "uploads"
                    if not os.path.exists(upload_dir):
                        os.makedirs(upload_dir)
                    file_path = os.path.join(upload_dir, uploadedFile.name)
                    with open(file_path, "wb") as f:
                        f.write(uploadedFile.getvalue())

                    processed_data = process_csv(file_path)

                    if processed_data is not None:
                        # Display a success message
                        st.write("CSV file processed successfully.")

                        # Download link for processed CSV file
                        # Convert processed data to CSV format
                        csv_file = '\n'.join([','.join(row)
                                             for row in processed_data])
                        # Convert CSV data to base64
                        b64 = base64.b64encode(csv_file.encode()).decode()
    
                        href = f'<a href="data:file/csv;base64,{b64}" download="{uploadedFile.name}">Download processed data</a>'
                        st.markdown(href, unsafe_allow_html=True)
                except Exception as e:
                    print(f"Error processing CSV file:----{e}")
                finally:
                    # Delete the uploaded file after processing
                    if os.path.exists(file_path):
                        os.remove(file_path)  
        # Display the result analysis within an expander
        
        with st.expander("Result Analysis"):
            try:
                result_analysis_df = pd.DataFrame()
                total_students = len(df)
                result_analysis_df = pd.DataFrame(
                    columns=['Particulars', 'No of Students', 'Percentage'])
                new_row = pd.DataFrame({'Particulars': ['Total Number of Students'], 'No of Students': [
                                       total_students], 'Percentage': [100]})
                result_analysis_df = pd.concat(
                    [result_analysis_df, new_row], ignore_index=True)

                # All clear
                all_clear_students = df[df['score'] != 0]
                all_clear_count = len(all_clear_students)
                all_clear_percentage = (all_clear_count / total_students) * 100
                new_row = pd.DataFrame({'Particulars': ['All Clear'], 'No of Students': [
                                       all_clear_count], 'Percentage': [all_clear_percentage]})
                result_analysis_df = pd.concat(
                    [result_analysis_df, new_row], ignore_index=True)

                # Filter students who failed ('O' in the 'score' column)
                fail_students = df[df['score'] == 0]
                fail_students_count = len(fail_students)
                fail_students_percentage = (
                    fail_students_count / total_students) * 100

                # Append fail students to the result analysis DataFrame
                new_row_fail = pd.DataFrame({'Particulars': ['Fail Students'], 'No of Students': [
                                            fail_students_count], 'Percentage': [fail_students_percentage]})
                result_analysis_df = pd.concat(
                    [result_analysis_df, new_row_fail], ignore_index=True)

                # Additional classifications
                criteria = {
                    'First Class with Distinction': (7.75, float('inf')),
                    'First Class': (6.75, 7.75),
                    'Higher Second Class': (6.25, 6.75),
                    'Second Class': (5.5, 6.25),
                    '1 Backlog': (1, 2),
                    '2 Backlogs': (2, 3),
                    '3 Backlogs': (3, 4),
                    '4 or More Backlogs': (4, float('inf'))
                }

                for category, score_range in criteria.items():
                    if category == '1 Backlog':
                        category_students = df[(df.filter(like='TOT').eq(
                            'FF').sum(axis=1) == score_range[0])]
                    elif category == '2 Backlogs':
                        category_students = df[(df.filter(like='TOT').eq(
                            'FF').sum(axis=1) == score_range[0])]
                    elif category == '3 Backlogs':
                        category_students = df[(df.filter(like='TOT').eq(
                            'FF').sum(axis=1) == score_range[0])]
                    elif category == '4 or More Backlogs':
                        category_students = df[(df.filter(like='TOT').eq(
                            'FF').sum(axis=1) >= score_range[0])]
                    else:
                        category_students = df[(df['score'] >= score_range[0]) & (
                            df['score'] < score_range[1])]

                    category_count = len(category_students)
                    category_percentage = (
                        category_count / total_students) * 100
                    new_row_category = pd.DataFrame({'Particulars': [category], 'No of Students': [
                                                    category_count], 'Percentage': [category_percentage]})
                    result_analysis_df = pd.concat(
                        [result_analysis_df, new_row_category], ignore_index=True)

                # Display the updated result analysis DataFrame
                st.dataframe(result_analysis_df)
            except Exception as e:
                st.error(f'Error occurred while loading the data: {str(e)}')

        with st.expander("Result Analysis Visualization", expanded=True):
            try:
                if len(result_analysis_df) > 0:
                    # colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                    #           '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
                    # colors = ['#FFD700', '#F4A460','#FF7F50',  '#FF6347', '#87CEEB', '#4169E1', '#9370DB', '#20B2AA']
                    colors = [        '#0000CD',  # Dark blue (Primary color)
    '#4169E1',  # Dark blue (Cold tone)
    '#1155CC',  # Blue (Cold tone)
    '#1E90FF',  # Dodger blue (Cold tone)
    '#6AA6FF',  # Light sky blue (Cold tone)
    '#ADD8E6',  # Light blue (Cold tone)
    '#87CEFA',  # Light sky blue (Warm tone)
    '#B0E0E6'  ]


                    total_students = result_analysis_df.loc[0,
                                                            'No of Students']
                    all_clear_students = result_analysis_df.loc[1,
                                                                'No of Students']
                    fail_students = result_analysis_df.loc[2, 'No of Students']

                    # Create pie chart for each category
                    for i, (start, end, title) in enumerate([(1, 3, 'Student Distribution'), (2, 7, 'Class Categories')]):
                        fig, ax = plt.subplots(figsize=(10, 6))
                        
                        sorted_data = result_analysis_df.loc[start:end-1].sort_values(by='No of Students', ascending=False)
                        wedges, texts = ax.pie(
                            sorted_data['No of Students'],
                            startangle=90,
                            colors=colors[start:end],
                            wedgeprops=dict(edgecolor='w'),)
                        # wedges, texts = ax.pie(
                        #     result_analysis_df.loc[start:end -
                        #                            1, 'No of Students'],
                        #     startangle=90,
                        #     colors=colors[start:end],
                        #     wedgeprops=dict(edgecolor='w'),
                        # )
                        ax.axis('equal')
                        # Add padding to the title
                        ax.set_title(title, fontsize=16,
                                     fontweight='bold', pad=40)

                        # Add a legend for each pie chart
                        sorted_particulars = sorted_data['Particulars']  #new
                        ax.legend(wedges, sorted_particulars,
                          title="Particulars", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
                        # ax.legend(wedges, result_analysis_df.loc[start:end-1, 'Particulars'],
                        #           title="Particulars", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
                        # Adjust layout to make room for the legend
                        plt.subplots_adjust(right=0.7)

                        # Create a table to represent data with proper spacing
                        # data = result_analysis_df.loc[start:end -
                        #                               1, ['Particulars', 'No of Students']]
                        
                        data = sorted_data[['Particulars', 'No of Students']]
                        if start == 1:  # Add total number of students row in the first pie chart table
                            total_row = pd.DataFrame(
                                {'Particulars': ['Total Students'], 'No of Students': [total_students]})
                            data = pd.concat(
                                [total_row, data], ignore_index=True)
                        data['Percentage'] = (data['No of Students'].astype(
                            float) / total_students * 100).round(2)
                        ax.table(cellText=data.values,
                                 colLabels=data.columns,
                                 cellLoc='center',
                                 loc='bottom',
                                 bbox=[0, -0.4, 1, 0.3])  # Adjust table position and size

                        st.pyplot(fig)

                    # backlog_colors = ['#FF9999',
                    #                   '#66B2FF', '#99FF99', '#FFCC99']

                    # fig, ax = plt.subplots(figsize=(10, 6))
                    # wedges, texts = ax.pie(
                    #     result_analysis_df.loc[7:, 'No of Students'],
                    #     startangle=90,
                    #     colors=backlog_colors,
                    #     wedgeprops=dict(edgecolor='w'),
                    # )
                    # ax.axis('equal')
                    # # Add padding to the title
                    # ax.set_title('Backlogs', fontsize=16,
                    #              fontweight='bold', pad=40)

                    # # Add a legend for the last pie chart
                    # ax.legend(wedges, result_analysis_df.loc[7:, 'Particulars'],
                    #           title="Particulars", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
                    # # Adjust layout to make room for the legend
                    # plt.subplots_adjust(right=0.7)

                    # # Add a table for the last pie chart
                    # data_backlogs = result_analysis_df.loc[7:, [
                    #     'Particulars', 'No of Students']]
                    # data_backlogs['Percentage'] = (data_backlogs['No of Students'].astype(
                    #     float) / total_students * 100).round(2)
                    # ax.table(cellText=data_backlogs.values,
                    #          colLabels=data_backlogs.columns,
                    #          cellLoc='center',
                    #          loc='bottom',
                    #          bbox=[0, -0.4, 1, 0.3])  # Adjust table position and size

                    # st.pyplot(fig)

            except Exception as e:
                st.error(f'Error occurred while loading the data: {str(e)}')

        # Subject wise result analysis
        with st.expander("Subject Wise Result Analysis"):
            try:
                # Initialize an empty DataFrame for the subject-wise analysis
                subject_analysis_df = pd.DataFrame(
                    columns=['Subject', 'No of Passed Students', 'Highest Marks Scored', '% of Passing'])

                # Get the list of subject and total columns
                subject_columns = [
                    col for col in df.columns if 'subject' in col]
                tot_columns = [col for col in df.columns if 'TOT' in col]

                # Iterate over each subject column and its corresponding total column
                for subject_col, tot_col in zip(subject_columns, tot_columns):
                    # Extract the subject name from the column
                    # Assuming subject names are in the first row
                    subject = df[subject_col].iloc[0]

                    # Filter DataFrame for the current subject and total column
                    subject_df = df[[subject_col, tot_col]].copy()

                    # Replace 'FF' values in 'TOT' column with 0
                    subject_df[tot_col] = subject_df[tot_col].replace('FF', 0)
                    # Count the number of 'AB' values (absent students)
                    absent_students = subject_df[tot_col].eq('AB').sum()
                    # print("absent students ------",absent_students)
                    subject_df[tot_col] = subject_df[tot_col].replace('AB', 0)

                    # Convert 'TOT' column to numeric values
                    subject_df[tot_col] = pd.to_numeric(
                        subject_df[tot_col], errors='coerce')

                    # print(subject_df[tot_col] )

                    # Calculate statistics for the current subject
                    total_students_subject = len(subject_df)
                    # Count passed students for this subject
                    passed_students = len(
                        subject_df[(subject_df[tot_col] != 0)])

                    highest_marks_scored = subject_df[tot_col].max()
                    percentage_passing = (
                        passed_students / total_students_subject) * 100
                    # print('_+++++++++++++++++' , highest_marks_scored)

                    # Append the analysis for the current subject to the subject_analysis_df
                    new_row_subject = pd.DataFrame({
                        'Subject': [subject],
                        'No of Passed Students': [f'{passed_students}/{total_students_subject}'],
                        'Highest Marks Scored': [highest_marks_scored],
                        '% of Passing': [percentage_passing]
                    })

                    # Append the analysis for the current subject to the subject_analysis_df
                    if not new_row_subject.isnull().values.all():  # Check if the new row contains any NaN values
                        subject_analysis_df = pd.concat(
                            [subject_analysis_df, new_row_subject], ignore_index=True)

                # Display the subject-wise analysis DataFrame
                st.dataframe(subject_analysis_df)

            except Exception as e:
                st.error(f'Error occurred while loading the data: {str(e)}')

        # Display the details of the top 5 students based on SGPA
        with st.expander("Get Topper Details"):
            try:
                df = df.sort_values(by=['score'], ascending=False)
                df['Rank'] = df['score'].rank(
                    method='dense', ascending=False).astype(int)
                top_students = df[df['Rank'] <= 5][[
                    'Rank', 'seat_no', 'name', 'score']].reset_index(drop=True)
                st.dataframe(top_students)
            except Exception as e:
                st.error(f'Error occurred while loading the data: {str(e)}')


main()

