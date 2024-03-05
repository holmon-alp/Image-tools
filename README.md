# Image tools

#### This app is just an amateur creation. The app may contain errors and omissions from various situations.
Using this program: 
- apply effects to images;
- remove background;
- extract text from image;
- generate QR code;
- generate image via Prompt;
    
The program was prepared by **Mirjamol Mirislomov**
> 02.27.2024

> [Go Live](https://image-tools.streamlit.app/)

# Installation
## Step 1 Clone the project from Github
```git clone https://github.com/holmon-alp/Image-tools.git```
###### Go to the folder where the repository is located
```cd <path/to/repository>```

## Step 2.1 Open Terminal, CMD, or another command line, and create a virtual environment for Python
```python -m venv venv```

## Step 2.2 Activate venv
> For Linux Based OS Or Mac-OS:

```source venv/bin/activate```

> For Windows With CMD:

```.\venv\Scripts\activate.bat```

> For Windows With Power shell:

```.\venv\Scripts\activate.ps1```

> For Windows With Unix Like Shells For Example Git Bash CLI:

```source venv/Scripts/activate```

## Step 3 Install requirements packages
```pip install -r requirements.txt```

## Step 4 Install **tesseract**
> On Mac:

```brew install tesseract```

```brew install tesseract --all-languages ```

> On Windows:
>> You can download .exe file from [here](https://github.com/UB-Mannheim/tesseract/wiki)

> On Linux:

```sudo apt install tesseract-ocr -y```

```sudo apt install tesseract-ocr-heb```

## Step 5 Run the project in localhost
```streamlit run app.py```
##### Then you can open this app your browser with: https://localhost:8080

## Requirements
- Python 3.10 or higher
- Git
- Minimum 8GB RAM
- GPU
- 10GB free space
