# import django_filters
# from .models import People
#
# class PeopleFilter(django_filters.FilterSet):
#   age = django_filters.RangeFilter()
#
#   class Meta:
#       model = People
#       fields = ['age']

from django_filters import FilterSet
from django_filters.filters import RangeFilter
from .models import People
from .forms import PeopleFilterFormHelper
from .widgets import CustomRangeWidget

class AllRangeFilter(RangeFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        values = [p.age for p in People.objects.all()]
        min_value = min(values)
        max_value = max(values)
        self.extra['widget'] = CustomRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})

class PeopleFilter(FilterSet):
  age = AllRangeFilter()

  class Meta:
      model = People
      fields = ['age']
      form = PeopleFilterFormHelper
