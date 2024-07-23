package adv_java.comp_proj;

public class usemyComp implements MyComparator<Integer> {
    public int compare(Integer o1, Integer o2) {
        return o1 - o2;
    }

    public boolean equals(Integer o1, Integer o2) {
        
        return o1.equals(o2);
    }

    public static void main(String[] args) {
        usemyComp comp = new usemyComp();
        System.out.println(comp.compare(1, 2));
        System.out.println(comp.equals(1, 1));
    }
    
}
