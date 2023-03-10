# Generated by Django 3.2.12 on 2022-09-26 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0032_alter_register_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='alamat_lembaga',
        ),
        migrations.RemoveField(
            model_name='register',
            name='alamat_sekolah',
        ),
        migrations.RemoveField(
            model_name='register',
            name='anak_ke',
        ),
        migrations.RemoveField(
            model_name='register',
            name='bahasa',
        ),
        migrations.RemoveField(
            model_name='register',
            name='berat_badan',
        ),
        migrations.RemoveField(
            model_name='register',
            name='golongan_darah',
        ),
        migrations.RemoveField(
            model_name='register',
            name='kelas',
        ),
        migrations.RemoveField(
            model_name='register',
            name='keterangan_sekolah',
        ),
        migrations.RemoveField(
            model_name='register',
            name='masuk_lembaga',
        ),
        migrations.RemoveField(
            model_name='register',
            name='nama_panggilan',
        ),
        migrations.RemoveField(
            model_name='register',
            name='pekerjaan_wali',
        ),
        migrations.RemoveField(
            model_name='register',
            name='pendidikan_ayah',
        ),
        migrations.RemoveField(
            model_name='register',
            name='pendidikan_ibu',
        ),
        migrations.RemoveField(
            model_name='register',
            name='pendidikan_wali',
        ),
        migrations.RemoveField(
            model_name='register',
            name='penghasilan_ayah',
        ),
        migrations.RemoveField(
            model_name='register',
            name='penghasilan_ibu',
        ),
        migrations.RemoveField(
            model_name='register',
            name='penghasilan_wali',
        ),
        migrations.RemoveField(
            model_name='register',
            name='riwayat_ayah',
        ),
        migrations.RemoveField(
            model_name='register',
            name='riwayat_ibu',
        ),
        migrations.RemoveField(
            model_name='register',
            name='riwayat_wali',
        ),
        migrations.RemoveField(
            model_name='register',
            name='saudara_angkat',
        ),
        migrations.RemoveField(
            model_name='register',
            name='saudara_kandung',
        ),
        migrations.RemoveField(
            model_name='register',
            name='saudara_tiri',
        ),
        migrations.RemoveField(
            model_name='register',
            name='status_anak',
        ),
        migrations.RemoveField(
            model_name='register',
            name='tanggal_daftar',
        ),
        migrations.RemoveField(
            model_name='register',
            name='tempat_kelahiran_ayah',
        ),
        migrations.RemoveField(
            model_name='register',
            name='tempat_kelahiran_ibu',
        ),
        migrations.RemoveField(
            model_name='register',
            name='tempat_kelahiran_wali',
        ),
        migrations.RemoveField(
            model_name='register',
            name='tgl_lahir_ayah',
        ),
        migrations.RemoveField(
            model_name='register',
            name='tgl_lahir_ibu',
        ),
        migrations.RemoveField(
            model_name='register',
            name='tgl_lahir_wali',
        ),
        migrations.RemoveField(
            model_name='register',
            name='tinggi_badan',
        ),
        migrations.RemoveField(
            model_name='register',
            name='wali',
        ),
    ]
