from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 

class TalentForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Music'), ('2', 'Sports'), ('3', 'Entertainment'),('4','Other')])
    content = TextAreaField('YOUR TALENT')
    submit = SubmitField('Post Your Talent')

class UpvoteForm(FlaskForm):
    '''
    Class to create a wtf form for upvoting a talent
    '''
    submit = SubmitField('Upvote')
    
