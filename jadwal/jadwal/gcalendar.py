from django.db.models import Q
from oauth2client.client import AccessTokenCredentials
from apiclient.discovery import build
from gdata.calendar_resource.client import CalendarResourceClient
from gdata.gauth import OAuth2Token
from jadwal import settings
import httplib2

class GCalendar:
    def __init__(self, request):
        self.service = None
        self.oauth2token = None
        try:
            if request.user:
                provider = request.session.get('social_auth_last_login_backend')
                social = request.user.social_auth.filter(
                    Q(user_id=request.user.id), 
                    Q(uid=request.user.email), 
                    Q(provider=provider)
                )
                credential = AccessTokenCredentials(
                    social[0].tokens['access_token'], 
                    'HTTP/1.1'
                )
                http = httplib2.Http()
                http = credential.authorize(http)
                self.service = build("calendar", "v3", http=http)

                self.oauth2token = OAuth2Token(
                    client_id = settings.GOOGLE_OAUTH2_CLIENT_ID,
                    client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
                    scope = 'https://apps-apis.google.com/a/feeds/calendar/resource/',
                    access_token = social[0].tokens['access_token'],
                    user_agent='HTTP/1.1'
                )
        except: pass
                
    def CreateCalendarResources(self,
        resource_id,
        resource_common_name,
        resource_description,
        resource_email,
        resource_type
        ):
        if self.oauth2token is not None:
            client = CalendarResourceClient(domain='ums.ac.id')
            client.auth_token = self.oauth2token
            client.ssl = True
            return client.CreateResource(
                resource_id=resource_id,
                resource_common_name=resource_common_name,
                resource_description=resource_description,
                resource_email=resource_email,
                resource_type=resource_type)
        else: return False

    def GetCalendarResources(self, resource_id):
        if self.oauth2token is not None:
            client = CalendarResourceClient(domain='ums.ac.id')
            client.auth_token = self.oauth2token
            client.ssl = True
            return client.GetResource(resource_id=resource_id)
        else: return None

    def GetAllCalendarResources(self):
        if self.oauth2token is not None:
            client = CalendarResourceClient(domain='ums.ac.id')
            client.auth_token = self.oauth2token
            client.ssl = True
            return client.GetResourceFeed().entry
        else: return None

    def UpdateCalendarResources(self,
        resource_id,
        resource_common_name,
        resource_description,
        resource_email,
        resource_type
        ):
        if self.oauth2token is not None:
            client = CalendarResourceClient(domain='ums.ac.id')
            client.auth_token = self.oauth2token
            client.ssl = True
            return client.UpdateResource(
                resource_id=resource_id,
                resource_common_name=resource_common_name,
                resource_description=resource_description,
                resource_email=resource_email,
                resource_type=resource_type)
        else: return False

    def DelCalendarResources(self, resource_id):
        if self.oauth2token is not None:
            client = CalendarResourceClient(domain='ums.ac.id')
            client.auth_token = self.oauth2token
            client.ssl = True
            client.DeleteResource(resource_id=resource_id)
            return True
        else: return False

    def GetCalendarList(self, page_token=None):
        if self.service is not None:
            try:
                calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
                page_token = calendar_list.get('nextPageToken')
                return page_token, calendar_list['items']
            except: return None
        else: return None

