# Generated by Django 3.2 on 2021-05-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_quiz_answer_poll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerchoice',
            name='selected',
        ),
        migrations.AddField(
            model_name='answerquestion',
            name='text',
            field=models.CharField(blank=True, max_length=4096),
        ),
    ]
