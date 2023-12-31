# Generated by Django 3.2.22 on 2023-11-25 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distribution_number', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=40)),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('gender', models.CharField(blank=True, max_length=80, null=True)),
                ('date_of_birth', models.DateTimeField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('sum_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('original_acquisition', models.TextField(default='')),
                ('stripe_pid', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineObject_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineobjects', to='checkout.customer_order')),
            ],
        ),
    ]
