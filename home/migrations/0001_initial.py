# Generated by Django 4.2.4 on 2023-08-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pessoa',
            fields=[
                ('pes_cod', models.BigAutoField(primary_key=True, serialize=False)),
                ('pes_cpf', models.CharField(blank=True, max_length=19, null=True)),
                ('pes_rg', models.CharField(blank=True, max_length=19, null=True)),
                ('pes_emissor', models.CharField(blank=True, max_length=19, null=True)),
                ('pes_nascimento', models.CharField(blank=True, max_length=19, null=True)),
                ('pes_telefone1', models.CharField(blank=True, max_length=19, null=True)),
                ('pes_telefone2', models.CharField(blank=True, max_length=19, null=True)),
                ('pes_inscricao_estadual', models.CharField(blank=True, max_length=50, null=True)),
                ('pes_celular', models.CharField(blank=True, max_length=19, null=True)),
                ('pes_cep', models.CharField(blank=True, max_length=19, null=True)),
                ('pes_cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('pes_enreco', models.CharField(blank=True, max_length=50, null=True)),
                ('pes_bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('pes_complemento', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pessoa_juridica',
            fields=[
                ('pjuri_cod', models.BigAutoField(primary_key=True, serialize=False)),
                ('pjuri_razao', models.CharField(blank=True, max_length=100, null=True)),
                ('pjuri_nome', models.CharField(blank=True, max_length=100, null=True)),
                ('pjuri_cnpj', models.CharField(blank=True, max_length=19, null=True)),
                ('pjuri_inscricao_estadual', models.CharField(blank=True, max_length=50, null=True)),
                ('pjuri_telefone1', models.CharField(blank=True, max_length=19, null=True)),
                ('pjuri_telefone2', models.CharField(blank=True, max_length=19, null=True)),
                ('pjuri_celular', models.CharField(blank=True, max_length=19, null=True)),
                ('pjuri_cep', models.CharField(blank=True, max_length=19, null=True)),
                ('pjuri_cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('pjuri_enreco', models.CharField(blank=True, max_length=50, null=True)),
                ('pjuri_bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('pjuri_complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('pjuri_responsavel_nome', models.CharField(blank=True, max_length=100, null=True)),
                ('pjuri_responsavel_email', models.CharField(blank=True, max_length=100, null=True)),
                ('pjuri_email', models.CharField(blank=True, max_length=100, null=True)),
                ('pjuri_tipo', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
