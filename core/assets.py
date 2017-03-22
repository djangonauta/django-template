"""Gerenciamento de assets."""

import django_assets

files = [
    'app/app.module.js',
    'app/app.config.js',
    'app/app.routes.js',
    'app/**/*.js',
    'app/**/components/*.js',
]

js_all = django_assets.Bundle(*files, filters='uglifyjs', output='js/bundle')
django_assets.register('js_all', js_all)
