class RichMaximumException(Exception):
    def __init__(self, group_number):
        self.group_number = group_number

    def __str__(self):
       return f"ERROR! The maximum amount for group {self.group_number} students is reached."