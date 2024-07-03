import random,string
from .models import bid
def random_id_generator():
    for i in range(0,1000):
        x=''.join(random.sample(list(string.ascii_uppercase),1))
        y = ''.join(random.sample(list(string.ascii_uppercase),1))
        num_1 = random.sample(range(0,10),1)[0]
        num_2 = random.sample(range(0,10),1)[0]
        num_3 = random.sample(range(0,10),1)[0]
        UIDT =  f"{x}{y}{num_1}{num_2}{num_3}"
        if UIDT not in bid.objects.all():
            break
    return UIDT





