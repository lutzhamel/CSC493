class Person {
    private String name;
    private int age;

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return this.age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}

class MyProgram {
    public static void main(String[] args) {
        Person joe = new Person();
        joe.setName("Joe");
        joe.setAge(32);
        System.out.println(joe.getName()+" is "+joe.getAge()+" years old");
    }
}

