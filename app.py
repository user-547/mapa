from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Mapeamento trip_id → linha e sentido (copie sua lista completa aqui)
trip_info = {
    2936465: {"linha": "A1", "sentido": "VOLTA"},
    2936464: {"linha": "A1", "sentido": "IDA"},
    2936467: {"linha": "A2", "sentido": "VOLTA"},
    2936468: {"linha": "A2", "sentido": "IDA"},
    2936471: {"linha": "A3", "sentido": "VOLTA"},
    2936472: {"linha": "A3", "sentido": "IDA"},
    2936475: {"linha": "C1", "sentido": "IDA"},
    4570959: {"linha": "C1", "sentido": "VOLTA"},
    2936479: {"linha": "C2", "sentido": "IDA"},
    2936482: {"linha": "C3", "sentido": "IDA"},
    2936483: {"linha": "C4", "sentido": "IDA"},
    2936484: {"linha": "C5", "sentido": "IDA"},
    2936485: {"linha": "C6", "sentido": "IDA"},
    2936486: {"linha": "C7", "sentido": "IDA"},
    2952464: {"linha": "C7", "sentido": "VOLTA"},
    2952463: {"linha": "C7", "sentido": "IDA"},
    2965215: {"linha": "C7", "sentido": "VOLTA"},
    2952459: {"linha": "C8", "sentido": "IDA"},
    2952460: {"linha": "C8", "sentido": "VOLTA"},
    2936488: {"linha": "C9", "sentido": "IDA"},
    2937754: {"linha": "LA", "sentido": "IDA"},
    2937755: {"linha": "LA", "sentido": "VOLTA"},
    2937726: {"linha": "P1", "sentido": "IDA"},
    2937727: {"linha": "P1", "sentido": "VOLTA"},
    2952461: {"linha": "P2", "sentido": "VOLTA"},
    2952462: {"linha": "P2", "sentido": "IDA"},
    2937732: {"linha": "R1", "sentido": "VOLTA"},
    2937733: {"linha": "R1", "sentido": "IDA"},
    2937734: {"linha": "R2", "sentido": "IDA"},
    2937735: {"linha": "R2", "sentido": "VOLTA"},
    2945677: {"linha": "R2", "sentido": "IDA"},
    2945678: {"linha": "R2", "sentido": "VOLTA"},
    2937736: {"linha": "R3", "sentido": "VOLTA"},
    2937737: {"linha": "R3", "sentido": "IDA"},
    2945672: {"linha": "R3", "sentido": "IDA"},
    2945673: {"linha": "R3", "sentido": "VOLTA"},
    2937738: {"linha": "R4", "sentido": "IDA"},
    2937739: {"linha": "R4", "sentido": "VOLTA"},
    2937741: {"linha": "T1A", "sentido": "IDA"},
    2937740: {"linha": "T1A", "sentido": "VOLTA"},
    2963711: {"linha": "T1A", "sentido": "IDA"},
    2937743: {"linha": "T1B", "sentido": "IDA"},
    2937742: {"linha": "T1B", "sentido": "IDA"},
    2962469: {"linha": "T1B", "sentido": "IDA"},
    2937744: {"linha": "T2A", "sentido": "VOLTA"},
    2937745: {"linha": "T2A", "sentido": "IDA"},
    2962476: {"linha": "T2A", "sentido": "IDA"},
    2937747: {"linha": "T2B", "sentido": "VOLTA"},
    2937746: {"linha": "T2B", "sentido": "IDA"},
    2962475: {"linha": "T2B", "sentido": "IDA"},
    2937749: {"linha": "T3A", "sentido": "VOLTA"},
    2937748: {"linha": "T3A", "sentido": "IDA"},
    2937750: {"linha": "T3B", "sentido": "IDA"},
    2937751: {"linha": "T3B", "sentido": "VOLTA"},
    3062424: {"linha": "T3B", "sentido": "VOLTA"},
    3062425: {"linha": "T3B", "sentido": "IDA"},
    2937752: {"linha": "T4", "sentido": "VOLTA"},
    2937753: {"linha": "T4", "sentido": "IDA"},
    2962472: {"linha": "T4", "sentido": "IDA"},
}

trip_ids = list(trip_info.keys())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vehicles')
def vehicles():
    all_vehicles = []
    for trip_id in trip_ids:
        url = f"https://mobilibus.com/api/vehicles?origin=web&trip_id={trip_id}"
        try:
            resp = requests.get(url, timeout=5)
            data = resp.json()
            # Acrescenta linha e sentido em cada veículo retornado
            for vehicle in data:
                vehicle["linha"] = trip_info[trip_id]["linha"]
                vehicle["sentido"] = trip_info[trip_id]["sentido"]
                all_vehicles.append(vehicle)
        except Exception as e:
            print(f"Erro ao buscar trip_id {trip_id}: {e}")

    return jsonify(all_vehicles)

if __name__ == '__main__':
    app.run(debug=True)
