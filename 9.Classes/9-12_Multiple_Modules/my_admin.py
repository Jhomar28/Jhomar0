from admin import admin

jhomar = admin('jhomar', 'rosaliere', 'j_rosaliere', 'j_rosaliere@Icloud.com', 'pennsylvania')
jhomar.describe_user()

jhomar_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
jhomar.privileges.privileges = jhomar_privileges

print(f"\nThe admin {jhomar.username} has these privileges: ")
jhomar.privileges.show_privileges()