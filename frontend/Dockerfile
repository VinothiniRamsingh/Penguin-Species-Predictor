FROM python:3.9-slim

WORKDIR /penguin_species_predictor

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ml_app.py .

EXPOSE 8501

CMD ["streamlit", "run", "ml_app.py", "--server.address=0.0.0.0"]
