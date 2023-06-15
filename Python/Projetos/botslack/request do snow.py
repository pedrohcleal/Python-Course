import requests
from lxml import html

r = requests.get('https://us-east-1.signin.aws/platform/login?workflowStateHandle=51dd6918-6ed7-4dc1-aa93-38d447abe142')

print(r.text)