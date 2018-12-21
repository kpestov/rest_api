from wtforms import Form, StringField, TextAreaField


class Itemform(Form):
    title = StringField('Title')
    body = TextAreaField('Body')