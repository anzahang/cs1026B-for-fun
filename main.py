from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    try:
        with open(fileName, 'r') as f:
            patients = {}
            for line in f:
                line = line.strip().split(',')
                if len(line) != 8:
                    print(f"Invalid number of fields ({len(line)}) in line: {line}")
                    continue
                try:
                    patientID = int(line[0])
                    date = str(line[1])
                    temperature = float(line[2])
                    heartRate = int(line[3])
                    respiratoryRate = int(line[4])
                    systolicBP = int(line[5])
                    diastolicBP = int(line[6])
                    oxygenSaturation = int(line[7])
                except ValueError:
                    print(f"Invalid data type in line: {line}")
                    continue
                if temperature < 30 or temperature > 43:
                    print(f"Invalid temperature value ({temperature}) in line: {line}")
                    continue
                if heartRate < 30 or heartRate > 200:
                    print(f"Invalid heart rate value ({heartRate}) in line: {line}")
                    continue
                if respiratoryRate < 5 or respiratoryRate > 60:
                    print(f"Invalid respiratory rate value ({respiratoryRate}) in line: {line}")
                    continue
                if systolicBP < 50 or systolicBP > 250:
                    print(f"Invalid systolic blood pressure value ({systolicBP}) in line: {line}")
                    continue
                if diastolicBP < 30 or diastolicBP > 150:
                    print(f"Invalid diastolic blood pressure value ({diastolicBP}) in line: {line}")
                    continue
                if oxygenSaturation < 80 or oxygenSaturation > 100:
                    print(f"Invalid oxygen saturation value ({oxygenSaturation}) in line: {line}")
                    continue
                if patientID not in patients:
                    patients[patientID] = []
                patients[patientID].append([date, temperature, heartRate, respiratoryRate, systolicBP, diastolicBP, oxygenSaturation])
            return patients
    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")
        return {}
    except:
        print("An unexpected error occurred while reading the file.")
        return {}



def displayPatientData(patients, patientId=0):
    # If patientId is not given, set it to 0 to display data for all patients
    if patientId == 0:
        # If patient dictionary is empty, print a message and return
        if not patients:
            print("No patients found.")
            return
        # Otherwise, print data for all patients
        for patientId, patientData in patients.items():
            # Print patient ID
            print(f"Patient ID: {patientId}")
            # Print data for each visit
            for visit in patientData:
                print(" Visit Date:", visit[0])
                print(f"  Temperature: {'%.2f' % visit[1]} C")
                print(f"  Heart Rate: {visit[2]} bpm")
                print(f"  Respiratory Rate: {visit[3]} bpm")
                print(f"  Systolic Blood Pressure: {visit[4]} mmHg")
                print(f"  Diastolic Blood Pressure: {visit[5]} mmHg")
                print(f"  Oxygen Saturation: {visit[6]} %")
    # If patientId is given, print data for that patient only
    else:
        # If patientId is not found in patients, print an error message and return
        if patientId not in patients:
            print(f"Patient with ID {patientId} not found.")
            return
        # Otherwise, print data for that patient only
        print(f"Patient ID: {patientId}")
        for visit in patients[patientId]:
            print(" Visit Date:", visit[0])
            print(f"  Temperature: {'%.2f' % visit[1]} C")
            print(f"  Heart Rate: {visit[2]} bpm")
            print(f"  Respiratory Rate: {visit[3]} bpm")
            print(f"  Systolic Blood Pressure: {visit[4]} mmHg")
            print(f"  Diastolic Blood Pressure: {visit[5]} mmHg")
            print(f"  Oxygen Saturation: {visit[6]} %")




def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """

    # Check if patients is a dictionary
    if not isinstance(patients, dict):
        print("Error: 'patients' should be a dictionary.")
        return

    # Check if patientId is an integer
    if not isinstance(patientId, int):
        print("Error: 'patientId' should be an integer.")
        return

    # Calculate the average vital signs for all patients
    if patientId == 0:
        # Check if there is data for at least one patient
        if len(patients) == 0:
            print("No data found.")
            return

        # Calculate the total sum of all vital signs
        temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = ox_sum = num_visits = 0
        for patient in patients.values():
            for visit in patient:
                temp_sum += visit[1]
                hr_sum += visit[2]
                rr_sum += visit[3]
                sbp_sum += visit[4]
                dbp_sum += visit[5]
                ox_sum += visit[6]
                num_visits += 1

        # Calculate the averages
        temp_avg = temp_sum / num_visits
        hr_avg = hr_sum / num_visits
        rr_avg = rr_sum / num_visits
        sbp_avg = sbp_sum / num_visits
        dbp_avg = dbp_sum / num_visits
        ox_avg = ox_sum / num_visits

        # Print the averages
        print("Vital Signs for All Patients:")
        print("  Average temperature: {:.2f} °C".format(temp_avg))
        print("  Average heart rate: {:.2f} bpm".format(hr_avg))
        print("  Average respiratory rate: {:.2f} bpm".format(rr_avg))
        print("  Average systolic blood pressure: {:.2f} mmHg".format(sbp_avg))
        print("  Average diastolic blood pressure: {:.2f} mmHg".format(dbp_avg))
        print("  Average oxygen saturation: {:.2f}%".format(ox_avg))

    # Calculate the average vital signs for a specific patient
    elif patientId > 0:
        # Check if the patientId is in the dictionary
        if patientId not in patients:
            print("No data found for patient with ID {}.".format(patientId))
            return

        # Check if there is data for the patient
        patient = patients[patientId]
        if len(patient) == 0:
            print("No data found for patient with ID {}.".format(patientId))
            return

        # Calculate the total sum of all vital signs for the patient
        temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = ox_sum = num_visits = 0
        for visit in patient:
            temp_sum += visit[1]
            hr_sum += visit[2]
            rr_sum += visit[3]
            sbp_sum += visit[4]
            dbp_sum += visit[5]
            ox_sum += visit[6]
            num_visits += 1

        # Calculate the averages
        temp_avg = temp_sum / num_visits
        hr_avg = hr_sum / num_visits
        rr_avg = rr_sum / num_visits
        sbp_avg = sbp_sum / num_visits
        dbp_avg = dbp_sum / num_visits
        os_avg = os_sum / num_visits
        # Print the results
        if patientId == 0:
            if num_patients == 0:
                print("No data found for any patients.")
            else:
                print("Vital Signs for All Patients:")
                print("  Average temperature:", "%.2f" % temp_avg, "C")
                print("  Average heart rate:", "%.2f" % hr_avg, "bpm")
                print("  Average respiratory rate:", "%.2f" % rr_avg, "bpm")
                print("  Average systolic blood pressure:", "%.2f" % sbp_avg, "mmHg")
                print("  Average diastolic blood pressure:", "%.2f" % dbp_avg, "mmHg")
                print("  Average oxygen saturation:", "%.2f" % os_avg, "%")
        elif patientId in patients:
            visits = patients[patientId]
            num_visits = len(visits)
            if num_visits == 0:
                print("No data found for patient with ID {}.".format(patientId))
            else:
                print("Vital Signs for Patient {}:".format(patientId))
                print("  Average temperature:", "%.2f" % temp_avg, "C")
                print("  Average heart rate:", "%.2f" % hr_avg, "bpm")
                print("  Average respiratory rate:", "%.2f" % rr_avg, "bpm")
                print("  Average systolic blood pressure:", "%.2f" % sbp_avg, "mmHg")
                print("  Average diastolic blood pressure:", "%.2f" % dbp_avg, "mmHg")
                print("  Average oxygen saturation:", "%.2f" % os_avg, "%")
        else:
            print("No data found for patient with ID {}.".format(patientId))


def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    # check if patientId exists in patients
    if patientId not in patients:
        print(f"Error: Patient #{patientId} does not exist.")
        return

    # check if all inputs are valid
    try:
        temp = float(temp)
        hr = int(hr)
        rr = int(rr)
        sbp = int(sbp)
        dbp = int(dbp)
        spo2 = int(spo2)
    except ValueError:
        print("Error: Invalid input. Please enter valid values.")
        return

    # add new visit to patient's list of visits
    patients[patientId].append({
        'date': date,
        'temp': temp,
        'hr': hr,
        'rr': rr,
        'sbp': sbp,
        'dbp': dbp,
        'spo2': spo2
    })

    # append new data to the text file
    with open(fileName, 'a') as f:
        f.write(f"{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}\n")

    print(f"Visit is saved successfully for Patient #{patientId}")




def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    for patient_id, patient_visits in patients.items():
        for visit in patient_visits:
            if len(visit) != 8:  # ignore visits with incomplete data
                continue
            date_parts = visit[0].split('-')
            if len(date_parts) != 3:  # ignore visits with invalid date format
                continue
            try:
                visit_year = int(date_parts[0])
                visit_month = int(date_parts[1])
                visit_day = int(date_parts[2])
            except ValueError:  # ignore visits with invalid date values
                continue
            if year is not None and visit_year != year:  # filter by year
                continue
            if month is not None and visit_month != month:  # filter by month
                continue
            visits.append((patient_id, visit))
    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits due to abnormal health stats.
    """
    followup_patients = []
    for patient_id, visits in patients.items():
        for visit in visits:
            hr = visit[2]
            sys_bp = visit[4]
            dia_bp = visit[5]
            spo2 = visit[6]
            if hr > 100 or hr < 60 or sys_bp > 140 or dia_bp > 90 or spo2 < 90:
                followup_patients.append(patient_id)
                break
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    if patientId not in patients:
        print(f"No data found for patient with ID {patientId}")
        return

    del patients[patientId]
    print(f"Data for patient {patientId} has been deleted.")

    with open(filename, 'w') as f:
        for pid, visits in patients.items():
            for visit in visits:
                f.write(f"{pid},{visit['date']},{visit['temp']},{visit['hr']},{visit['rr']},{visit['sbp']},{visit['dbp']},{visit['spo2']}\n")





###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()