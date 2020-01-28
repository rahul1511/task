'''PROJECT DESCRIPTION: This project mainly based on the type of social network where a user can create own profile by registering and also having the facility to login/logout and can see the post of the users by accessing on the profiles by login credentials.'''



'''
REQUIREMENTS TO INSTALL:
1.Django version 2.2
2.Rest_framework
3.Python version 3
4.Crispy forms
'''




'''
STEPS TO CONFIGURE THE ENVIRONMENT:
1.settings.py file in tellitest folder ------ 
   a.application settings i.e in Installed Apps.
   b.Media files settings i.e CRISPY_TEMPLATE_PACK ='bootstrap4'
			      # for login redirect
			      LOGIN_REDIRECT_URL='blog-post-home'
                              LOGIN_URL = 'login'.
   c.Default database is sqlite3 which is already configured with the project.
'''