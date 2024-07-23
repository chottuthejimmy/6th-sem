package java.comparators;

// Introduction to Comparators in Java 8 with examples

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Student {
    String name;
    int age;
    int marks;

    public Student(String name, int age, int marks) {
        this.name = name;
        this.age = age;
        this.marks = marks;
    }

    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", marks=" + marks +
                '}';
    }
}

public class sorting {
    public static void main(String[] args) {
        List<Student> students = new ArrayList<>();
        students.add(new Student("Alice", 20, 90));
        students.add(new Student("Bob", 22, 80));
        students.add(new Student("Charlie", 21, 95));
        students.add(new Student("David", 23, 85));

        // Sorting by name
        Comparator<Student> nameComparator = Comparator.comparing(student -> student.name);
        Collections.sort(students, nameComparator);
        System.out.println("Sorting by name: " + students);

        // Sorting by age
        Comparator<Student> ageComparator = Comparator.comparing(student -> student.age);
        Collections.sort(students, ageComparator);
        System.out.println("Sorting by age: " + students);

        // Sorting by marks
        Comparator<Student> marksComparator = Comparator.comparing(student -> student.marks);
        Collections.sort(students, marksComparator);
        System.out.println("Sorting by marks: " + students);
    }
}

// Output:
// Sorting by name: [Student{name='Alice', age=20, marks=90}, Student{name='Bob', age=22, marks=80}, Student{name='Charlie', age=21, marks=95}, Student{name='David', age=23, marks=85}]