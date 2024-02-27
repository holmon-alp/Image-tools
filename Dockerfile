FROM python:3.11.7

ENV PYTHONUNBUFFERED True

EXPOSE 8080

RUN apt-get -y update && apt-get -y install tesseract-ocr

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . ./

RUN pip install -r requirements.txt

# CMD streamlit run --server.port 8080 --server.enableCORS false app.py
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
