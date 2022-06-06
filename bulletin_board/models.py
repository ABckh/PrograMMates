from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


LANGUAGES = [
    ('', 'Not selected'),
    ('Afar', 'Afar'),
    ('Abkhazian', 'Abkhazian'),
    ('Afrikaans', 'Afrikaans'),
    ('Akan', 'Akan'),
    ('Albanian', 'Albanian'),
    ('Amharic', 'Amharic'),
    ('Arabic', 'Arabic'),
    ('Aragonese', 'Aragonese'),
    ('Armenian', 'Armenian'),
    ('Assamese', 'Assamese'),
    ('Avaric', 'Avaric'),
    ('Avestan', 'Avestan'),
    ('Aymara', 'Aymara'),
    ('Azerbaijani', 'Azerbaijani'),
    ('Bashkir', 'Bashkir'),
    ('Bambara', 'Bambara'),
    ('Basque', 'Basque'),
    ('Belarusian', 'Belarusian'),
    ('Bengali', 'Bengali'),
    ('Bihari languages', 'Bihari languages'),
    ('Bislama', 'Bislama'),
    ('Tibetan', 'Tibetan'),
    ('Bosnian', 'Bosnian'),
    ('Breton', 'Breton'),
    ('Bulgarian', 'Bulgarian'),
    ('Burmese', 'Burmese'),
    ('Catalan; Valencian', 'Catalan; Valencian'),
    ('Czech', 'Czech'),
    ('Chamorro', 'Chamorro'),
    ('Chechen', 'Chechen'),
    ('Chinese', 'Chinese'),
    ('Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic', 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'),
    ('Chuvash', 'Chuvash'),
    ('Cornish', 'Cornish'),
    ('Corsican', 'Corsican'),
    ('Cree', 'Cree'),
    ('Welsh', 'Welsh'),
    ('Czech', 'Czech'),
    ('Danish', 'Danish'),
    ('German', 'German'),
    ('Divehi; Dhivehi; Maldivian', 'Divehi; Dhivehi; Maldivian'),
    ('Dutch; Flemish', 'Dutch; Flemish'),
    ('Dzongkha', 'Dzongkha'),
    ('Greek, Modern (1453-)', 'Greek, Modern (1453-)'),
    ('English', 'English'),
    ('Esperanto', 'Esperanto'),
    ('Estonian', 'Estonian'),
    ('Basque', 'Basque'),
    ('Ewe', 'Ewe'),
    ('Faroese', 'Faroese'),
    ('Persian', 'Persian'),
    ('Fijian', 'Fijian'),
    ('Finnish', 'Finnish'),
    ('French', 'French'),
    ('Western Frisian', 'Western Frisian'),
    ('Fulah', 'Fulah'),
    ('Georgian', 'Georgian'),
    ('German', 'German'),
    ('Gaelic; Scottish Gaelic', 'Gaelic; Scottish Gaelic'),
    ('Irish', 'Irish'),
    ('Galician', 'Galician'),
    ('Manx', 'Manx'),
    ('Greek, Modern (1453-)', 'Greek, Modern (1453-)'),
    ('Guarani', 'Guarani'),
    ('Gujarati', 'Gujarati'),
    ('Haitian; Haitian Creole', 'Haitian; Haitian Creole'),
    ('Hausa', 'Hausa'),
    ('Hebrew', 'Hebrew'),
    ('Herero', 'Herero'),
    ('Hindi', 'Hindi'),
    ('Hiri Motu', 'Hiri Motu'),
    ('Croatian', 'Croatian'),
    ('Hungarian', 'Hungarian'),
    ('Armenian', 'Armenian'),
    ('Igbo', 'Igbo'),
    ('Icelandic', 'Icelandic'),
    ('Ido', 'Ido'),
    ('Sichuan Yi; Nuosu', 'Sichuan Yi; Nuosu'),
    ('Inuktitut', 'Inuktitut'),
    ('Interlingue; Occidental', 'Interlingue; Occidental'),
    ('Interlingua (International Auxiliary Language Association)', 'Interlingua (International Auxiliary Language Association)'),
    ('Indonesian', 'Indonesian'),
    ('Inupiaq', 'Inupiaq'),
    ('Icelandic', 'Icelandic'),
    ('Italian', 'Italian'),
    ('jv', 'Javanese'),
    ('Japanese', 'Japanese'),
    ('Kalaallisut; Greenlandic', 'Kalaallisut; Greenlandic'),
    ('Kannada', 'Kannada'),
    ('Kashmiri', 'Kashmiri'),
    ('Georgian', 'Georgian'),
    ('Kanuri', 'Kanuri'),
    ('Kazakh', 'Kazakh'),
    ('Central Khmer', 'Central Khmer'),
    ('Kikuyu; Gikuyu', 'Kikuyu; Gikuyu'),
    ('Kinyarwanda', 'Kinyarwanda'),
    ('Kirghiz; Kyrgyz', 'Kirghiz; Kyrgyz'),
    ('Komi', 'Komi'),
    ('Kongo', 'Kongo'),
    ('Korean', 'Korean'),
    ('Kuanyama; Kwanyama', 'Kuanyama; Kwanyama'),
    ('Kurdish', 'Kurdish'),
    ('Lao', 'Lao'),
    ('Latin', 'Latin'),
    ('Latvian', 'Latvian'),
    ('Limburgan; Limburger; Limburgish', 'Limburgan; Limburger; Limburgish'),
    ('Lingala', 'Lingala'),
    ('Lithuanian', 'Lithuanian'),
    ('Luxembourgish; Letzeburgesch', 'Luxembourgish; Letzeburgesch'),
    ('Luba-Katanga', 'Luba-Katanga'),
    ('Ganda', 'Ganda'),
    ('Macedonian', 'Macedonian'),
    ('Marshallese', 'Marshallese'),
    ('Malayalam', 'Malayalam'),
    ('Maori', 'Maori'),
    ('Marathi', 'Marathi'),
    ('Malay', 'Malay'),
    ('Micmac', 'Micmac'),
    ('Macedonian', 'Macedonian'),
    ('Malagasy', 'Malagasy'),
    ('Maltese', 'Maltese'),
    ('Mongolian', 'Mongolian'),
    ('Maori', 'Maori'),
    ('Malay', 'Malay'),
    ('Burmese', 'Burmese'),
    ('Nauru', 'Nauru'),
    ('Navajo; Navaho', 'Navajo; Navaho'),
    ('Ndebele, South; South Ndebele', 'Ndebele, South; South Ndebele'),
    ('Ndebele, North; North Ndebele', 'Ndebele, North; North Ndebele'),
    ('Ndonga', 'Ndonga'),
    ('Nepali', 'Nepali'),
    ('Dutch; Flemish', 'Dutch; Flemish'),
    ('Norwegian Nynorsk; Nynorsk, Norwegian', 'Norwegian Nynorsk; Nynorsk, Norwegian'),
    ('Bokmål, Norwegian; Norwegian Bokmål', 'Bokmål, Norwegian; Norwegian Bokmål'),
    ('Norwegian', 'Norwegian'),
    ('Occitan (post 1500)', 'Occitan (post 1500)'),
    ('Ojibwa', 'Ojibwa'),
    ('Oriya', 'Oriya'),
    ('Oromo', 'Oromo'),
    ('Ossetian; Ossetic', 'Ossetian; Ossetic'),
    ('Panjabi; Punjabi', 'Panjabi; Punjabi'),
    ('Persian', 'Persian'),
    ('Pali', 'Pali'),
    ('Polish', 'Polish'),
    ('Portuguese', 'Portuguese'),
    ('Pushto; Pashto', 'Pushto; Pashto'),
    ('Quechua', 'Quechua'),
    ('Romansh', 'Romansh'),
    ('Romanian; Moldavian; Moldovan', 'Romanian; Moldavian; Moldovan'),
    ('Romanian; Moldavian; Moldovan', 'Romanian; Moldavian; Moldovan'),
    ('Rundi', 'Rundi'),
    ('Russian', 'Russian'),
    ('Sango', 'Sango'),
    ('Sanskrit', 'Sanskrit'),
    ('Sinhala; Sinhalese', 'Sinhala; Sinhalese'),
    ('Slovak', 'Slovak'),
    ('Slovak', 'Slovak'),
    ('Slovenian', 'Slovenian'),
    ('Northern Sami', 'Northern Sami'),
    ('Samoan', 'Samoan'),
    ('Shona', 'Shona'),
    ('Sindhi', 'Sindhi'),
    ('Somali', 'Somali'),
    ('Sotho, Southern', 'Sotho, Southern'),
    ('Spanish; Castilian', 'Spanish; Castilian'),
    ('Albanian', 'Albanian'),
    ('Sardinian', 'Sardinian'),
    ('Serbian', 'Serbian'),
    ('Swati', 'Swati'),
    ('Sundanese', 'Sundanese'),
    ('Swahili', 'Swahili'),
    ('Swedish', 'Swedish'),
    ('Tahitian', 'Tahitian'),
    ('Tamil', 'Tamil'),
    ('Tatar', 'Tatar'),
    ('Telugu', 'Telugu'),
    ('Tajik', 'Tajik'),
    ('Tagalog', 'Tagalog'),
    ('Thai', 'Thai'),
    ('Tibetan', 'Tibetan'),
    ('Tigrinya', 'Tigrinya'),
    ('Tonga (Tonga Islands)', 'Tonga (Tonga Islands)'),
    ('Tswana', 'Tswana'),
    ('Tsonga', 'Tsonga'),
    ('Turkmen', 'Turkmen'),
    ('Turkish', 'Turkish'),
    ('Twi', 'Twi'),
    ('Uighur; Uyghur', 'Uighur; Uyghur'),
    ('Ukrainian', 'Ukrainian'),
    ('Urdu', 'Urdu'),
    ('Uzbek', 'Uzbek'),
    ('Venda', 'Venda'),
    ('Vietnamese', 'Vietnamese'),
    ('Volapük', 'Volapük'),
    ('Welsh', 'Welsh'),
    ('Walloon', 'Walloon'),
    ('Wolof', 'Wolof'),
    ('Xhosa', 'Xhosa'),
    ('Yiddish', 'Yiddish'),
    ('Yoruba', 'Yoruba'),
    ('Zhuang; Chuang', 'Zhuang; Chuang'),
    ('Chinese', 'Chinese'),
    ('Zulu', 'Zulu')
]

PROGRAMMING_LANGUAGES = [
    ('', 'Not selected'),
    ('JavaScript', 'JavaScript'),
    ('HTML and CSS', 'HTML and CSS'),
    ('Python', 'Python'),
    ('C++', 'C++'),
    ('TypeScript', 'TypeScript'),
    ('Rust', 'Rust'),
    ('Java', 'Java'),
    ('Scheme', 'Scheme'),
    ('Kotlin', 'Kotlin'),
    ('C#', 'C#'),
    ('Perl', 'Perl'),
    ('PHP', 'PHP'),
    ('Scala', 'Scala'),
    ('Swift', 'Swift'),
    ('SQL', 'SQL'),
    ('Golang (GO)', 'Golang (GO)'),
    ('Ruby', 'Ruby'),
    ('C', 'C'),
    ('Visual Basic .NET', 'Visual Basic .NET'),
    ('Delphi', 'Delphi'),
]

GENDER_CHOICE = [
    ('', 'Not selected'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Not given', 'Not given')
]


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    information = models.TextField(blank=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    language = models.CharField(max_length=80, choices=LANGUAGES)
    slug = models.SlugField(max_length=250, db_index=True, unique=True, verbose_name="URL")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", null=True, blank=True,
                              default='default/avatardefault_92824.png')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(Users, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('about_user', kwargs={'user_slug': self.slug})

    def get_edit_url(self):
        return reverse('edit_profile', kwargs={'user_slug': self.slug})

    def my_profile_url(self):
        return reverse('profile', kwargs={'user_slug': self.slug})

    # def get_contact_url(self):
    #     return reverse('contact', kwargs={'user_slug': self.slug})

    class Meta:
        verbose_name = 'User'


class Advert(models.Model):
    title = models.CharField(max_length=80, choices=PROGRAMMING_LANGUAGES)
    description = models.TextField(blank=False)
    dat_of_pub = models.DateTimeField(auto_now=True, null=True)
    is_pub = models.BooleanField(default=True)
    username = models.ForeignKey(Users, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=250, db_index=True, unique=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.description)
        super(Advert, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', kwargs={'ad_slug': self.slug})

    def get_delete_url(self):
        return reverse('delete_advert', kwargs={'ad_slug': self.slug})

    def get_edit_url(self):
        return reverse('edit_advert', kwargs={'ad_slug': self.slug})

    class Meta:
        ordering = ['-dat_of_pub', 'title']
        verbose_name = 'Advert'


