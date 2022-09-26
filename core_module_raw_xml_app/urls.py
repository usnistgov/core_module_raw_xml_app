""" Url router for the raw xml module
"""

from django.urls import re_path

from core_module_raw_xml_app.views.views import RawXmlModule

urlpatterns = [
    re_path(
        r"module-raw-xml",
        RawXmlModule.as_view(),
        name="core_module_raw_xml_view",
    ),
]
