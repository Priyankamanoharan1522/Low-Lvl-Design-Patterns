# from tabnanny import check


class AccountVerification:
    def verify_aadhar_card(self) :
        print(f'Aadhar Card is verified successfully')

    def verify_mobile_no(self):
        print(f'Mobile number verified successfully')

    def verification_status(self):
        print("Verification Successfully")
# loan eligible
# credic check
# notification
class LoanEligible:
    def check_age_limit(self,age):
        print(f'Loan is eligible for {age} years old')

    def check_employement(self,Employee_type):
        print(f'Loan eligible for {Employee_type}')

    def eligibility_status(self):
        print("Loan Eligible")

class CreditCheck:
    def check_credit_score(self):
        print(f'Credit rating is high')

    def credit_status(self):
        print(f'Credit Rating Verification Successfully')

class Notification:
    def email_notify(self):
        print("Email Notification send")

    def sms_nofify(self):
        print("SMS Notification send")

class LoanFacade:
    def __init__(self):
        self.loan_eligible=LoanEligible()
        self.acc_verify=AccountVerification()
        self.credit_check=CreditCheck()
        self.notify=Notification()

    def check_Loan_eligible(self):
        print("------------Check Eligibility----------------")
        self.acc_verify.verify_aadhar_card()
        self.acc_verify.verify_mobile_no()
        self.loan_eligible.check_age_limit(27)
        self.loan_eligible.check_employement("Self Employed")
        self.credit_check.check_credit_score()

    def Eligible_status(self):
        print("---------------Eligible Status--------------")
        self.acc_verify.verification_status()
        self.loan_eligible.eligibility_status()
        self.credit_check.credit_status()

    def nofification(self):
        print("--------------Noticication----------------------")
        self.notify.email_notify()
        self.notify.email_notify()

obj1=LoanFacade()
obj1.check_Loan_eligible()
obj1.Eligible_status()
obj1.nofification()