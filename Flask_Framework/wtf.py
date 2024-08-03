from flask import Flask, render_template, redirect, url_for, flash, request, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pramod@123'  # Replace with a strong secret key

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create a PDF in memory
        pdf_buffer = BytesIO()
        c = canvas.Canvas(pdf_buffer, pagesize=letter)
        c.drawString(100, 750, f"Username: {form.username.data}")
        c.drawString(100, 730, f"Email: {form.email.data}")
        c.drawString(100, 710, "Password: (hidden)")
        c.drawString(100, 690, "Confirm Password: (hidden)")
        c.save()
        pdf_buffer.seek(0)
        
        return send_file(pdf_buffer, as_attachment=True, download_name='registration.pdf', mimetype='application/pdf')
    return render_template('form.html', form=form)

@app.route("/")
def home():
    return "Home Page"

if __name__ == '__main__':
    app.run(debug=True)
