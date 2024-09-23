# Description: This file contains the routes for the application.

from tracker import app, db
from flask import render_template, redirect, url_for, flash
from tracker.form import RegisterForm, DataForm, LoginForm
from tracker.model import User, Data
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/home')
@login_required
def home_page():
    # The home_page function is used to render the home page. It is used to check if the user is logged in. It is used to return the home page template.
    return render_template('home.html')

@app.route('/')
@app.route('/landing')
def landing_page():
    # The landing_page function is used to render the landing page. It is used to return the landing page template.
    return render_template('index.html')

@app.route('/about')
def about_page():
    # The about_page function is used to render the about page. It is used to return the about page template.
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    # The login_page function is used to render the login page. It is used to validate the login form. It is used to check if the user exists in the database. It is used to log in the user and redirect to the home page. It is used to display the error message if the user does not exist.
    form = LoginForm()
    # Check if the form is validated
    if form.validate_on_submit():
        # Check if the user exists in the database
        user_email = User.query.filter_by(email=form.email.data).first()
        if user_email and user_email.check_password(form.password.data):
            # Log in the user
            login_user(user_email)
            # flash(f'Welcome,  {user_email.firstname}!', category='success')
            return redirect(url_for('home_page'))
        else:
            # Display the error message if the user does not exist
            flash('Invalid email or password. Please try again.', category='danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    # The register_page function is used to render the registration page. It is used to validate the registration form. It is used to create a new user and add it to the database. It is used to log in the user and redirect to the home page. It is used to display the error message if the form is not validated.
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password_hash=form.password1.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f'Account created for {form.firstname.data}!', category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for error in form.errors.values():
            flash(f'There was an error with creating a account: {error}', category='danger')
    return render_template('registration.html', form=form)

@app.route('/logout')
def logout_page():
    # The logout_page function is used to log out the user. It is used to flash the logout message. It is used to redirect to the landing page.
    logout_user()
    flash("You have been logged out.", category='info')
    return redirect(url_for('landing_page'))



@app.route('/data', methods=['GET', 'POST'])
@login_required
def data_page():
    # The data_page function is used to render the data page. It is used to validate the data form. It is used to add the blood pressure data to the database. It is used to determine the blood pressure category. It is used to flash the blood pressure category.
    form = DataForm()
    if form.validate_on_submit():
        data = Data(systolic=form.systolic.data, diastolic=form.diastolic.data, pulse=form.pulse.data, user_id=current_user.id)
        db.session.add(data)
        db.session.commit()
        
        # Get the systolic and diastolic values
        systolic_value = form.systolic.data
        diastolic_value = form.diastolic.data
        
        # Logic to determine the blood pressure category
        def determine_bp(systolic, diastolic):
            # Determine the blood pressure category based on the systolic and diastolic values
            if systolic < 90 and diastolic < 60:
                return '''
              <h3>Below is your result!</h3> </br>
              <h2>Your blood pressure is LOW: HYPOTENSION!</h2>'
<h3>Recommendations for managing low blood pressure</h3>
<p>
  While low blood pressure is often less concerning than high blood pressure,
  it is important to manage it effectively to avoid discomfort and prevent any
  potential complications. By following these recommendations and working
  closely with your healthcare provider, you can maintain healthy blood pressure
  levels and overall well-being
</p>
<ul>
  <li>Cautiously increase salt intake</li>
  <li>Drink more fluids</li>
  <li>Eat small frequent meals</li>
  <li>Engage in regular exercise: To improve blood circulation</li>
  <li>
    Rise slowly: Standing up quickly can cause sudden drop in blood pressure
  </li>
  <li>Avoid alcohol: It causes dehydration</li>
  <li>Monitor your blood pressure regularly</li>
  <li>Consult your doctor</li>
</ul>'''
            elif systolic < 120 and diastolic < 80:
                return '''
            <h3>Below is your result!</h3> </br>
            <h2>Normal Blood Pressure</h2>
<h3>Normal Blood Pressure Recommendations</h3>
<p>
  Congratulations! Your blood pressure is within the normal range, which is an
  excellent indicator of your cardiovascular health. Maintaining normal blood
  pressure is crucial for preventing long-term health issues. Here are some
  recommendations to help you keep your blood pressure at a healthy level
</p>
<ul>
  <li>Maintain a Balanced Diet</li>
  <li>Stay Physically Active</li>
  <li>Maintain a Healthy Weight</li>
  <li>Limit Alcohol Consumption</li>
  <li>Avoid Smoking</li>
  <li>Manage Stress</li>
  <li>Get Adequate Sleep</li>
  <li>Stay hydrated</li>
</ul>
            '''
            
            elif systolic < 130 and diastolic < 80:
                return '''
            <h3>Below is your result!</h3> </br>
            <h2>Elevated Blood Pressure: Pre-hypertension</h2>
<h3>Recommendations for managing elevated blood pressure</h3>
<p>
  Managing elevated blood pressure is crucial to preventing the development of
  hypertension and reducing the risk of heart disease, stroke, and other
  complications. By following these recommendations and working closely with
  your healthcare provider, you can effectively manage your blood pressure and
  maintain long-term heart health
</p>
<ul>
  <li>Reduce Sodium Intake</li>
  <li>Increase Potassium Intake</li>
  <li>Limit Saturated and Trans Fats</li>
  <li>Increase Physical Activity</li>
  <li>Maintain a Healthy Weight</li>
  <li>Limit Alcohol Consumption</li>
  <li>Quit Smoking</li>
  <li>Manage Stress</li>
  <li>Monitor Your Blood Pressure at Home</li>
  <li>Limit Caffeine</li>
  <li>Consult your doctor</li>
</ul>
            '''
            
            elif systolic < 140 and diastolic < 90:
                return '''
            <h3>Below is your result!</h3> </br>
            <h2>Elevated Blood Pressure: Stage 1 Hypertension</h2>
<h3>Recommendations for managing stage 1 hypertension</h3>
<p>
  Managing hypertension Stage 1 is crucial for reducing the risk of serious
  health complications. By following these recommendations, adopting
  heart-healthy habits, and working closely with your healthcare provider, you
  can effectively control your blood pressure and enhance your overall
  well-being.
</p>
<ul>
  <li>Reduce Sodium and increase Potassium Intake</li>
  <li>Limit Saturated and Trans Fats</li>
  <li>Increase Physical Activity</li>
  <li>Maintain a Healthy Weight</li>
  <li>Limit Alcohol Consumption</li>
  <li>Quit Smoking</li>
  <li>Reduce Stress</li>
  <li>Monitor Your Blood Pressure at Home</li>
  <li>Highly limit Caffeine</li>
  <li>Consult your doctor</li>
</ul>
            '''
            
            elif systolic < 180 and diastolic < 120:
                return '''
            <h3>Below is your result!</h3> </br>
            <h2>Elevated Blood Pressure: Stage 2 Hypertension</h2>
<h3>Recommendations for managing stage 2 hypertension</h3>
<p>
  Managing hypertension Stage 2 is crucial for reducing the risk of serious
  health complications. By following these recommendations, adopting
  heart-healthy habits, and working closely with your healthcare provider, you
  can effectively control your blood pressure and enhance your overall
  well-being.
</p>
<ul>
  <li>Reduce Sodium and Increase Intake</li>
  <li>Adopt a More Restrictive Heart-Healthy Diet</li>
  <li>Increase Physical Activity Significantly</li>
  <li>Achieve and Maintain a Healthy Weight</li>
  <li>Strictly Limit Alcohol and Avoid Smoking Entirely</li>
  <li>Medication is Typically Required</li>
  <li>Frequent Monitoring and Doctor Visits</li>
  <li>Manage Stress</li>
</ul>
            '''
            
            else:
                return '''
            <h3>Below is your result!</h3> </br>
            <h2>Hypertensive Emergency!</h2>
<h3>Immediate Actions During a Hypertensive Crisis</h3>
<p>
  A hypertensive crisis is a serious medical condition that requires immediate
  attention and long-term management. By understanding the causes, recognizing
  the symptoms, and adhering to a strict treatment plan, you can effectively
  manage your condition and reduce the risk of life-threatening complications.
  Always work closely with your healthcare provider to tailor a treatment plan
  specific to your needs and to ensure the best possible outcome.
</p>
<ul>
  <li>Seek Emergency Medical Care Immediately!</li>
  <li>Do Not Attempt to Self-Treat</li>
  <li>Strict Adherence to Medication Regimen</li>
  <li>Intensive Lifestyle Modifications</li>
  <li>Home Blood Pressure Monitoring</li>
  <li>Addressing Comorbid Conditions</li>
</ul>
            '''
            
        
            
         # Get the blood pressure category
        category = determine_bp(systolic_value, diastolic_value)
        # Flash the category of the blood pressure
        flash(category, category='bp_result')
    return render_template('data.html', form=form)

@app.route('/history')
@login_required
def history_page():
    # The history_page function is used to render the history page. It is used to query the blood pressure data from the database. It is used to return the blood pressure data to the history page template.
    return render_template('history.html')