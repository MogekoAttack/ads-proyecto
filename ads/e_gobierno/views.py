from django.http import JsonResponse

import os
import pandas as pd

from .models import Material

#Función de exportar a excel
def export(request):
    carpeta = 'media/gobierno/'
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    id = request.GET.get('id', None)
    name = request.GET.get('name', None)

    name_records = Material.objects.all()
    records = Material.objects.all()

    # if name is None:
    #     return JsonResponse({
    #         'success': False
    #     })

    # if id is None:
    #     return JsonResponse({
    #         'success': False
    #     })
    
    df = pd.DataFrame(
        columns=[
            "nombre",
        ],
        index=None,
    )

    print(records)
    for record in records:
        df = pd.concat(
            [
                df,
                pd.DataFrame(
                    [
                        {
                            "nombre":record.nombre,
                        }
                    ],
                    index=None
                ),
            ],
            ignore_index=True,
        )
        
    # df.to_excel('media/NSG/' + str(name_records) + '.xlsx',index=False)
    df.to_excel(os.path.join(carpeta, "gobierno" + '.xlsx'), index=False)

    return JsonResponse({
        'success': True
    })