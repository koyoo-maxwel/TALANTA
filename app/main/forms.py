from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField , ValidationError , FileField
from wtforms.validators import Required
import imghdr

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


class UploadForm(FlaskForm):
    image_file = FileField('Image file')
    submit = SubmitField('Submit')

    def validate_image_file(self, field):
        if field.data.filename[-4:].lower() != '.jpg':
            raise ValidationError('Invalid file extension')
        if imghdr.what(field.data) != 'jpeg':
            raise ValidationError('Invalid image format')
