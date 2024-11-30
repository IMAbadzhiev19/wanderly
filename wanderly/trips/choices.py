from django.db import models

class CategoryChoices(models.TextChoices):
    FOOD = 'food', 'Food & Dining'
    TRANSPORT = 'transport', 'Transport'
    ACCOMMODATION = 'accommodation', 'Accommodation'
    ENTERTAINMENT = 'entertainment', 'Entertainment'
    SHOPPING = 'shopping', 'Shopping'
    OTHER = 'other', 'Other'


class ActivityChoices(models.TextChoices):
    SIGHTSEEING = 'sightseeing', 'Sightseeing'
    DINING = 'dining', 'Dining'
    ADVENTURE = 'adventure', 'Adventure'
    RELAXATION = 'relaxation', 'Relaxation'
    SHOPPING = 'shopping', 'Shopping'


class NoteCategoryChoices(models.TextChoices):
    GENERAL = 'general', 'General'
    PACKING = 'packing', 'Packing'
    REMINDER = 'reminder', 'Reminder'
    FEEDBACK = 'feedback', 'Feedback'
