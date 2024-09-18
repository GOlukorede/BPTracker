# BP_TRACKER - Blood Pressure Monitoring App

## Introduction

**BP_TRACKER** is a comprehensive web-based application designed to help users monitor and track their blood pressure levels. With features such as user authentication, input of blood pressure data, graphical representations of blood pressure trends over time, and health status analysis, this app provides a simple and effective way for users to maintain their cardiovascular health.

Users can log in, view past records, track trends, and receive real-time feedback on whether their blood pressure is high, low, or normal. The application is built with Flask, SQLAlchemy, and uses modern web technologies for an intuitive and responsive experience.

## Deployed Application

You can access the live version of the app at: [BP_TRACKER Deployed Site](#)

Read more about the project in our final blog post: [Project Blog Article](#)

Author: [Olukorede Samson Gbenga](#https://www.linkedin.com/in/GOlukorede)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bp_tracker.git
   cd bp_tracker
   ```
2. Create a virtual environment and activate it:

   ```python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required dependencies:
   pip install -r requirements.txt

3. Set up the environment variables by creating a .env file:

   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   DATABASE_URL=sqlite:///bp_tracker.db # Or your preferred database
   ```

4. Initialize the database:

   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the Flask application:
   ```
   flask run
   ```

## Usage

1. Sign up and log in to your account.
2. Input your blood pressure readings, including systolic, diastolic, and pulse rate
3. View your blood pressure trends over time through graphs and charts.
4. Receive health status feedback (normal, high, or low blood pressure) after submitting data.
5. Access your history of blood pressure readings and detailed reports.

## Contributing

1. Fork the repository.

2. Create a feature branch:

```git checkout -b feature/new-feature

```

3. Commit your changes:

`git commit -m 'Add some feature'`

4. Push the branch to your fork

```
git push origin feature/new-feature
```

5. Create a pull request.
   For major changes, please open an issue first to discuss what you would like to improve.

## Related Projects

1. Flask
2. SQLAlchemy
3. Flask-RESTful

## License

---

Ensure you replace the placeholders (`#link-to-deployed-site`, `#link-to-blog-article`, `#link-to-your-linkedin-profile`, etc.) with actual links.

This template covers all the essential sections required for a professional `README.md` file.
