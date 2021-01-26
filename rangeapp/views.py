from django.shortcuts import render
from django.http import HttpResponse
import io
import base64 #Use this in Python 3x
import sys
sys.path.append('/home/jneronha/planerange/plane_range.py')
import plane_range
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000000

def index(request):
    return render(request, 'index.html')



def generate_image(request):
    if request.method == 'POST':
        aircraft = request.POST['Aircraft']
        airport_code = request.POST['Airport Code']

        # generate a matplotlib image, (I don't know how to do that)
        encoded_img = plane_range.plot_range(airport_code, aircraft)
        #imsrc = base64.b64encode(buf.read())
        #imuri = 'data:image/png;base64{}'.format(urllib.parse.quote(imsrc))

        #encoded_img = sio.getvalue().encode('Base64') # On Python 3x, use
        #encoded_img = base64.b64encode(sio.getvalue())
        #return HttpResponse('<img src="'+imuri+ '" />')
        return HttpResponse('<img src="data:image/png;base64,%s" width="700" height="525"/>' %encoded_img)
        #return HttpResponse('<img src="data:image/png;base64, {{ img_encoded }}" alt="somealt" />')
    else:
        # Do something ...
        pass
