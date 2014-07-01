# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render
from django.shortcuts import render_to_response
from elcatuserprofile.models import chb
from django.contrib.auth.models import User
from elcatuserprofile.forms import ProfileForm
from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse, HttpRequest

from django.shortcuts import get_object_or_404, render_to_response
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.template import RequestContext

from elcatuserprofile.models import *  #E.g. Main, Nested, MainForm, etc.

@login_required
def elcat_user_profile(request):
    return render (
                   request,'index.html',
                  )