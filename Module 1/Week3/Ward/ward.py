from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass

    def get_yob(self):
        return self._yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name=name, yob=yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name=name, yob=yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name=name, yob=yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = list()

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Name: {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        counter = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                counter += 1

        return (f"Number of doctor: {counter}")

    def sort_yob(self):
        return self.__list_people.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_avarage(self):
        total = 0
        count = 0
        for p in self.__list_people:
            if isinstance(p, Teacher):
                total += p.get_yob()
                count += 1

        return total / count


if __name__ == "__main__":
    student1 = Student('Gia', 2004, 14)
    # student1.describe()
    doctor1 = Doctor('He', 1991, "Dentist")
    teacher1 = Teacher("Ha", 1992, "Math")
    ward1 = Ward('Ward1')
    ward1.add_person(student1)
    ward1.add_person(doctor1)
    ward1.add_person(teacher1)
    ward1.describe()
    print(ward1.count_doctor())
    ward1.sort_yob()
    print(ward1.describe())
