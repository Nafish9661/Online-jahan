# Generated by Django 5.0.6 on 2024-06-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfs', '0013_customuser_assign_to_alter_multi_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Assign_To',
            field=models.CharField(choices=[('Gopalganj', 'Gopalganj'), ('Siwan', 'Siwan'), ('Patna', 'Patna'), ('Champaran', 'Champaran'), ('Motihari', 'Motihari'), ('Chhapra', 'Chhapra'), ('Aurangabad', 'Aurangabad'), ('Gaya', 'Gaya'), ('Sasaram', 'Sasaram')], default='Gopalganj', max_length=15),
        ),
    ]
