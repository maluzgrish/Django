
from django.shortcuts import render
from django.http import JsonResponse
from intake.models import Waterintake


def listdifference(request):
    return render(request,'ajax.html')

def list_intakes(request):
   intake_list = Waterintake.objects.filter(user=request.user).all()
   intake_data = [
        {   'id': intake.id,
            'date': intake.date.strftime('%d-%m-%Y'),  # or any other format you prefer
            'quantity': intake.quantity
        }
        for intake in intake_list
    ]
   return JsonResponse(intake_data, safe=False)
def calculate_difference(request):
    start_id = request.GET.get('start_id')
    end_id = request.GET.get('end_id')
    user = request.user

    try:
        start_entry = Waterintake.objects.get(id=start_id, user=user)
        end_entry = Waterintake.objects.get(id=end_id, user=user)
    except Waterintake.DoesNotExist:
        return JsonResponse({'error': 'Entries not found for the given IDs'}, status=400)
    difference = end_entry.quantity - start_entry.quantity
    return JsonResponse({'difference': difference})
   
    