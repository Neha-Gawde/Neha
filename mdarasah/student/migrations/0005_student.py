# Generated by Django 3.0.8 on 2020-07-27 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parent', '0001_initial'),
        ('student', '0004_auto_20200727_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentClass', to='student.Class')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentParent', to='parent.Parent')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentSection', to='student.Section')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Studentuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
