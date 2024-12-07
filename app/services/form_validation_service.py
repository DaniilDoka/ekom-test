import re
from app.repositories.form_validation_repository import FormValidationRepository

class FormValidationService:
    def __init__(self, repo: FormValidationRepository):
        self.repo = repo
        self.patterns = {
            'phone': r'^\+7 \d{3} \d{3} \d{2} \d{2}$',
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'date': r'^(?:(\d{2}\.\d{2}\.\d{4})|(\d{4}-\d{2}-\d{2}))$'
        }

    def __check_type(self, arg) -> str:
        if isinstance(arg, str):
            for t, p in self.patterns.items():
                if re.match(p, arg):
                    return t
            return 'text'
        return None

    def get_types(self, body: dict) -> dict:
        result = {}
        for k, v in body.items():
            t = self.__check_type(v)
            result[k] = t
        return result

    def get_form_name(self, types: dict) -> str:
        form_name = None
        for form in self.repo.get_forms():
            has = True
            for k, v in form.items():
                if k in ('_id', 'name'):
                    continue
                if v not in types.values():
                    has = False
                    break
            if has:
                form_name = form['name']
                break
        return form_name
