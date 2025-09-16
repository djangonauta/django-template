from django.contrib.staticfiles.storage import StaticFilesStorage
from django_weasyprint import WeasyTemplateResponseMixin


class BaseReportResponseMixin(WeasyTemplateResponseMixin):
    static_files_storage = StaticFilesStorage()

    pdf_stylesheets = [
        static_files_storage.path("css/normalize.min.css"),
        static_files_storage.path("css/paper.min.css"),
    ]
