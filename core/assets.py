"""Gerenciamento de assets."""

import django_assets

js_files = [
    'app/app.module.js',
    'app/app.config.js',
    'app/*.js',
    'app/**/*.js',
    'app/**/componentes/*.js'
]
js = django_assets.Bundle(*js_files, filters='uglifyjs', output='js/bundle.min.js')

css_files = [
    'css/base.css',
]
css = django_assets.Bundle(*css_files, filters='cssmin', output='css/bundle.min.css')

django_assets.register('js_all', js)
django_assets.register('css_all', css)
