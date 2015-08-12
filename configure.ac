# Process this file with autoconf to produce a configure script
AC_INIT(Rodan,0.01)
AC_COPYRIGHT(Copyright 2011-2015 Distributed Digital Music Archives and Libraries Lab)


# Check features
# debug (default disable)
AC_ARG_ENABLE([debug],
        AS_HELP_STRING([--enable-debug], [enable debug mode]))
AS_IF([test "x$enable_debug" = "xyes"], [ENABLE_DEBUG=True], [ENABLE_DEBUG=False])



# diva.js (default enable)
AC_ARG_ENABLE([diva],
        AS_HELP_STRING([--disable-diva], [disable Diva.js]))
AS_IF([test "x$enable_diva" != "xno"], [ENABLE_DIVA=True], [ENABLE_DIVA=False])

# substitute variables
AC_SUBST(ENABLE_DEBUG)
AC_SUBST(ENABLE_DIVA)



# Checks for programs for jobs
# graphicsmagick
AC_ARG_WITH(graphicsmagick-search-path,
                AS_HELP_STRING([--with-graphicsmagick-search-path],[specify the additional graphicsmagick search path]),
                [graphicsmagick_search_path=$withval])

AC_PATH_PROG([BIN_GM], [gm], [:], [${graphicsmagick_search_path}:$PATH])
if test ! -f "$BIN_GM"; then
        AS_IF([test "x$ENABLE_DIVA" = "xTrue"], [AC_MSG_ERROR(Can't find graphicsmagick for Diva.js)], [AC_MSG_WARN(Can't find graphicsmagick)])
        BIN_GM=None               # Python None
else
        BIN_GM="'$BIN_GM'"   # Python string
fi

# kdu_compress (if with diva)
AC_ARG_WITH(kdu_compress-search-path,
                AS_HELP_STRING([--with-kdu_compress-search-path],[specify the additional kdu_compress search path]),
                [kdu_compress_search_path=$withval])

AC_PATH_PROG([BIN_KDU_COMPRESS], [kdu_compress], [:], [${kdu_compress_search_path}:$PATH])

if test ! -f "$BIN_KDU_COMPRESS"; then
        AS_IF([test "x$ENABLE_DIVA" = "xTrue"], [AC_MSG_ERROR(Can't find kdu_compress for Diva.js)], [AC_MSG_WARN(Can't find kdu_compress)])
        BIN_KDU_COMPRESS=None                    # Python None
else
        BIN_KDU_COMPRESS="'$BIN_KDU_COMPRESS'"   # Python string
fi

# xmllint
AC_ARG_WITH(xmllint-search-path,
                AS_HELP_STRING([--with-xmllint-search-path],[specify the additional xmllint search path]),
                [xmllint_search_path=$withval])

AC_PATH_PROG([BIN_XMLLINT], [xmllint], [:], [${xmllint_search_path}:$PATH])

if test ! -f "$BIN_XMLLINT"; then
        AC_MSG_WARN(Can't find xmllint)
        BIN_XMLLINT=None                  # Python None
else
        BIN_XMLLINT="'$BIN_XMLLINT'"      # Python string
fi

# vips
AC_ARG_WITH(vips-search-path,
                AS_HELP_STRING([--with-vips-search-path],[specify the additional vips search path]),
                [vips_search_path=$withval])

AC_PATH_PROG([BIN_VIPS], [vips], [:], [${vips_search_path}:$PATH])

if test ! -f "$BIN_VIPS"; then
        AC_MSG_WARN(Can't find vips)
        BIN_VIPS=None               # Python None
else
        BIN_VIPS="'$BIN_VIPS'"   # Python string
fi

# substitute variables
AC_SUBST(BIN_GM)
AC_SUBST(BIN_KDU_COMPRESS)
AC_SUBST(BIN_XMLLINT)
AC_SUBST(BIN_VIPS)



# Set directories
RODAN_APP_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
AC_ARG_VAR([RODAN_VENV_DIR], [Virtual environment directory (full path)])
AC_ARG_VAR([RODAN_DATA_DIR], [Rodan data directory (full path)])

# check values
if test -z "$RODAN_VENV_DIR"; then
  AC_MSG_ERROR(RODAN_VENV_DIR missing in arguments)
else
  if test ! -d "$RODAN_VENV_DIR"; then
    AC_MSG_ERROR(RODAN_VENV_DIR doesn't exist)
  fi
fi

if test -z "$RODAN_DATA_DIR"; then
  AC_MSG_ERROR(RODAN_DATA_DIR missing in arguments)
else
  if test ! -d "$RODAN_DATA_DIR"; then
    AC_MSG_ERROR(RODAN_DATA_DIR doesn't exist)
  fi
fi

# always add training slash for directories
length=${#RODAN_APP_DIR}
last_char=${RODAN_APP_DIR:length-1:1}
[[ $last_char != "/" ]] && RODAN_APP_DIR="$RODAN_APP_DIR/"; :

length=${#RODAN_VENE_DIR}
last_char=${RODAN_VENV_DIR:length-1:1}
[[ $last_char != "/" ]] && RODAN_VENV_DIR="$RODAN_VENV_DIR/"; :

length=${#RODAN_DATA_DIR}
last_char=${RODAN_DATA_DIR:length-1:1}
[[ $last_char != "/" ]] && RODAN_DATA_DIR="$RODAN_DATA_DIR/"; :


# substitute variables
AC_SUBST(RODAN_APP_DIR)
AC_SUBST(RODAN_VENV_DIR)
AC_SUBST(RODAN_DATA_DIR)


# Database
AC_ARG_VAR([DB_NAME], [Database name (default rodan)])
AC_ARG_VAR([DB_USER], [Database user (default rodan)])
AC_ARG_VAR([DB_PASSWORD], [Database password])
AC_ARG_VAR([DB_HOST], [Database host (default localhost)])
AC_ARG_VAR([DB_PORT], [Database port (default 5432)])

if test -z "$DB_NAME"; then
  DB_NAME=rodan
fi
if test -z "$DB_USER"; then
  DB_USER=rodan
fi
if test -z "$DB_PASSWORD"; then
  AC_MSG_ERROR(DB_PASSWORD missing in arguments)
fi
if test -z "$DB_HOST"; then
  DB_HOST=localhost
fi
if test -z "$DB_PORT"; then
  DB_PORT=5432
fi


# Celery broker
AC_ARG_VAR([CELERY_BROKER_URL], [Celery broker URL (default amqp://rodanuser:DDMALrodan@localhost:5672/DDMAL)])

if test -z "$CELERY_BROKER_URL"; then
   CELERY_BROKER_URL=amqp://rodanuser:DDMALrodan@localhost:5672/DDMAL
fi


# Domain name
AC_ARG_VAR([DOMAIN_NAME], [Domain name])

if test -z "$DOMAIN_NAME"; then
  AC_MSG_ERROR(DOMAIN_NAME missing in arguments)
fi

# substitute variables
AC_SUBST(DB_NAME)
AC_SUBST(DB_USER)
AC_SUBST(DB_PASSWORD)
AC_SUBST(DB_HOST)
AC_SUBST(DB_PORT)
AC_SUBST(CELERY_BROKER_URL)
AC_SUBST(DOMAIN_NAME)


# IIPServer bin
AC_ARG_VAR([IIPSRV_FCGI], [IIPServer fcgi binary (required if --enable-diva)])

if test "x$ENABLE_DIVA" = "xTrue"; then
  if test -z "$IIPSRV_FCGI"; then
    AC_MSG_ERROR([IIPSRV_FCGI required when --enable-diva=yes])
  fi
  if test ! -f "$IIPSRV_FCGI"; then
    AC_MSG_ERROR([IIPSRV_FCGI fcgi binary not found])
  fi
fi


# output
AC_CONFIG_FILES(celery_start.sh gunicorn_start.sh rodan/settings_production.py etc/supervisor/conf.d/rodan.conf etc/supervisor/conf.d/rodan-celery.conf)

if test "x$ENABLE_DIVA" = "xTrue"; then
  AC_CONFIG_FILES(etc/supervisor/conf.d/iipserver.conf)
  AC_CONFIG_FILES(etc/nginx/sites-available/rodan_with_diva)
  AC_OUTPUT()
else
  AC_CONFIG_FILES(etc/nginx/sites-available/rodan_without_diva)
  AC_OUTPUT()
fi