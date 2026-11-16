from sqladmin import ModelView


class BaseModelView(ModelView):
    form_excluded_columns = (
        "created_at",
        "updated_at",
    )
