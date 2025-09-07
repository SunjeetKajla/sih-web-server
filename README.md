# Ocean Hazard Reporter - FastAPI Backend

FastAPI backend for the Ocean Hazard Reporter platform with PostgreSQL + PostGIS for geospatial data.

## Features

- **RESTful API** for hazard report management
- **PostGIS integration** for geospatial queries
- **DBSCAN clustering** for hotspot detection
- **Real-time WebSocket** communication
- **Image upload** handling
- **Statistics API** for dashboard analytics

## Setup

### Prerequisites
- Python 3.8+
- PostgreSQL with PostGIS extension
- Redis (optional, for real-time features)

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Setup PostgreSQL with PostGIS:
```sql
CREATE DATABASE oceandb;
\c oceandb;
CREATE EXTENSION postgis;
```

3. Configure environment:
```bash
copy .env.example .env
# Edit .env with your database credentials
```

4. Run the server:
```bash
python main.py
```

API will be available at `http://localhost:8000`
Documentation at `http://localhost:8000/docs`

## API Endpoints

### Reports
- `POST /api/reports` - Create hazard report
- `GET /api/reports` - Get all reports (with filters)
- `GET /api/reports/{id}` - Get specific report
- `PATCH /api/reports/{id}/status` - Update report status
- `POST /api/reports/{id}/upload-image` - Upload image

### Geospatial
- `GET /api/geospatial/hotspots` - Get DBSCAN hotspots
- `GET /api/geospatial/reports-in-radius` - Get nearby reports

### Statistics
- `GET /api/statistics/dashboard` - Dashboard stats
- `GET /api/statistics/reports-by-period` - Time-based analytics
- `GET /api/statistics/severity-breakdown` - Severity distribution

## Database Schema

```sql
hazard_reports:
- id (Primary Key)
- latitude, longitude (Coordinates)
- location (PostGIS Point)
- type (Hazard type)
- severity (low/medium/high)
- status (pending/verified/resolved)
- description (Optional text)
- image_url (Optional image path)
- timestamp, updated_at
```

## Real-time Features

WebSocket events:
- `new_hazard_report` - New report created
- `report_status_update` - Status changed
- `emergency_alert` - Critical alerts
- `hotspot_update` - Hotspot data updated