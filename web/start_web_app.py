from app import app
import logging

logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
