from django.shortcuts import redirect
from django.views import View
from ..models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from pathlib import Path
from django.contrib import messages
from ..base_classes.clients import BaseClient
from ..base_classes.lawyers import BaseLawyer

@method_decorator(login_required(login_url="login"), name='dispatch')
class UpdateProfilePic(View, BaseClient, BaseLawyer):

    def post(self, request):
        new_avatar = request.FILES.get('profile_pic')

        # Image should be of specific mime type
        if new_avatar.content_type not in self.PROFILE_PICTURE_MIME_TYPES:
            messages.error(request, 'This image type is not supported')
            return redirect('profile', username=request.user.username)
        
        # It should be less or equal to 300MB 
        if  new_avatar.size > 300000:
            messages.error(request, 'The image is too big')
            return redirect('profile', username=request.user.username)
        
        # We rename the image with a unique name
        new_avatar.name = self.rename_image(new_avatar.name)

        # We get the path to the previous avatar using the Path object
        profile = Profile.objects.filter(user=request.user).first()
        previous_avatar_path = Path(profile.avatar.path)

        # We delete the previous avatar file (only if it is not avatar.png)
        if previous_avatar_path.exists() and not profile.avatar.name == self.default_profile_pic_name:
            previous_avatar_path.unlink()  
            print(f"File {previous_avatar_path} has been deleted.")
        else:
            print(f"File {previous_avatar_path} does not exist.")

        # Save the newly received image as the profile pic
        profile.avatar = new_avatar
        profile.save()

        return redirect('profile', username=request.user.username)