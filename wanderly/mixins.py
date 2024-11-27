class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():
            placeholder = field.widget.attrs.get('placeholder') or field.label or field_name.replace('_', ' ').capitalize()
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()