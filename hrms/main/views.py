from django.shortcuts import render,redirect
from .models import User,User_Data
# Create your views here.

#register_page and user creation views
def register_page(request):
    return render(request,"register.html")

def register(request):
    try:
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]
        if password==password2:
            insert = User.objects.create(email=email, password=password)
            if insert:
                success_msg= "Account created"
                return render(request, 'register.html',{'success_msg':success_msg})
        else:
            password_error = "password didn't match"
            return render(request,'register.html',{'password_error':password_error})
    except:
        error_msg ="Invalid Input"
        return render(request, 'register.html',{'error_msg':error_msg})



#login page and login views
def login_page(request):
    if 'employee_id' in request.session:
        uid = User.objects.get(employee_id=request.session['employee_id'])
        return render(request, 'login.html')
    else:
         return render(request,'login.html')

def login(request):
    try:
        employee_id = request.POST['employee_id']
        password = request.POST['password']
        uid= User.objects.get(employee_id=employee_id)

        if uid:
            if uid.password==password:
                uid_emp = User_Data.objects.get(id=uid.id)
                request.session['id'] = uid.id
                request.session['employee_id']=uid.employee_id
                request.session['email']=uid.email
                request.session['roll_user']=uid.roll_user
                index_active = "active"
                print("--------------------------> login sucess")
                return render(request,'index.html',{'index_active':index_active,'uid_emp':uid_emp})
            else:
                password_error = "password didn't match"
                return render(request,'login.html',{'password_error':password_error})
        else:
            user_error = "Invalid user"
            return render(request, 'login.html', {'user_error':user_error})
    except:
        user_error = "User Does not exist "
        return render(request, 'login.html', {'user_error': user_error})



#change password views
def change_password_page(request):
    chp_active = "active"
    return render(request, 'change-password.html',{'chp_active': chp_active})

def change_password(request):
    if 'employee_id' in request.session:
        chp_active = "active"
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        uid = User.objects.get(employee_id=request.session['employee_id'])
        if old_password==uid.password:
            if new_password1==new_password2:
                uid.password=new_password1
                uid.save()
                s_msg = "Password Change Sucessfully"
                print("--------------------> password change sucessfully")
                return render(request, 'change-password.html',{'chp_active': chp_active,'s_msg':s_msg})
            else:
                p_error = "New password didn't match"
                return render(request, 'change-password.html', {'chp_active': chp_active,'p_error':p_error})
        else:
            p_error = "Old password didn't match"
            return render(request, 'change-password.html', {'chp_active': chp_active, 'p_error': p_error})
    else:
        return render(request, 'login.html')


def forgot_password(request):
    return render(request,'forgot-password.html')



def index(request):
    if 'employee_id' in request.session:
        uid = User.objects.get(employee_id=request.session['employee_id'])
        uid_emp = User_Data.objects.get(id=uid.id)
        index_active = "active"
        return render(request,'index.html',{'index_active':index_active,'uid_emp':uid_emp})
    else:
        return render(request, 'login.html')

def search(request):
    return render(request,'search.html')

def activities(request):
    return render(request,'activities.html')

def chat(request):
    return render(request,'chat.html')

def profile(request):
    if 'employee_id' in request.session:
        uid = User.objects.get(employee_id=request.session['employee_id'])
        uid_emp = User_Data.objects.get(id=uid.id)
        pro_active = "active"
        return render(request,'profile.html',{'pro_active':pro_active,'uid_emp':uid_emp})
    else:
        return render(request, 'login.html')

def settings(request):
    settings_active = "active"
    if 'employee_id' in request.session:
        uid = User.objects.get(employee_id=request.session['employee_id'])
        uid_emp = User_Data.objects.get(id=uid.id)
        return render(request,'settings.html',{'settings_active':settings_active,'uid_emp':uid_emp})
    else:
        return render(request,'login.html')

def employee_dashboard(request):
    if 'employee_id' in request.session:
        uid = User.objects.get(employee_id=request.session['employee_id'])
        uid_emp = User_Data.objects.get(id=uid.id)
        emp_dash = "active"
    return render(request,'employee-dashboard.html',{'emp_dash':emp_dash,'uid_emp':uid_emp})

def voice_call(request):
    return render(request,'voice-call.html')

def events(request):
    return render(request,'events.html')

def contacts(request):
    return render(request,'contacts.html')

def inbox(request):
    return render(request,'inbox.html')

def file_manager(request):
    return render(request,'file-manager.html')

def all_employees(request):
    if 'employee_id' in request.session:
        uid = User.objects.get(employee_id=request.session['employee_id'])
        uid_emp = User_Data.objects.get(id=uid.id)
        emp_active = "active"
        return render(request,'employees.html',{'emp_active':emp_active,'uid_emp':uid_emp})
    else:
        return render(request, 'login.html')

# add employee
def employees(request):
    if 'employee_id' in request.session:
        uid = User.objects.get(employee_id=request.session['employee_id'])
        uid_emp = User_Data.objects.get(id=uid.id)
        emp_active = "active"

        if request.method == "POST":
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            employee_id = request.POST['employee_id']
            roll_user = request.POST['roll_user']

            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user_name = request.POST['user_name']
            joining_date = request.POST['joining_date']
            mobile_no = request.POST['mobile_no']
            department = request.POST['department']
            if password1==password2:
                try:
                    insert_data = User.objects.create(email=email,password=password1,employee_id=employee_id,roll_user=roll_user)
                    if insert_data:
                            insert_user_data = User_Data.objects.create(first_name=first_name, last_name=last_name,
                                                                    user_name=user_name, joining_date=joining_date,
                                                                    mobile_no=mobile_no, department=department,user=insert_data)
                            print("--------------- data created")
                            return redirect("/all_employees/")
                    else:
                        print("nothing to print")
                        return redirect("/all_employees/")
                except:
                    print("invalid input")
                    return redirect("/all_employees/")
            else:
                print("password not matching")
                return redirect("/all_employees/")
        else:
            print("nothing in post")
            return redirect("/all_employees/")
    else:
        print("-------------- render to login")
        return render(request, 'login.html')

def employees_list(request):
    return render(request,'employees-list.html')

def holidays(request):
    return render(request,'holidays.html')

def leaves(request):
    return render(request,'leaves.html')

def leaves_employee(request):
    return render(request,'leaves-employee.html')

def leave_settings(request):
    return render(request,'leave-settings.html')

def leave_type(request):
    le_t_active = "active"
    return render(request,'leave-type.html',{'le_t_active':le_t_active})

def attendance(request):
    return render(request,'attendance.html')

def attendance_employee(request):
    return render(request,'attendance-employee.html')

def departments(request):
    return render(request,'departments.html')

def designations(request):
    return render(request,'designations.html')

def timesheet(request):
    return render(request,'timesheet.html')

def overtime(request):
    return render(request,'overtime.html')

def clients(request):
    return render(request,'clients.html')

def projects(request):
    return render(request,'projects.html')

def tasks(request):
    return render(request,'tasks.html')

def task_board(request):
    return render(request,'task-board.html')

def task_view(request):
    return render(request,'task-view.html')

def leads(request):
    return render(request,'leads.html')

def tickets(request):
    return render(request,'tickets.html')

def ticket_view(request):
    return render(request,'ticket-view.html')

def estimates(request):
    return render(request,'estimates.html')

def create_estimate(request):
    return render(request,'create-estimate.html')

def estimate_view(request):
    return render(request,'estimate-view.html')

def edit_estimate(request):
    return render(request,'edit-estimate.html')

def invoices(request):
    return render(request,'invoices.html')

def create_invoice(request):
    return render(request,'create-invoice.html')

def edit_invoice(request):
    return render(request,'edit-invoice.html')

def payments(request):
    return render(request,'payments.html')

def expenses(request):
    return render(request,'expenses.html')

def provident_fund(request):
    return render(request,'provident-fund.html')

def taxes(request):
    return render(request,'taxes.html')

def salary(request):
    return render(request,'salary.html')

def salary_view(request):
    return render(request,'salary-view.html')

def salary_settings(request):
    if 'employee_id' in request.session:
        uid = User.objects.get(employee_id=request.session['employee_id'])
        uid_emp = User_Data.objects.get(id=uid.id)
        sal_s_active = "active"
        return render(request,'salary-settings.html',{'sal_s_active':sal_s_active,'uid_emp':uid_emp})
    else:
        return render(request, 'login.html')

def payroll_items(request):
    return render(request,'payroll-items.html')

def policies(request):
    return render(request,'policies.html')

def expense_reports(request):
    return render(request,'expense-reports.html')

def invoice_reports(request):
    return render(request,'invoice-reports.html')

def performance_indicator(request):
    return render(request,'performance-indicator.html')

def performance(request):
    return render(request,'performance.html')

def performance_appraisal(request):
    return render(request,'performance-appraisal.html')

def goal_tracking(request):
    return render(request,'goal-tracking.html')

def goal_type(request):
    return render(request,'goal-type.html')

def training(request):
    return render(request,'training.html')

def trainers(request):
    return render(request,'trainers.html')

def training_type(request):
    return render(request,'training-type.html')

def promotion(request):
    return render(request,'promotion.html')

def resignation(request):
    return render(request,'resignation.html')

def termination(request):
    return render(request,'termination.html')

def assets(request):
    return render(request,'assets.html')

def jobs(request):
    return render(request,'jobs.html')

def job_applicants(request):
    return render(request,'job-applicants.html')

def job_list(request):
    return render(request,'job-list.html')

def job_details(request):
    return render(request,)

def knowledgebase(request):
    return render(request,'knowledgebase.html')

def knowledgebase_view(request):
    return render(request,'knowledgebase-view.html')

def users(request):
    return render(request,'users.html')

def client_profile(request):
    return render(request,'client-profile.html')

def clients_list(request):
    return render(request,'clients-list.html')

def otp(request):
    return render(request,'otp.html')

def lock_screen(request):
    return render(request,'lock-screen.html')

def error_404(request):
    return render(request,'error-404.html')

def error_500(request):
    return render(request,'error-500.html')

def faq(request):
    return render(request,'faq.html')

def terms(request):
    return render(request,'terms.html')

def privacy_policy(request):
    return render(request,'privacy-policy.html')

def blank_page(request):
    return render(request,'blank_page.html')

def form_basic_inputs(request):
    return render(request,'form-basic-inputs.html')

def form_input_groups(request):
    return render(request,'form-input-groups.html')

def form_horizontal(request):
    return render(request,'form-horizontal.html')

def form_vertical(request):
    return render(request,'form-vertical.html')

def form_mask(request):
    return render(request,'form-mask.html')

def form_validation(request):
    return render(request,'form-validation.html')

def tables_basic(request):
    return render(request,'tables-basic.html')

def data_tables(request):
    return render(request,'data-table.html')

def invoice_view(request):
    return render(request,'invoice-view.html')


def project_view(request):
    return render(request,'project-view.html')

def project_list(request):
    return render(request,'project-list.html')

def video_call(request):
    return render(request,'video-call.html')

def outgoing_call(request):
    return render(request,'outgoing-call.html')

def incoming_call(request):
    return render(request,'incoming-call.html')

def components(request):
    return render(request,'componetns.html')

def compose(request):
    return render(request,'compose.html')

def mail_view(request):
    return render(request,'mail-view.html')

def apply_job(request):
    return render(request,'job-list.html')

def job_view(request):
    return render(request,'job-view.html')

def localization(request):
    loc_active = "active"
    return render(request,'localization.html',{'loc_active':loc_active})

def theme_settings(request):
    theme_active= "active"
    return render(request,'theme-settings.html',{'theme_active':theme_active})

def roles_permissions(request):
    rp_active="active"
    return render(request,'roles-permissions.html',{'rp_active':rp_active})

def email_settings(request):
    email_s_active = "active"
    return render(request,'email-settings.html',{'email_s_active':email_s_active})

def invoice_settings(request):
    inv_s_active = "active"
    return render(request,'invoice-settings.html',{'inv_s_active':inv_s_active})

def notifications_settings(request):
    noti_s_active= "active"
    return render(request,'notifications-settings.html',{'noti_s_active':noti_s_active})

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        del request.session['id']
        del request.session['employee_id']
        del request.session['roll_user']
        print("---------------------> logout sucess")
        return render(request,'login.html')
    else:
        return render(request, 'login.html')