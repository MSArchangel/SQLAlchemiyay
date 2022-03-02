from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, TextAreaField, StringField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Текст нвости:')
    is_private = BooleanField('Личная новость')
    submit = SubmitField('Применить')
