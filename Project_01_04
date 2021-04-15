"""TechWorld, a technology training center, wants to allocate courses for instructors.
An instructor is identified by name, technology skills, experience and average feedback.
An instructor is allocated a course, if he/she satisfies the below two conditions:

eligibility criteria:
if experience is more than 3 years, average feedback should be 4.5 or more
if experience is 3 years or less, average feedback should be 4 or more
he/she should posses the technology skill for the course
"""
#!/usr/bin/python3

class Instructor:
    def __init__(self):
        self.__instructor_name=None
        self.__technology_skill=None
        self.__experience=None
        self.__avg_feedback=None
        
        
        
    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback
    
    def set_experience(self, experience):
        self.__experience = experience
        
    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name
    
    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill
        
    
    def get_avg_feedback(self):
        return self.__avg_feedback
    
    def get_experience(self):
        return self.__experience
        
    def get_instructor_name(self):
        return self.__instructor_name
    
    def get_technology_skill(self):
        return self.__technology_skill
        
    def check_eligibility(self):
        if self.__experience>3 and self.__avg_feedback>=4.5:
            return True
        elif self.__experience<=3 and self.__avg_feedback>=4:
            return True
        else:
            return False
    
    def allocate_course(self, technology):
        if((technology==self.__technology_skill) or (technology=="C++")):
            return True
        else:
            return False
            
    
    



