package defaulted_methods;

public class Functions {

    static defaulted_methods_md.Root root = new defaulted_methods_md.Root();


    public static final void main(String[] args) {
        main(new java.util.ArrayList(java.util.Arrays.asList(args)));
    }

    public static void main(java.util.ArrayList<String> args) {
        pkg.T1 t1 = new pkg.T1();
        (t1).foo();
        (t1).bar();
        do{System.out.println("===");System.out.flush();}while(false);
        pkg.T2 t2 = new pkg.T2();
        (t2).foo();
        (t2).bar();
        do{System.out.println("===");System.out.flush();}while(false);
        pkg.T3 t3 = new pkg.T3();
        (t3).foo();
        (t3).bar();
        do{System.out.println("===");System.out.flush();}while(false);
        pkg.T4 t4 = new pkg.T4();
        (t4).foo();
        (t4).bar();
        do{System.out.println("===");System.out.flush();}while(false);
        pkg.T5 t5 = new pkg.T5();
        (t5).foo();
        (t5).bar();
    }
}
