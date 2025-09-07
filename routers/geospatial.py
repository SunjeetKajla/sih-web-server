from fastapi import APIRouter
from database import get_firestore_db
import math
from collections import defaultdict

router = APIRouter()
COLLECTION_NAME = 'hazardReports'

@router.get("/hotspots")
async def get_hotspots(radius: float = 0.1):
    db = get_firestore_db()
    docs = db.collection(COLLECTION_NAME).stream()
    
    coordinates = []
    for doc in docs:
        data = doc.to_dict()
        coordinates.append([data['latitude'], data['longitude']])
    
    if len(coordinates) < 3:
        return {"hotspots": []}
    
    # Simple clustering by proximity
    clusters = []
    used = set()
    
    for i, coord in enumerate(coordinates):
        if i in used:
            continue
            
        cluster = [coord]
        used.add(i)
        
        for j, other_coord in enumerate(coordinates):
            if j in used:
                continue
                
            distance = math.sqrt((coord[0] - other_coord[0])**2 + (coord[1] - other_coord[1])**2)
            if distance <= radius:
                cluster.append(other_coord)
                used.add(j)
        
        if len(cluster) >= 3:
            center_lat = sum(c[0] for c in cluster) / len(cluster)
            center_lng = sum(c[1] for c in cluster) / len(cluster)
            clusters.append({
                "cluster_id": len(clusters),
                "center_latitude": center_lat,
                "center_longitude": center_lng,
                "report_count": len(cluster)
            })
    
    return {"hotspots": clusters}

@router.get("/reports-in-radius")
async def get_reports_in_radius(latitude: float, longitude: float, radius: float = 10):
    db = get_firestore_db()
    docs = db.collection(COLLECTION_NAME).stream()
    
    nearby_reports = []
    for doc in docs:
        data = doc.to_dict()
        distance = math.sqrt(
            (data['latitude'] - latitude) ** 2 + (data['longitude'] - longitude) ** 2
        ) * 111
        
        if distance <= radius:
            data['id'] = doc.id
            nearby_reports.append(data)
    
    return {"reports": nearby_reports, "count": len(nearby_reports)}