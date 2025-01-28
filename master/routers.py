class SchemaRouter:
    """
    A router to control all database operations for models in different schemas.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read models in sgrh or arquivos.
        """
        if model._meta.db_table.startswith('sgrh'):
            return 'default'  # Could route to a separate DB if necessary
        if model._meta.db_table.startswith('arquivos'):
            return 'default'  # Could route to a separate DB if necessary
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write models in sgrh or arquivos.
        """
        if model._meta.db_table.startswith('sgrh'):
            return 'default'
        if model._meta.db_table.startswith('arquivos'):
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations between models in the same schema.
        """
        if obj1._meta.db_table.startswith('sgrh') and obj2._meta.db_table.startswith('sgrh'):
            return True
        if obj1._meta.db_table.startswith('arquivos') and obj2._meta.db_table.startswith('arquivos'):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the migration occurs for models in their respective schema.
        """
        if model_name in ['product', 'customer']:  # Or use specific app_label/model_name
            return True
        return None
