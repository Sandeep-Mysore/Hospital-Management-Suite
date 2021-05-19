def gimme_a_nurse():
	#flag 5 is for all nurses stored in query
	query = {"flag": 5}
	#get all users into collections
	collection = db["users"]
	#select only nurses into docs
	docs = collection.find(query)

	nurse = []
	#add nurses into nurse array
	for doc in docs:
		nurse.append(doc)
	#sort based on number of patients tended to by doc
	nurse.sort(key = lambda x: len(x["incharge_patients"]))
	#check curret time
	now = datetime.datetime.now()
	time = now.time()

	i = 0
	while i < len(nurse):
		#check availability of nurse at the time
		start = datetime.datetime.strptime(nurse[i]["check_in_time"], "%H:%M").time()
		end = datetime.datetime.strptime(nurse[i]["check_out_time"], "%H:%M").time()
		if(start <= time < end):
			break
		i += 1
	#select nurse
	selected_nurse = nurse[i]
	print("selected_nurse:", selected_nurse)
	#return id
	return selected_nurse["_id"]

def gimme_a_doctor(specialization):
	# flag 1 is for doctors and choose specialization
	query = {"flag": 1, "specialization": specialization}
	# get all users in collections
	collection = db["users"]
	#get current time and date
	now = datetime.datetime.now()
	now =  now.strftime("%m/%d/%Y %H:%M")
	date = now.split(" ")[0]
	time = now.split(" ")[1]
	time2 = datetime.datetime.strptime(time, "%H:%M").time()
	
	docs = collection.find(query, {"_id": 1, "name": 1, "check_in_time": 1, "check_out_time": 1, "avg_time_per_patient": 1, "specialization": 1, "appointments": 1, })

	doctors = []
	for doc in docs:
		start = datetime.datetime.strptime(doc["check_in_time"], "%H:%M").time()
		end = datetime.datetime.strptime(doc["check_out_time"], "%H:%M").time()
		if(start <= time2 < end):
			doctors.append(doc)

	random_doctor = False
	print("doctors: ", doctors)
	for doctor in doctors:
		try:
			appointments_today = doctor["appointments"][date]
			if appointments_today:
				for time in appointments_today:
					start = time
					hrs = int(start.split(":")[0])
					mins = int(start.split(":")[1])
					mins += int(doctor["avg_time_per_patient"])
					if(mins >= 60):
						hrs += 1
						mins = mins % 60
					end = str(hrs) + ":" + str(mins)
					start = datetime.datetime.strptime(start, "%H:%M").time()
					end = datetime.datetime.strptime(end, "%H:%M").time()
					if(start <= time2 < end):
						break
				else:
					selected_doctor = doctor
					break
			else:
				selected_doctor = doctor
				break
		except:
			print("No appointments on this day")
			print(date)
			selected_doctor = doctor
			break
	else:
		print("No doctor is free hence selecting a random doctor")
		selected_doctor = doctors[random.randint(0, len(doctors) - 1)]
		random_doctor = True

	print("selected_doctor: ", selected_doctor)

	return selected_doctor["_id"]
