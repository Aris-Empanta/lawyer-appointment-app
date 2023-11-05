from ..models import User, Profile, Lawyer
from .profile import BaseProfile
from django.utils import timezone
from django.utils.timesince import timesince

class BaseLawyer(BaseProfile):

    # This method takes a lawyer's username and returns its Queryset.
    def get_lawyer_by_username(self, lawyer_username)-> Lawyer:
        # We fetch the lawyer object using the received username.
        lawyer_user_obj = User.objects.filter(username=lawyer_username).first()
        lawyer_profile_obj = Profile.objects.filter(user=lawyer_user_obj).first()
        lawyer = Lawyer.objects.filter(profile=lawyer_profile_obj).first()

        return lawyer
    
    # This method takes a list of appointments object, and creates a context from 
    # their fields with all the info needed to be rendered.
    def format_booked_appointments_data(self, appointments_objects_list)->list:
        
        return [
                  {
                    'day_name': appointment.starting_time.strftime('%A'),
                    'date': appointment.starting_time.strftime('%d/%m/%Y'),
                    'starting_time': appointment.starting_time.strftime('%H:%M'),
                    'ending_time': appointment.ending_time.strftime('%H:%M'), 
                    'first_name': appointment.client.profile.user.first_name, 
                    'last_name': appointment.client.profile.user.last_name,
                    'profile_link': f'/profile/{appointment.client.profile.user.username}',
                    'avatar': appointment.client.profile.avatar.name,
                    'avatar_is_external_link': self.is_avatar_external_link(appointment.client.profile.avatar.name),
                    'checked': appointment.checked,
                    'time_since': timesince(appointment.time_booked, timezone.now())
                  } 
                  for appointment in appointments_objects_list
                ] 