from wtforms import Form, StringField, TextAreaField


class Itemform(Form):
    title = StringField('Name')
    body = TextAreaField('Description')