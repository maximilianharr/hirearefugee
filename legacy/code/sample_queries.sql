-- Get user with user details
SELECT * FROM auth_user
	INNER JOIN userclass_userdetails 
	ON auth_user.id = userclass_userdetails.user_id
