medical_cause = input('Did you cause the medical cause? (Yes or No)').strip().upper()
if medical_cause == 'Yes':
    print('You are allowed to attend the exam.')
else:
    attendance = int(input('What is the attendance '))
    if attendance >= 76:
        print('you are allowed to attend the exam.')
    else:
        print('you are not allowed to attend the exam.')