from fastapi import APIRouter
from database import get_firestore_db
from datetime import datetime, timedelta
from collections import defaultdict

router = APIRouter()
COLLECTION_NAME = 'hazardReports'

@router.get("/dashboard")
async def get_dashboard_stats():
    db = get_firestore_db()
    docs = db.collection(COLLECTION_NAME).stream()
    
    total_reports = 0
    pending = 0
    verified = 0
    resolved = 0
    today_reports = 0
    today = datetime.now().date()
    
    for doc in docs:
        data = doc.to_dict()
        total_reports += 1
        
        status = data.get('status', 'pending')
        if status == 'pending':
            pending += 1
        elif status == 'verified':
            verified += 1
        elif status == 'resolved':
            resolved += 1
        
        if data.get('timestamp') and data['timestamp'].date() == today:
            today_reports += 1
    
    active_hazards = pending + verified
    
    return {
        "total_reports": total_reports,
        "active_hazards": active_hazards,
        "reports_today": today_reports,
        "verified_reports": verified,
        "pending_reports": pending,
        "resolved_reports": resolved
    }

@router.get("/reports-by-period")
async def get_reports_by_period(period: str = "7d"):
    db = get_firestore_db()
    
    days = 7 if period == "7d" else 30 if period == "30d" else 7
    start_date = datetime.now() - timedelta(days=days)
    
    docs = db.collection(COLLECTION_NAME).where('timestamp', '>=', start_date).stream()
    
    date_counts = defaultdict(int)
    for doc in docs:
        data = doc.to_dict()
        if data.get('timestamp'):
            date_str = data['timestamp'].date().isoformat()
            date_counts[date_str] += 1
    
    return {
        "period": period,
        "data": [{"date": date, "count": count} for date, count in sorted(date_counts.items(), reverse=True)]
    }

@router.get("/severity-breakdown")
async def get_severity_breakdown():
    db = get_firestore_db()
    docs = db.collection(COLLECTION_NAME).stream()
    
    severity_counts = defaultdict(int)
    for doc in docs:
        data = doc.to_dict()
        severity = data.get('severity', 'low')
        severity_counts[severity] += 1
    
    return {
        "breakdown": [{"severity": severity, "count": count} for severity, count in severity_counts.items()]
    }