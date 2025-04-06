Steps to run the bookfinder project.

1. Clone the repository and go inside BookFinder directory.

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. From a different cmd, run the mongodb docker container.
```bash
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-enterprise-server:latest
```

4. Populate books in the database
```bash
python app.py
```

5. Run the Flask app
```bash
fastapi dev main.py
```

6. From a different cmd go inside my-book-finder directory and run the following command to start the React app:
```bash
npm start
```

7. Open your browser and go to http://localhost:3000 to see the app in action.

