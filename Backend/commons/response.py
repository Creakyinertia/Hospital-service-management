import json
from pathlib import Path


cwd = Path(__file__).parents[0]
print(cwd)

fileName = cwd/'success_code.json'
with open(fileName) as fp:
	success_message = json.load(fp)
success_message


fileName = cwd/'error_code.json'
with open(fileName) as fp:
	error_message = json.load(fp)
error_message

