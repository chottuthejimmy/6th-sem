package adv_java.comp_proj;

import java.util.*;

public class thenComp {
    static class Employee {
        private int departmentId;
        private String name;

        public Employee(int departmentId, String name) {
            this.departmentId = departmentId;
            this.name = name;
        }

        public int getDepartmentId() {
            return departmentId;
        }

        public String getName() {
            return name;
        }

        @Override
        public String toString() {
            return "Employee{" +
                   "departmentId=" + departmentId +
                   ", name='" + name + '\'' +
                   '}';
        }
    }

    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee(101, "Alice"),
            new Employee(100, "Bob"),
            new Employee(101, "David"),
            new Employee(100, "Carol")
        );

        Comparator<Employee> byDepartment = Comparator.comparingInt(Employee::getDepartmentId);
        Comparator<Employee> byNameAscending = Comparator.comparing(Employee::getName);

        employees.sort(byDepartment.thenComparing(byNameAscending));

        for(Employee employee : employees) {
            System.out.println(employee);
        }
    }
}

