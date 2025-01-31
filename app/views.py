from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import GarbageSchedule, Location, GarbageType

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ProjectsPageView(TemplateView):
    template_name = 'app/Projects.html'

class GarbageScheduleListView(ListView):
    model = GarbageSchedule
    context_object_name = 'garbage_schedules'
    template_name = 'app/GarbageSchedule_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')

        if query:
            filtered_GarbageSchedule = GarbageSchedule.objects.filter(location__address__icontains=query)
        else:
            filtered_GarbageSchedule = GarbageSchedule.objects.all()

        context['garbage_schedules'] = filtered_GarbageSchedule
        context['search_query'] = query
        context['total_displayed_schedules'] = filtered_GarbageSchedule.count()
        context['total_displayed_collection_dates'] = filtered_GarbageSchedule.values('collection_date').distinct().count()
        context['total_displayed_time_slots'] = filtered_GarbageSchedule.values('time_slot').distinct().count()
        context['total_displayed_garbage_types'] = sum(schedule.garbage_type.count() for schedule in filtered_GarbageSchedule)

        return context

class GarbageScheduleDetailView(DetailView):
    model = GarbageSchedule
    context_object_name = 'garbage_schedule'
    template_name = 'app/GarbageSchedule_detail.html'

class GarbageScheduleCreateView(CreateView):
    model = GarbageSchedule
    fields = ['location', 'collection_date', 'time_slot', 'garbage_type', 'status']
    template_name = 'app/GarbageSchedule_create.html'
    success_url = reverse_lazy('GarbageSchedule')

    def form_valid(self, form):
        print("Form submitted with the following data:")
        print(form.cleaned_data)  # Print the cleaned data to see what was submitted

        # If the time format is invalid, raise an error
        schedule = form.save(commit=False)
        print(f"Saving schedule: {schedule.location}, {schedule.collection_date}, {schedule.time_slot}")
        schedule.save()
        schedule.garbage_type.set(form.cleaned_data['garbage_type'])
        return super().form_valid(form)

class GarbageScheduleUpdateView(UpdateView):
    model = GarbageSchedule
    fields = ['location', 'collection_date', 'time_slot', 'garbage_type', 'status']
    template_name = 'app/GarbageSchedule_update.html'
    success_url = reverse_lazy('GarbageSchedule')

class GarbageScheduleDeleteView(DeleteView):
    model = GarbageSchedule
    template_name = 'app/GarbageSchedule_delete.html'
    success_url = reverse_lazy('GarbageSchedule')
