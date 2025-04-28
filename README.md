# 📚 Demo AI App

## 🎉 Welcome to the Demo AI App!
This application showcases the seamless integration of various technologies for leveraging AI agents. These AI agents operate directly on your own PC, which enhances the security of your data. You can interact with powerful language models without the need for external servers, ensuring that your sensitive information remains private and secure. Experience how simple and efficient collaboration with artificial intelligence can be, all while maintaining control over your data.

In this example we use a small model. The response will be slow! So do not wonder! The model can be replaced by other models such as Mistral. At TA! at the moment as freelancer growing community, we develop customized solutions based on the needs of our Clients course I can develop the agents for my customers, so that advanced functions can be implented.

## 📂 Table of Contents
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Installation](#installation)

## 🛠️ Technologies Used
- **Streamlit**: A framework for building web applications in Python. For more information, visit [Streamlit](https://streamlit.io).
- **Langchain**: A framework for developing applications powered by language models. Learn more at [Langchain](https://www.langchain.com/).
- **Ollama**: A tool for running large language models locally. Visit [Ollama](https://ollama.com) for details.

## Requirements
- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## 🚀 Installation
To run this application, ensure that you have Docker and Docker Compose installed. Follow the steps below to set up the application:

### Step 1: Clone the Git Repository
To clone the repository, use the following command in your terminal:
```bash
 git clone <repository_url>
```
This command creates a local copy of the repository on your machine. Make sure to replace `<repository_url>` with the actual URL of the repository.

### Step 2: Navigate to the Project Directory
After cloning the repository, navigate into the project directory using the command:
```bash
 cd <repository_directory>
```
Replace `<repository_directory>` with the name of the folder that was created when you cloned the repository. This folder contains all the necessary files to run the application.

### Step 3: Build and Run the Application
Once you are in the project directory, execute the following command to build and run the application:
```bash
 docker-compose up -d --build
```
This command will start the application in detached mode and build the necessary Docker containers.

### Step 4: Check if the Ollama Container is Running
Before proceeding with model installation, ensure that the Ollama container is running. You can check this by visiting [http://localhost:11434](http://localhost:11434) in your web browser.

**Note:** You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models. This information is sourced from [Ollama's GitHub repository](https://github.com/ollama/ollama?tab=readme-ov-file#model-library).

### Step 5: Install a Model
Once you confirm that the Ollama container is up and running, you can install a model by executing the following command in your terminal:
```bash
docker exec -ti ollama ollama pull <model>
```
Replace `<model>` with the specific model you wish to install. For more model options, you can visit [https://ollama.com/search](https://ollama.com/search) to search for available models.

### Step 6: Access the Application
After building the application, you can access it at [http://localhost:8501](http://localhost:8501).
