from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.db.models import Sum
from django.http import JsonResponse
from django.http import Http404

from .forms import UploadFileForm
from .models import Deal

import csv
import xmltodict


class BaseView(TemplateView):
    form = UploadFileForm

    def get(self, request):
        return render(request, 'post.html', {'form': self.form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            error = self._csv_handler(request.FILES['file'])
            if error:
                return render(request, 'post.html', {'form': form, 'error': error})
            return redirect('app1:handle', fmt="table")
        return render(request, 'post.html', {'form': form})

    def _csv_handler(self, file):
        Deal.objects.all().delete()
        reader = csv.DictReader(line.decode() for line in file)
        fieldname = ['customer', 'item', 'total', 'quantity', 'date']
        if len(set(fieldname).symmetric_difference(set(reader.fieldnames))) > 0:
            return {'Status': 'Error',
                    'Desc': 'Проверьте правильность заполнения ' \
                            'колонок в файле -- "customer", "item", "total", "quantity", "date"'}
        for row in reader:
            Deal.objects.create(customer=row['customer'], item=row['item'], total=row['total'])


class HandleView(TemplateView):
    def get(self, request, fmt):
        qs = Deal.objects.values('customer')
        customer_set = set(i['customer'] for i in qs)
        tmp_total = {}
        tmp_gems = {}
        key_list = {}
        gems = {}
        result = []
        for customer in customer_set:
            customer_price = Deal.objects.filter(customer=customer).aggregate(total=Sum('total'))
            customer_gems = Deal.objects.filter(customer=customer).values('item')
            tmp_gems[customer] = set(i['item'] for i in customer_gems)
            tmp_total[customer] = customer_price['total']
        for i in range(5):
            max_val = max(tmp_total.values())
            tmp = [k for k, v in tmp_total.items() if v == max_val]
            key_list[tmp[0]] = max_val
            tmp_total.pop(tmp[0])
        for k in key_list.keys():
            intersec = set()
            for k2 in key_list:
                if tmp_gems[k] == tmp_gems[k2]:
                    continue
                if tmp_gems[k].intersection(tmp_gems[k2]):
                    for i in tmp_gems[k].intersection(tmp_gems[k2]):
                        intersec.add(i)
            gems[k] = intersec
            result.append({'username': k, 'spent_money': key_list[k], 'gems': list(gems[k])})
        if fmt == 'xml':
            return self._get_xml(result)
        elif fmt == 'json':
            return self._get_json(result)
        elif fmt =='table':
            return render(request, 'handle.html', {'result': result})
        else:
            raise Http404

    def _get_xml(self,result):
        d = {'response': result}
        return HttpResponse(xmltodict.unparse(d), {'Content-type': 'text/xml'})

    def _get_json(self, result):
        return JsonResponse({'response': result})
