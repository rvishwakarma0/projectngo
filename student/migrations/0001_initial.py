# Generated by Django 3.0.4 on 2020-04-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('rollno', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('pic', models.ImageField(blank='False', upload_to='student_profile_pics')),
                ('fname', models.CharField(blank='False', max_length=50)),
                ('lname', models.CharField(blank='False', max_length=50)),
                ('age', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=50)),
                ('mothername', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('school', models.CharField(max_length=50)),
                ('sclass', models.IntegerField(blank='False', choices=[('1', 1), ('8', 8), ('2', 2), ('9', 9), ('3', 3), ('10', 10), ('4', 4), ('11', 11), ('5', 5), ('12', 12), ('6', 6), ('7', 7)], default='5')),
            ],
        ),
    ]
