dev:
		cd src && python3 -m pytest && pipenv run uvicorn main:app --reload --port 8008 --host 0.0.0.0
