from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
@register.filter
@stringfilter
def split(value,sep):
	"""
			Return value by sep
	"""
	return value.split(sep)

@register.filter
def n_range(num):
	list=[]
	for i in range(5):
		list.append(i)
	return list
