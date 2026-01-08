data_points = [
    [49.9, 20.1, 2.10, 0.249],
    [50.0, 15.0, 2.40, 0.350],
    [80.0, 10.1, 2.65, 0.150],
    [39.9, 100.1, 1.79, 0.500],
    [55.0, 25.0, 2.30, 0.200],
    [45.0, 15.0, 2.70, 0.251],
    [35.0, 120.0, 2.00, 0.400],
    [100.0, 20.0, 2.50, 0.301],
    [60.0, 5.0, 2.80, 0.100],
    [30.0, 80.0, 1.90, 0.600]
]

def klasifikasi(gr, res, rhob, nphi):

    # Coal
    if gr < 40 and res > 100 and rhob < 1.8 and nphi > 0.50:
        return "Coal"

    # Sandstone
    elif gr < 50 and res > 20 and 2.10 <= rhob <= 2.65 and nphi < 0.25:
        return "Sandstone"

    # Limestone
    elif 20 <= gr <= 80 and res > 10 and 2.65 <= rhob <= 2.85 and 0.15 <= nphi <= 0.30:
        return "Limestone"

    # Shale 
    elif 50 <= gr <= 120 and (res < 15 or rhob > 2.4 or nphi > 0.35):
        return "Shale"

    # Unknown
    else:
        return "Unknown"


print("TITIK | GR | RES | RHOB | NPHI | LITOLOGI")
print("-" * 50)

for i, data in enumerate(data_points, start=1):
    hasil = klasifikasi(*data)
    print(f"{i:5} | {data[0]:4} | {data[1]:4} | {data[2]:4} | {data[3]:5} | {hasil}")



