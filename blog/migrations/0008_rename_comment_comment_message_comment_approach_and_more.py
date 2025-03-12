# Generated by Django 5.1.6 on 2025-03-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_email_comment_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='message',
        ),
        migrations.AddField(
            model_name='comment',
            name='approach',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True),
        ),
    ]
