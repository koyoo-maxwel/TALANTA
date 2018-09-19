from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField ,ValidationError ,FileField 
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Comment')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Update') 

class TalentForm(FlaskForm):
    title = StringField('Title',validators = [Required()])
    category = SelectField('Category', choices=[('Music','Music'),('Art & Craft','Art & Craft'),('Sports','Sports'),('Creativity','Creativity'),('other','other')])
    description = TextAreaField('Description')
    image_file = FileField('Upload Video',validators = [Required()])
    submit = SubmitField('Talanta')
