# Generated by Django 2.2.3 on 2019-08-07 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20190807_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='address_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.StudentAddressInfo'),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='guardian_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.GuardianInfo'),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='personal_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.PersonalInfo'),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='previous_academic_certificate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.PreviousAcademicCertificate'),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='previous_academic_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.PreviousAcademicInfo'),
        ),
    ]