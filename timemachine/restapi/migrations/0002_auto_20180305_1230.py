# Generated by Django 2.0.2 on 2018-03-05 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=200)),
                ('inputs', models.TextField(default='[]')),
                ('outputs', models.TextField(default='[]')),
            ],
        ),
        migrations.RemoveField(
            model_name='problem',
            name='solution',
        ),
        migrations.AlterField(
            model_name='problem',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restapi.User'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Problem'),
        ),
    ]