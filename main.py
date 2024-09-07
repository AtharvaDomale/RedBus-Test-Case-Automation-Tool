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
               RedBus App Testing Scenarios
Here are some detailed test cases for the RedBus mobile app:

1. Source, Destination, and Date Selection
Description:
This test case verifies that the user can successfully search for available buses by entering the source city, destination city, and travel date.

Pre-conditions:

The RedBus app is installed on the user's mobile device.
The user has an active internet connection.
Testing Steps:

Launch the RedBus app.
On the home screen, tap the "From" field and enter the source city (e.g., "Chatrapati Sambhajinagar").
Select the correct source city from the suggestions that appear.
Tap the "To" field and enter the destination city (e.g., "Mumbai").
Select the correct destination city from the suggestions that appear.
Tap the "Date of Journey" field and select the desired travel date from the calendar.
Tap the "Search buses" button.
Expected Result:

The app should display a list of available buses for the selected source city, destination city, and travel date.
The list should include relevant bus details such as bus operator, departure and arrival times, available seats, and ticket price.
2. Bus Selection
Description:
This test case verifies that the user can select a specific bus from the search results based on their preferences.

Pre-conditions:

The user has successfully searched for available buses (Test Case 1).
Testing Steps:

From the list of available buses, scroll through the options and tap on the desired bus that meets your criteria (time, price, rating, etc.).
Expected Result:

The app should display a detailed view of the selected bus, including all relevant information (amenities, seat availability, fare breakdown, boarding/dropping points, etc.).
3. Seat Selection
Description:
This test case verifies that the user can select their desired seat(s) on the chosen bus.

Pre-conditions:

The user has selected a specific bus (Test Case 2).
Testing Steps:

On the bus details screen, tap on the "View Seats" or similar button.
A seat map of the bus will be displayed.
Tap on the desired seat(s) to select them. Selected seats will be highlighted.
If needed, choose the seat type (sleeper/seater) and berth preference (upper/lower).
Expected Result:

The selected seats should be marked on the seat map.
The total fare should update accordingly based on the chosen seat type and number of seats.
4. Pick-up and Drop-off Point Selection
Description:
This test case ensures the user can select their preferred boarding and dropping points for the journey.

Pre-conditions:

The user has selected a bus and seat(s) (Test Case 3).
Testing Steps:

Proceed to the booking page.
On the booking page, you should see options to select boarding and dropping points.
Tap on each option to view available locations.
Select your desired pick-up and drop-off points from the list.
Expected Result:

The selected boarding and dropping points should be reflected on the booking summary.
The app may display any additional charges related to specific pick-up/drop-off points.
5. Offers
Description:
This test case verifies that available discounts and promotions are correctly applied during booking.

Pre-conditions:

The user has reached the payment stage of booking.
Testing Steps:

On the payment page, look for a section titled "Offers," "Promo Codes," or similar.
If there are applicable offers, tap on "View all" or an equivalent option.
Select the offer you want to use. You might need to enter a promo code.
Expected Result:

The discount should be applied to the final ticket price.
The booking summary should clearly show the original price, applied discount, and the final payable amount.
6. Filters
Description:
This test case verifies the functionality of filters in sorting and refining bus search results.

Pre-conditions:

The user has performed a bus search (Test Case 1).
Testing Steps:

On the bus list page, locate the "Filters" or "Sort" option (usually represented by icons or a drop-down menu).
Experiment with different filters:
Bus Type: Select specific bus types (e.g., AC, Non-AC, Sleeper, Seater).
Price: Set a price range to filter buses within your budget.
Departure/Arrival Time: Choose preferred departure or arrival time slots.
Bus Operator: Select your preferred bus operator from the list.
Expected Result:

The app should dynamically update the displayed bus list based on the applied filters.
The filtered results should only display buses that match the selected criteria.
7. Bus Information
Description:
This test case verifies that detailed information about the bus is readily available to the user.

Pre-conditions:

The user has selected a specific bus (Test Case 2).
Testing Steps:

Scroll through the bus details screen to view information about:
Amenities: Check if the bus has features like AC, charging points, blankets, water bottles, etc.
Photos: Look for images of the bus interior and exterior.
User Reviews: Read reviews and ratings from previous passengers.
Bus Operator Information: View details about the bus operator's reliability and services.
Expected Result:

The app should display accurate and detailed information about the selected bus, aiding the user in making an informed decision.
Photos should be clear and relevant, and user reviews should be genuine and insightful.

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
