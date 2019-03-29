# AWS Lambda Debug Local Machine

This project guides how to debug an aws lambda on local machine with nodejs and python

### NodeJS
###### Install library
```
npm install -g lambda-local
```

###### Run command debug lambda
```
lambda-local -l index.js -h handler -e sample/event.js --envfile .env
```

### Python
###### Install library
```
pip install python-lambda-local
```

###### Run command debug lambda
```
python-lambda-local -f handler -e debug/env.json function.py debug/event.json
```