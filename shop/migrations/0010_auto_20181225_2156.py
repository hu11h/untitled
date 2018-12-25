# Generated by Django 2.1.3 on 2018-12-25 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20181225_2059'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='markett',
            new_name='market',
        ),
        migrations.AlterModelOptions(
            name='market',
            options={'ordering': ('name',), 'verbose_name': 'market', 'verbose_name_plural': 'markets'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='store',
        ),
        migrations.AddField(
            model_name='category',
            name='market',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='market', to='shop.market'),
            preserve_default=False,
        ),
    ]
