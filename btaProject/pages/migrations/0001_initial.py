# Generated by Django 4.1.1 on 2022-12-28 16:41

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('assigned_personnel', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('project_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='managed_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], max_length=50)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN', max_length=50)),
                ('type', models.CharField(choices=[('BUG/ERROR', 'Bug/Error'), ('NEW FEATURE', 'New Feature'), ('ENHANCEMENT', 'Ehancement'), ('CHANGE', 'Change')], max_length=50)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('assigned_developer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assigned_tickets', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='pages.project')),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('ASSIGNED_TO_USER', 'Assigned to User'), ('STATUS_UPDATED', 'Status Updated'), ('PRIORITY_CHANGED', 'Priority Changed')], max_length=50)),
                ('prev_value', models.CharField(blank=True, max_length=50, null=True)),
                ('new_value', models.CharField(max_length=50)),
                ('date_changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='pages.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='TicketFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='pages.ticket')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pages.ticket')),
            ],
        ),
    ]
