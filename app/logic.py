from . import models
from . import serializers

# Get one student serialised
def get_student_as_json(student_number):
    user = models.User.objects.get(pk=str(student_number))

    serialised_user = serializers.UserSerializer(user, many=False)

    return serialised_user.data


# Get a list of all students
def get_all_students_as_json():
    users = models.User.objects.all()

    serialized_users = serializers.UserSerializer(users, many=True)

    return serialized_users.data

def post_review_as_json(request_data):

    serialised_review = serializers.ReviewSerializer(data=request_data, many=False)
    if serialised_review.is_valid():
        serialised_review.save()
        return True
    else:
        return False