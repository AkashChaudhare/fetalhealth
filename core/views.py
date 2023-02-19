from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from joblib import load
import pickle
import sklearn

# Create your views here.


class Home(ListView):
    model = User
    template_name = 'core/home.html'


class About(ListView):
    model = User
    template_name = 'core/about.html'


class Diagnose(ListView):
    model = User
    template_name = 'core/diagnose.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #baseline_value = self.request.GET.get('baseline_value')
        #print(baseline_value)
        #accelerations = self.request.GET.get('accelerations')
        #fetal_movement = self.request.GET.get('fetal_movement')
        #uterine_contractions = self.request.GET.get('uterine_contractions')
        #light_decelerations = self.request.GET.get('light_decelerations')
        #severe_decelerations = self.request.GET.get('severe_decelerations')
        #prolongued_decelerations = self.request.GET.get('prolongued_decelerations')
        #abnormal_short_term_variability = self.request.GET.get('abnormal_short_term_variability')
        #mean_value_of_short_term_variability = self.request.GET.get('mean_value_of_short_term_variability')
        #percentage_of_time_with_abnormal_long_term_variability = self.request.GET.get('percentage_of_time_with_abnormal_long_term_variability')
        #mean_value_of_long_term_variability = self.request.GET.get('mean_value_of_long_term_variability')
        #histogram_width = self.request.GET.get('histogram_width')
        #histogram_min = self.request.GET.get('histogram_min')
        #histogram_max = self.request.GET.get('histogram_max')
        #histogram_number_of_peaks = self.request.GET.get('histogram_number_of_peaks')
        #histogram_number_of_zeroes = self.request.GET.get('histogram_number_of_zeroes')
        #histogram_mode = self.request.GET.get('histogram_mode')
        #histogram_mean = self.request.GET.get('histogram_mean')
        #histogram_median = self.request.GET.get('histogram_median')
        #histogram_variance = self.request.GET.get('histogram_variance')
        #histogram_tendency = self.request.GET.get('histogram_tendency')

        fff = ('baseline_value', 'accelerations', 'fetal_movement',
           'uterine_contractions', 'light_decelerations', 'severe_decelerations',
           'prolongued_decelerations', 'abnormal_short_term_variability',
           'mean_value_of_short_term_variability',
           'percentage_of_time_with_abnormal_long_term_variability',
           'mean_value_of_long_term_variability', 'histogram_width',
           'histogram_min', 'histogram_max', 'histogram_number_of_peaks',
           'histogram_number_of_zeroes', 'histogram_mode', 'histogram_mean',
           'histogram_median', 'histogram_variance', 'histogram_tendency')

        ddd=dict()
        model = load("savedmodels/model.pkl")
        try:
            for val in fff:
                if self.request.GET.get(val):
                    ddd[val]=float(self.request.GET.get(val))
            print([ddd[val] for val in fff])
            
            print('ran till model loading')
            prediction = model.predict([[ddd[val] for val in fff]])
            print('prediction done')
            if prediction[0]>=2:
                prediction='Pathological'
            elif prediction[0]>=1:
                prediction='Suspicious'
            else:
                prediction='Normal'
            context['prediction']=prediction
            print('context added')

        except:
            pass
       

        #context['a']=ddd['baseline_value']
        #print(type(context['a']))
        #)
        #context['prediction']=prediction
        #print([ddd[val] for val in fff])

        return context
