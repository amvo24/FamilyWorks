# Generated by Django 3.2.4 on 2024-06-28 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0006_alter_invitation_expiry_date'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='family',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.family'),
            preserve_default=False,
        ),
    ]
