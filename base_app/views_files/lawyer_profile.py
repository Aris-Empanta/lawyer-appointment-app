from django.views import View
from django.shortcuts import redirect, render
from ..models import User, Lawyer
import urllib.parse

class Profile(View):
    
    def get(self, request, username):
        
        try:
            user = User.objects.get(username=username)
            avatar = user.profile.avatar
            member_since = user.date_joined.strftime("%b %Y")
            first_name = user.first_name
            last_name = user.last_name
            is_static = False

            # The variable that indicates if the authenticated user is a lawyer
            lawyer_authenticated = False 
            # The variable that indicates if the visited profile is the 
            # authenticated user's profile
            my_own_profile = False

            # We parse the url, to get the encoded special characters (/, :, etc...)
            avatar_url = urllib.parse.unquote(avatar.url[1:])

            # we examine if the avatar's url is a file belonging to our server 
            # or a google image url. We save this info in a variable and pass it 
            # to the template through context
            if(avatar_url[0:4] != 'http'):
                is_static = True
                avatar_url = f'img/profile-pics/{avatar.url}'
            
            context = { 'avatar_url': avatar_url,
                        'member_since': member_since,
                        'first_name': first_name,
                        'last_name': last_name,
                        'username': username,
                        'is_static': is_static }
            
            # if the user is a lawyer, we add some extra context with the lawyer's details.
            if user.profile.Lawyer: 
                    lawyer = Lawyer.objects.get(profile=user.profile)
                    context['description'] = lawyer.description if lawyer.description is not None else "No description available"
                    context['areasOfExpertise']  = lawyer.areasOfExpertise.split(':') if lawyer.areasOfExpertise is not None else ""
                    context['city']  = lawyer.city  
                    context['yearsOfExperience']  = lawyer.yearsOfExperience
                    context['averageRating']  = lawyer.averageRating 
                    context['hourlyRate']  = lawyer.hourlyRate  if lawyer.hourlyRate is not None else "Contact Lawyer to learn price"
                    context['address']  = lawyer.address
                    context['lisenceStatus']  = lawyer.lisenceStatus
                    context['phone']  = lawyer.phone if lawyer.phone is not None else "Not available"
                    context['lawyer_authenticated'] = lawyer_authenticated
                    context['my_own_profile'] = my_own_profile
            

            # If there is an authenticated user and this user is a lawyer, we mention
            # it through a boolean, in order to hide the appointment button from other 
            # lawyers. Only a client can book appointments.
            if request.user.is_authenticated and request.user.profile.Lawyer:
                lawyer_authenticated = True
                context['lawyer_authenticated'] = lawyer_authenticated

            # First we check if there is an authenticated user, and if his username 
            # is the same as the username in the url parameter. Then, depending if 
            # the user is a lawyer or a client, we render the appropriate template.
            if request.user.is_authenticated and request.user.username == username:

                my_own_profile = True
                context['my_own_profile'] = my_own_profile

                if user.profile.Lawyer:             
                    return render(request, 'components/profile/editable_lawyer_profile.html', context)
                else:
                    return render(request,'components/profile/editable_client_profile.html', context)
            else:

                if user.profile.Lawyer:                      
                    return render(request, 'components/profile/lawyer_profile.html', context)
                else:                                        
                    return render(request, 'components/profile/client_profile.html', context)

        except User.DoesNotExist:
            print('user does not exist')
            return render(request, 'components/reusable/404.html')
        except Exception as e:
            print(f'General exception: {e}')
            return render(request, 'components/reusable/500.html')        