from privileges import Admin

#create an admin
admin = Admin( 'nothing' , 'nothing' , 999 , 'none' )
#admin.describe_user()
admin.privileges.privileges = [ 'can block' , 'can approve' , 'can hide' ]
admin.privileges.show_privileges()
