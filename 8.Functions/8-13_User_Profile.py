def bulid_profile(first_name, last_name, **kwargs):
    """Builds a dictionary containing user information."""
    profile = {'first_name': first_name, 'last_name': last_name}
    profile.update(kwargs)
    return profile

# Build your profile
my_profile = bulid_profile('John', 'Doe', age=30, city='New york', hobby='coding')
print(my_profile)