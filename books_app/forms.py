from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import Audience, Book, Author, Genre

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    publish_date = DateField('Date Published', validators=[DataRequired()])
    author = QuerySelectField('Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')

    def validate_title(self, field):
        if field.data is None:
            raise ValidationError('Title is required')
        
    def validate_publish_date(self, field):
        if field.data > date.today():
            raise ValidationError('Publish date cannot be in the future')
    
    def validate_author(self, field):
        if field.data is None:
            raise ValidationError('Author must be selected')
    
    def validate_genres(self, field):
        if len(field.data) < 1:
            raise ValidationError('At least one genre must be selected')
    
    

class AuthorForm(FlaskForm):
    """Form to create an author."""
    name = StringField('Author Name', validators=[DataRequired()])
    biography = StringField('Biography', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        if field.data is None:
            raise ValidationError('Name is required')
    
    def validate_biography(self, field):
        if field.data is None:
            raise ValidationError('Biography is required')


class GenreForm(FlaskForm):
    """Form to create a genre."""
    name = StringField('Genre Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        if field.data is None:
            raise ValidationError('Name is required')