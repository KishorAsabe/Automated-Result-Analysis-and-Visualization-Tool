
# dont  touch this code 
# # itdepartment.py

# import streamlit as st
# import pandas as pd
# import PyPDF2
# import base64
# import re
# import os 
# from st_aggrid import  GridOptionsBuilder

# # Replace PdfFileReader with PdfReader
# from PyPDF2 import PdfReader


# @st.cache_data
# def replace_at_odd_positions(string, old_str, new_str):
#     result = ''
#     count = 0
#     i = 0
#     while i < len(string):
#         if string[i:i + len(old_str)] == old_str:
#             if count % 2 != 0:
#                 result += new_str
#             else:
#                 result += old_str
#             count += 1
#             i += len(old_str)
#         else:
#             result += string[i]
#             i += 1
#     return result



# @st.cache_data
# def getSubjectNames(text):
#     pattern = r"\d{6}\s(.+?)\s\s\*"
#     subject_codes = re.findall(pattern, text)
#     return subject_codes

# @st.cache_data
# def getSubjectCodes(text: str, subjectCodeCount: int) -> list:
#     pattern = re.findall(r'[1-4]{1}\d{4,6}\w{1}', text)
#     d = {}
#     for i in pattern:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     return list(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)).keys())[:subjectCodeCount]

# @st.cache_data
# def studentDetails(text: str):
#     l = []
#     pattern = re.findall(r'[STB]\d{9}\s*\w*\s*\w*\s*\w*\s*\w*\w*\s*\w*\s*\w*\s*\w*\s*', text)
#     d = {'seat_no': [], 'name': []}
#     for i in pattern:
#         temp = i.split()
#         d['seat_no'].append(temp[0])
#         d['name'].append(temp[1]+' '+temp[2]+' '+temp[3])
#     return pd.DataFrame(d)

# @st.cache_data
# def studentSgpa(text: str):
#     pattern = re.findall(r'SGPA1\W*\d*\W*\d*', text)
#     # pattern = re.findall(r'SGPA1?\W*\d*\W*\d*(?!\W*,)', stored_text)
    
#     d = {'sgpa':[],'score':[]}
#     for i in pattern:
#         temp = i.split()
#         d['sgpa'].append(temp[0])
#         d['score'].append(temp[1])
#     return pd.DataFrame(d)

# @st.cache_data
# def getTabledownloadLink(df):
#     """Generates a link allowing the data in a given panda dataframe to be downloaded"""
#     csv = df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()
#     href = f'<a href="data:file/csv;base64,{b64}" download="output.csv">Download Excel file</a>'
#     return href


# @st.cache_data
# def cleanText(text: str) -> str:
#     subjects = ['OBJECT ORIENTED PROG. LAB','DATA STRUCTURES & ALGO. LAB','LOGIC DESIGN COMP. ORG. LAB','LOGIC DESIGN & COMP. ORG.','DATA STRUCTURES & ALGO.','INFORMATION AND CYBER SECURITY', 'MACHINE LEARNING & APPS.','DESIGN AND ANALYSIS OF ALG.' 
#             'SOFTWARE DESIGN AND MODELING', 'BUS. ANALYTICS & INTEL.', 'SW. TESTING & QA.',
#             'COMPUTER LABORATORY-VII', 'COMPUTER LABORATORY-VII', 'COMPUTER LABORATORY-VIII', 
#             'COMPUTER LABORATORY-VIII', 'PROJECT PHASE-I', 'CRITICAL THINKING',
#             'DISTRIBUTED COMPUTING SYSTEM', 'UBIQUITOUS COMPUTING', 'INTERNET OF THINGS (IOT)', 
#             'INTERNET OF THINGS (IOT)', 'SOCIAL MEDIA ANALYTICS', 'COMPUTER LABORATORY-IX', 'COMPUTER LABORATORY-IX', 
#             'COMPUTER LABORATORY-X', 'PROJECT WORK', 'PROJECT WORK', 'IOT- APPLI. IN ENGG. FIELD','INFO. & STORAGE RETRIEVAL','DIGI ELECTRO & LOGIC DESIGN','FUNDAMENTAL OF DATASTRUCTURE','PROB SOLVI & OOPS','DIGITAL LABORATORY','PROGRAMMING LABORATORY','OBJECT ORIEN PROGRAMMING','COMMUNICATION SKILLS','ROAD SAFETY','ENGINEERING MATHEMATICS -III','COMPUTER GRAPHICS','PROCESSOR ARCH AND INTERFACING','DATA STRUCTURES & FILES','FOUND OF COMM & COMP NETWORK','PROCESSOR INTERFACING LAB','DATA STRUCTURE & FILES LAB','COMPUTER GRAPHICS LABORATORY','WATER MANAGEMENT','DISCRETE STRUCTURES','INFORMATION AND CYBER SEC.', 'MACHINE LEARNING & APPS.', 'SOFTWARE DESIGN AND MODELING', 'BUS. ANALYTICS & INTEL.', 'SW. TESTING & QA. ', 'COMPUTER LABORATORY-VII', 'COMPUTER LABORATORY-VII', 'COMPUTER LABORATORY-VIII', 'COMPUTER LABORATORY-VIII', 'PROJECT PHASE-I', 'DISTRIBUTED COMPUTING SYSTEM', 'UBIQUITOUS COMPUTING', 'INTERNET OF THINGS (IOT)', 'INTERNET OF THINGS (IOT)', 'SOCIAL MEDIA ANALYTICS ', 'COMPUTER LABORATORY-IX', 'COMPUTER LABORATORY-IX', 'COMPUTER LABORATORY-X', 'PROJECT WORK', 'PROJECT WORK', 'ENTREPRENEURSHIP', 'HON-MACH. LEARN.& DATA SCI.', 'HON-A.I. FOR BIG DATA ANA.','HON-MACHINE LEARNING',' HON-IOT & EMBEDED SECURITY',' HON-INFO. SYS. MGMT.','HON-RISK ASSMNT LABORATORY','ENGINEERING MATHEMATICS-III','ENGINEERING MATHEMATICS-III','PROCESSOR ARCHITECTURE','DATABASE MANAGEMENT SYSTEM','COMPUTER GRAPHICS LAB','SOFTWARE ENGINEERING','PROG. SKILL DEVELOPMENT LAB','DATABASE MGMT. SYSTEM LAB','COMPUTER GRAPHICS','PROJECT BASED LEARNING','INTELLECTUAL PROPERTY RIGHTS', 'CYBER SECURITY AND LAW' ]
    
#     for i in subjects:
#         text = text.replace(i, '')

#     # SE subject names and TE subject names
#     text = text.replace('DESIGN AND ANALYSIS OF ALG.','')
#     text = text.replace('COMPUTER ORGANIZATION & ARCH.','')
#     text = text.replace('THEORY OF COMPUTATION', '')
#     text = text.replace('MACHINE LEARNING', '')
#     text = text.replace('HUMAN COMPUTER INTERACTION', '')
#     # text = text.replace('A DESIGN AND ANALYSIS OF ALG.', '')
#     # text = text.replace('SEMINAR', '')
#     text = text.replace('HUMAN COMP. INTERACTION-LAB.', '')
#     text = text.replace('LABORATORY PRACTICE-I', '')
#     text = text.replace('OPERATING SYSTEMS LAB(TW+PR)', '')
#     text = text.replace('OPERATING SYSTEMS', '')
#     ### 
#     text = text.replace('SAVITRIBAI PHULE PUNE UNIVERSITY ,S.E.(2019 CREDIT PAT.) EXAMINATION, OCT/NOV 2023', '')
#     text = text.replace('COLLEGE: [CEGP010530] - D.Y. PATIL COLLEGE OF ENGINEERING, PUNE ', '')
#     text = text.replace('BRANCH CODE:  29-S.E.(2019 PAT.)(INFORMATION TECHNOLOGY)', '')
#     ###
#     text = text.replace('STARTUP ECOSYSTEMS', '')
#     text = text.replace('SEMINAR', '')
#     text = text.replace('...........                 ...... ...... ...... ...... ...... ......   ..  .. ..  .... ......', '')
#     text = text.replace('............ ....... ....... ....... ....... ....... ....... ... ... ... ... ... ... ... ...', '')
#     text = text.replace('  ...........                 ...... ...... ...... ...... ...... ......   ..  .. ..  .... ......', '')
#     text = text.replace('DISCRETE MATHEMATICS', '')
#     text = text.replace('LOGIC DESIGN & COMP. ORG.', '')
#     text = text.replace('OBJECT ORIENTED PROG. LAB', '')
#     text = text.replace('OBJECT ORIENTED PROGRAMMING', '')
#     text = text.replace('BASIC OF COMPUTER NETWORK', '')
#     text = text.replace('LOGIC DESIGN COMP. ORG. LAB', '')
#     text = text.replace('DATA STRUCTURES & ALGO. LAB', '')
#     # text = text.replace('DATA STRUCTURES & ALGO. LAB', '')
#     # text = text.replace('DATA STRUCTURES & ALGO.', '')
#     text = text.replace('SOFT SKILL LAB', '')
#     text = text.replace('ETHICS AND VALUES IN IT', '')
#     text = text.replace('LAB.', '')
#     text = text.replace(
#         'SAVITRIBAI PHULE PUNE UNIVERSITY ,T.E.(2019 COURSE) EXAMINATION, OCT/NOV 2023', '') #
#     text = text.replace(
#         'COLLEGE: [CEGP010530] - D.Y. PATIL COLLEGE OF ENGINEERING, PUNE', '') #
#     text = text.replace(
#         'BRANCH CODE:  29-S.E.(2019 PAT.)(INFORMATIOM TECHNOLOGY)', '')
#     text = text.replace('DATE : 21 APR 2022 ', '')
#     text = text.replace(
#         'COURSE NAME ISE ESE TOTAL TW PR OR TUT Tot% Crd Grd GP CP P&R ORD', '')
#     text = text.replace(
        
#         'SAVITRIBAI PHULE PUNE UNIVERSITY, S.E.(2015 COURSE) EXAMINATION,MAY 2018', '')
#     text = text.replace(' COURSE NAME                      ISE      ESE     TOTAL      TW       PR       OR    Tot% Crd  Grd   GP  CP  P&R ORD', '')

#     # text = text.replace('SAVITRIBAI PHULE PUNE UNIVERSITY ,T.E.(2019 COURSE) EXAMINATION, APR/MAY 2022', '')
#     text = text.replace('COLLEGE    : D.Y. PATIL COLLEGE OF ENGINEERING,  PUNE', '')
#     text = text.replace('COLLEGE: [CEGP010530] - D.Y. PATIL COLLEGE OF ENGINEERING,  PUNE', '')
#     text = text.replace('BRANCH CODE: 29-S.E.(2015 PAT.)(INFORMATIOM TECHNOLOGY)', '')
#     text = text.replace('BRANCH CODE: 60-T.E.(2019 PAT.)(INFORMATION TECHNOLOGY)', '')
#     text = text.replace('INFO. & STORAGE RETRIEVAL', '')
#     text = text.replace('SOFTWARE PROJECT MANAGEMENT', '')
#     text = text.replace('DEEP LEARNING', '')
#     text = text.replace('MOBILE COMPUTING', '')
#     text = text.replace('INTRODUCTION TO DEVOPS', '')
#     text = text.replace('LAB PRACTICE III', '')
#     text = text.replace('LAB PRACTICE IV', '')
#     text = text.replace('PROJECT STAGE-I', '')
#     text = text.replace(' COPYRIGHTS AND PATENTS ', '')
#     # text = text.replace('DATE : 06 MAY 2022', '')
#     text = text.replace('SUBJECT NAME OE TH [OE+TH] TW PR OR Tot% Crd Grd GP CP P&R ORD', '') # 

#     text = text.replace('COURSE NAME                      ISE      ESE     TOTAL      TW       PR       OR     TUT  Tot%  Crd  Grd  GP   CP  P&R ORD', '') # 
#     text = text.replace('...........                 ...... ...... ...... ...... ...... ......   ..  .. ..  .... ......', '') # 
#     # text = text.replace('16 JAN 2024', '') # 
#     text = text.replace('............CONFIDENTIAL- FOR VERIFICATION AND RECORD ONLY AT COLLEGE, NOT FOR DISTRIBUTION.......................................', '')
#     text = text.replace('.........................CONFIDENTIAL- FOR VERIFICATION AND RECORD ONLY AT COLLEGE, NOT FOR DISTRIBUTION..........................', '')
#     text = text.replace('....................................................................................................', '')
#     # text = text.replace('SUBJECT NAME IN TH [IN+TH] TW PR OR TUT Tot% Crd Grd GP CP P&R ORD', '')
#     # text = text.replace('............ ....... ....... ....... ....... ....... ....... ... ... ... ... ... ... ... ...', '')

#     # text = text.replace('PAGE :-', '')
#     text = text.replace('SEAT NO.', '')
#     text = text.replace('SEAT NO.:', '')
#     text = text.replace('NAME :', '')
#     text = text.replace('MOTHER :', '')
#     text = text.replace('PRN :', '')
#     text = text.replace('CLG.: DYPP[8]', '')

#     text = text.replace('..............................', '')
#     text = text.replace('SEM.:1', '')
#     text = text.replace('SEM.:2', '')
#     text = text.replace(
#         'OE       TH     [OE+TH]     TW       PR       OR    Tot% Crd  Grd  Pts   Pts', '')
#     text = text.replace(
#         'OE       TH     [OE+TH]     TW       PR       OR    Tot% Crd  Grd  Pts   Pts', '')
#     text = text.replace('DYPP', '')
#     text = text.replace('Grd   Crd', '')
#     text = text.replace('SEM. 2', '')
#     text = text.replace('SEM. 1', '')
#     text = text.replace('~', '')
#     text = text.replace(' .', '')
#     text.replace('~', 'nan')
#     text = text.replace('*', ' ')
#     text = text.replace(':', ' ')
#     # text = text.replace('-', 'n')
#     # text = text.replace('SECOND YEAR ', '')
#     text = text.replace('TOTAL CREDITS EARNED ', '')

#     # NEW
#     text = text.replace('HON-ENT. ARCH. AND COMP.', '')
#     text = text.replace('HON-STAT. AND MAC. LRNG.', '') 
#     text = text.replace('HON-DATA SCI. & VISU.', '')      
#     text = text.replace('HON-INFO. AND CYBER SEC.', '')   
#     text = text.replace('INTERNSHIP', '')
#     text = text.replace('CLOUD COMPUTING', '')
#     text = text.replace('WEB APPLICATION DEV.', '')
#     text = text.replace('DS & BDA', '')
#     text = text.replace('DATA SCI. & BIG DATA ANA.', '')
#     text = text.replace('COMP. NET. & SEC.', '')
#     text = text.replace('COMPUTER NET. & SECURITY', '')
#     text = text.replace('LEAD. & PERSONALITY DEV.', '')
#     text = text.replace('DATE', '')
#     # text = text.replace('I', '')
#     text = text.replace('-', 'n')
#     # text = text.replace('.', '')
#     text = text.replace('#', '') # for grace marks


#     text = text.strip()
#     return text


# @st.cache_data
# def displayPDF(file):
#     base64_pdf = base64.b64encode(file.read()).decode('utf-8')
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)


# @st.cache_data
# def pdfToText(path):
#     pdfreader = PdfReader(path)
#     no_of_pages = len(pdfreader.pages)  # Use len(reader.pages) instead of reader.numPages

#     with open('final_txt.txt', 'w') as f:
#         for i in range(0, no_of_pages):
#             pagObj = pdfreader.pages[i]
#             f.write(pagObj.extract_text())

#     # Merge additional code here
#     with open("final_txt.txt", 'r') as file:
#         content = file.read()
#     # for_SE1 = replace_at_odd_positions(content, '314451', '666777')
#     # for_SE2 = replace_at_odd_positions(for_SE1, '314452', '666778')
#     # for_SE3 = replace_at_odd_positions(for_SE2, '207003', '207033')
#     for_SE1 = replace_at_odd_positions(content, '214441', '244441')
#     for_SE2 = replace_at_odd_positions(for_SE1, '207003', '247003')
#     for_SE3 = replace_at_odd_positions(for_SE2, 'SECOND YEAR SGPA ', 'SGPA1')

#     #BE
#     # for_BE1 = replace_at_odd_positions(for_SE3, '414458', '444458')
#     # for_BE2 = replace_at_odd_positions(for_BE1, '414459', '444459')
#     # for_BE3 = replace_at_odd_positions(for_BE2, '414464A', '444464A')
#     # for_BE4 = replace_at_odd_positions(for_BE3, '414466', '444466')
#     # for_BE5 = replace_at_odd_positions(for_BE4, '414468', '444468')

#     #TE
#     for_TE1 = replace_at_odd_positions(for_SE3, '314452', '344452')
#     for_TE2 = replace_at_odd_positions(for_TE1, '314451', '344451')




#     with open("final_txt.txt", 'w') as file:
#         file.write(for_TE2)
#     # End of merged code

#     with open('final_txt.txt', 'r') as f:
#         text = f.read()
    
#     if os.path.exists("final_txt.txt"):
#         os.remove("final_txt.txt")
        
#     return text

# @st.cache_data
# def showUploadedFile(file):
#     f = pd.read_csv(file)
#     return f

# @st.cache_data
# def cleanMarks(text: str, subject_codes) -> dict:
#     for codes in subject_codes.keys():
#         # Skip 214450A subject
#         if codes == '214450A': # SE
#             continue
        
#         if codes == '214459D': # SE
#             continue
        
#         pattern = re.findall(fr'{codes}[A-Z]?\s+\w+[\/!#&$@ \*~]*\w*\s*\w*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\+]*\w*\s*\+*\w*\s*\+*\w*\s*\w*\+*\s*\w*\s*\+*\w*\s', text)
        
#         # SE sem1+sem2 
#         # d = {'subject': [],  'OE': [], 'TH': [], 'OE_TH': [], 'TW': [], 'PR': [], 'OR': [], 'TOT': [], 'CRD': [], 'GRD': [], 'PTS1' : [], 'PTS2' : []}
        
#         # prefect for SE-TE sem-1 | NoT for BE-sem-1
#         d = {'subject': [],  'OE': [], 'TH': [], 'OE_TH': [], 'TW': [], 'PR': [], 'OR': [], 'TOT': [], 'TUT' : [], 'CRD': [], 'GRD': []}
       
        
#         for i in pattern:
#             temp = i.split()
#             # print(temp)

#             if len(temp) < 13: # for odd sem noT processing to ReSolve it.
#                 while len(temp)!=13:
#                     temp.append('X')


#             # SE sem1+sem2 
#             # d['subject'].append(temp[0])
#             # d['OE'].append(temp[1])
#             # d['TH'].append(temp[2])
#             # d['OE_TH'].append(temp[3])
#             # d['TW'].append(temp[4])
#             # d['PR'].append(temp[5])
#             # d['OR'].append(temp[6])
#             # d['TOT'].append(temp[7])
#             # d['CRD'].append(temp[8])
#             # d['GRD'].append(temp[9])
#             # d['PTS1'].append(temp[10])
#             # d['PTS2'].append(temp[11])


#             # prefect for SE-TE sem-1 | NoT for BE-sem-1
#             d['subject'].append(temp[0])
#             d['OE'].append(temp[1])
#             d['TH'].append(temp[2])
#             d['OE_TH'].append(temp[3])
#             d['TW'].append(temp[4])
#             d['PR'].append(temp[5])
#             d['OR'].append(temp[6])
#             d['TUT'].append(temp[7])
#             d['TOT'].append(temp[8])
#             d['CRD'].append(temp[9])
#             d['GRD'].append(temp[10])

#             # d['PTS1'].append(temp[10])
#             # d['PTS2'].append(temp[11])
       


#         dataframe = pd.DataFrame(d)
#         subject_codes[codes] = dataframe
#     return subject_codes



# ajeet code  new 
# itdepartment.py
# itdepartment.py

import streamlit as st
import pandas as pd
import PyPDF2
import base64
import re
import os 
# from st_aggrid import  GridOptionsBuilder

# Replace PdfFileReader with PdfReader
from PyPDF2 import PdfReader

@st.cache_data
def replace_at_odd_positions(string, old_str, new_str):
    result = ''
    count = 0
    i = 0
    while i < len(string):
        if string[i:i + len(old_str)] == old_str:
            if count % 2 != 0:
                result += new_str
            else:
                result += old_str
            count += 1
            i += len(old_str)
        else:
            result += string[i]
            i += 1
    return result



@st.cache_data
def getSubjectNames(text):
    pattern = r"\d{6}\s(.+?)\s\s\*"
    subject_codes = re.findall(pattern, text)
    return subject_codes

@st.cache_data
def getSubjectCodes(text: str, subjectCodeCount: int) -> list:
    pattern = re.findall(r'[1-4]{1}\d{4,6}\w{1}', text)
    d = {}
    for i in pattern:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return list(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)).keys())[:subjectCodeCount]

@st.cache_data
def studentDetails(text: str):
    l = []
    pattern = re.findall(r'[STB]\d{9}\s*\w*\s*\w*\s*\w*\s*\w*\w*\s*\w*\s*\w*\s*\w*\s*', text)
    d = {'seat_no': [], 'name': []}
    for i in pattern:
        temp = i.split()
        d['seat_no'].append(temp[0])
        d['name'].append(temp[1]+' '+temp[2]+' '+temp[3])
    return pd.DataFrame(d)

@st.cache_data
def studentSgpa(text: str):
    pattern = re.findall(r'SGPA1\W*\d*\W*\d*', text)
    # pattern = re.findall(r'SGPA1?\W*\d*\W*\d*(?!\W*,)', stored_text)
    
    d = {'sgpa':[],'score':[]}
    for i in pattern:
        temp = i.split()
        d['sgpa'].append(temp[0])
        d['score'].append(temp[1])
    return pd.DataFrame(d)

@st.cache_data
def getTabledownloadLink(df, file_name=str):
    """Generates a link allowing the data in a given panda dataframe to be downloaded"""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">Download Excel file</a>'
    return href


@st.cache_data
def cleanText(text: str) -> str:
    subjects = ['OBJECT ORIENTED PROG. LAB','DATA STRUCTURES & ALGO. LAB','LOGIC DESIGN COMP. ORG. LAB','LOGIC DESIGN & COMP. ORG.','DATA STRUCTURES & ALGO.','INFORMATION AND CYBER SECURITY', 'MACHINE LEARNING & APPS.','DESIGN AND ANALYSIS OF ALG.' 
            'SOFTWARE DESIGN AND MODELING', 'BUS. ANALYTICS & INTEL.', 'SW. TESTING & QA.',
            'COMPUTER LABORATORY-VII', 'COMPUTER LABORATORY-VIII', 'LABORATORY PRACTICE-II',
            'COMPUTER LABORATORY-VIII', 'PROJECT PHASE-I', 'CRITICAL THINKING',
            'DISTRIBUTED COMPUTING SYSTEM', 'UBIQUITOUS COMPUTING', 'INTERNET OF THINGS (IOT)', 
            'INTERNET OF THINGS (IOT)', 'SOCIAL MEDIA ANALYTICS', 'COMPUTER LABORATORY-IX', 'COMPUTER LABORATORY-IX', 
            'COMPUTER LABORATORY-X', 'PROJECT WORK', 'PROJECT WORK', 'IOT- APPLI. IN ENGG. FIELD','INFO. & STORAGE RETRIEVAL','DIGI ELECTRO & LOGIC DESIGN','FUNDAMENTAL OF DATASTRUCTURE','PROB SOLVI & OOPS','DIGITAL LABORATORY','PROGRAMMING LABORATORY','OBJECT ORIEN PROGRAMMING','COMMUNICATION SKILLS','ROAD SAFETY','ENGINEERING MATHEMATICS -III','COMPUTER GRAPHICS','PROCESSOR ARCH AND INTERFACING','DATA STRUCTURES & FILES','FOUND OF COMM & COMP NETWORK','PROCESSOR INTERFACING LAB','DATA STRUCTURE & FILES LAB','COMPUTER GRAPHICS LABORATORY','WATER MANAGEMENT','DISCRETE STRUCTURES','INFORMATION AND CYBER SEC.', 'MACHINE LEARNING & APPS.', 'SOFTWARE DESIGN AND MODELING', 'BUS. ANALYTICS & INTEL.', 'SW. TESTING & QA. ', 'COMPUTER LABORATORY-VIII', 'COMPUTER LABORATORY-VIII', 'PROJECT PHASE-I', 'DISTRIBUTED COMPUTING SYSTEM', 'UBIQUITOUS COMPUTING', 'INTERNET OF THINGS (IOT)', 'INTERNET OF THINGS (IOT)', 'SOCIAL MEDIA ANALYTICS ', 'COMPUTER LABORATORY-IX', 'COMPUTER LABORATORY-IX', 'COMPUTER LABORATORY-X', 'PROJECT WORK', 'PROJECT WORK', 'HON-MACH. LEARN.& DATA SCI.', 'HON-A.I. FOR BIG DATA ANA.','HON-MACHINE LEARNING',' HON-IOT & EMBEDED SECURITY',' HON-INFO. SYS. MGMT.','HON-RISK ASSMNT LABORATORY','ENGINEERING MATHEMATICS-III','ENGINEERING MATHEMATICS-III','PROCESSOR ARCHITECTURE','DATABASE MANAGEMENT SYSTEM','COMPUTER GRAPHICS LAB','SOFTWARE ENGINEERING','PROG. SKILL DEVELOPMENT LAB','DATABASE MGMT. SYSTEM LAB','COMPUTER GRAPHICS','PROJECT BASED LEARNING','INTELLECTUAL PROPERTY RIGHTS', 'CYBER SECURITY AND LAW','PROJECT STAGE II', 'DISTRIBUTED SYSTEMS', 'GAME ENGINEERING', 'BLOCKCHAIN TECHNOLOGY', 'STARTUP & ENTREPRENEURSHIP', 'LAB PRACTICE VI', 'LAB PRACTICE V', 'CYBER LAWS & USE OF S.M.' ,'ENTREPRENEURSHIP','FE SGPA :', 'SE SGPA :', 'TE SGPA :']
    
    for i in subjects:
        text = text.replace(i, '')

    # SE subject names and TE subject names
    text = text.replace('DESIGN AND ANALYSIS OF ALG.','')
    text = text.replace('COMPUTER ORGANIZATION & ARCH.','')
    text = text.replace('THEORY OF COMPUTATION', '')
    text = text.replace('MACHINE LEARNING', '')
    text = text.replace('HUMAN COMPUTER INTERACTION', '')
    # text = text.replace('A DESIGN AND ANALYSIS OF ALG.', '')
    # text = text.replace('SEMINAR', '')
    text = text.replace('HUMAN COMP. INTERACTION-LAB.', '')
    text = text.replace('LABORATORY PRACTICE-I', '')
    text = text.replace('OPERATING SYSTEMS LAB(TW+PR)', '')
    text = text.replace('OPERATING SYSTEMS', '')
    ### 
    text = text.replace('SAVITRIBAI PHULE PUNE UNIVERSITY ,S.E.(2019 CREDIT PAT.) EXAMINATION, OCT/NOV 2023', '')
    text = text.replace('COLLEGE: [CEGP010530] - D.Y. PATIL COLLEGE OF ENGINEERING, PUNE ', '')
    text = text.replace('BRANCH CODE:  29-S.E.(2019 PAT.)(INFORMATION TECHNOLOGY)', '')
    ###
    text = text.replace('STARTUP ECOSYSTEMS', '')
    text = text.replace('SEMINAR', '')
    text = text.replace('...........                 ...... ...... ...... ...... ...... ......   ..  .. ..  .... ......', '')
    text = text.replace('............ ....... ....... ....... ....... ....... ....... ... ... ... ... ... ... ... ...', '')
    text = text.replace('  ...........                 ...... ...... ...... ...... ...... ......   ..  .. ..  .... ......', '')
    text = text.replace('DISCRETE MATHEMATICS', '')
    text = text.replace('LOGIC DESIGN & COMP. ORG.', '')
    text = text.replace('OBJECT ORIENTED PROG. LAB', '')
    text = text.replace('OBJECT ORIENTED PROGRAMMING', '')
    text = text.replace('BASIC OF COMPUTER NETWORK', '')
    text = text.replace('LOGIC DESIGN COMP. ORG. LAB', '')
    text = text.replace('DATA STRUCTURES & ALGO. LAB', '')
    # text = text.replace('DATA STRUCTURES & ALGO. LAB', '')
    # text = text.replace('DATA STRUCTURES & ALGO.', '')
    text = text.replace('SOFT SKILL LAB', '')
    text = text.replace('ETHICS AND VALUES IN IT', '')
    text = text.replace('LAB.', '')
    text = text.replace(
        'SAVITRIBAI PHULE PUNE UNIVERSITY ,T.E.(2019 COURSE) EXAMINATION, OCT/NOV 2023', '') #
    text = text.replace(
        'COLLEGE: [CEGP010530] - D.Y. PATIL COLLEGE OF ENGINEERING, PUNE', '') #
    text = text.replace(
        'BRANCH CODE:  29-S.E.(2019 PAT.)(INFORMATIOM TECHNOLOGY)', '')
    text = text.replace('DATE : 21 APR 2022 ', '')
    text = text.replace(
        'COURSE NAME ISE ESE TOTAL TW PR OR TUT Tot% Crd Grd GP CP P&R ORD', '')
    text = text.replace(
        
        'SAVITRIBAI PHULE PUNE UNIVERSITY, S.E.(2015 COURSE) EXAMINATION,MAY 2018', '')
    text = text.replace(' COURSE NAME                      ISE      ESE     TOTAL      TW       PR       OR    Tot% Crd  Grd   GP  CP  P&R ORD', '')

    # text = text.replace('SAVITRIBAI PHULE PUNE UNIVERSITY ,T.E.(2019 COURSE) EXAMINATION, APR/MAY 2022', '')
    text = text.replace('COLLEGE    : D.Y. PATIL COLLEGE OF ENGINEERING,  PUNE', '')
    text = text.replace('COLLEGE: [CEGP010530] - D.Y. PATIL COLLEGE OF ENGINEERING,  PUNE', '')
    text = text.replace('BRANCH CODE: 29-S.E.(2015 PAT.)(INFORMATIOM TECHNOLOGY)', '')
    text = text.replace('BRANCH CODE: 60-T.E.(2019 PAT.)(INFORMATION TECHNOLOGY)', '')
    text = text.replace('INFO. & STORAGE RETRIEVAL', '')
    text = text.replace('SOFTWARE PROJECT MANAGEMENT', '')
    text = text.replace('DEEP LEARNING', '')
    text = text.replace('MOBILE COMPUTING', '')
    text = text.replace('INTRODUCTION TO DEVOPS', '')
    text = text.replace('LAB PRACTICE III', '')
    text = text.replace('LAB PRACTICE IV', '')
    text = text.replace('PROJECT STAGE-I', '')
    text = text.replace(' COPYRIGHTS AND PATENTS ', '')
    # text = text.replace('DATE : 06 MAY 2022', '')
    text = text.replace('SUBJECT NAME OE TH [OE+TH] TW PR OR Tot% Crd Grd GP CP P&R ORD', '') # 

    text = text.replace('COURSE NAME                      ISE      ESE     TOTAL      TW       PR       OR     TUT  Tot%  Crd  Grd  GP   CP  P&R ORD', '') # 
    text = text.replace('...........                 ...... ...... ...... ...... ...... ......   ..  .. ..  .... ......', '') # 
    # text = text.replace('16 JAN 2024', '') # 
    text = text.replace('............CONFIDENTIAL- FOR VERIFICATION AND RECORD ONLY AT COLLEGE, NOT FOR DISTRIBUTION.......................................', '')
    text = text.replace('.........................CONFIDENTIAL- FOR VERIFICATION AND RECORD ONLY AT COLLEGE, NOT FOR DISTRIBUTION..........................', '')
    text = text.replace('....................................................................................................', '')
    # text = text.replace('SUBJECT NAME IN TH [IN+TH] TW PR OR TUT Tot% Crd Grd GP CP P&R ORD', '')
    # text = text.replace('............ ....... ....... ....... ....... ....... ....... ... ... ... ... ... ... ... ...', '')

    # text = text.replace('PAGE :-', '')
    text = text.replace('SEAT NO.', '')
    text = text.replace('SEAT NO.:', '')
    text = text.replace('NAME :', '')
    text = text.replace('MOTHER :', '')
    text = text.replace('PRN :', '')
    text = text.replace('CLG.: DYPP[8]', '')

    text = text.replace('..............................', '')
    text = text.replace('SEM.:1', '')
    text = text.replace('SEM.:2', '')
    text = text.replace(
        'OE       TH     [OE+TH]     TW       PR       OR    Tot% Crd  Grd  Pts   Pts', '')
    text = text.replace(
        'OE       TH     [OE+TH]     TW       PR       OR    Tot% Crd  Grd  Pts   Pts', '')
    text = text.replace('DYPP', '')
    text = text.replace('Grd   Crd', '')
    text = text.replace('SEM. 2', '')
    text = text.replace('SEM. 1', '')
    text = text.replace('~', '')
    text = text.replace(' .', '')
    text.replace('~', 'nan')
    text = text.replace('*', ' ')
    text = text.replace(':', ' ')
    # text = text.replace('-', 'n')
    # text = text.replace('SECOND YEAR ', '')
    text = text.replace('TOTAL CREDITS EARNED ', '')

    # NEW
    text = text.replace('HON-ENT. ARCH. AND COMP.', '')
    text = text.replace('HON-STAT. AND MAC. LRNG.', '') 
    text = text.replace('HON-DATA SCI. & VISU.', '')      
    text = text.replace('HON-INFO. AND CYBER SEC.', '')   
    text = text.replace('INTERNSHIP', '')
    text = text.replace('CLOUD COMPUTING', '')
    text = text.replace('WEB APPLICATION DEV.', '')
    text = text.replace('DS & BDA', '')
    text = text.replace('DATA SCI. & BIG DATA ANA.', '')
    text = text.replace('COMP. NET. & SEC.', '')
    text = text.replace('COMPUTER NET. & SECURITY', '')
    text = text.replace('LEAD. & PERSONALITY DEV.', '')
    text = text.replace('DATE', '')
    # text = text.replace('I', '')
    text = text.replace('-', 'n')
    # text = text.replace('.', '')
    text = text.replace('#', '') # for grace marks


    text = text.strip()
    return text


@st.cache_data
def displayPDF(file):
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


@st.cache_data
def pdfToText(path):
    pdfreader = PdfReader(path)
    no_of_pages = len(pdfreader.pages)  # Use len(reader.pages) instead of reader.numPages

    with open('final_txt.txt', 'w') as f:
        for i in range(0, no_of_pages):
            pagObj = pdfreader.pages[i]
            f.write(pagObj.extract_text())

    # Merge additional code here
    with open("final_txt.txt", 'r') as file:
        content = file.read()
    # for_SE1 = replace_at_odd_positions(content, '314451', '666777')
    # for_SE2 = replace_at_odd_positions(for_SE1, '314452', '666778')
    # for_SE3 = replace_at_odd_positions(for_SE2, '207003', '207033')
    for_SE1 = replace_at_odd_positions(content, '214441', '244441')
    for_SE2 = replace_at_odd_positions(for_SE1, '207003', '247003')
    for_SE3 = replace_at_odd_positions(for_SE2, 'SECOND YEAR SGPA ', 'SGPA1')

    #BE
    # for_BE1 = replace_at_odd_positions(for_SE3, '414458', '444458')
    # for_BE2 = replace_at_odd_positions(for_BE1, '414459', '444459')
    # for_BE3 = replace_at_odd_positions(for_BE2, '414464A', '444464A')
    # for_BE4 = replace_at_odd_positions(for_BE3, '414466', '444466')
    # for_BE5 = replace_at_odd_positions(for_BE4, '414468', '444468')

    #TE
    for_TE1 = replace_at_odd_positions(for_SE3, '314452', '344452')
    for_TE2 = replace_at_odd_positions(for_TE1, '314451', '344451')






    with open("final_txt.txt", 'w') as file:
        file.write(for_TE2)
    # End of merged code

    with open('final_txt.txt', 'r') as f:
        text = f.read()
    
    if os.path.exists("final_txt.txt"):
        os.remove("final_txt.txt")
        
    return text

@st.cache_data
def showUploadedFile(file):
    f = pd.read_csv(file)
    return f

"""

@st.cache_data
def cleanMarks(text: str, subject_codes) -> dict:
    for codes in subject_codes.keys():
        # Skip 214450A subject
        if codes == '214450A': # SE
            continue
        
        if codes == '214459D': # SE
            continue
        
        pattern = re.findall(fr'{codes}[A-Z]?\s+\w+[\/!#&$@ \*~]*\w*\s*\w*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\+]*\w*\s*\+*\w*\s*\+*\w*\s*\w*\+*\s*\w*\s*\+*\w*\s', text)

        # d = {'subject': [],  'OE': [], 'TH': [], 'OE_TH': [], 'TW': [], 'PR': [], 'OR': [], 'TOT': [], 'CRD': [], 'GRD': [], 'PTS1' : [], 'PTS2' : []}
        d = {'subject': [],  'OE': [], 'TH': [], 'OE_TH': [], 'TW': [], 'PR': [], 'OR': [], 'TOT': [], 'TUT' : [], 'CRD': [], 'GRD': []}
        
        for i in pattern:
            temp = i.split()
            # print(temp)
            print("SEM----------" , getSem)

            if len(temp) < 13: # for odd sem noT processing to ReSolve it.
                while len(temp)!=13:
                    temp.append('X')



            
            # BE-sem1 | SE | TE     

            # d['subject'].append(temp[0])
            # d['OE'].append(temp[1])
            # d['TH'].append(temp[2])
            # d['OE_TH'].append(temp[3])
            # d['TW'].append(temp[4])
            # d['PR'].append(temp[5])
            # d['OR'].append(temp[6])
            # d['TOT'].append(temp[7])
            # d['CRD'].append(temp[8])
            # d['GRD'].append(temp[9])
            # d['PTS1'].append(temp[10])
            # d['PTS2'].append(temp[11])


            # BE | SE-sem1 | TE-sem1-2024 | TE-sem1 

            d['subject'].append(temp[0])
            d['OE'].append(temp[1])
            d['TH'].append(temp[2])
            d['OE_TH'].append(temp[3])
            d['TW'].append(temp[4])
            d['PR'].append(temp[5])
            d['OR'].append(temp[6])
            d['TUT'].append(temp[7])
            d['TOT'].append(temp[8])
            d['CRD'].append(temp[9])
            d['GRD'].append(temp[10])

            # d['PTS1'].append(temp[10])
            # d['PTS2'].append(temp[11])
       


        dataframe = pd.DataFrame(d)
        subject_codes[codes] = dataframe
    return subject_codes

"""

@st.cache_data
def cleanMarks1(text: str, subject_codes) -> dict:
    for codes in subject_codes.keys():
        # Skip 214450A subject
        if codes == '214450A': # SE
            continue
        
        if codes == '214459D': # SE
            continue
        
        pattern = re.findall(fr'{codes}[A-Z]?\s+\w+[\/!#&$@ \*~]*\w*\s*\w*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\+]*\w*\s*\+*\w*\s*\+*\w*\s*\w*\+*\s*\w*\s*\+*\w*\s', text)

        d = {'subject': [],  'OE': [], 'TH': [], 'OE_TH': [], 'TW': [], 'PR': [], 'OR': [], 'TOT': [], 'CRD': [], 'GRD': [], 'PTS1' : [], 'PTS2' : []}
        
        for i in pattern:
            temp = i.split()
            # print(temp)

            if len(temp) < 13: # for odd sem noT processing to ReSolve it.
                while len(temp)!=13:
                    temp.append('X')


            
            # BE-sem1 | SE | TE     
            

            d['subject'].append(temp[0])
            d['OE'].append(temp[1])
            d['TH'].append(temp[2])
            d['OE_TH'].append(temp[3])
            d['TW'].append(temp[4])
            d['PR'].append(temp[5])
            d['OR'].append(temp[6])
            d['TOT'].append(temp[7])
            d['CRD'].append(temp[8])
            d['GRD'].append(temp[9])
            d['PTS1'].append(temp[10])
            d['PTS2'].append(temp[11])



        dataframe = pd.DataFrame(d)
        subject_codes[codes] = dataframe
    return subject_codes


@st.cache_data
def cleanMarks(text: str, subject_codes) -> dict:
    for codes in subject_codes.keys():
        # Skip 214450A subject
        if codes == '214450A': # SE
            continue
        
        if codes == '214459D': # SE
            continue
        
        pattern = re.findall(fr'{codes}[A-Z]?\s+\w+[\/!#&$@ \*~]*\w*\s*\w*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\/!#&$@ \*~^]*\w*\s*[\+]*\w*\s*\+*\w*\s*\+*\w*\s*\w*\+*\s*\w*\s*\+*\w*\s', text)

        d = {'subject': [],  'OE': [], 'TH': [], 'OE_TH': [], 'TW': [], 'PR': [], 'OR': [], 'TOT': [], 'TUT' : [], 'CRD': [], 'GRD': []}
        
        for i in pattern:
            temp = i.split()
            # print(temp)

            if len(temp) < 13: # for odd sem noT processing to ReSolve it.
                while len(temp)!=13:
                    temp.append('X')


            # BE | SE-sem1 | TE-sem1-2024 | TE-sem1 

            d['subject'].append(temp[0])
            d['OE'].append(temp[1])
            d['TH'].append(temp[2])
            d['OE_TH'].append(temp[3])
            d['TW'].append(temp[4])
            d['PR'].append(temp[5])
            d['OR'].append(temp[6])
            d['TUT'].append(temp[7])
            d['TOT'].append(temp[8])
            d['CRD'].append(temp[9])
            d['GRD'].append(temp[10])

            # d['PTS1'].append(temp[10])
            # d['PTS2'].append(temp[11])
       


        dataframe = pd.DataFrame(d)
        subject_codes[codes] = dataframe
    return subject_codes
