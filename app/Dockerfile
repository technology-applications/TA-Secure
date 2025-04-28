FROM python:3.12-bookworm

WORKDIR /app

COPY python/requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "python/app.py"]
