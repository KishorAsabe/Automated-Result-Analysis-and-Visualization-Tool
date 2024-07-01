
import streamlit as st

st.set_page_config(
    page_title='Result Analysis',
    page_icon='📃'
)

# Add main title without splitting and apply custom CSS class
st.markdown(
    """
    <div class='custom-header'>
        <h1>D Y PATIL COLLEGE OF ENGINEERING AKURDI, PUNE</h1>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class='custom-subheader'>
        <p>Department of Information Technology</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='custom-projectname'>
        <h1>Result Analyzer</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Set background image and customize header style with CSS
st.markdown(
    """
    <style>
    .image-container {

        background-size: cover; /* Cover the entire background */
        background-attachment: fixed; /* Ensure the background image does not scroll */
        height: auto; /* Set height to auto */
        width: 920px; /* Set width to 700px */
        margin: 0; /* Remove default margin */
        padding: 30px; /* Add padding */
        border-radius: 12px; /* Apply border radius to the container */
        position: relative; /* Set position to relative */
        left: 10px;
        right: 10px;
    }
    
    .custom-image {
        width: 100%; /* Set width to 100% */
        height: 100%; /* Set height to 100% */
        object-fit: cover; /* Cover the entire image */
        border-radius: 12px; /* Apply border radius to the image */
        margin: 0 -100px; /* Set margin to -10px on the left and right */
 

    }

    .custom-header {
        margin-left: -150px; 
        margin-right: auto; 
        margin-top : -67px;
        position: relative; /* Set position to relative */
        z-index: 1; /* Set a higher z-index to appear above the background */
    }
    .custom-header h1 {
        font-size: 46px;
        color: white;
        text-align: center;
        margin: 0;
        white-space: nowrap;
        
    }
    .custom-subheader p {
        font-size: 42px;
        color: grey;
        text-align: center;
        margin: 0;
        white-space: nowrap;
        position: relative; /* Set position to relative */
        z-index: 1; /* Set a higher z-index to appear above the background */
        margin-top:-25px;
    }
    
    .custom-projectname {
        margin-left: auto; 
        margin-right: auto; 
        margin-top : 10px;
        position: relative; /* Set position to relative */
        z-index: 1; /* Set a higher z-index to appear above the background */
    }
    
    .custom-projectname h1 {
        font-size: 42px;
        color: white;
        text-align: center;
        margin: 0;
        white-space: nowrap;
        
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Wrap the image in a div with the image-container class
st.markdown(
    """
    <div class='image-container'>
      <img src='https://i.postimg.cc/5N5q93XL/College-Photo.jpg' alt='D Y PATIL COLLEGE OF ENGINEERING AKURDI, PUNE' class='custom-image' />
    </div>
    """,
    unsafe_allow_html=True,
)

if __name__ == "__main__":

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
