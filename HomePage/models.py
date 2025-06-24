# from django.db import models
# from django.urls import reverse
# import qrcode
# from io import BytesIO
# from django.core.files import File
# import qrcode.constants
# from django.utils import timezone

# class User_all_data(models.Model):
#     First_Name = models.CharField(max_length=100, blank = True, null= True)
#     Last_Name = models.CharField(max_length=100, blank = True, null= True)
#     Father_Name = models.CharField(max_length=100, blank= True, null= True)
#     Mother_Name = models.CharField(max_length=100, blank= True, null= True)
#     Total_family_mamber = models.CharField(max_length=10, blank= True, null= True)
#     Data_of_birth = models.CharField(max_length=10, blank= True, null= True)
#     Nid_card_number = models.CharField(max_length=15, blank= True, null= True)
#     phone_number = models.CharField(max_length=14, blank = True, null= True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     qr_code = models.ImageField(upload_to='HomePage/media', blank= True, null= True)
    
    

#     def __str__(self):
#         return self.First_Name
    
#     def save(self, *args, **kwargs):
        
#         created_on_str = self.created_on.strftime('%Y-%m-%d %H:%M:%S')
        
#         qr_data = f'First Name : {self.First_Name}\nLast Name : {self.Last_Name}\nFather Name : {self.Father_Name}\Mother Name : {self.Mother_Name}\Total Family Member : {self.Total_family_mamber}\Date of Birth : {self.Data_of_birth}\nNID Card Number : {self.Nid_card_number}\nPhone Number : {self.phone_number}\nCreated On :  {created_on_str}'
        
#         qr = qrcode.QRCode(
#             version = 1,
#             error_correction = qrcode.constants.ERROR_CORRECT_L,
#             box_size = 10,
#             border = 4,
#         )
        
#         qr.add_data(qr_data)
#         qr.make(fit = True)
        
#         img = qr.make_image(fill_color ='black', back_color = 'white')
#         buffer = BytesIO()
#         img.save(buffer, format="PNG")
#         file_name = f'{self.First_Name} {self.Last_Name}_qr.png'
#         self.qr_code.save(file_name, File(buffer), save=False)
#         super().save(*args, **kwargs)        
        
        
        
        
from django.db import models
from django.urls import reverse 
import qrcode
from io import BytesIO
from django.core.files import File
import qrcode.constants
from django.utils import timezone

        
        
 
class User_Data_all(models.Model):
    First_Name = models.CharField(max_length=100, blank=True, null=True)
    Last_Name = models.CharField(max_length=100, blank=True, null=True)
    Father_Name = models.CharField(max_length=100, blank=True, null=True)
    Mother_Name = models.CharField(max_length=100, blank=True, null=True)
    Total_family_mamber = models.CharField(max_length=10, blank=True, null=True)
    Data_of_birth = models.CharField(max_length=10, blank=True, null=True)
    Nid_card_number = models.CharField(max_length=15, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='HomePage/media', blank=True, null=True)

    def __str__(self):
        return self.First_Name

    def save(self, *args, **kwargs):
        created_on_str = self.created_on.strftime('%Y-%m-%d %H:%M:%S') if self.created_on else 'N/A'

        qr_data = f'First Name : {self.First_Name}\nLast Name : {self.Last_Name}\nFather Name : {self.Father_Name}\nMother Name : {self.Mother_Name}\nTotal Family Member : {self.Total_family_mamber}\nDate of Birth : {self.Data_of_birth}\nNID Card Number : {self.Nid_card_number}\nPhone Number : {self.phone_number}\nCreated On : {created_on_str}'

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        file_name = f'{self.First_Name}_{self.Last_Name}_qr.png'
        self.qr_code.save(file_name, File(buffer), save=False)
        super().save(*args, **kwargs)

        
        
        