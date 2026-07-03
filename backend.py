#step 1:import database objects
from database import engine, init_db, Appointment, get_db
import datetime as dt
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import select
init_db()  # Initialize the database and create tables if they don't exist



class AppointmentRequest(BaseModel):
    patient_name: str
    reason: str
    start_time: dt.datetime  # Use datetime for simplicity; you can convert it to str later

class AppointmentResponse(BaseModel):
    id: int
    patient_name: str
    reason: str
    start_time: dt.datetime
    cancelled: bool
    created_at: dt.datetime
    is_confirmed: bool

class CancelAppointmentRequest(BaseModel):
    patient_name: str
    date: dt.date

class CancelAppointmentResponse(BaseModel):
    cancel_count: int

class ListAppointmentsRequest(BaseModel):
    date: dt.date

#step 2:create fast Api
from fastapi import FastAPI, HTTPException,Depends
app = FastAPI()

#schedule Appointment
@app.post("/schedule_appointment/")
def schedule_appointment(request: AppointmentRequest,db:Session=Depends(get_db)):
    # with engine.begin() as conn:
    #     conn.add(appointment)
    #     conn.commit()
    # return {"message": "Appointment scheduled successfully", "appointment_id": appointment.id}

    new_appointment = Appointment(
        patient_name=request.patient_name,
        reason=request.reason,
        start_time=request.start_time,
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    new_appointment_return=AppointmentResponse(
        id=new_appointment.id,
        patient_name=new_appointment.patient_name,
        reason=new_appointment.reason,
        start_time=new_appointment.start_time,
        cancelled=new_appointment.cancelled,
        created_at=new_appointment.created_at,
        is_confirmed=new_appointment.is_confirmed
    )
    return new_appointment_return


#cancel Appointment
# @app.post("/cancel_appointment/")
# def cancel_appointment(request: CancelAppointmentRequest,db:Session=Depends(get_db)):
#     start_dt=dt.datetime.combine(request.datetime.date(), dt.time.min)
#     end_dt=start_dt+dt.timedelta(days=1)
#     result=db.execute(
#         select(Appointment)
#         .where(Appointment.patient_name==request.patient_name)
#         .where(Appointment.start_time>=start_dt)
#         .where(Appointment.start_time<end_dt)
#         .where(Appointment.cancelled==False)
#     )
#     Appointments_to_cancel=result.scalars().all()
#     if not Appointments_to_cancel:
#         raise HTTPException(status_code=404, detail="No appointments found to cancel for the given patient and date.")
#     for appointment in Appointments_to_cancel:
#         appointment.cancelled=True
#     db.commit()
#     return CancelAppointmentResponse(cancel_count=len(Appointments_to_cancel))



from sqlalchemy import select, func
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
import datetime as dt

@app.post("/cancel_appointment/")
def cancel_appointment(
    request: CancelAppointmentRequest,
    db: Session = Depends(get_db)
):
    start_dt = dt.datetime.combine(
        request.date,
        dt.time.min
    )

    end_dt = start_dt + dt.timedelta(days=1)

    appointments_to_cancel = db.execute(
        select(Appointment)
        .where(
            func.lower(Appointment.patient_name)
            == request.patient_name.lower()
        )
        .where(Appointment.start_time >= start_dt)
        .where(Appointment.start_time < end_dt)
        .where(Appointment.cancelled == False)
    ).scalars().all()

    if not appointments_to_cancel:
        raise HTTPException(
            status_code=404,
            detail="No active appointment found for this patient on the selected date."
        )

    for appointment in appointments_to_cancel:
        appointment.cancelled = True

    db.commit()

    return {
        "cancel_count": len(appointments_to_cancel),
        "message": "Appointment cancelled successfully"
    }



@app.get("/debug")
def debug(db: Session = Depends(get_db)):
    appointments = db.execute(
        select(Appointment)
    ).scalars().all()

    return [
        {
            "patient_name": a.patient_name,
            "start_time": str(a.start_time),
            "cancelled": a.cancelled
        }
        for a in appointments
    ]

#list Appointments
@app.post("/list_appointments/")
def list_appointments(
    request: ListAppointmentsRequest,
    db: Session = Depends(get_db)
):
    start_dt = dt.datetime.combine(
        request.date,
        dt.time.min
    )

    end_dt = start_dt + dt.timedelta(days=1)

    result = db.execute(
        select(Appointment)
        .where(Appointment.cancelled == False)
        .where(Appointment.start_time >= start_dt)
        .where(Appointment.start_time < end_dt)
        .order_by(Appointment.start_time.asc())
    )

    appointments_db = result.scalars().all()

    appointments = []

    for appointment in appointments_db:
        appointments.append(
            AppointmentResponse(
                id=appointment.id,
                patient_name=appointment.patient_name,
                reason=appointment.reason,
                start_time=appointment.start_time,
                cancelled=appointment.cancelled,
                created_at=appointment.created_at,
                is_confirmed=appointment.is_confirmed
            )
        )

    return appointments

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)
