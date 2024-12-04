from django.db import models

class CategoryChoices(models.TextChoices):
    FOOD = 'Food & Dining', 'Food & Dining'
    TRANSPORT = 'Transport', 'Transport'
    ACCOMMODATION = 'Accommodation', 'Accommodation'
    ENTERTAINMENT = 'Entertainment', 'Entertainment'
    SHOPPING = 'Shopping', 'Shopping'
    OTHER = 'Other', 'Other'


class ActivityChoices(models.TextChoices):
    SIGHTSEEING = 'Sightseeing', 'Sightseeing'
    DINING = 'Dining', 'Dining'
    ADVENTURE = 'Adventure', 'Adventure'
    RELAXATION = 'Relaxation', 'Relaxation'
    SHOPPING = 'Shopping', 'Shopping'


class NoteCategoryChoices(models.TextChoices):
    GENERAL = 'General', 'General'
    PACKING = 'Packing', 'Packing'
    REMINDER = 'Reminder', 'Reminder'
    FEEDBACK = 'Feedback', 'Feedback'
