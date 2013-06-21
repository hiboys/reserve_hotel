#encoding=utf-8
from hotel.forms.SearchForm import SearchForm
from django.shortcuts import render_to_response
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class HomeController:
    INSTANCE = None
    @classmethod
    def instance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = HomeController()
        return cls.INSTANCE

    def execute(self, request):
        form = SearchForm()
        form.fields['city'].initial = "广州"
        return render_to_response('index.html', {'form':form})
