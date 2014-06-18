import os
import json
import logging
import httplib2
import feedparser
import xml.etree.ElementTree as ET

from apiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from kegiatan.models import CredentialsModel
from kalender import settings
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), '..', 'client_secrets.json')

FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope=[
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/calendar.readonly',
        'https://apps-apis.google.com/a/feeds/calendar/resource/',
    ],
    redirect_uri='http://localhost:8000/oauth2callback')


@login_required
def index(request):
    storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid == True:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY, request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        headers = {'Content-type': 'application/atom+xml'}
        resp, content = http.request(
                     'https://apps-apis.google.com/a/feeds/calendar/resource/2.0/ums.ac.id/',
                     'GET',
                     headers=headers)
        data = xmltodict.parse(content)
        print data
        return render_to_response('aset/daftar.html', {
                'daftar_aset': data.entries,
                })

@login_required
def detail(request,aset_id):
    storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid == True:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY, request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        headers = {'Content-type': 'application/atom+xml'}
        url = 'https://apps-apis.google.com/a/feeds/calendar/resource/2.0/ums.ac.id/%s' % aset_id
        resp, content = http.request(
                     url,
                     'GET',
                     headers=headers)
        tree = tree = ET.ElementTree(ET.fromstring(content))
        data = []
        for elem in tree.getiterator():
            if 'property' in elem.tag:
                data.append(elem.attrib)
                print elem.attrib['name']
        return render_to_response('aset/detail.html', {
                'detail_aset': data,
                })
