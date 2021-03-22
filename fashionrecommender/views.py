from django.shortcuts import render

# make sure this view is only accessible on login
@method_decorator(login_required, name="dispatch")
class EmployeeView(TemplateView):
    # our hybrid template, shown above
    template_name = "myapp/employee_home.html"

    def get_context_data(self, **kwargs):
        # passing the department choices to the template in the context
        return {
            "department_choices": [
                {"id": c[0], "name": c[1]} for c in Employee.DEPARTMENT_CHOICES
            ],
        }
