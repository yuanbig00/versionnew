# Generated by Django 2.0 on 2019-12-20 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255, verbose_name='事件名称')),
                ('event_description', models.CharField(max_length=255, verbose_name='事件简介')),
                ('time', models.DateField(verbose_name='事件事时间')),
                ('neutral_remark', models.IntegerField(verbose_name='中性评论')),
                ('positive_remark', models.IntegerField(verbose_name='积极评论')),
                ('negative_remark', models.IntegerField(verbose_name='消极评论')),
                ('comment', models.IntegerField(null=True, verbose_name='评论量')),
                ('transmit', models.IntegerField(null=True, verbose_name='转发量')),
                ('follow', models.IntegerField(null=True, verbose_name='点赞量')),
                ('famale', models.IntegerField(verbose_name='女性')),
                ('male', models.IntegerField(verbose_name='男性')),
                ('age_05', models.IntegerField(verbose_name='05后')),
                ('age_00', models.IntegerField(verbose_name='00后')),
                ('age_95', models.IntegerField(verbose_name='95后')),
                ('age_90', models.IntegerField(verbose_name='90后')),
                ('age_85', models.IntegerField(verbose_name='85后')),
                ('hot', models.IntegerField(null=True, verbose_name='热度')),
            ],
            options={
                'verbose_name': '事件',
                'verbose_name_plural': '事件',
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='past_hours_hot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('past_onehour_hot', models.IntegerField(verbose_name='过去一小时的热度')),
                ('past_twohour_hot', models.IntegerField(verbose_name='过去两小时的热度')),
                ('past_threehour_hot', models.IntegerField(verbose_name='过去三小时的热度')),
                ('past_fourhour_hot', models.IntegerField(verbose_name='过去四小时的热度')),
                ('past_fivehour_hot', models.IntegerField(verbose_name='过去五小时的热度')),
                ('past_sixhour_hot', models.IntegerField(verbose_name='过去六小时的热度')),
            ],
            options={
                'verbose_name': '事件热度',
                'verbose_name_plural': '事件热度',
                'db_table': 'past_hours_hot',
            },
        ),
        migrations.CreateModel(
            name='person_remarks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person1_name', models.CharField(max_length=255, verbose_name='用户1')),
                ('person1_remark', models.CharField(max_length=255, verbose_name='评论1')),
                ('person1_pic', models.CharField(max_length=255, verbose_name='用户头像')),
                ('person2_name', models.CharField(max_length=255, verbose_name='用户2')),
                ('person2_remark', models.CharField(max_length=255, verbose_name='评论2')),
                ('person2_pic', models.CharField(max_length=255, verbose_name='用户头像')),
                ('person3_name', models.CharField(max_length=255, verbose_name='用户3')),
                ('person3_remark', models.CharField(max_length=255, verbose_name='评论3')),
                ('person3_pic', models.CharField(max_length=255, verbose_name='用户头像')),
                ('person4_name', models.CharField(max_length=255, verbose_name='用户4')),
                ('person4_remark', models.CharField(max_length=255, verbose_name='评论4')),
                ('person4_pic', models.CharField(max_length=255, verbose_name='用户头像')),
                ('person5_name', models.CharField(max_length=255, verbose_name='用户5')),
                ('person5_remark', models.CharField(max_length=255, verbose_name='评论5')),
                ('person5_pic', models.CharField(max_length=255, verbose_name='用户头像')),
                ('person6_name', models.CharField(max_length=255, verbose_name='用户6')),
                ('person6_remark', models.CharField(max_length=255, verbose_name='评论6')),
                ('person6_pic', models.CharField(max_length=255, verbose_name='用户头像')),
            ],
            options={
                'verbose_name': '人员评论',
                'verbose_name_plural': '人员评论',
                'db_table': 'person_remarks',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AddField(
            model_name='events',
            name='past_hour_hot',
            field=models.ForeignKey(default=50, on_delete=django.db.models.deletion.CASCADE, to='front.past_hours_hot', verbose_name='过去一小时热度'),
        ),
        migrations.AddField(
            model_name='events',
            name='relative_person_remark',
            field=models.ForeignKey(default=50, on_delete=django.db.models.deletion.CASCADE, to='front.person_remarks', verbose_name='评论数'),
        ),
    ]
