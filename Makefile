dev:
		cd src && python3 -m pytest &&  uvicorn main:app --reload --host 0.0.0.0 --port 10000
