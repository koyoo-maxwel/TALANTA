from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField , ValidationError 
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Comment')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Update') 

class TalentForm(FlaskForm):
    category = SelectField('Category', choices=[('Music','Music'),('Art & Craft','Art & Craft'),('Sports','Sports'),('Creativity','Creativity'),('other','other')])
    content = TextAreaField('Description')
    submit = SubmitField('Talanta')
