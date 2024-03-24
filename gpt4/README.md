### Step 1: Clone the Repository

Clone the repository containing the Streamlit app to your local machine.

```bash
git clone from main repo
cd gpt4
```

### Step 2: Create and Activate a Virtual Environment

Create a virtual environment to isolate the dependencies for the app.

```bash
python3.8 -m venv venv
source venv/bin/activate
```


### Step 3: Install Dependencies

Install the required Python dependencies from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```



### Step 4: Create and Activate a Conda Environment for GPT 4 DALL-E

Create a Conda environment named "gpt4" to isolate the dependencies for the app.

```bash
conda create -n gpt4
```

### Activate the "gpt4" Environment

Activate the "gpt4" environment using the following command:

```bash
conda activate gpt4
```

### Install Necessary Libraries

Install the necessary libraries using pip:

```bash
pip install streamlit langchain trulens-eval openai
```

### Set Up Streamlit Secrets

To incorporate your OpenAI API key and HuggingFace Access Token into Streamlit secrets, follow these steps:

1. Create a `.streamlit/secrets.toml` file within your project directory:

```bash
touch .streamlit/secrets.toml
```

### Configure API Keys

To configure your API keys for OpenAI and HuggingFace, follow these steps:

1. create `.streamlit/secrets.toml` file in your project directory.

2. Add the following lines to the file, replacing `"YOUR_API_KEY"` and `"YOUR_ACCESS_TOKEN"` with your respective keys:

```toml
OPENAI_API_KEY = "YOUR_API_KEY"
```

### Step 5: Run the Streamlit App

Run the Streamlit app using the `streamlit` command.
```bash
pip install -r requirements.txt
```


```bash
streamlit run AIKidArtist.py
```

### Step 6: Access the App

Access the Streamlit app in your web browser by navigating to the URL provided by Streamlit, typically [http://localhost:8501](http://localhost:8501).