from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000000
import pandas as pd
from sqlalchemy import create_engine
import math
from Circles.circles import circle
import io
from base64 import b64encode

engine = create_engine("mysql+pymysql://joshuane_joshneronha:joshuajn8@webhosting2011.is.cc/joshuane_airlines",
                                encoding='latin1');
airport_data = pd.read_sql("airports.dat",engine)
airport_data_clean = airport_data[airport_data["IATA Code"].str.len() == 3][["Airport","IATA Code","Lat","Long"]]
airplane_data = pd.read_sql("Airplane Data - Sheet1",engine)

def haversine_dist(lat1, long1, lat2, long2) -> float:
    lat_1 = lat1
    long_1 = long1

    lat_2 = lat2
    long_2 = long2

    R = 6371

    phi_1 = lat_1 * math.pi/180
    phi_2 = lat_2 * math.pi/180

    delta_phi = (lat_2 - lat_1) * math.pi/180
    delta_lambda = (long_2 - long_1) * math.pi/180

    a = math.sin(delta_phi/2) * math.sin(delta_phi/2) + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    dist = R * c # in km
    return float(dist)

def airport_coord(airport: str) -> tuple:
    try:
        lat = airport_data[airport_data["IATA Code"] == airport]["Lat"].iloc[0]
        long = airport_data[airport_data["IATA Code"] == airport]["Long"].iloc[0]
        return(lat,long)
    except:
        print("Airport does not exist")

def aircraft_range(aircraft: str) -> float:
    try:
        return(1.852*airplane_data[airplane_data["Model"] == aircraft]["Max Range (nm)"].iloc[0])
    except:
        print("Aircraft does not exist")

 # A basic map
def plot_range(airport: str,aircraft: str):
    aircraft_ran = aircraft_range(aircraft)
    airport_lat = airport_coord(airport.upper())[0]
    airport_lon = airport_coord(airport.upper())[1]
    # if aircraft_ran < (111*(90-abs(airport_lat))):
    #     m=Basemap(llcrnrlon=max(-180,airport_lon-(15/1000*aircraft_ran)), llcrnrlat=max(-90,airport_lat-(15/1000*aircraft_ran)),urcrnrlon=min(180,airport_lon+(15/1000*aircraft_ran)),urcrnrlat=min(90,airport_lat+(15/1000*aircraft_ran)),resolution='l')
    # elif aircraft_ran < 8000:
    #     m=Basemap(projection="ortho", lon_0 = airport_lon, lat_0 = airport_lat,resolution='l')
    # else:
    #     m=Basemap(projection="aeqd", lon_0 = airport_lon, lat_0 = airport_lat,resolution='c')
    # m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
    # m.fillcontinents(color="#008080", lake_color = '#A6CAE0')
    # m.drawcoastlines(linewidth=0.1, color="black")
    # m.plot(airport_lon,airport_lat,100,marker='o',color='orange',latlon=True)

    if aircraft_ran < (111*(90-abs(airport_lat))) and aircraft_ran < 5000:
        #m=Basemap(llcrnrlon=max(-180,airport_lon-(15/1000*aircraft_ran)), llcrnrlat=max(-90,airport_lat-(15/1000*aircraft_ran)),urcrnrlon=min(180,airport_lon+(15/1000*aircraft_ran)),urcrnrlat=min(90,airport_lat+(15/1000*aircraft_ran)),resolution='l')
        plt.title("Projection type: Near-Sided Perspective Projection")
        m=Basemap(projection='nsper', lon_0=airport_lon, lat_0=airport_lat, satellite_height=2000000*(aircraft_ran/1000)+2000000, resolution='l')

    elif aircraft_ran < 8000:
        plt.title("Projection type: Orthographic Projection")
        m=Basemap(projection="ortho", lon_0 = airport_lon, lat_0 = airport_lat,resolution='l')
    else:
        plt.title("Projection type: Azimuthal Equidistant Projection")
        m=Basemap(projection="aeqd", lon_0 = airport_lon, lat_0 = airport_lat,resolution='c')
    m.drawlsmask(land_color="#008080", ocean_color = '#A6CAE0')
    m.drawcoastlines(linewidth=0.1, color="black")
    m.plot(airport_lon,airport_lat,marker='o',color='orange',latlon=True)

    (x,y) = zip(*circle(m,airport_lon,airport_lat,radius=aircraft_ran))
    #print(x,y)
    m.plot(x,y,3,color="orange",linewidth=2)

    #plt.savefig("map.png",dpi=400)
    #sio = io.StringIO()
    sio = io.BytesIO()
    plt.savefig(sio, format="png",dpi=300)
    #sio.seek(0)
    pic_hash = b64encode(sio.getvalue()).decode("utf-8").replace("\n", "")
    plt.close()
    return pic_hash
    #return sio

    #encoded = b64encode(plt)



