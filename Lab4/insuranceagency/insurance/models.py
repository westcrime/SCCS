from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

from insuranceagency import settings
from django.contrib.auth.models import AbstractUser


class InsuranceCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Вид страхования")
    content = models.TextField(blank=True, verbose_name="Информация об страховании")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    ins_coef = models.FloatField(help_text='Страховой коэффициент услуги (цена объекта * Страховой коэффициент услуги)',
                                 verbose_name='Страховой коэффициент услуги')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('insurance_category', kwargs={'ins_cat_slug': self.slug})

    class Meta:
        verbose_name = 'Виды страхования'
        verbose_name_plural = 'Виды страхования'
        ordering = ['id']


class ObjectOfInsurance(models.Model):
    class InsuredRisks(models.TextChoices):
        HIGH = "Высокие"
        NORMAL = "Нормальные"
        LOW = "Низкие"

    insured_risks = models.CharField(max_length=11, choices=InsuredRisks.choices, default=InsuredRisks.LOW, )
    ins_cat = models.ForeignKey('InsuranceCategory', on_delete=models.PROTECT, verbose_name="Вид страхования")
    cost = models.FloatField(verbose_name='Цена объекта')
    user = models.ForeignKey('User', on_delete=models.SET_DEFAULT, default=None, verbose_name="Владелец объекта")

    class Meta:
        verbose_name = 'Объекты страхования'
        verbose_name_plural = 'Объекты страхования'
        ordering = ['id']


class InsuranceAgent(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя агента")
    total_earning = models.FloatField(help_text='Общий заработок', default=0, verbose_name='Общий заработок')
    last_name = models.CharField(max_length=30, verbose_name="Фамилия агента")
    surname = models.CharField(max_length=30, verbose_name="Отчество агента")
    address = models.CharField(max_length=30, verbose_name="адрес агента")
    phone_regex = RegexValidator(regex=r'^\+37529\d{7}$',
                                 message="Телефонный номер должен быть введен в формате: '+37529xxxxxxx'. Разрешено до 15 цифр")
    phone_number = models.CharField(validators=[phone_regex], unique=True, max_length=17,
                                    blank=True)  # Validators should be a list
    ins_branch = models.ForeignKey('InsuranceBranch', on_delete=models.PROTECT, verbose_name="Филиал страхования")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('insurance_agent', kwargs={'ins_agent_slug': self.slug})

    class Meta:
        verbose_name = 'Страховые агенты'
        verbose_name_plural = 'Страховые агенты'
        ordering = ['id']


class InsuranceBranch(models.Model):  # Филиал страхования
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название филиала")
    address = models.CharField(max_length=30, verbose_name="адрес филиала")
    phone_regex = RegexValidator(regex=r'^\+37529\d{7}$', message="Телефонный номер должен быть введен в формате: "
                                                                  "'+37529xxxxxxx'. Разрешено до 15 цифр")
    phone_number = models.CharField(validators=[phone_regex], unique=True, max_length=17, blank=True)  # Validators
    # should be a list
    tariff_rate = models.FloatField(help_text='Тарифная ставка', verbose_name='Тарифная ставка')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('insurance_branch', kwargs={'ins_branch_slug': self.slug})

    class Meta:
        verbose_name = 'Страховые филиалы'
        verbose_name_plural = 'Страховые филиалы'
        ordering = ['id']


class InsuranceContract(models.Model):
    ins_object = models.ForeignKey('ObjectOfInsurance', on_delete=models.PROTECT, verbose_name="Объект страхования")
    time_create = models.DateTimeField(auto_now=True, verbose_name="Дата и время заключения")
    time_end = models.DateTimeField(verbose_name="Дата и время окончания договора")
    ins_agent = models.ForeignKey('InsuranceAgent', on_delete=models.PROTECT, verbose_name="агент страхования")
    ins_client = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name="агент страхования")
    total_cost = models.FloatField(help_text='Общая цена услуги', verbose_name='Общая цена услуги')

    def get_absolute_url(self):
        return reverse('insurance_contract', kwargs={'ins_contract_id': self.pk})

    class Meta:
        verbose_name = 'Страховые договоры'
        verbose_name_plural = 'Страховые договоры'
        ordering = ['id']


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+37529\d{7}$', message="Телефонный номер должен быть введен в формате: "
                                                                  "'+37529xxxxxxx'. Разрешено до 15 цифр")
    phone_number = models.CharField(validators=[phone_regex], unique=True, max_length=17)  # Validators
