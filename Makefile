dev:
		cd src && pipenv run uvicorn main:app --reload --port 8008 --host 0.0.0.0
