# Generated by Django 4.2.5 on 2023-09-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_testme_alter_client_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donneeecg',
            name='sante_patient',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True, verbose_name='etat patient'),
        ),
    ]
