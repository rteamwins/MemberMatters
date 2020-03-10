"""
Django settings for membermatters project.

Generated by "django-admin startproject" using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from collections import OrderedDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get("PORTAL_SECRET_KEY", "l)#t68rzepzp)0l#x=9mntciapun$whl+$j&=_@nl^zl1xm3j*")

# Default config is for dev environments and is overwritten in prod
DEBUG = True
ALLOWED_HOSTS = ["*"]
SESSION_COOKIE_SAMESITE = None

# this allows the frontend dev server to talk to the dev server
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost",
    "http://127.0.0.1",
]

if os.environ.get("PORTAL_ENV") == "Production":
    ENVIRONMENT = "Production"
    DEBUG = False
    ALLOWED_HOSTS = [os.environ.get("PORTAL_DOMAIN", "portal.example.org")]
    CORS_ORIGIN_WHITELIST = []

    # Slightly hacky, but allows a direct IP while on the local network.
    # These may or may not be required for the interlocks, doors, etc. depending on your setup
    for x in range(1, 255):
        ALLOWED_HOSTS.append("10.0.0." + str(x))
        ALLOWED_HOSTS.append("10.0.1." + str(x))
        ALLOWED_HOSTS.append("192.168.0." + str(x))
        ALLOWED_HOSTS.append("192.168.1." + str(x))

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "profile",
    "portal",
    "access",
    "group",
    "memberbucks",
    "spacedirectory",
    "api_general",
    "constance",
    'corsheaders',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "membermatters.middleware.ForceCsrfCookieMiddleware"
]

ROOT_URLCONF = "membermatters.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "constance.context_processors.config",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "membermatters.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("PORTAL_DB_LOCATION", "/usr/src/data/db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": os.environ.get("PORTAL_LOG_LOCATION", "/usr/src/logs/django.log"),
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-au"

TIME_ZONE = "Australia/Brisbane"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/signin"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.environ.get("PORTAL_MEDIA_LOCATION", "/usr/src/data/media/")

AUTH_USER_MODEL = "profile.User"

REQUEST_TIMEOUT = 0.05

# Django constance configuration
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}]
}

CONSTANCE_CONFIG = {
    # General site info
    "SITE_NAME": ("MemberMatters Portal", "The title shown at the top of the page and as the tab title."),
    "SITE_OWNER": ("MemberMatters", "The name of the legal entity/association/club that is running this site."),
    "ENTITY_TYPE": ("Association", "This is the type of group you are such as an association, club, etc."),

    # Email config
    "EMAIL_SYSADMIN": ("example@example.com", "The default sysadmin email that should receive technical errors etc."),
    "EMAIL_ADMIN": ("example@example.com", "The default admin email that should receive administrative notifications."),
    "EMAIL_DEFAULT_FROM": (
        "\"MemberMatters Portal\" <example@example.org>", "The default email that outbound messages are sent from."),
    "SITE_MAIL_ADDRESS": ("123 Example St, Nowhere", "This address is used in the footer of all emails for anti spam."),

    # URLs
    "SITE_URL": ("https://membermatters.org", "The publicly accessible URL of your MemberMatters instance."),
    "MAIN_SITE_URL": ("https://membermatters.org", "The URL of your main website."),
    "INDUCTION_URL": ("https://eventbrite.com.au", "The URL members should visit to book in for a site induction."),

    # Logo and favicon
    'SITE_LOGO': ('img/logo/logo_small.png', 'Site logo (rectangular)', 'image_field'),
    'SITE_FAVICON': ('img/logo/logo_square_small.png', 'Site favicon (square)', 'image_field'),

    # Localisation of terminology
    "MEMBERBUCKS_NAME": ("Memberbucks", "You can customise the name of the portals currency."),
    "GROUP_NAME": ("Group", "You can customise what the portal calls a group."),
    "ADMIN_NAME": ("Administrators", "You can specify a different name for your admin group like exec or leaders."),
    "HOME_PAGE_CARDS": (
        "[{\"title\": \"Example\", \"description\": \"Example\", \"icon\": \"forum\", \"url\": \"https://membermatters.org/\", \"btn_text\": \"Click Here\"}]",
        "You can specify cards that go on the home page with JSON. See https://github.com/jabelone/MemberMatters/blob/master/GETTING_STARTED.md."),
    "WELCOME_EMAIL_CARDS": (
        "",
        "Same syntax as HOME_PAGE_CARDS but icons are ignored. If nothing is specified we will use HOME_PAGE_CARDS."),

    # Space API config
    "SPACE_DIRECTORY_ENABLED": (True, "Turn on the space directory API available at /api/spacedirectory."),
    "SPACE_DIRECTORY_OPEN": (False, "Sets the open state."),
    "SPACE_DIRECTORY_MESSAGE": (
        "This is the default MemberMatters (membermatters.org) space directory message.", "Sets the message."),
    "SPACE_DIRECTORY_ICON_OPEN": ("", "Sets the icon shown while in the open state."),
    "SPACE_DIRECTORY_ICON_CLOSED": ("", "Sets the icon shown while in the closed state."),
    "SPACE_DIRECTORY_LOCATION_ADDRESS": ("123 Setme St", "Sets the snail mail address."),
    "SPACE_DIRECTORY_LOCATION_LAT": (0, "Sets the latitude."),
    "SPACE_DIRECTORY_LOCATION_LON": (0, "Sets the longitude."),
    "SPACE_DIRECTORY_FED_SPACENET": (False, "Sets support for spacenet."),
    "SPACE_DIRECTORY_FED_SPACESAML": (False, "Sets support for spacesaml."),
    "SPACE_DIRECTORY_CAMS": ("[]", "A JSON list of strings (URLs) that webcam snapshots of the space can be found."),
    "SPACE_DIRECTORY_CONTACT_EMAIL": ("notset@example.com", "Sets the general contact email."),
    "SPACE_DIRECTORY_CONTACT_TWITTER": ("", "Sets the twitter handle."),
    "SPACE_DIRECTORY_CONTACT_FACEBOOK": ("", "Sets the Facebook page URL."),
    "SPACE_DIRECTORY_CONTACT_PHONE": (
        "", "Sets the general contact phone number, include country code with a leading +."),
    "SPACE_DIRECTORY_PROJECTS": ("[]", "A JSON list of strings (URLs) to project sites like wikis, GitHub, etc."),
}

CONSTANCE_CONFIG_FIELDSETS = OrderedDict([
    ("General", ("SITE_NAME", "SITE_OWNER", "ENTITY_TYPE",)),
    ("Contact Information", ("EMAIL_SYSADMIN", "EMAIL_ADMIN", "EMAIL_DEFAULT_FROM", "SITE_MAIL_ADDRESS")),
    ("URLs", ("SITE_URL", "MAIN_SITE_URL", "INDUCTION_URL")),
    ("Images", ("SITE_LOGO", "SITE_FAVICON")),
    ("Group Localisation", ("MEMBERBUCKS_NAME", "GROUP_NAME", "ADMIN_NAME", "HOME_PAGE_CARDS", "WELCOME_EMAIL_CARDS")),
    ("Space Directory", (
        "SPACE_DIRECTORY_ENABLED", "SPACE_DIRECTORY_OPEN", "SPACE_DIRECTORY_MESSAGE", "SPACE_DIRECTORY_ICON_OPEN",
        "SPACE_DIRECTORY_ICON_CLOSED", "SPACE_DIRECTORY_LOCATION_ADDRESS", "SPACE_DIRECTORY_LOCATION_LAT",
        "SPACE_DIRECTORY_LOCATION_LON", "SPACE_DIRECTORY_FED_SPACENET", "SPACE_DIRECTORY_FED_SPACESAML",
        "SPACE_DIRECTORY_CAMS", "SPACE_DIRECTORY_CONTACT_EMAIL", "SPACE_DIRECTORY_CONTACT_TWITTER",
        "SPACE_DIRECTORY_CONTACT_FACEBOOK", "SPACE_DIRECTORY_CONTACT_PHONE", "SPACE_DIRECTORY_PROJECTS"))
])
