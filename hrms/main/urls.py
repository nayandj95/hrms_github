"""digi_hrms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.login_page, name='login_page'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register, name='register'),
    path('register_page/', views.register_page, name='register_page'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('index/',views.index,name='index'),
    path('search/',views.search, name='search'),
    path('activities/',views.activities,name='activities'),
    path('chat/',views.chat,name='chat'),
    path('profile/',views.profile,name='profile'),
    path('settings/',views.settings,name='settings'),
    path('employee_dashboard/',views.employee_dashboard,name="employee_dashboard"),
    path('voice_call/',views.voice_call,name='voice_call'),
    path('events/',views.events,name='events'),
    path('contacts/',views.contacts,name='contacts'),
    path('inbox/',views.inbox,name='inbox'),
    path('file_manager/',views.file_manager,name='file_manager'),
    path('all_employees/',views.all_employees,name='all_employees'),
    path('employees/',views.employees,name='employees'),
    path('employees_list/',views.employees_list,name='employees_list'),
    path('holidays/',views.holidays,name='holidays'),
    path('leaves/',views.leaves,name='leaves'),
    path('leaves_employee',views.leaves_employee,name='leaves_employee'),
    path('leave_settings/',views.leave_settings,name='leave_settings'),
    path('leave_type/',views.leave_type,name='leave_type'),
    path('attendance/',views.attendance,name='attendance'),
    path('attendance_employee/',views.attendance_employee,name='attendance_employee'),
    path('departments/',views.departments,name='departments'),
    path('designations/',views.designations,name='designations'),
    path('timesheet/',views.timesheet,name='timesheet'),
    path('overtime/',views.overtime,name='overtime'),
    path('clients/',views.clients,name='clients'),
    path('clients_list/',views.clients,name='clients_list'),
    path('projects/',views.projects,name='projects'),
    path('project_list/',views.project_list,name='project_list'),
    path('tasks/',views.tasks,name='tasks'),
    path('task_board',views.task_board,name='task_board'),
    path('task_view/',views.task_view,name='task_view'),
    path('leads/',views.leads,name='leads'),
    path('tickets/',views.tickets,name='tickets'),
    path('ticket_view/',views.ticket_view,name='ticket_view'),
    path('estimates',views.estimates,name='estimates'),
    path('create_estimate/',views.create_estimate,name='create_estimate'),
    path('estimate_view/',views.estimate_view,name='estimate_view'),
    path('edit_estimate/',views.edit_estimate,name='edit_estimate'),
    path('invoices/',views.invoices,name='invoices'),
    path('create_invoice/',views.create_invoice,name='create_invoice'),
    path('edit_invoice/',views.edit_invoice,name='edit_invoice'),
    path('payments/',views.payments,name='payments'),
    path('expences/',views.expenses,name='expenses'),
    path('provident_fund/',views.provident_fund,name='provident_fund'),
    path('taxes/',views.taxes,name='taxes'),
    path('salary/',views.salary,name='salary'),
    path('salary_view/',views.salary_view,name='salary_view'),
    path('payroll_items/',views.payroll_items,name='payroll_items'),
    path('policies/',views.policies,name='policies'),
    path('expense_reports/',views.expense_reports,name='expense_reports'),
    path('invoice_reports/',views.invoice_reports,name='invoice_reports'),
    path('performance_indicator/',views.performance_indicator,name='performance_indicator'),
    path('performance/',views.performance,name='performance'),
    path('performance_appraisa/',views.performance_appraisal,name='performance_appraisal'),
    path('goal_tracking/',views.goal_tracking,name='goal_tracking'),
    path('goal_type/',views.goal_type,name='goal_type'),
    path('training/',views.training,name='training'),
    path('trainers/',views.trainers,name='trainers'),
    path('training_type/',views.training_type,name='training_type'),
    path('promotion/',views.promotion,name='promotion'),
    path('resignation/',views.resignation,name='resignation'),
    path('termination/',views.termination,name='termination'),
    path('assets/',views.assets,name='assets'),
    path('jobs/',views.jobs,name='jobs'),
    path('job_applicants/',views.job_applicants,name='job_applicants'),
    path('job_details/',views.job_details,name='job_details'),
    path('knowledgebase/',views.knowledgebase,name='knowledgebase'),
    path('knowledgebase_view/',views.knowledgebase_view,name='knowledgebase_view'),
    path('users/',views.users,name='users'),
    path('client_profile/',views.client_profile,name='client_profile'),
    path('otp/',views.otp,name='otp'),
    path('lock_screen/',views.lock_screen,name='lock_screen'),
    path('error_404/',views.error_404,name='error_404'),
    path('error_500/',views.error_500,name='error_500'),
    path('faq/',views.faq,name='faq'),
    path('terms/',views.terms,name='terms'),
    path('privacy_policy/',views.privacy_policy,name='privacy_policy'),
    path('blank_page/',views.blank_page,name='blank_page'),
    path('form_basic_inputs/',views.form_basic_inputs,name='form_basic_inputs'),
    path('form_input_groups/',views.form_input_groups,name='form_input_groups'),
    path('form_horizontal/',views.form_horizontal,name='form_horizontal'),
    path('form_vertical/',views.form_vertical,name='form_vertical'),
    path('form_mask/',views.form_mask,name='form_mask'),
    path('form_validation/',views.form_validation,name='form_validation'),
    path('tables_basic/',views.tables_basic,name='tables_basic'),
    path('data_tables/',views.data_tables,name='data_tables'),
    path('invoice_view/',views.invoice_view,name='invoice_view'),
    path('project_view/',views.project_view,name='project_view'),
    path('video_call/',views.video_call,name='video_call'),
    path('outgoing_call',views.outgoing_call,name='outgoing_call'),
    path('incoming_call/',views.incoming_call,name='incoming_call'),
    path('components/',views.components,name='components'),
    path('compose/',views.compose,name='compose'),
    path('mail_view/',views.mail_view,name='mail_view'),
    path('localization/',views.localization,name='localization'),
    path('theme_settings/',views.theme_settings,name='theme_settings'),
    path('roles_permissions/',views.roles_permissions,name='roles_permissions'),
    path('email_settings/',views.email_settings,name='email_settings'),
    path('invoice-settings/',views.invoice_settings,name='invoice_settings'),
    path('salary_settings/',views.salary_settings,name='salary_settings'),
    path('notifications_settings/',views.notifications_settings,name='notifications_settings'),
    path('change_password_page/',views.change_password_page,name='change_password_page'),
    path('change_password/',views.change_password,name='change_password'),
    path('apply_job/',views.apply_job,name='apply_job'),
    path('job_view/',views.job_view,name='job_view'),
    path('job_list/',views.job_list,name='job_list'),

]
 