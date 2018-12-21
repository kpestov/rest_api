from wtforms import Form, StringField, TextAreaField


class ItemForm(Form):
    name = StringField('Title')
    body = TextAreaField('Body')