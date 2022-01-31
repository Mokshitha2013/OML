import oci
config = oci.config.from_file()
identity = oci.identity.IdentityClient(config)
dbclient = oci.database.DatabaseClient(config)
user = identity.get_user(config["user"]).data
listdb=identity.list_compartments(config["tenancy"],name="OML")
print("-------")
print(listdb.data[0].id)
print("-------")

print("----ATP-- on this compartement ---"+listdb.data[0].name)

ldb = dbclient.list_autonomous_databases(listdb.data[0].id)
print(ldb.data[0].db_name)
print("OCID is : " +ldb.data[0].id)
print("life cycle stat is : " +ldb.data[0].lifecycle_state)
if(ldb.data[0].lifecycle_state =='STOPPED'):
	print('Database is stopped')
	Question = input("Do you want to start ????  (yes/no) :")
	if Question == ("yes"):
		print ("well done")
		start_autonomous_database_response = dbclient.start_autonomous_database(ldb.data[0].id)
		print(start_autonomous_database_response.data)
	elif Question == ("no"):
		print ("try again")
else:
	print('Database is up and RUNNING.....')
	Question = input("Do you want to STOP ????  (yes/no) :")
	if Question == ("yes"):
		print ("well done")
		stop_autonomous_database_response = dbclient.stop_autonomous_database(ldb.data[0].id)
		print(stop_autonomous_database_response.data)
	elif Question == ("no"):
		print ("try again")

