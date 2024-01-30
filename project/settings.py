from pathlib import Path
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#____________________________________________________________

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v5ingjf@q!(ds&er0$!_h^))tg_j@oav-j&1)37zwc!*$*toy_'
#_________________________________________________________________________________

#            ##---> DEBUG <---##
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#_____________________________________________________________________

# hosts
ALLOWED_HOSTS = []
#______________________________________________________________


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # app application
    'app',
    'account',

    # libraries
    'rest_framework',
    'rest_framework.authtoken',
    # djoser
    'djoser',
    # simple jwt
    'rest_framework_simplejwt',
    

]
#___________________________

# site id

#________________________________


#________________MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
     # Add the account middleware:
   
    #____________________________________________
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]#________________________________________________________________


# root url for appliction her is name -> project <-
ROOT_URLCONF = 'project.urls'
#______________________________________________________________


# frontend templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
#_____________________________________________________________________________


# application wagt project
WSGI_APPLICATION = 'project.wsgi.application'
#_____________________________________________________________________


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#________________________________________________________________________


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
#_____________________________________________________________________________________


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
#_____________________________________________________


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
#__________________________________________________________


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#_______________________________________________________________________


######################### -> AUTHENTICATION <- ########################
# authe user conect change the old USER MODEL with new create class UserAccount model 
AUTH_USER_MODEL = 'account.UserAccount'
# __________________________________________________________________________


# conect with Gmail
EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER = 'project.django.rest@gmail.com'
EMAIL_HOST_PASSWORD= 'zvzi drju avyg xxqa'
EMAIL_USE_TLS = True
#_________________________________________________________________________


#________________REST_FRAMEWORK_AUTHENTICATION_Simple_jwt_________________
REST_FRAMEWORK = { 
    'DEFAULT_AUTHENTICATION_CLASSES': ( 
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
     'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': ( 
    #     'rest_framework.authentication.TokenAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    # ) 

}
#___________________________________________________________________________


#___________________________djoser_AUTHENTICATION_____________________________
DJOSER = { 

      # login by email
      'LOGIN_FIELD':'email',
      # to validate password equality.
      'USER_CREATE_PASSWORD_RETYPE':True,
      # change -> USERNAME <- endpoints will send confirmation email to user
      'USERNAME_CHANGED_EMAIL_CONFIRMATION':True,
      # change -> PASSWORD <- endpoints will send confirmation email to user
      'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
      # register or activation endpoint will send confirmation email to user.
      'SEND_CONFIRMATION_EMAIL':True,
      # to validate username equality.
      'SET_USERNAME_RETYPE':True,
      # to validate password equality.
      'SET_PASSWORD_RETYPE':True,
      # to your frontend password reset page, It should contain {uid} and {token} placeholders
      'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
      # to your frontend username reset page, It should contain {uid} and {token} placeholders
      'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
      #URL to your frontend activation page. It should contain {uid} and {token} placeholders 
      'ACTIVATION_URL': 'activetpage/activate/{uid}/{token}',
      #user will be required to click activation link sent in email after 
      'SEND_ACTIVATION_EMAIL':True,

      # use serializer model
      'SERIALIZER':{ 
          
          # create serializer and use it 
          # to create -> id, email, first_name, last_name and password 
          'user_create': 'account.serializer.UserCreateSerializer',

          # use the -> id, email, first_name, last_name and password
          'user': 'account.serializer.UserCreateSerializer',

          # delete -> id, email, first_name, last_name and password 
          'user_delete': 'djoser.serializer.UserDeleteSerializer',
      } 
}
#_____________________________________________________________________


# Configure django-rest-framework-simplejwt to use the Authorization: JWT <access_token> header:
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}
#________________________________________________________________

