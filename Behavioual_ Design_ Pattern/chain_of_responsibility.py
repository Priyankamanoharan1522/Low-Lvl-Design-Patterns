class SupportLevel:
    def __init__(self,name):
        self.name=name
        self.next_level=None
        
    def set_next_level(self,next_level):
        self.next_level=next_level
        
    def handle_request(self,request):
        if self.can_handle(request):
            print(f'{self.name} handles {request}')
        elif self.next_level:
            self.next_level.handle_request(request)
        else:
            print(f"cant handles {request}")
            
    def can_handle(self,request):
        return False
    
class Level1Support(SupportLevel):
    def can_handle(self, request):
        return request in ['balance_check','billing']

class Level2Support(SupportLevel):
    def can_handle(self, request):
        return request in ['config_change','settings_change']
    
class Level3Support(SupportLevel):
    def can_handle(self, request):
        return request in ['security_issue','critical_issue']
    
class Manager(SupportLevel):
    pass

level1=Level1Support('Level 1 Support')
level2=Level2Support('Level 2 Support')
level3=Level3Support('Level 3 Support')

level1.set_next_level(level2)
level2.set_next_level(level3)
level1.handle_request('security_issue')

manager=Manager('Manager')
manager.handle_request('bug')