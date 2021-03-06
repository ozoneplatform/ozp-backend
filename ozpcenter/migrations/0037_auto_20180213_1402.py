# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-13 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ozpcenter', '0036_listing_featured_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_subtype',
            field=models.CharField(choices=[('listing_new', 'listing_new'), ('listing_review', 'listing_review'), ('listing_private_status', 'listing_private_status'), ('pending_deletion_to_owner', 'pending_deletion__to_owner'), ('pending_deletion_to_steward', 'pending_deletion_to_steward'), ('pending_deletion_approved', 'pending_deletion_approved'), ('review_request', 'review_request'), ('subscription_category', 'subscription_category'), ('subscription_tag', 'subscription_tag')], default='system', max_length=36, null=True),
        ),
    ]
