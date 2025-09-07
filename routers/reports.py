from fastapi import APIRouter, HTTPException, UploadFile, File
from database import get_firestore_db
from schemas import HazardReportCreate, HazardReportResponse, StatusUpdate
from typing import List, Optional
from datetime import datetime
import shutil
import os

router = APIRouter()
COLLECTION_NAME = 'hazardReports'

@router.post("", response_model=HazardReportResponse)
async def create_report(report: HazardReportCreate):
    db = get_firestore_db()
    
    report_data = {
        "latitude": report.latitude,
        "longitude": report.longitude,
        "type": report.type,
        "severity": report.severity.value,
        "status": "pending",
        "description": report.description,
        "timestamp": datetime.now(),
        "updated_at": datetime.now()
    }
    
    doc_ref, doc = db.collection(COLLECTION_NAME).add(report_data)
    report_data["id"] = doc.id
    
    return report_data

@router.get("", response_model=List[HazardReportResponse])
async def get_reports(status: Optional[str] = None, severity: Optional[str] = None):
    db = get_firestore_db()
    query = db.collection(COLLECTION_NAME).order_by("timestamp", direction="DESCENDING")
    
    if status:
        query = query.where("status", "==", status)
    if severity:
        query = query.where("severity", "==", severity)
    
    docs = query.stream()
    reports = []
    
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        reports.append(data)
    
    return reports

@router.get("/{report_id}", response_model=HazardReportResponse)
async def get_report(report_id: str):
    db = get_firestore_db()
    doc = db.collection(COLLECTION_NAME).document(report_id).get()
    
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Report not found")
    
    data = doc.to_dict()
    data["id"] = doc.id
    return HazardReportResponse(**data)

@router.patch("/{report_id}/status", response_model=HazardReportResponse)
async def update_status(report_id: str, status_update: StatusUpdate):
    db = get_firestore_db()
    doc_ref = db.collection(COLLECTION_NAME).document(report_id)
    
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Report not found")
    
    doc_ref.update({
        "status": status_update.status.value,
        "updated_at": datetime.now()
    })
    
    updated_doc = doc_ref.get()
    data = updated_doc.to_dict()
    data["id"] = updated_doc.id
    return HazardReportResponse(**data)

@router.post("/{report_id}/upload-image")
async def upload_image(report_id: str, image: UploadFile = File(...)):
    db = get_firestore_db()
    doc_ref = db.collection(COLLECTION_NAME).document(report_id)
    
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Report not found")
    
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = f"{upload_dir}/{report_id}_{image.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    doc_ref.update({
        "image_url": file_path,
        "updated_at": datetime.now()
    })
    
    return {"message": "Image uploaded successfully", "image_url": file_path}