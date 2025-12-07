from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School('ABC', 'Dhaka')

eight = ClassRoom('Eight')
nine = ClassRoom('Nine')
ten = ClassRoom('Ten')

# adding classroom
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# adding Student
rakib = Student('Rakib', eight)
sakib = Student('Sakib', nine)
rafi = Student('Rafi', ten)
saki = Student('Saki', ten)

school.student_admission(rakib)
school.student_admission(sakib)
school.student_admission(rafi)
school.student_admission(saki)

# adding teachers
abul = Teacher('Abul Khan')
babul = Teacher('Babul Khan')
kabul = Teacher('Kabul Khan')

# adding subjects

bangla = Subject('Bangla', abul)
physics = Subject('Physics', babul)
chemistry = Subject('Chemistry', kabul)
biology = Subject('Biology', abul)


eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics) 
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)



