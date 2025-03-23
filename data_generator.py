from app_one import models
from django.core.exceptions import ValidationError
from datetime import datetime
import random

# [10*(page-1), 10*page)
def create_data():
    for _ in range(10):
        phone_num = "153" + str(int(random.random()*10**8))
        
        status = random.randint(0,1)
  
        now = datetime.now()
        create_time = now.strftime("%b. %d, %Y")
        
        price = random.randint(5000, 7000)
        
        user_id = random.randint(2, 5)
        try:
            models.Assets.objects.create(
                phone_num=phone_num,
                status=status,
                create_time=create_time,
                price=price,
                user_id=user_id,
            )
        except ValidationError:
            continue
