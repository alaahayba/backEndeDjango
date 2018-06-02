from .models import User
import re



EMAIL_REGEX= '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$';
DATE_REGEX= '^(19[5-9][0-9]|20[0-4][0-9]|2050)[-\/](0?[1-9]|1[0-2])[-\/](0?[1-9]|[12][0-9]|3[01])$';


def validateUserData(user):
    error={}
    if( user.first_name in [False ,'']):
        error['first_name']=["{'error','blank'}"]

    if(user.last_name in [False ,'']):
        error['last_name']=["{'error','blank'}"]

    if(user.passwordin [False ,'']):
        error['password']=["{'error','blank'}"]

    if(user.gender in [False ,'']):
        error['gender']=["{'error','blank'}"]

    if(not (user.gender in ['female','male',''])):
        error['gender']=[{"error": "inclusion" }];

    if( user.birthDate and not re.match(DATE_REGEX, user.birthDate )):
        error['birth_date']=[{"error": "invaild format it must be yyyy-mm-dd" }];
        
    if (user.email and not re.match(EMAIL_REGEX, user.email )):
            error['email']=[{"error": "Invalid email format" }];

    return error


def getUserData(data):
        User_data=User()
        User_data.first_name='first_name' in data and data['first_name']
        User_data.last_name='last_name' in data and data['last_name']
        User_data.birthDate='birth_date' in data and data['birth_date']
        User_data.gender='gender' in data and data['gender']
        User_data.email='email' in data and data['email']
        User_data.phone_number='phone_number' in data and data['phone_number']
        User_data.countryCode='country_code' in data and data['country_code']
        User_data.password='password' in data and data['password']

        return User_data
