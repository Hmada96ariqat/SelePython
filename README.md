# DockerHub Automation with Selenium

This project automates several DockerHub tasks using Selenium WebDriver. The script includes functionalities such as logging into DockerHub, creating a new repository, and deleting it. 

## Features

- **Logging into DockerHub**: Automates the login process using specified credentials.
- **Creating a Repository**: Generates a random repository name and creates it on DockerHub.
- **Deleting a Repository**: Deletes the repository created during the automation process.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YourUsername/SelePyDocker.git
   cd SelePyDocker


2. **The project requires Python and several libraries, which can be installed using pip:**

    pip install -r requirements.txt

3. **Usage**

Update Credentials

    Modify the username and password in the DockerHubAutomation class within the SelePyDocker.py script:

        self.username = 'YourDockerHubUsername'
        self.password = 'YourDockerHubPassword'


4. **Execute the script to perform the automated tasks:**

    python SelePyDocker.py


# Customization

    Repository Name and Description: The script generates a random repository name. This behavior can be modified by editing the generate_random_string method or directly providing a static name.
    Web Elements: XPaths used to locate elements are specific to DockerHub's current UI and may need updating if DockerHub changes its UI.