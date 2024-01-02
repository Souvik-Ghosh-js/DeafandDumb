
from django.shortcuts import render
from django.http import HttpResponse
from .models import Guardian, Student, AdmissionData, Query
# Create your views here.
def query(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new Query instance and save it to the database
        query = Query(name=name, phone=phone, email=email, message=message)
        query.save()

        return HttpResponse("Query submitted successfully. Data saved to the database.")

    # If the request method is not POST, render the form
    return render(request, 'app/query_form.html')  #


def index(request):
    return render(request, 'app/index.html')

def contact(request):
    return render(request, 'app/contact.html')

def vehicle(request):
    return render(request, 'app/vehicle.html')



def admission(request):
    if request.method == 'POST':
        # Get form data
        student_name = request.POST.get('student_name')
        father_name = request.POST.get('father_name')
        father_qualification = request.POST.get('father_qualification')
        father_profession = request.POST.get('father_profession')
        mother_name = request.POST.get('mother_name')
        mother_qualification = request.POST.get('mother_qualification')
        mother_profession = request.POST.get('mother_profession')
        guardian_name = request.POST.get('guardian_name')
        guardian_qualification = request.POST.get('guardian_qualification')
        guardian_profession = request.POST.get('guardian_profession')
        guardian_monthly_income = request.POST.get('monthly_income')
        residential_certificate = request.FILES.get('residential_certificate')
        adhaar_card = request.FILES.get('adhaar_card')
        weight_of_child = request.POST.get('child_weight')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        guardian_mobile_number = request.POST.get('guardian_mobile')
        aadhar_card = request.FILES.get('aadhar_card')
        ration_card = request.FILES.get('ration_card')
        birth_certificate = request.FILES.get('birth_certificate')
        has_disability = request.POST.get('has_disability') == 'Yes'
        disability_certificate = request.FILES.get('disability_certificate')
        applied_for_disability_certificate = request.POST.get('applied_for_disability_certificate') == 'Yes'
        medical_report = request.FILES.get('medical_report')
        cast_certificate = request.FILES.get('cast_certificate')
        taking_medicines_daily = request.POST.get('taking_medicines_daily') == 'Yes'
        behaves_inappropriately = request.POST.get('behaves_inappropriately') == 'Yes'
        problem_description = request.POST.get('inappropriate_behavior_details') if behaves_inappropriately else ''
        hears_name_when_called = request.POST.get('hears_name') == 'Yes'
        received_allowance = request.POST.get('received_allowance') == 'Yes'
        enrollment_class = request.POST.get('enrollment_class')
        bank_name = request.POST.get('bank_name')
        branch_name = request.POST.get('branch_name')
        ifsc_code = request.POST.get('ifsc_code')
        account_number = request.POST.get('account_number')

        # Create Guardian instances
        father = Guardian(name=father_name, qualification=father_qualification, profession=father_profession, monthly_income=guardian_monthly_income)
        father.save()

        mother = Guardian(name=mother_name, qualification=mother_qualification, profession=mother_profession, monthly_income=0.0)
        mother.save()

        guardian = Guardian(name=guardian_name, qualification=guardian_qualification, profession=guardian_profession, monthly_income=0.0)
        guardian.save()

        # Create Student instance
        student = Student(name=student_name, father=father, mother=mother, guardian=guardian, date_of_birth=date_of_birth, address=address)
        student.save()

        # Create AdmissionData instance
        admission_data = AdmissionData(
            student=student,
            residential_certificate=residential_certificate,
            adhaar_card=adhaar_card,
            weight_of_child=weight_of_child,
            has_disability=has_disability,
            disability_certificate=disability_certificate,
            applied_for_disability_certificate=applied_for_disability_certificate,
            medical_report=medical_report,
            cast_certificate=cast_certificate,
            taking_medicines_daily=taking_medicines_daily,
            behaves_inappropriately=behaves_inappropriately,
            problem_description=problem_description,
            hears_name_when_called=hears_name_when_called,
            received_allowance=received_allowance,
            enrollment_class=enrollment_class,
            bank_name=bank_name,
            branch_name=branch_name,
            ifsc_code=ifsc_code,
            account_number=account_number,
        )
        admission_data.save()

        return HttpResponse("Form submitted successfully. Data saved to the database.")

    # If the request method is not POST, render the form
    return render(request, 'app/index.html')
