# Generated by Django 4.2.7 on 2023-11-17 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('class_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('government_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.government')),
            ],
        ),
        migrations.CreateModel(
            name='UnionExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=10)),
                ('password_hash', models.CharField(max_length=50)),
                ('role_number', models.IntegerField(choices=[(1, '政府'), (2, '学校'), (3, '老师')])),
            ],
        ),
        migrations.CreateModel(
            name='UnionExamScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.unionexam')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('class_room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.classroom')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.school'),
        ),
    ]
