from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Partner
from .forms import PartnerForm, PartnerHTMLForm, PartnerSimpleForm


# Create your views here.
def partners_list(request):
    partners = Partner.objects.order_by('name')
    return render(request, 'partners/partners.html', {'partners': partners})


def partner_html_new(request):
    post = ''
    if request.method == 'POST':
        form = PartnerHTMLForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect(
                'partners.views.partners_list',
            )
    return render(
        request,
        'partners/partner_form_html_edit.html',
        {'partner': post})


def partner_html_edit(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        form = PartnerHTMLForm(request.POST, instance=partner)
        if form.is_valid():
            partner = form.save()
            return redirect('partners.views.partners_list')
    else:
        form = PartnerHTMLForm(instance=partner)
    return render(
        request,
        'partners/partner_form_html_edit.html', {'partner': partner})


def partner_new(request):
    form = PartnerForm()
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('partners.views.partners_list')
    return render(request, 'partners/partner_edit.html', {'form': form})


def partner_edit(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == "POST":
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            partner = form.save()
            return redirect('partners.views.partners_list')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'partners/partner_edit.html', {'form': form})


def partner_simple_new(request):
    form = PartnerSimpleForm()
    if request.method == 'POST':
        form = PartnerSimpleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('partners.views.partners_list')
    return render(request, 'partners/partner_simple_edit.html', {'form': form})


def partner_simple_edit(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == "POST":
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            partner = form.save()
            return redirect('partners.views.partners_list')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'partners/partner_simple_edit.html', {'form': form})
