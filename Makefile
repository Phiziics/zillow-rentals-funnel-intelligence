install:
	pip install -r requirements-dev.txt

run-api:
	uvicorn app.api.main:app --reload

run-streamlit:
	streamlit run app/streamlit/app.py

test:
	pytest -q