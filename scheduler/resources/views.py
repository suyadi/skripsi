from gdata.calendar_resource.client import CalendarResourceClient
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from scheduler import settings
from resources.models import CalendarResources, ResourceForm


manager_required = user_passes_test(
    lambda u:u.groups.filter(name='Manager').count(), 
    login_url='/accounts/login/')


def GetClient():
    client = CalendarResourceClient(domain='ums.ac.id')
    client.ClientLogin(email=settings.GMAIL, password=settings.GPASS, source='apps')
    client.ssl = True
    return client


@manager_required
def list_of_resurces(request):
    try:
        if request.GET['q'] is not '':
            q = request.GET['q']
            resources = CalendarResources.objects.filter(
                            resource_common_name__icontains=q
                        ).order_by('resource_common_name')
        else:
            q = ''
    except:
        q = ''
        resources = CalendarResources.objects.all().order_by('resource_common_name')
    return render(request, 'resources/list_of_resources.html', {
        'title': 'Daftar Sumber Daya',
        'resources': resources,
        'q': q,
        
    })


@manager_required
def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            r = CalendarResources(
                 resource_common_name=request.POST['resource_common_name'],
                 resource_description=request.POST['resource_description'],
                 resource_type=request.POST['resource_type'])
            r.save()
            r = CalendarResources.objects.latest('updated')
            r.resource_id = 'r%s' % r.id
            r.save()
            client = GetClient()
            try:
                client.CreateResource(
                     resource_id=r.resource_id,
                     resource_common_name=request.POST['resource_common_name'],
                     resource_description=request.POST['resource_description'],
                     resource_type=request.POST['resource_type'])
            except:
                client.UpdateResource(
                     resource_id=r.resource_id,
                     resource_common_name=request.POST['resource_common_name'],
                     resource_description=request.POST['resource_description'],
                     resource_type=request.POST['resource_type'])
            return HttpResponseRedirect('/resource/%s' % r.resource_id)
    else:
        form = ResourceForm()

    return render(request, 'resources/edit_form.html', {
        'title': 'Tambah Sumber Daya',
        'form': form,
    })


@manager_required
def edit_resource(request, resource_id):
    try:
        r = CalendarResources.objects.get(resource_id=resource_id)
    except:
        return HttpResponseRedirect('/resources/')
    try:
        q = request.GET['q']
    except:
        q = ''
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            r.resource_common_name = request.POST['resource_common_name']
            r.resource_description = request.POST['resource_description']
            r.resource_type = request.POST['resource_type']
            r.save()
            client = GetClient()
            try:
                client.UpdateResource(
                     resource_id=resource_id,
                     resource_common_name=request.POST['resource_common_name'],
                     resource_description=request.POST['resource_description'],
                     resource_type=request.POST['resource_type'])
            except:
                client.CreateResource(
                     resource_id=resource_id,
                     resource_common_name=request.POST['resource_common_name'],
                     resource_description=request.POST['resource_description'],
                     resource_type=request.POST['resource_type'])
            return HttpResponseRedirect('/resources/?q=%s' % q)
    else:
        initial = {
            'resource_common_name': r.resource_common_name,
            'resource_description': r.resource_description,
            'resource_type': r.resource_type,
        }
        form = ResourceForm(initial=initial)

    title = 'Edit Sumber Daya'
    return render(request, 'resources/edit_form.html', {
        'title': title,
        'resource_common_name': r.resource_common_name,
        'form': form,
    })


@manager_required
def del_resource(request, resource_id):
    try:
        q = request.GET['q']
    except:
        q = ''
    try:
        GetClient().DeleteResource(resource_id=resource_id)
        CalendarResources.objects.get(resource_id=resource_id).delete()
    except:
        pass
    return HttpResponseRedirect('/resources/?q=%s' % q)


@manager_required
def out_of_sync(request):
    client = GetClient()
    calendar_resources = client.GetResourceFeed()
    resources = []
    for resource in calendar_resources.entry:
        try:
            r = CalendarResources.objects.get(resource_id=resource.resource_id)
        except:
            resources.append(resource)
    return render_to_response('resources/out_of_sync.html', {
        'title': 'Sumber daya belum disinkronkan',
        'resources': resources,
    })


@manager_required
def sync(request, resource_id):
    try:
        client = GetClient()
        resource = client.GetResource(resource_id=resource_id)
    except:
        return HttpResponseRedirect('/resources/out_of_sync')
    try:
        r = CalendarResources.objects.get(resource_id=resource.resource_id)
    except:
        r = CalendarResources(
             resource_id=resource.resource_id,
             resource_common_name=resource.resource_common_name,
             resource_description=resource.resource_description,
             resource_type=resource.resource_type)
        r.save()
        return HttpResponseRedirect('/resources/out_of_sync')
