
# import os
# import base64
# from PIL import Image
# from io import BytesIO
# import numpy as np
# from rembg import remove
# from django.conf import settings
import subprocess
from django.http import HttpResponse
from django.shortcuts import render
import os


def homePage(request):
    
    message = None
    if request.method == "POST":
        if "image" in request.FILES:
            image = request.FILES["image"]
            print(image,"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

            if not image.name.endswith('.bin'):
                return HttpResponse('Error: Invalid file type. Please upload a .bin file.')


            # Specify the directory where you want to save the uploaded file
            directory = "te/.pio/build/esp32dev/"
            if not os.path.exists(directory):
                os.makedirs(directory)
                
            # Check if a file with the same name already exists and replace it
            file_path = os.path.join(directory, image.name)
            if os.path.exists(file_path):
                os.remove(file_path)
                
            with open(file_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)


            # Change to the directory where your firmware project is located
            os.chdir('/home/engmaged/Desktop/Django/Photo/ESP_upload/')

            # # Build and upload the firmware to ESP32
            # os.system('platformio run --target upload')        
            # 

            try:
                output = subprocess.check_output(['platformio', 'run', '--target', 'upload'], cwd='te')
                print(output.decode('utf-8'),"RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                message = output.decode('utf-8').replace('\n', '<br>')
            except subprocess.CalledProcessError as e:
                print(e.output.decode('utf-8'),"ssssssssssssssssssssssssssssssssssssss")
                message = e.output.decode('utf-8').replace('\n', '<br>')

        else:
            image = None


       
    context={  
        # "form":form,
        # "image" : image,
        "message" : message,
    }
    return render(request,'base.html',context)