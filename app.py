from flask import Flask
import logging

app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    app.logger.info('Info: Hello, World!')
    app.logger.debug('Debug: Debugging message')
    app.logger.error('Error: Something went wrong')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

