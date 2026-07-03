import streamlit as st
import requests
import datetime as dt

st.set_page_config(page_title="Appointment Management")

st.title("🏥 Appointment Management System")

BASE_URL = "http://127.0.0.1:8000"

tab1, tab2, tab3 = st.tabs(
    ["Schedule", "Cancel", "List"]
)

# ==================================
# Schedule Appointment
# ==================================

with tab1:

    st.subheader("Schedule Appointment")

    patient_name = st.text_input(
        "Patient Name",
        key="schedule_name"
    )

    reason = st.text_input(
        "Reason",
        key="schedule_reason"
    )

    appointment_date = st.date_input(
        "Date",
        value=dt.date.today()
    )

    appointment_time = st.time_input(
        "Time",
        value=dt.time(9, 0)
    )

    if st.button("Schedule"):

        start_datetime = dt.datetime.combine(
            appointment_date,
            appointment_time
        )

        payload = {
            "patient_name": patient_name,
            "reason": reason,
            "start_time": start_datetime.isoformat()
        }

        try:
            response = requests.post(
                f"{BASE_URL}/schedule_appointment/",
                json=payload
            )

            if response.status_code == 200:
                st.success("Appointment Scheduled")
                st.json(response.json())
            else:
                st.error(response.text)

        except Exception as e:
            st.error(str(e))


# ==================================
# Cancel Appointment
# ==================================

with tab2:

    st.subheader("Cancel Appointment")

    cancel_name = st.text_input(
        "Patient Name",
        key="cancel_name"
    )

    cancel_date = st.date_input(
        "Appointment Date",
        key="cancel_date"
    )

    if st.button("Cancel"):

        # payload = {
        #     "patient_name": cancel_name,
        #     "datetime": dt.datetime.combine(
        #         cancel_date,
        #         dt.time.min
        #     ).isoformat()
        # }
        # st.write(payload)

        payload = {
    "patient_name": cancel_name,
    "date": cancel_date.isoformat()
}

        try:
            response = requests.post(
                f"{BASE_URL}/cancel_appointment/",
                json=payload
            )

            if response.status_code == 200:
                st.success("Appointment Cancelled")
                st.json(response.json())
            else:
                st.error(response.text)

        except Exception as e:
            st.error(str(e))


# ==================================
# List Appointments
# ==================================

# with tab3:

#     st.subheader("List Appointments")

#     list_date = st.date_input(
#         "Select Date",
#         key="list_date"
#     )

#     if st.button("Show Appointments"):

#         payload = {
#             "date": dt.datetime.combine(
#                 list_date,
#                 dt.time.min
#             ).isoformat()
#         }

#         try:


#             response = requests.get(
#                 f"{BASE_URL}/list_appointments/",
#                 json=payload
#             )

#             if response.status_code == 200:

#                 appointments = response.json()

#                 if len(appointments) == 0:
#                     st.info("No appointments found")
#                 else:
#                     st.dataframe(appointments)

#             else:
#                 st.error(response.text)

#         except Exception as e:
#             st.error(str(e))


with tab3:

    st.subheader("List Appointments")

    list_date = st.date_input(
        "Select Date",
        key="list_date"
    )

    if st.button("Show Appointments"):

        payload = {
            "date": list_date.isoformat()
        }

        try:

            response = requests.post(
                f"{BASE_URL}/list_appointments/",
                json=payload
            )

            if response.status_code == 200:

                appointments = response.json()

                if not appointments:
                    st.info("No appointments found")
                else:
                    st.dataframe(appointments)

            else:
                st.error(response.text)

        except Exception as e:
            st.error(str(e))