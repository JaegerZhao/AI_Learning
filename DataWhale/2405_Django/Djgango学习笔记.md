# Django框架学习笔记

> Django 是一个使用 Python 编写的开源 Web 应用程序框架，它提供了一套用于快速开发安全、 可扩展和高效的 Web 应用程序的工具和功能。Django 基于 MVC（Model-View-Controller）架构模式，采用了最佳实践，强调代码的可重用性和可维护性。它的设计理念是 DRY（Don't Repeat Yourself）， 通过提供许多内置功能和现成的解决方案，使开发人员能够专注于业务逻辑而不必从头开始构建所有组件。

​	Django 是使用 Python 语言编写的一个广受欢迎且功能完整的服务器端网站框架。我参加了5月份 DataWhale 的 Django 后端入门开发组队学习，课程链接如下 [Django课程链接](https://mp.weixin.qq.com/s/iPmzb72Yk0mhIA2NYezXDg) ，在这里记录一下学习内容。

## 1 Django 环境搭建与项目配置

1. 配置环境

   创建虚拟环境，在教程里采用指令 `python -m venv erp_venv` 创建虚拟环境。而我选择了利用 conda 创建环境。

   ```
   conda create -n django
   ```

   接着运行以上建立的环境。

   ```
   conda activae django
   ```

2. 安装项目依赖包

   - 安装 Django

     ```
     pip install Django==4.2
     ```

     Django 是一个 Python web 框架，提供许多功能，如 ORM、认证、表单、模板等，它可以帮助你更快、更轻松地开发 web 应用程序。

   - 安装 DRF

     ```
     pip install django-filter
     ```

     Django-Filter 是一个基于 Django 的库，它提供了一种简单、灵活的方式来过滤 Django 模型的查询集。Django-Filter 的 API 允许开发者使用简单的查询表达式，构建和应用复杂的过滤器，从而在查询集中选择和排除数据。

   - 安装Django Spectacular

     ```
     pip install drf_spectacular
     ```

     DRF Spectacular 是 DRF 的 OpenAPI 规范工具。它可以自动构建和生成 OpenAPI 规范文档，并提供方便的 API 测试工具，使你能够更加轻松地创建、测试和维护 RESTful API。同时，它也支持集成 Django Filter，允许你通过 URL 参数过滤查询数据。

   - 安装debug_toolbar库

     ```
     pip install django-debug-toolbar
     ```

   - 安装django_.extensions库

     ```
     pip install django_extensions
     ```

   > 还可以使用 `pip install -r requirements.txt` 命令一键安装

3. 创建 Django 项目和 APP

   - 创建项目

     ```
     django-admin startproject djangolearn
     ```

     其中 `djangolearn` 为我创建项目的名字。

   - 创建 APP

     在创建好的 `djangolearn` 文件夹下，有个 `manage.py` 文件，执行以下指令创建 APP。

     ```
     django-admin startapp test
     ```

     其中 `test` 为应用的名字，此时文件夹结构如下。

     ```
     djangolearn
     │  manage.py
     │
     ├─test
     │  │  admin.py
     │  │  apps.py
     │  │  models.py
     │  │  tests.py
     │  │  views.py
     │  │  __init__.py
     │  │
     │  └─migrations
     │          __init__.py
     │
     └─djangolearn
             asgi.py
             settings.py
             urls.py
             wsgi.py
             __init__.py
     ```

   - 参数调整

     更新应用文件下 `apps.py` 文件。将 `testConfig` 类的 `name` 改为 `name = "apps.test"`。

     ```py
     from django.apps import AppConfig
     
     class testConfig(AppConfig):
         default_auto_field = "django.db.models.BigAutoField"
         name = "apps.test"
     ```

4. 设置 `setting.py` 文件

   加入安装的库，与新增的APP。

   ```py
   INSTALLED_APPS = [
       "django.contrib.admin",
       "django.contrib.auth",
       "django.contrib.contenttypes",
       "django.contrib.sessions",
       "django.contrib.messages",
       "django.contrib.staticfiles",
       'apps.test',
       'rest_framework',
       'django_filters',
       'drf_spectacular'
   ]
   ```

5. 启动项目

   运行项目先执行数据库相关操作，再启动 django 项目，在下文将详细讲到数据库迁移。

   - 数据库迁移操作

     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

   - 启动Django服务

     ```
     python manage.py runserver
     ```

     ![image-20240515225509412](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240515225509412.png)

     执行命令后打开链接 `http://127.0.0.1:8000/`，可以看到成功启动Django服务。

     ![image-20240515225742989](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240515225742989.png)

## 2 数据表构建与数据迁移与管理——models.py的应用

​	在 `Django` 中，我们使用 `models.py` 定义数据模型，这些模型代表了应用程序中的数据表。本小节我选择构建作业中的数据，在 `models.py`文件中定义班级和学生模型。

```py
from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

​	这里我们定义了两个模型，`Classroom`和`Student`，并在`Student`模型中通过`ForeignKey`字段关联了`Classroom`模型。

1. 生成迁移脚本

   执行以下命令生成迁移脚本：

   ```bash
   python manage.py makemigrations
   ```

   这个命令会在`test/migrations/`目录下生成一个迁移脚本文件。

2. 执行迁移命令

   执行以下命令将模型应用到数据库中：

   ```bash
   python manage.py migrate
   ```

   这个命令会将迁移脚本应用到数据库中，创建相应的班级和学生表。如果迁移成功，就可以在Django的admin后台管理页面中看到这两个表，并进行增删改查等操作。

   ![image-20240515234413606](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240515234413606.png)

   执行成功后，如上图所示，构建了一个班级和学生的表。

3. 创建管理员

   在终端运行命令

   ```
   python manage.py createsuperuser
   ```

   ![image-20240515234713158](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240515234713158.png)

   登录 admin 后台

   ```
   http://127.0.0.1:8000/admin
   ```

   ![image-20240515234822056](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240515234822056.png)

   输入用户名密码后，成功进入后台。

   ![image-20240515234856992](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240515234856992.png)

## 3 QuerySet 和 Instance 应用