# RedBus-Test-Case-Automation-Tool

This project is a web-based tool designed to automatically generate detailed test cases for digital products, specifically focusing on features of the RedBus mobile app. Using Google Generative AI and a multimodal approach, this tool processes screenshots and optional context to provide a structured, step-by-step guide for testing various app functionalities.

## Table of Contents
- Overview
- Features
- How It Works
- Setup and Installation
- Usage
- Example Output
- Contributing

## Overview

The **RedBus-Test-Case-Automation-Tool** leverages a multimodal Language Learning Model (LLM) to generate comprehensive testing instructions for various features of the RedBus mobile app. It takes in screenshots and optional context as inputs and outputs a detailed list of test cases that include:

- **Description**: A summary of the test case.
- **Pre-conditions**: Setup or requirements before testing.
- **Testing Steps**: Step-by-step instructions to perform the test.
- **Expected Result**: The desired outcome if the feature works correctly.

## Features

- **Image Upload**: Allows users to upload multiple screenshots of the app.
- **Context Input**: Provides an optional text box for additional context.
- **Test Case Generation**: Automatically generates test cases using the Google Generative AI model.
- **Interactive Interface**: A simple web-based interface using Streamlit.

## How It Works

1. **Image Upload**: Users upload screenshots of the app's features they want to test.
2. **Context Input**: Users can provide optional text context to specify additional details.
3. **Prompt Creation**: The tool formulates a detailed prompt combining the provided context and default instructions.
4. **AI Processing**: The prompt and images are sent to the Google Generative AI model (`gemini-1.5-pro`) for processing.
5. **Output Generation**: The model returns a structured list of test cases, which are displayed on the web interface.

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit]
- Pillow(PIL library for image processing)
- Google Generative AI SDK

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AtharvaDomale/RedBus-Test-Case-Automation-Tool.git

2. **Install Required Packages**
   ```bash
   pip install -r requirements.txt

3. **Set Up Google Generative AI Key Replace "YOUR_API_KEY" in the code with your actual API key or set it as an environment variable**
  
2. **Run the Application**
   ```bash
   streamlit run main.py
## Contributing
  Contributions are welcome! 
  Please fork the repository and submit a pull request with your proposed changes. For major changes, please open an issue to discuss them first.
