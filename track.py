import json,folium
from folium.plugins import MiniMap,Fullscreen
from folium.elements import MacroElement
from jinja2 import Template
from datetime import datetime as dt
l="gps_log.json"
e=[json.loads(i) for i in open(l).readlines()]
m=folium.Map(location=[e[0]["latitude"],e[0]["longitude"]],zoom_start=18,tiles='CartoDB dark_matter')
c=[]
for x in e:
 t=dt.fromisoformat(x["timestamp"])
 p=f"Entry {x['entry']}\nTanggal: {t.strftime('%d %B %Y')}\nJam: {t.strftime('%H:%M:%S')}"
 folium.CircleMarker(location=[x["latitude"],x["longitude"]],radius=7,color='lime',fill=True,fill_color='lime',fill_opacity=0.9,popup=folium.Popup(p,max_width=200)).add_to(m)
 c.append([x["latitude"],x["longitude"]])
folium.PolyLine(c,color="lime",weight=4,opacity=0.8).add_to(m)
MiniMap(tile_layer='CartoDB dark_matter',position='bottomright').add_to(m)
Fullscreen(position='topright').add_to(m)
h=""
for x in e:h+=f"<pre style='margin:0;color:lime;font-family:monospace;font-size:11px;background:transparent;'>Entry:{x['entry']}\\nTimestamp:{x['timestamp']}\\nLatitude:{x['latitude']}\\nLongitude:{x['longitude']}\\nAltitude:{x['altitude']}\\nAccuracy:{x.get('accuracy','N/A')}\\nVertical Accuracy:{x.get('vertical_accuracy','N/A')}\\nBearing:{x.get('bearing','N/A')}\\nSpeed:{x.get('speed','N/A')}\\nElapsedMs:{x.get('elapsedMs','N/A')}\\nProvider:{x.get('provider','N/A')}\\nMethod:{x.get('method','N/A')}</pre><hr style='border-color:lime;border-width:1px;margin:3px 0;'>"
o=f"<div id='raw-overlay' style='position:fixed;bottom:10px;left:10px;z-index:9999;max-height:300px;max-width:260px;overflow-y:auto;resize:both;padding:4px;'>{h}</div>"
class F(MacroElement):
 def __init__(s,h):super().__init__();s._template=Template(f"{{% macro script(this, kwargs) %}}var overlay=document.createElement('div');overlay.innerHTML=`{h}`;document.body.appendChild(overlay);{{% endmacro %}}")
m.get_root().add_child(F(o))
m.save("gps_map.html")
print("Map created: gps_map.html")
