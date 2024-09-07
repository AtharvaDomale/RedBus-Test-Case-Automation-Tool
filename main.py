import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configure the API key for Gemini
genai.configure(api_key="API_KEY")  # Replace "API_KEY" with your actual API key or use environment variables

# Define the model
model = genai.GenerativeModel("gemini-1.5-pro")

# Streamlit page title
st.title("RedBus-Test-Case-Automation-Tool")

# Upload multiple images
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Optional context text input
context_text = st.text_input("Enter additional context (optional):", "")

if uploaded_files:
    image_list = [Image.open(uploaded_file) for uploaded_file in uploaded_files]
    
    # Display uploaded images
    for image in image_list:
        st.image(image, caption='Uploaded Image', use_column_width=True)

    # Prepare the prompt with multiple examples
    prompt = (
        '''
               You are a highly experienced software tester with a proven track record of creating comprehensive and effective test case formats. Your task is to generate detailed test cases for several key features of the RedBus mobile app. Below are the features for which you need to create test cases based on the provided screenshots:

                1. **Source, Destination, and Date Selection**: The user chooses the origin, destination, and travel date.
                2. **Bus Selection**: Display and select a bus from the available options.
                3. **Seat Selection**: Allow the user to choose a seat on the selected bus.
                4. **Pick-up and Drop-off Point Selection**: Choose where the journey starts and ends.
                5. **Offers**: Highlight any discounts or promotions available.
                6. **Filters**: Options for sorting buses by time, price, or other criteria.
                7. **Bus Information**: Details about the bus, such as amenities, photos, and user reviews.

                For each feature, generate a comprehensive test case that includes the following:

                    - **Description**: A brief summary of what the test case is about.
                    - **Pre-conditions**: The necessary setup or conditions that need to be in place before testing.
                    - **Testing Steps**: A detailed list of clear, step-by-step instructions to perform the test.
                    - **Expected Result**: The outcome that should be observed if the feature works correctly.

                    Please use the screenshots provided to identify the necessary elements and steps for each test case. Ensure that each test case is clear, precise, and follows a structured format to be easily understood by a QA team. If any additional context is provided, incorporate that into the test cases as needed.
                        Source, Destination, and Date Selection: The user chooses where they're going, where they’re starting, and when.
                        
                        Bus Selection: Display and choose from available buses.

                        Seat Selection: Let the user pick their seat on the selected bus.
                        
                        Pick-up and Drop-off Point Selection: Choose where the journey starts and ends.
                        
                        Offers: Highlight any discounts or promotions available.
                        
                        Filters: Options for sorting buses by time, price, or other criteria.
                        Bus Information: Details about the bus, such as amenities, photos, and user reviews.

                    Make sure to fill in each section with appropriate and relevant information for the specified features.


        '''
        )
    
    if context_text:
        prompt += f" {context_text}"

    # Button to generate the content
    if st.button('Describe Testing Instructions'):
        with st.spinner('Generating the Content...'):
            try:
                # Convert image list to the format required by the model
                image_inputs = [img for img in image_list]  # Directly use PIL images
                response = model.generate_content([prompt] + image_inputs)
                
                # Display the output with proper formatting
                st.write("### Generated Test Cases:")
                st.markdown(response.text, unsafe_allow_html=True)  # Use Markdown for better formatting
            except Exception as e:
                st.error(f"An error occurred: {e}")
