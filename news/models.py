from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Column(models.Model):
    name = models.CharField('栏目名称', max_length = 256)
    slug = models.CharField('栏目网址', max_length = 256)
    intro = models.TextField('栏目简介', default = '')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']   #按照哪个栏目排序


class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name = '归属栏目')
    title = models.CharField('标题', max_length = 256)
    slug = models.CharField('网址', max_length = 256, db_index = True)

    author = models.ForeignKey('auth.User', blank = True, null = True, verbose_name = '作者')
    #null = True 数据库范畴，将空值存储为空
    #如果希望表单中允许空值，属于表单范畴，还要设置blank = True，表单验证时允许输入空值
    content = models.TextField('内容', default='', blank = True)

    published = models.BooleanField('正式发布', default = True) #true/false字段，默认值为none

    pub_date = models.DateTimeField('发表时间', auto_now_add = True, editable = True)
    update_time = models.DateTimeField('更新时间', auto_now = True, null = True)
    #DateField.auto_now 每次保存对象时，自动设置该字段为当前时间，用于最后一次修改时间戳，覆盖
    #DateField.auto_now_add 对象第一次被创建时自动设置当前时间，用于创建时间的时间戳


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'
