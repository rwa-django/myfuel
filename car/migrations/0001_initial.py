# Generated by Django 2.1.3 on 2019-02-11 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle_Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Fuel_Pos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.SmallIntegerField(default=1)),
                ('booked', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('amount', models.DecimalField(decimal_places=2, help_text='Kosten', max_digits=10)),
                ('km', models.PositiveSmallIntegerField(default=0, help_text='KM Stand')),
                ('liter', models.DecimalField(decimal_places=2, default=0, help_text='Liter', max_digits=10)),
                ('info', models.CharField(help_text='Buchungs Info', max_length=200)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Vehicle_Fuel')),
            ],
            options={
                'ordering': ['car_id', 'pos'],
            },
        ),
        migrations.CreateModel(
            name='Vehicle_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
                ('type', models.CharField(default='CAR', help_text='Type', max_length=10)),
                ('pos', models.SmallIntegerField(default=1)),
                ('aktiv', models.BooleanField(default=False, help_text='Aktiv')),
                ('label', models.CharField(help_text='Beschreibung', max_length=200)),
            ],
            options={
                'ordering': ['login', 'pos'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='vehicle_type',
            unique_together={('login', 'type', 'pos')},
        ),
        migrations.AddField(
            model_name='vehicle_fuel',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='car.Vehicle_Type'),
        ),
        migrations.AlterUniqueTogether(
            name='vehicle_fuel_pos',
            unique_together={('car_id', 'pos')},
        ),
        migrations.AlterUniqueTogether(
            name='vehicle_fuel',
            unique_together={('login', 'type')},
        ),
    ]
