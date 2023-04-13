# Generated by Django 4.1.7 on 2023-04-13 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioPsicologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentariosPsicologia', to='AppCoder.plan_psicologia_deportiva')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
        migrations.CreateModel(
            name='ComentarioPreparacionFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentariosPreparacionFisca', to='AppCoder.plan_preparacion_fisica')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
        migrations.CreateModel(
            name='ComentarioNutricion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentariosNutricion', to='AppCoder.plan_nutricion')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
        migrations.CreateModel(
            name='ComentarioMedicina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentariosMedicina', to='AppCoder.plan_medicina_deportiva')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
        migrations.CreateModel(
            name='ComentarioKinesiologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentariosKinesiologia', to='AppCoder.plan_kinesiologia_fisioterapia')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
    ]